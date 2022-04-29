Web 应用防火墙提供域名 IPV6 接入配置和防护能力，在开启 IPV6 功能后，Web 应用防火墙与用户源站之间的链路将支持 IPV6 功能。

## 前提条件
- SAAS-Waf 开启 IPV6 需要 waf 版本为企业版以上。
- CLB-Waf 支持全版本开启 IPV6。
- 开启 IPV6 功能前，请核实**源站业务是否支持 IPV6**，同时源站回源地址也需要新增 IPV6 回源。


## 操作步骤
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，在左侧导航栏选择**域名列表**。
2. 在域名列表域名，选择要开启 IPV6功能的域名，单击![](https://qcloudimg.tencent-cloud.cn/raw/4c2a6f21d580a298869fd5455dbf46f1.png)。
![](https://qcloudimg.tencent-cloud.cn/raw/246b09ddb9b62b638fc37a7325904adb.png)
3. 单击**确认**，即可开启 IPV6功能。
![](https://qcloudimg.tencent-cloud.cn/raw/b5b8c1db4b8b877679afa34538d92710.png)
4. 验证 IPV6 是否开启。Dig 域名 AAAA记录后即可查看 waf 是否开启 IPV6，出现 IPV6 地址后即为开启成功。
![](https://qcloudimg.tencent-cloud.cn/raw/76c1a8076691df60d42411fcb0594ddc.png)


## 热点问题
### 如果源站没有设置 IPv6 回源，那访问端是否支持以 IPV6 形式访问？
当源站没有 IPv6资源时，访问端以 IPv6形式访问，waf会自行将资源转换为 IPv6回源。


### 如果源站没有设置 IPv4 回源，那访问端是否支持以 IPV4形式访问？
当源站没有V4资源时，访问端以V4形式访问，waf会自行将资源转换为V6回源。

即 waf 会自行转换I PV4与 IPV6，使其符合源站对应的回源。
![](https://qcloudimg.tencent-cloud.cn/raw/9c24a1f20a3fcf8cc8c3d14df3662305.png)

### 当开启 IPv6选项后，出现提示当前“实例所属集群节点升级中”等异常报错怎么办？
当出现异常报错时，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

### 开启 IPV6选项后，支持开启单个域名吗?
目前在开启 IPV6开关后，会开启实例内所有域名的 IPV6，针对单个域名开启还在优化中。
