## 概述

腾讯云和权威的数字证书授权（CA）机构和专家级证书代理商合作，支持域名型、企业型、企业增强型SSL证书的申请和上传管理，并且腾讯云CDN、负载均衡服务均支持SSL证书的快速部署。

您可以在腾讯云上一站式实现全站Https，下面详细说明如何操作。

## 1. 获取证书
腾讯云SSL证书服务支持域名型（DV）SSL证书的免费申请，**企业型（OV）、企业增强型（EV）等付费证书目前支持线下选购申请**。

### 1.1 域名型证书申请入口
进入 [SSL证书管理控制台](https://console.qcloud.com/ssl) ，点击【申请证书】

![](https://mc.qcloudimg.com/static/img/4efe78b416cc29cacba1cbc2ba475bb6/2.png)

### 1.2 填写提交申请

填写申请域名，注意免费证书目前不支持一级域名申请（例如qcloud.com），请填写例如www.qcloud.com，demo.test.qlcoud.com形式二级、三级等域名。
如果需要部署到

![](https://mc.qcloudimg.com/static/img/4961164252cd488c9695475e173c0b8c/4.png)

### 1.3 DNS验证域名身份

证书默认支持手动DNS验证，验证方法可查看[详情](https://www.qcloud.com/doc/product/400/4142#2.-.E6.89.8B.E5.8A.A8dns.E9.AA.8C.E8.AF.81)。

![](https://mc.qcloudimg.com/static/img/2f90c6cdf51ec98ba0fd7a112a891e13/5.png)

如果所申请域名已成功在 [云解析平台](https://console.qcloud.com/cns/domains) 进行解析，可以支持自动DNS验证，验证方法可查看[详情](https://www.qcloud.com/doc/product/400/4142#1.-.E8.87.AA.E5.8A.A8dns.E9.AA.8C.E8.AF.81)。

![](https://mc.qcloudimg.com/static/img/8c10bfb9fa50a520e0b8b45f3b7a9f74/6.png)

提交申请成功后需要前往【证书详情页】获取CName记录添加解析，获取CName记录如Tips中显示，需要尽快成功添加解析，方可通过CA机构审核：

![](https://mc.qcloudimg.com/static/img/1f0d7d113cd4ee14cda423a32e853fe4/8.png)

### 1.4 提交申请失败

如遇到下图所示弹窗，是提交域名未通过CA机构安全审核，具体原因参考[安全审核失败原因](https://www.qcloud.com/doc/product/400/5439)。

![](https://mc.qcloudimg.com/static/img/25451d24cf3c717454830a44925642ec/1.png)

## 2. 部署证书到负载均衡
### 2.1 选择证书
首先成功申请获取证书（参考[如何免费申请域名型证书](https://www.qcloud.com/document/product/400/6814)），或者选择上传的证书，展开【更多】操作，选择【部署到负载均衡】。
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2.2 选择LB实例
根据项目和地区筛选LB实例（目前不支持华南地区-深圳金融），且只能选择一个实例。
![](https://mc.qcloudimg.com/static/img/b6261451a354dac96679737014938e52/2.png)

### 2.3 创建监听器
跳转到负载均衡控制台，打开创建监听器弹窗，并且监听协议端口已切换到Https，服务器证书为已选中的证书，然后完成剩余的基本配置。
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 2.4 继续完成配置
继续完成创建监听器的其他配置，即可实现负载均衡的Https。

## 3. 部署证书到CDN
### 3.1 选择域名
选择需要配置证书的加速域名，注意：

+ 域名需要已经接入 CDN，且状态为 **部署中** 或 **已启动**，关闭状态的域名无法部署证书；
+ COS 或 万象优图开启 CDN 加速后，默认的 .file.myqcloud.com 或 .image.myqcloud.com 域名无法配置证书；
+ SVN 托管源暂时无法配置证书。

![](https://mc.qcloudimg.com/static/img/973e75c6a0b1672f1a1f11f9667bf6f0/image.png)

### 3.2 使用腾讯云托管证书
可以在 [SSL 证书管理](https://console.qcloud.com/ssl) 页面申请证书成功颁发后，选择【腾讯云托管证书】，即可看到SSL证书管理中对该域名可用的证书列表：

![](https://mc.qcloudimg.com/static/img/8e6c6afcfa701fa4cdd3dc0711780c2b/image.png)

+ 从证书列表中选择要使用的证书；
+ 证书列表中展示格式为 证书ID（备注），可前往 [SSL 证书管理](https://console.qcloud.com/ssl) 查看更多证书详情。

### 3.3 回源方式
配置证书后，您可以选择 CDN 节点回源站获取资源时的回源方式：

![](https://mc.qcloudimg.com/static/img/ba856a03ab0709f6befaafc7840e1cc9/image.png)

+ 选择 HTTP 回源配置成功后，用户至CDN 节点请求支持 HTTPS/HTTP，CDN 节点回源站请求均为 HTTP；
+ 选择 HTTPS 回源，要求源站已经配置证书，否则可能导致回源失败。配置成功后，用户至 CDN 节点请求为 HTTP 时，CDN 节点回源请求也为 HTTP；用户至 CDN 节点请求为 HTTPS 时，CDN 节点回源请求也为 HTTPS；
+ COS 源或 FTP 源域名暂时不支持 HTTPS 回源；
+ 配置HTTPS回源，您的源站配置需要无端口约束，或配置为443端口，否则会导致配置失败。

#### 3.4 配置成功

配置成功后，您可以在【证书管理】页面看到已经配置成功的域名及证书情况：

![](https://mc.qcloudimg.com/static/img/ec3d8d968918cd3e190c4f01194a6236/2.png)
