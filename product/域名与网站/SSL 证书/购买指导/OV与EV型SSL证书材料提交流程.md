企业型 OV（包括企业型专业版 OV Pro）与增强型 EV（包括增强型专业版 EV Pro）SSL 证书在购买成功后（详情见购买流程），需要进行相关材料提交。
CA 认证审核通过后，会正式颁发证书，用户可下载付费证书进行安装。

### 1. 证书材料提交入口

1. 登录 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)。
2. 在 “证书列表” 页面，选择已购买到的证书行，单击【提交资料】。如下图所示：
![](https://main.qcloudimg.com/raw/d440dc0710e5d5219be5892e3766c539.png)

### 2. 填写域名

根据实际需求，选择 CSR 生成方式。
- 选择 “在线生成CSR” 方式，执行 [在线生成 CSR 的操作](#SitemapCSR)。
- 选择 “粘贴CSR” 方式，执行 [粘贴 CSR 的操作](#PasteCSR)。

<span id="SitemapCSR"></span>
#### 在线生成 CSR
>? 不同域名类型的证书，需填写信息略有不同。本操作以多域名证书为例。
>
1. 填写域名信息。如下图所示：
![](https://main.qcloudimg.com/raw/69e519cf60d0e7fd4873371560a98c6b.png)
主要参数信息如下：
 - 通用名称：填写绑定证书的域名/泛域名。
 - 域名：填写与通用名称不同的其它域名/泛域名。
 >? 单个域名证书无此参数。
 - 私钥密码：可选填，填写后不可更改。
2. 填写公司信息。
>? 请如实填写公司名称（全称），公司部门，公司所在城市与地址以及公司固话号码。
3. 单击【下一步】，[补充信息](#AdditionalInformation)。

<span id="PasteCSR"></span>
#### 粘贴 CSR

>? 不同域名类型的证书，需填写信息略有不同。本操作以单个带通配符的域名为例。
>
1. 将已准备好的 CSR 信息粘贴至文本框中，输入“域名信息”，并如实填写公司名称（全称），公司部门，公司所在城市与地址以及公司固话号码等公司相关信息。如下图所示：
![](https://main.qcloudimg.com/raw/f3088fe45f96672af78a2119ab7a104a.png)
2. 单击【下一步】，[补充信息](#AdditionalInformation)。

<span id="AdditionalInformation"></span>
### 3. 补充信息

1. 填写管理人信息与联系人信息。如果两者信息一致，可勾选 “与管理人相同”。如下图所示：
![](https://main.qcloudimg.com/raw/beb2eb64e7163005cbf22bec356827d2.png)
2. 单击【下一步】。
3. 在弹出的 “提交CSR” 窗口中，单击【确定】，进行 CSR 提交。   
![](https://main.qcloudimg.com/raw/e73c64688de642b0ca333f518c9973d1.png)

### 4. 上传审核

>! GlobalSign EV 证书相关盖章文件在您递交审核后，证书审核机构会在2 - 3个工作日内通过邮件发送给您，不需要控制台上传。
>
1. 单击【下载确认函】，进行确认函信息补充填写。如下图所示：
![](https://main.qcloudimg.com/raw/d9e1b51451e4ca51e6ac2f9a85162c11.png)
2. 完成确认函填写后，加盖公章，并进行文件扫描。
3. 单击【上传审核】，确认函上传。
4. 在弹出的“已提交”窗口中，确认信息，单击【确定】，并等待线下亚洲诚信工作人员与 CA 机构对提交材料进行确认与审核。如下图所示：
![](https://main.qcloudimg.com/raw/ca877a9432947956a78d6f65893c8dbb.png)
