> !新版自定义监控开正在开发中，目前自定义监控暂不支持申请使用。

本文介绍如何使用 Shell 命令+SDK 方式上报云数据库 MySQL 的指标至自定义监控，查看指标并配置告警。

## 实践背景

定期监控云数据库 MySQL 的关键指标。当这些监控指标触发您设置的告警条件时，发送短信告警。

## 前提条件

- 购买了腾讯云 [云服务器 CVM](https://cloud.tencent.com/product/cvm) 并安装 MySQL 或购买了[云数据库 MySQL](https://cloud.tencent.com/product/cdb)。
- 安装 Python 2.7以上环境。

## 数据上报

### 步骤1：准备上报环境

安装 Python 语言 SDK：

- [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)

### 步骤2：数据采集授权

在数据库中执行以下代码，进行云数据库中的数据采集授权：

```
grant select on *.* to monitor@'x.x.x.x' identified by 'monitor!@#asd';
```

> ?
> - 'x.x.x.x'：表示服务器 IP 地址。
> - `*.*`：表示的意思是任意数据库下的任意数据表。

### 步骤3：上报数据

1. 在`/usr/local/bin`目录下新建如下两个文件:
	1. 新建 ToMonitor.py，代码如下：
	```
	from tencentcloud.common import credential
	from tencentcloud.common.profile.client_profile import ClientProfile
	from tencentcloud.common.profile.http_profile import HttpProfile
	from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
	from tencentcloud.monitor.v20180724 import monitor_client, models
	import sys,json
	try:
			SecretId = sys.argv[1]
			SecretKey = sys.argv[2]
			region = sys.argv[3]
			metricList = json.loads(sys.argv[4])
			cred = credential.Credential(SecretId, SecretKey)
			httpProfile = HttpProfile()
			httpProfile.endpoint = "monitor.tencentcloudapi.com"

			clientProfile = ClientProfile()
			clientProfile.httpProfile = httpProfile
			client = monitor_client.MonitorClient(cred, region , clientProfile)

			req = models.PutMonitorDataRequest()
			paramList = []
			for single in metricList:
				 for MetricName,metricValue in single.items():
						newParams = {}
						newParams["MetricName"] = MetricName
						newParams["Value"] = int(metricValue)
						paramList.append(newParams)
			params = '{"Metrics":%s}' %json.dumps(paramList)
			req.from_json_string(params)

			resp = client.PutMonitorData(req)
			print(resp.to_json_string())

	except TencentCloudSDKException as err:
			print(err)
	```
	2. 新建 MySQLStatusToMonitor.sh 文件，代码如下：
	```
	#!/bin/bash

	#需要采集数据的 MySQL 地址
	MYSQLHOST="1.1.1.1"
	#需要采集数据的 MySQL 端口
	MYSQLPORT=3306
	#需要采集数据的访问用户名
	MYSQLUSER="monitor"
	#需要采集数据的 MySQL 访问密码
	MYSQLPWD="monitor!@#asdxxxx"
	#用户专属的 SecretId
	SecretId="xxxxxxxxx"
	#用户专属的 SecretKey
	SecretKey="xxxxxxxx"
	#需要上报到监控系统所属区域
	region="ap-guangzhou"

	function Log()
	{
	msg=$1
	logType=$2
	logFile="./MySQLStatusToMonitor.log"
	echo "["`date +"%Y-%m-%d %X"`"]$msg" >> $logFile
	}
	MYSQLCON="/usr/bin/mysql -h$MYSQLHOST -P$MYSQLPORT -u$MYSQLUSER -p$MYSQLPWD"

	#采集
	NEEDEDMYSQLSTATUS=`$MYSQLCON -e "show status;"|grep -Ew "Aborted_connects|Innodb_row_lock_current_waits|Uptime"`

	#记录相关参数
	AbConnections=`echo "$NEEDEDMYSQLSTATUS"|awk '/Aborted_connects/{print $2}'`
	InnodbRLCW=`echo "$NEEDEDMYSQLSTATUS"|awk '/Innodb_row_lock_current_waits/{print $2}'`
	MYSQLUptime=`echo "$NEEDEDMYSQLSTATUS"|awk '/Uptime/{print $2}'`
	Log "uploading Aborted_connects:$AbConnections,Innodb_row_lock_current_waits:$InnodbRLCW,MySQL_uptime:$MYSQLUptime."

	#上报到自定义监控
	/bin/python ToMonitor.py "$SecretId" "$SecretKey" "$region" '[{"AbConnections":'$AbConnections'},{"InnodbRLCW":'$InnodbRLCW'}, {"MYSQLUptime":'$MYSQLUptime'}]'
	```
>?代码中：MYSQLHOST、MYSQLPORT、MYSQLUSER、MYSQLPWD、SecretId、SecretKey、Region 字段需根据您的实际情况修改
>- Region：地域，可查询可用 [地域列表](https://cloud.tencent.com/document/product/397/40208#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
>- SecretId 和 SecretKey，请前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
>- ToMonitor.py 和 MySQLStatusToMonitor.sh 两个 Demo 也可放到其它目录下。本文以放`/usr/local/bin`为例。
2. 输入 Shell 命令，即可完成监控指标数据持续上报。
```shell
chmod a+x  /usr/local/bin/MySQLStatusToMonitor.sh ToMonitor.py
bash MySQLStatusToMonitor.sh
crontab -l > /tmp/cron.bak
echo "* * * * * /usr/local/bin/MySQLStatusToMonitor.sh &" >> /tmp/cron.bak
crontab /tmp/cron.bak
```

## 数据查询

数据上报完成后，可以在 [指标视图](https://console.cloud.tencent.com/monitor/indicator-view) 看到刚才上报的数据。

> ?
> 1. 配置告警和接收告警仅做一个场景举例。
> 2. 配置云数据库 MySQL 上报过的其它指标配置，请执行下述配置告警中的步骤2-3。

## 配置告警

**场景：定期监控云数据库 MySQL 异常连接数，当异常连接次数大于0时发送短信告警。**

1. 确认用户消息通道已验证，可在 [CAM 鉴权](https://console.cloud.tencent.com/cam) 页面查看验证情况。
   ![](https://main.qcloudimg.com/raw/f6a76736f4b054a2f65176bf2c84f2ff.jpg)
2. 进入自定义监控 [指标视图](https://console.cloud.tencent.com/monitor/indicator-view) 页面，在指标视图右上角【配置告警】。
   ![](https://main.qcloudimg.com/raw/7fdfce322ad0b79d567ecbbbeebad25d.png)
3. 根据背景需求配置告警规则，更详细的配置操作可参见 [配置告警策略](https://cloud.tencent.com/document/product/397/40223)。
   如图示例为：云数据库 MySQL 异常连接数大于0时发送短信告警，持续一个统计周期（1分钟），每5分钟告警一次。
   ![](https://main.qcloudimg.com/raw/fa908b3298cfd649b259719cc72e13ce.png)

## 接收告警

如果云数据库 MySQL 异常连接数大于0，5分钟后将会收到短信告警，短信内容如下：

```
【腾讯云】云监控自定义监控指标告警触发
账号 ID：34xxxxxxxx，昵称：自定义监控
告警详情
告警内容：指标视图 | 云数据库 MySQL 异常连接数大于0
告警对象：Aborted_connects
当前数据：1
APPID：125xxxxxxx
告警策略：视图告警
触发事件：2019-12-09 22:36:00（UTC+08:00）
```

## <span id="jump">指标说明</span>

| 指标中文名    | 指标英文名                    | 单位 |
| ------------- | ----------------------------- | ---- |
| 异常连接数    | Aborted_connects              | 次   |
| 行锁等待时间  | Innodb_row_lock_current_waits | 秒   |
| MySQL 运行时间 | MySQL_uptime                  | 秒   |


