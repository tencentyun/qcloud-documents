## 功能介绍

腾讯云CDN默认开启TLS 1.0/1.1/1.2 ，关闭TLS 1.3，您可按需关闭/开启指定TLS版本。

>!
>- 配置前需确保已成功配置HTTPS证书。
>- 部分平台正在升级中，暂未开放此配置功能。



## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择【域名管理】，单击域名操作列的【管理】，进入域名配置页面，切换 Tab 至【HTTPS配置】，即可找到【TLS版本配置】。

默认情况下，TLS 1.0/1.1/1.2为开启状态，TLS 1.3为关闭状态：

![](https://main.qcloudimg.com/raw/62bfd147322215f5bcb5ce745505415b.png)


### 修改配置

您可按需关闭/开启指定TLS版本，单击【修改配置】：
<img src="https://main.qcloudimg.com/raw/82b93c2c47ded2029793b4931a098b29.png"/ style="height:280px">


**配置约束**

- 只可开启连续或单个版本号。例如，不可仅开启1.0和1.2而关闭1.1。
- 不可关闭全部版本。
