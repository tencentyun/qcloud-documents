> !新版自定义监控开正在开发中，目前自定义监控暂不支持申请使用。

## 简介

本文介绍如何使用无服务器的 [云函数 SCF](https://cloud.tencent.com/document/product/583) 上报数据至自定义监控，查看指标并配置告警。

云函数可帮助您在无需购买和管理服务器的情况下运行代码。云函数的配套监控功能覆盖了云函数自身的指标监控，如：函数被调用次数，错误次数，消耗内存等。

自定义监控可以帮助您监控业务逻辑，例如，某个逻辑错误的次数，红包活动中用户发送红包的数量，领取红包的数量等。您可以直接在代码内打点上报业务指标，系统自动汇聚后实时生成监控图表。可以针对上报指标配置告警，查看指标趋势变化。

## 示例逻辑

- 每次请求判断是否存在`‘key1’`字符传入：如有，则成功次数`(suc_counts)+1`；如无，则失败次数`(fail_counts)+1`。
- 本示例基于 Python2.7 环境演示。

## 准备工作

- 在使用 SCF 上报数据之前，请先了解 [云函数 SCF ](https://cloud.tencent.com/document/product/583)。
- 有一台本地设备或 [腾讯云服务器](https://cloud.tencent.com/product/cvm)，用于构建项目、打包代码。

## 操作步骤

### 步骤1：新建本地项目

```
[root@VM_0_3_centos /data]# mkdir MyProject
```

### 步骤2：编写业务逻辑

新建一个`index.py`，内容如下：

```
# -*- coding: utf8 -*-
import time
import urllib2
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.monitor.v20180724 import monitor_client, models
# 自定义监控初始化函数，指定region和secrecId、secretKey
def MONITOR(secretId,secretKey):
    try:
        # 获取 region 地区，这里填写云函数所在的地域
        region = "ap-guangzhou"

        cred = credential.Credential(secretId,secretKey )

        client = monitor_client.MonitorClient(cred, region)
    except TencentCloudSDKException as err:
        print(err)
    return client
# 自定义监控上报函数，传入函数名称，指标名称，指标值
def API(client,instanceName,MetricName,Value):
    req = models.PutMonitorDataRequest() 
    req.AnnounceInstance = instanceName
    req.AnnounceTimestamp = int(time.time())
    req.Metrics = [
      {"MetricName": MetricName,"Value": Value}
    ]
    resp = client.PutMonitorData(req)
    return resp.to_json_string()

def main_handler(event, context):
    client = MONITOR("yourSecretId", "yourSecretKey")
    if 'key1' in event.keys():
        # SCF 的名称需要包含 namespace 和函数名称，中间用"|"分割
        print(API(client,"default|scf_monitor_Test","scf_suc_count",1))
    else:
    	print(API(client,"default|scf_monitor_Test","scf_fail_count",1))
    return "hello from scf"  #return
```

### 步骤3：安装自定义监控 SDK

将自定义监控的 SDK 以及相关依赖安装到项目目录中。

```
[root@VM_0_3_centos /data/MyProject]# pip install tencentcloud-sdk-python -t
```

安装完成后，项目根目录文件如下：

```
[root@VM_0_3_centos /data/MyProject]# ll
total 3016
-rw-r--r--  1 root root    1348 Dec 16 20:31 index.py
drwxr-xr-x  4 root root    4096 Dec 16 20:40 QcloudApi
drwxr-xr-x 99 root root    4096 Dec 16 20:40 tencentcloud
drwxr-xr-x  2 root root    4096 Dec 16 20:40 tencentcloud_sdk_python-3.0.113.dist-info
```

> ?Python 语言 SDK 下载链接：[Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)。

<span id="step4"></span>
### 步骤4：打包项目文件

执行如下命令，将整个项目目录打包成 ZIP 文件：

```
[root@VM_0_3_centos /data/MyProject]# zip project.zip * -r
```

文件打包完后，下载文件到本地，后续需把整个项目上传到云函数。

### 步骤5：上传项目压缩包至云函数

1. 新建云函数
	1. 进入 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，选择云函数所在的区域。
		![](https://main.qcloudimg.com/raw/cc955704c81dd7768278a6165470c239.jpg)
	2. 单击【新建】，填写完基础信息后，单击【下一步】。
		![](https://main.qcloudimg.com/raw/1758adaad8119f597cb98bc4f246154d.jpg)
	3. 进入函数配置页，使用默认设置即可，单击【完成】。
2. 上传 [步骤4](#step4) 打包好的项目 ZIP 文件。
	1. 在云函数详情页，单击【函数代码】，进入函数编辑页面。
	2. 选择本地上传 ZIP 包。
![](https://main.qcloudimg.com/raw/eab27a56361beddb650429e52f495ccc.jpg)
	3. 上传成功后，系统会自动解压并展示`index.py`文件内的代码内容。
		![](https://main.qcloudimg.com/raw/d4bcd548ab85d0a9f9c987063de007f5.jpg)
	4. 单击【保存】即可完成项目上传

### 步骤6：触发调试

#### 新建测试模板
1. 在函数代码页面，选择【新建模板】。
![](https://main.qcloudimg.com/raw/180b138c45e7b8012105151342d99216.jpg)
2. 基于代码逻辑填入测试内容：
```
{
		"key1": "test value 1",
		"key2": "test value 2"
}
```
![](https://main.qcloudimg.com/raw/f8d6266d3e25e5945815e9210cf295c6.jpg)
3. 单击【提交】，提交测试模板。
4. 选择 scf_monitor_test 测试模板，单击【测试】进行测试。若测试结果出现`{"RequestId": "xxxxxxx"}`，即表示监控数据上报成功。
![](https://main.qcloudimg.com/raw/978e57490f1891c4050cda7570fc0e47.png)

### 步骤7：查看监控视图

进入 [自定义监控](https://console.cloud.tencent.com/monitor/indicator-view) 查看步骤6触发上报的指标视图。
![](https://main.qcloudimg.com/raw/8fb2e5bef9fb66d6565f6bb53ec172b7.jpg)


### 步骤8：配置告警

详细的告警配置步骤请参见 [配置告警策略](https://cloud.tencent.com/document/product/397/40223)。

