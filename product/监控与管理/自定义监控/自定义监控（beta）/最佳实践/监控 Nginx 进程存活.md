# 最佳实践：监控Nginx进程存活

本文介绍如何使用shell命令+CLI方式上报Nginx进程存活数据至自定义监控，查看指标并配置告警。

## 实践背景

定期监控云服务器上某个进程（Nginx）数量，当Nginx进程数少于2个时发送短信告警。

## 前提条件

- 购买了腾讯云CVM服务器，有登录服务器权限。
- 安装 Python 2.7以上环境和 pip 工具。

## 数据上报

### 步骤1：准备上报环境

参看[CLI方式上报数据](./上报监控指标数据)的第一和第二步，进行TCCLI工具的安装和配置。

### 步骤2：确定监控指标

确定需要监控的指标项，例如：

- Nginx进程数量：nginx_pro_cnt，可以使用系统命令获取
  `ps aux|grep nginx|grep -v grep|wc -l`

### 步骤3：编写shell

根据步骤2中获取监控指标的系统命令来编写shell脚本，如下示例：

```
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

### 步骤4：执行shell文件完成数据持续上报

将步骤3中的示例保存为test.sh后，在当前目录下执行以下命令，即可通过shell脚本在后台进行目标指标的持续上报。

```
chmod +x test.sh
nohup ./test.sh &
```



## 数据查询

数据上报完成后，可以在 [指标视图](https://console.cloud.tencent.com/monitor/indicator-view) 看到刚才上报的数据。

## 配置告警

1. 确认用户消息通道已验证，可在[CAM鉴权](https://console.cloud.tencent.com/cam)页面查看验证情况。
   ![](https://main.qcloudimg.com/raw/91e3beb4e4558261a58d0e57bf16b60f.png)

2. 单击在指标视图右上角【配置告警】。
   ![](https://main.qcloudimg.com/raw/96ec7d8d95fe24a5e20ac5499f52b986.png)

3. 根据背景需求配置告警规则，更详细的配置操作可参阅[配置告警策略]()。

   > Nginx进程数少于2个时发送短信告警，持续一个统计周期（1分钟），每5分钟告警一次。
   >
   > ![](https://main.qcloudimg.com/raw/b05f4bded7f492decbe79905ccc328fe.png)

## 接收告警

杀掉Nginx进程后，5分钟后收到短信告警。
![](https://main.qcloudimg.com/raw/dfa7493cf4a3b3bd5163dbd44aeeeeef.png)



