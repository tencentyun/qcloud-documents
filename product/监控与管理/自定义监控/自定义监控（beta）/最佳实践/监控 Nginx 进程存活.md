>!新版自定义监控已灰度上线，如需使用可进入 [申请页面](https://cloud.tencent.com/apply/p/4v84kyrkl0g) 申请体验。
若在使用过程中遇到任何问题，您可以加入自定义监控交流 QQ 群（793979710）进行咨询，我们将竭诚为您服务！  


本文介绍如何使用 Shell 命令+CLI 方式上报 Nginx 进程存活数据至自定义监控，查看指标并配置告警。

## 实践背景

定期监控云服务器上某个进程（Nginx）数量，当 Nginx 进程数少于2个时发送短信告警。

## 前提条件

- 购买了腾讯云 CVM 服务器。
- 安装 Python 2.7以上环境和 pip 工具。

## 数据上报

### 步骤1：准备上报环境

参看 [CLI 方式上报数据](https://cloud.tencent.com/document/product/397/40208#cli-.E6.96.B9.E5.BC.8F.E4.B8.8A.E6.8A.A5.E6.95.B0.E6.8D.AE) 的第一和第二步，进行 TCCLI 工具的安装和配置。

### 步骤2：确定监控指标

确定需要监控的指标项，例如：

Nginx 进程数量：nginx_pro_cnt，可以使用系统命令获取：
```shell
ps aux|grep nginx|grep -v grep|wc -l
```


### 步骤3：编写 Shell

根据步骤2中获取监控指标的系统命令来编写 Shell 脚本，如下示例：

```shell
#!/bin/bash
myip=$(curl http://metadata.tencentyun.com/latest/meta-data/local-ipv4 2>>/dev/null)
while true
do
nginx_pro_cnt=$(ps aux|grep nginx|grep -v grep|wc -l)
metrics=$(cat <<EOF
[
  {
    "MetricName": "nginx_pro_cnt", 
    "Value":$nginx_pro_cnt 
  }
]
EOF
)
tccli monitor PutMonitorData --Metrics "$metrics" --AnnounceIp "$myip"  --AnnounceTimestamp $(date +%s)
#自定义监控一分钟汇聚统计一次
sleep 60
done
```


### 步骤4：执行 Shell 文件完成数据持续上报

将步骤3中的示例保存为 test.sh 后，在当前目录下执行以下命令，即可通过 Shell 脚本在后台进行目标指标的持续上报。

```shell
chmod +x test.sh
nohup ./test.sh &
```



## 数据查询

数据上报完成后，可以在 [指标视图](https://console.cloud.tencent.com/monitor/indicator-view) 看到刚才上报的数据。

## 配置告警

1. 确认用户消息通道已验证，可在 [CAM 鉴权](https://console.cloud.tencent.com/cam) 页面查看验证情况。
![](https://main.qcloudimg.com/raw/98f7a88cb0821ea4681abaf0c696da92.jpg)
2. 进入自定义监控 [指标视图](https://console.cloud.tencent.com/monitor/indicator-view) 页面，在指标视图右上角【配置告警】。
![](https://main.qcloudimg.com/raw/e7d880dc8c7dc23fbb7719be863b4555.png)
3. 根据背景需求配置告警规则，更详细的配置操作可参阅 [配置告警策略](https://cloud.tencent.com/document/product/397/40223)。
如图示例为：Nginx 进程数少于2个时发送短信告警，持续一个统计周期（1分钟），每5分钟告警一次。
 ![](https://main.qcloudimg.com/raw/c19be124dc514bad8fcfa8c6be769ba6.jpg)


## 接收告警

杀掉 Nginx 进程后，5分钟后收到短信告警，短信内容如下：
```
【腾讯云】云监控自定义监控指标告警触发
账号 ID：34xxxxxxxx，昵称：自定义监控
告警详情
告警内容：指标视图 | nginx_pro_cnt 小于2
告警对象：nginx_pro_cnt
当前数据：1
APPID：125xxxxxxx
告警策略：视图告警
触发事件：2019-12-09 22:36:00（UTC+08:00）
```

