本文档通过介绍证书申请流程，让您可以充分了解如何申请证书以及填写资料验证的过程。

## 证书申请流程
购买证书完整流程如下图所示：
![](https://main.qcloudimg.com/raw/93b1e9c4322f048313ca8806fbcf1339.png)

### 步骤1：购买证书
1. 登录腾讯云  [SSL 证书控制台](https://console.cloud.tencent.com/ssl) ，进入 “证书列表” 管理页面，单击**购买证书**。如下图所示：
>?
>- 您也可以在腾讯云 [SSL 证书购买页](https://buy.cloud.tencent.com/ssl?fromSource=ssl) 进行购买。
>- 如您对证书种类以及品牌不熟悉，可单击**快速配置**，选择系统为您推荐的证书，更快速购买证书。
>
![](https://main.qcloudimg.com/raw/f7a50b9ebe05a5d01eed80075591c641.png)
2. 选择您需要的证书种类、证书品牌、域名类型以及证书年限等。具体操作请参考 [购买流程](https://cloud.tencent.com/document/product/400/7995)。

### 步骤2：提交资料验证
 #### 方式1
**域名型（DV）免费 SSL 证书：**
证书申请完成后，需进行域名所有权验证，验证成功后 CA 机构将签发证书。详情请查看  [域名型（DV）免费证书申请流程](https://cloud.tencent.com/document/product/400/6814)。

#### 方式2
**其他品牌 OV 与 EV 型 SSL 证书：**
购买证书完成后，请登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)  ，选择并进入**待提交**管理页面，提交资料并上传确认函进行证书申请，提交申请后，需人工审核，人工审核通过后 CA 机构将签发证书。详情请查看 [其他品牌 OV 与 EV 型证书材料提交流程](https://cloud.tencent.com/document/product/400/10257)。
>?
>- 您在提交资料过程中，如勾选使用 [我的资料](https://console.cloud.tencent.com/ssl/info) 中已通过审核的公司信息以及管理人信息，则无需上传确认函。
>- GlobalSign 证书在提交资料过程中仍需上传确认函。

#### 方式3
- **域名型（DV）SSL 证书：**
购买证书完成后，请登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)  ，选择并进入**待提交**管理页面，提交资料并完成域名身份验证后，CA 机构将签发证书。详情请查看 [域名型（DV）SSL 证书提交流程](https://cloud.tencent.com/document/product/400/47285)。
- **Wotrus 品牌 OV 与 EV 型 SSL 证书：**
购买证书完成后，请登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)  ，选择并进入**待提交**管理页面，提交资料进行证书预申请，预申请审核通过后需进行域名身份验证，域名验证通过后还需进行人工审核，人工审核通过后 CA 机构将签发证书。详情请查看 [Wotrus 品牌证书 OV 与 EV 型 SSL 证书提交流程](https://cloud.tencent.com/document/product/400/47284)。
- **DNSPod 品牌国密标准（SM2）OV 与 EV 型 SSL 证书：**
购买证书完成后，请登录 [证书管理控制台](https://console.cloud.tencent.com/certoverview)  ，选择并进入**待提交**管理页面，提交资料并上传确认函以及完成域名身份验证，提交申请后，需人工审核，人工审核通过后 CA 机构将签发证书。详情请查看 [DNSPod 品牌证书 OV 与 EV 型 SSL 证书材料提交流程](https://cloud.tencent.com/document/product/400/47283)。

### 步骤3：颁发证书
证书申请通过审核后，CA 机构会为您颁发证书。

### 步骤4：安装证书
1. 重新登录 [SSL 证书控制台](https://console.cloud.tencent.com/ssl)，进入 “我的证书” 管理页面。
2. 选择您需要安装的证书，单击操作栏的**下载**。
3. 下载证书后，将证书解压后安装至您的云服务资源中。具体操作请参考 [证书安装至云服务器](https://cloud.tencent.com/document/product/400/4143)。
 
