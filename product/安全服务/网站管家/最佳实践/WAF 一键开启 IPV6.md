Web 应用防火墙提供域名 IPv6接入配置和防护能力，在开启 IPv6功能后，Web 应用防火墙与用户源站之间的链路将支持 IPv6功能。

## 前提条件
- SAAS-WAF 开启 IPv6 需要 WAF 版本为企业版及以上版本。
- CLB-WAF 支持全版本开启 IPv6。
- 开启 IPv6功能前，请核实**源站业务是否支持 IPv6**，同时源站回源地址也需要新增 IPv6回源。


## 操作步骤
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，在左侧导航栏选择**接入管理**。
2. 在域名列表域名，选择要开启 IPv6功能的域名，单击![](https://qcloudimg.tencent-cloud.cn/raw/4c2a6f21d580a298869fd5455dbf46f1.png)。
![](https://qcloudimg.tencent-cloud.cn/raw/246b09ddb9b62b638fc37a7325904adb.png)
3. 单击**确认**，即可开启 IPv6功能。
![](https://qcloudimg.tencent-cloud.cn/raw/b5b8c1db4b8b877679afa34538d92710.png)
4. 验证 IPv6是否开启。Dig 域名 AAAA 记录后即可查看 WAF 是否开启 IPv6，出现 IPv6地址后即为开启成功。
![](https://qcloudimg.tencent-cloud.cn/raw/76c1a8076691df60d42411fcb0594ddc.png)


## 热点问题
### 如果源站没有设置 IPv6回源，那访问端是否支持以 IPv6形式访问？
当源站没有 IPv6资源时，访问端以 IPv6形式访问，WAF 会自行将资源转换为 IPv4回源。

### 如果源站没有设置 IPv4回源，那访问端是否支持以 IPv4形式访问？
当源站没有 IPv4资源时，访问端以 IPv4形式访问，WAF 会自行将资源转换为 IPv6回源。

即 WAF 会自行转换 IPv4与 IPv6，使其符合源站对应的回源。
![](https://qcloudimg.tencent-cloud.cn/raw/9c24a1f20a3fcf8cc8c3d14df3662305.png)

### 当开启 IPv6选项后，提示“实例所属集群节点升级中”等异常报错如何处理？
当出现异常报错时，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

### 开启 IPv6选项后，支持开启单个域名吗?
目前支持单个域名开启 IPv6。
