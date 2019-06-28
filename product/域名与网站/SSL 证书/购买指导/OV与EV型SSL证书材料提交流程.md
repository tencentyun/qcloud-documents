## 概述
腾讯云和权威的数字证书授权（CA）机构和专家级证书代理商合作，支持域名型、企业型、企业增强型 SSL 证书的申请和上传管理，并且腾讯云 CDN、负载均衡服务均支持 SSL 证书的快速部署。

您可以在腾讯云上一站式实现全站 Https，下面详细说明如何操作。

## 获取证书

腾讯云 SSL 证书服务支持域名型（DV） SSL 证书的免费申请。**企业型（OV）、企业增强型（EV）等付费证书目前支持线下选购申请**。

### 域名型证书申请入口
登录 [SSL证书管理控制台](https://console.cloud.tencent.com/ssl) ，单击【申请免费证书】。如下图所示：
![](https://main.qcloudimg.com/raw/2e3f8ffb5e7d6ed5b61aa0302aa1e481.png)

### 填写证书申请内容
填写申请域名，例如`qcloud.com`，`cloud.tencent.com`，`demo.test.qlcoud.com`。如下图所示：
>!如果需要部署到腾讯云负载均衡、CDN 等云服务，请勿填写私钥密码。

 ![](https://main.qcloudimg.com/raw/a73fa28bc925e65c03302e09dfa68a96.png)

### DNS 验证域名身份
- 选择手动 DNS 验证：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E6.89.8B.E5.8A.A8-dns-.E9.AA.8C.E8.AF.81)。如下图所示：
![](https://main.qcloudimg.com/raw/b837e572505d9ba789c008045ff443cf.png)
- 选择文件验证：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E6.96.87.E4.BB.B6.E9.AA.8C.E8.AF.81)。如下图所示：
![](https://main.qcloudimg.com/raw/37704d3dbbf30c92c207e001b4f76d40.png)
- 选择自动 DNS 验证：如果所申请域名已成功在 [云解析平台](https://console.cloud.tencent.com/cns/domains) 进行解析，可以支持自动 DNS 验证，验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E8.87.AA.E5.8A.A8-dns-.E9.AA.8C.E8.AF.81)。如下图所示：
![](https://main.qcloudimg.com/raw/98753e63341655f8391629922ec8f552.png)

### 提交申请
 - 若提交申请成功，需要单击【证书详情页】获取 TXT 记录尽快添加解析，方可通过 CA 机构审核。如下图所示：
 ![](https://main.qcloudimg.com/raw/17d8498c9607da699d6d8645699299a0.png)
 - 若提交申请失败，提交域名未通过 CA 机构安全审核，具体原因参考 [安全审核失败原因](https://cloud.tencent.com/doc/product/400/5439)。如下图所示：
![](https://mc.qcloudimg.com/static/img/25451d24cf3c717454830a44925642ec/1.png)

## 部署证书到负载均衡

### 选择证书
1. 首先成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。
2. 选择您需要部署的证书，展开【更多】操作，选择【部署到负载均衡】。如下图所示：
![](https://main.qcloudimg.com/raw/e59be48a8f0db68680611e4a9e40159f.png)

### 选择LB实例
根据项目和地区筛选 LB 实例，且只能选择一个实例。如下图所示：
>!目前不支持华南地区-深圳金融。
>
![](https://main.qcloudimg.com/raw/ef50fc5201e6e863dd409f101836dde9.png)

### 创建监听器
1. 跳转到负载均衡控制台，选择【监听器管理】页签。
2. 在【HTTP/HTTPS 监听器】中单击【新建】，弹出【创建监听器】弹窗。
3. 将【监听协议端口】切换到 HTTPS，服务器证书为已选中的证书，然后完成剩余的基本配置。如下图所示：
![](https://main.qcloudimg.com/raw/1816b8b07d1cfac0a603fbb2229b6873.png)

### 继续完成配置
继续完成创建监听器的其他配置，即可实现负载均衡的 Https。

## 部署证书到CDN

### 选择证书
1. 首先成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。
2. 选择您需要部署的证书，展开【更多】操作，选择【部署到国内 CDN】。如下图所示：
![](https://main.qcloudimg.com/raw/e59be48a8f0db68680611e4a9e40159f.png)

### 选择域名
跳转到 CDN 控制台，进入【配置证书】详情页，选择需要配置证书的域名。如下图所示：
>!
- 域名需要已经接入 CDN，且状态为 **部署中** 或 **已启动**，关闭状态的域名无法部署证书；
- COS 或 数据万象开启 CDN 加速后，默认的 .file.myqcloud.com 或 .image.myqcloud.com 域名无法配置证书；
- SVN 托管源暂时无法配置证书。

 ![](https://main.qcloudimg.com/raw/e56a5c8afd69ced54b177fa904f08bcb.png)

### 使用腾讯云托管证书
在 [SSL 证书管理](https://console.cloud.tencent.com/ssl) 页面申请证书成功颁发后，选择【腾讯云托管证书】，即可看到 SSL 证书管理中对该域名可用的证书列表。如下图所示：
![](https://main.qcloudimg.com/raw/8c5a9bbb0c7970f29c1608c308e1855f.png)
>?
- 从证书列表中选择要使用的证书。
- 证书列表中展示格式为**证书 ID（备注）**，可前往 [SSL 证书管理](https://console.cloud.tencent.com/ssl) 查看更多证书详情。

### 回源方式
配置证书后，您可以选择 CDN 节点回源站获取资源时的回源方式。如下图所示：
![](https://main.qcloudimg.com/raw/12c923e7d396fe7a73ba783620d41ec0.png)
>?
- 选择 HTTP 回源配置成功后，用户至 CDN 节点请求支持 HTTPS/HTTP，CDN 节点回源站请求均为 HTTP。
- 选择 HTTPS 回源，要求源站已经配置证书，否则可能导致回源失败。配置成功后，用户至 CDN 节点请求为 HTTP 时，CDN 节点回源请求也为 HTTP；用户至 CDN 节点请求为 HTTPS 时，CDN 节点回源请求也为 HTTPS。
- COS 源或 FTP 源域名暂时不支持 HTTPS 回源。
- 配置 HTTPS 回源，您的源站配置需要无端口约束，或配置为 443 端口，否则会导致配置失败。

### 配置成功
配置成功后，您可以在【证书管理】页面看到已经配置成功的域名以及证书情况。如下图所示：
![](https://main.qcloudimg.com/raw/f7b25ffdbe6ec31d38077a5574f73e2b.png)

