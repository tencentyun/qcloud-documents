## 操作场景
本文档指导您将 SSL 证书部署到负载均衡。

## 前提条件
已登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)，且成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤
>!操作之前，请确认您的 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3) 是否有实例，若没有实例，请您先创建实例。
>
1. 单击**已签发**页签，选择您需要部署的证书，并单击**证书详情**。如下图所示：
![](https://main.qcloudimg.com/raw/2dce1ac04efd170c9b7f2b55b6a07ffd.png)
2. 进入 “证书详情” 管理页面，单击**一键部署**，根据项目和地区筛选 CLB 实例。如下图所示：
>!目前不支持华南地区-深圳金融。
>
![](https://main.qcloudimg.com/raw/9032f32c9b014ed7ec3c39e693d8e7f4.png)
3. 在弹出的 “选择部署类型” 窗口中，选择**负载均衡**，选择资源实例以及监听器资源。如下图所示：
>?如您的负载均衡（CLB）资源未创建监听器资源，可参考 [添加监听器](#add) 进行操作。
>
![](https://main.qcloudimg.com/raw/3f0213b7d3036d15f73bb17fe2b5bc76.png)
4. 单击**确定**，即可操作成功。如下图所示：
![](https://main.qcloudimg.com/raw/bd60fa42c113da309e99545d060939d7.png)

## 添加监听器[](id:add)
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，选择您需要配置的监听器，并单击**配置监听器**。
2. 进入实例**基本信息**页面，选择**监听器管理**页签。
3. 在 **HTTP/HTTPS 监听器**中单击**新建**，弹出**创建监听器**弹窗。
4. 将**监听协议端口**切换到 HTTPS，服务器证书可选择已有的证书。如下图所示：
>? 此处选择的**服务器证书**为需部署至负载均衡实例的证书，则无需再进行部署至负载均衡操作。
>
![](https://main.qcloudimg.com/raw/6beb94b001fb5ead265e4fff72b6674f.png)
5. 单击**提交**，即可成功配置监听器。
