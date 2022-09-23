### 控制台报错 InternalError 要如何处理？
1. 非主账号在购买 EMR 集群时报错 InternalError。
问题原因：当前登录账号缺少权限。
解决方案：需先确定当前登录账号进行了实名认证，然后确认被授予了支付权限。
2. 非主账号单击控制台**硬件管理**时报错 InternalError。
问题原因：当前登录账号缺少权限。
解决方案：打开如下链接：
`https://console.cloud.tencent.com/cam/role/grant?roleName=EMR_QCSRole&policyName=QcloudAccessForEMRRole&principal=eyJzZXJ2aWNlIjoiZW1yLmNsb3VkLnRlbmNlbnQuY29tIn0=&serviceType=EMR`，然后使用主账号授予 EMR 权限即可。

