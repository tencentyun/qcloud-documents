## 概述
腾讯云和权威的数字证书授权（CA）机构和专家级证书代理商合作，支持域名型、企业型、企业增强型 SSL 证书的申请和上传管理，并且腾讯云 CDN、负载均衡服务均支持 SSL 证书的快速部署。

您可以在腾讯云上一站式实现全站 HTTPS，下面详细说明如何操作。

## 前提条件
成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤
### 部署证书到负载均衡
>!操作之前，请确认您的 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3) 是否有实例，若没有实例，请您先创建实例。
>
1. 选择您需要部署的证书，单击【部署】。如下图所示：
![](https://main.qcloudimg.com/raw/fe9df64283baa8440e5a3f1c20bf93b0.png)
2. 根据项目和地区筛选 CLB 实例，且只能选择一个实例。如下图所示：
>!目前不支持华南地区-深圳金融。
>
![](https://main.qcloudimg.com/raw/3c53330b67120756393be70356189753.png)
3. 单击【确定】，跳转到 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，进入实例【基本信息】页面。
4. 选择【监听器管理】页签。
5. 在【HTTP/HTTPS 监听器】中单击【新建】，弹出【创建监听器】弹窗。
6. 将【监听协议端口】切换到 HTTPS，服务器证书为已选中的证书，然后完成剩余的基本配置。如下图所示：
![](https://main.qcloudimg.com/raw/6beb94b001fb5ead265e4fff72b6674f.png)
7. 继续完成创建监听器的其他配置，即可实现负载均衡的 HTTPS。

### 部署证书到 CDN
 >!
 - 域名需要已经接入 CDN，且状态为**部署中**或**已启动**，关闭状态的域名无法部署证书。具体操作请参考 [接入域名](https://cloud.tencent.com/document/product/228/41215)。
 - COS 或 数据万象开启 CDN 加速后，默认的 .file.myqcloud.com 或 .image.myqcloud.com 域名无法配置证书。
 - SVN 托管源暂时无法配置证书。
 
1. 选择您需要部署的证书，单击【部署】。如下图所示：
![](https://main.qcloudimg.com/raw/fe9df64283baa8440e5a3f1c20bf93b0.png)
2. 在弹出的【选择部署类型】窗口中，选择【CDN】，并单击【确定】。
3. 跳转到 [CDN 控制台](https://console.cloud.tencent.com/cdn)，进入【配置证书】详情页，已显示对应的域名、证书来源以及证书 ID。
4. 选择回源协议方式，您可以选择 CDN 节点回源站获取资源时的回源方式。如下图所示：
![](https://main.qcloudimg.com/raw/890219d7c165edf23c7fe64d14fa9c65.png)
 - 选择 **HTTP** 回源配置成功后，用户至 CDN 节点请求支持 HTTPS/HTTP，CDN 节点回源站请求均为 HTTP。
 - 选择 **协议跟随** 回源配置，您的源站需要部署有效证书，否则将导致回源失败。配置成功后，用户至 CDN 节点请求为 HTTP 时，CDN 节点回源请求也为 HTTP。用户至 CDN 节点请求为 HTTPS 时，CDN 节点回源请求也为 HTTPS。
 - 若域名源站修改 HTTPS 端口为非 443 端口，会导致配置失败。
 - COS 源或 FTP 源域名仅支持 HTTP 回源。
5. 配置成功后，您可以在【证书管理】页面看到已经配置成功的域名以及证书情况。如下图所示：
![](https://main.qcloudimg.com/raw/c30cb345a0cca5d567f3b00d1425e59e.png)
