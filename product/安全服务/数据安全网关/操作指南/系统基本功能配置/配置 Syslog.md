## 操作场景

本文为您详细介绍配置堡垒机的 Syslog，将堡垒机运行产生的日志发生到 Syslog 服务器。


## 操作步骤

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录堡垒机。
2. 单击<img src=" https://main.qcloudimg.com/raw/82dfc809b5df76ff939d996ea3136a43.png"  style="margin:0;">，选择【系统配置】>【Syslog】，进入 Syslog 配置页面。
3. 配置如下相关信息：
 - 发送协议：根据实际环境选择 Syslog 协议。
 - IP 地址：Syslog 服务器 IP 地址。
 - IP 端口：Syslog 服务器运行的 Syslog 端口，默认为514。
 - 发送日志类型：勾选需要发送到 Syslog 服务器的日志类型。日志类型有内部审计日志、行为审计日志、行为审计命令日志、登录日志。
![](https://main.qcloudimg.com/raw/2cb86c4e4d92772d4536a769fe5633a6.png)
4. 配置完毕，单击【保存】，保存配置。
5. 单击【开启】，即可开启 Syslog。
