## 连接流程

![快速入门](https://mc.qcloudimg.com/static/img/8fbd4b6fe3c5694b4d664b31d590fc4a/image.png)
### 创建 Anycast 型 EIP

1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip
)，单击 【申请】 按钮。

 ![p1](https://mc.qcloudimg.com/static/img/a18a018f87701fd94182da23fb47188b/image.png)

2. 根据您的需求选择地域、带宽上限、数量，IP 地址类型选择 【加速 IP 地址】，再单击 【确定】 即可创建 Anycast 型 EIP。

 ![p2](https://main.qcloudimg.com/raw/f5a79c4df0aa779f3ff3c1327a250258.png)
 
### 绑定后端资源

登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip
) 后，选择 【更多】>【绑定】，绑定指定的资源，本文档以 CVM 为例。

 ![p3](https://mc.qcloudimg.com/static/img/22bf3f0500051c8929c39e7c60151ee2/image.png)
 
### 用加速 EIP 连接公网

登录您已绑定的后端资源后，即可通过加速 EIP 连接公网，使用 Anycast 公网加速。本文档中已绑定 CVM，即登录 CVM 后即可使用 Anycast 公网加速。

## 其他常见操作
### 变更 Anycast 弹性公网 IP 配置
#### 调整带宽

登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip )，在 EIP 列表中，选择要使用的 EIP，单击 【调整带宽】 即可。

 ![p4](https://mc.qcloudimg.com/static/img/18b5b10ac608d096578495f3e0c69d73/image.png)
