## 操作场景
本文档指导您将 SSL 证书支持部署到负载均衡。

## 前提条件
已登录 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)，且成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤
1. 选择您需要部署的证书，展开【更多】，选择【部署到负载均衡】。如下图所示：
![](https://main.qcloudimg.com/raw/e59be48a8f0db68680611e4a9e40159f.png)
2. 根据项目和地区筛选 LB 实例，且只能选择一个实例。如下图所示：
>!目前不支持华南地区-深圳金融。
>
![](https://main.qcloudimg.com/raw/ef50fc5201e6e863dd409f101836dde9.png)
3. 跳转到负载均衡控制台，选择【监听器管理】页签。
4. 在【HTTP/HTTPS 监听器】中单击【新建】，弹出【创建监听器】弹窗。
5. 将【监听协议端口】切换到 HTTPS，服务器证书为已选中的证书，然后完成剩余的基本配置。如下图所示：
![](https://main.qcloudimg.com/raw/b09b40de147452e036a4d2e9b8d6ac16.png)
6. 继续完成创建监听器的其他配置，即可实现负载均衡的 HTTPS。
