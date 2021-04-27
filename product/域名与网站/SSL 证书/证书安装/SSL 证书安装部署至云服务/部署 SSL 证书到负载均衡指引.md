## 操作场景
本文档指导您将 SSL 证书部署到负载均衡。

## 前提条件
已登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)，且成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤
>!操作之前，请确认您的 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3) 是否有实例，若没有实例，请您先创建实例。
>
1. 单击【已签发】页签，选择您需要部署的证书，并单击【证书详情】。如下图所示：
![](https://main.qcloudimg.com/raw/2dce1ac04efd170c9b7f2b55b6a07ffd.png)
2. 进入 “证书详情” 管理页面，单击【一键部署】，根据项目和地区筛选 CLB 实例，且只能选择一个实例。如下图所示：
>!目前不支持华南地区-深圳金融。
>
![](https://main.qcloudimg.com/raw/ee23a8c2078ffbc39dba538fc007dedf.png)
3. 单击【确认】，并跳转到 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，进入实例【基本信息】页面。
4. 选择【监听器管理】页签。
5. 在【HTTP/HTTPS 监听器】中单击【新建】，弹出【创建监听器】弹窗。
6. 将【监听协议端口】切换到 HTTPS，服务器证书为已选中的证书，然后完成剩余的基本配置。如下图所示：
![](https://main.qcloudimg.com/raw/6beb94b001fb5ead265e4fff72b6674f.png)
7. 继续完成创建监听器的其他配置，即可实现负载均衡的 HTTPS。
