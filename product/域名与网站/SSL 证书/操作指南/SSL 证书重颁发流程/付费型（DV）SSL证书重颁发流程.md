付费型（DV）SSL证书重颁发流程

### 操作场景  
本文档指导您重颁发付费型（DV）SSL证书。

> 说明：
证书处于已颁发状态且距过期时间大于90天才可进行重颁发操作。

### 前提条件  
已登录 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)，且成功申请获取付费型（DV）SSL证书。

### 操作步骤

1.  选择您需要重颁发的付费型（DV）SSL证书，单击展开【更多】，选择【重颁发】。如下图所示：

![](https://main.qcloudimg.com/raw/632e64d7cac2650469018cde0624a2ce.png)

2.在弹出的温馨提示弹窗中，单击【确定】。如下图所示：  
![](https://main.qcloudimg.com/raw/b1bb53c5c9952b4e374248b0db94418d.png)

3.进入证书重颁发申请页，选择CSR方式。

![](https://main.qcloudimg.com/raw/28c50c2ac83db56720da63ee4cedda7c.png)


+ **复用证书CSR**：使用该证书重颁发前的CSR。
+ **在线生成CSR**：由平台生成和管理您的CSR。
+ **粘贴已有CSR**：使用已有的CSR内容添加到该证书。

> 注意：
> 
> - 如果填写了私钥密码，请您牢记该密码，该密码暂不支持找回和修改。推荐使用在线生成CSR，由平台生成和管理您的私钥和公钥证书文件，避免私钥文件丢失。
> - 如需部署腾讯云负载均衡、CDN等云服务，请勿填写私钥密码。
> - 如果私钥密码不慎遗忘，请 [工单联系](https://console.cloud.tencent.com/workorder/category) 腾讯云工程师删除该证书，然后重新申请该域名证书。


4.单击【确认并进入下一步】，进入域名身份验证。
![](https://main.qcloudimg.com/raw/1ef7b8341d2a8a09def6d9181d0704a1.png)

5.付费（DV）SSL证书会根据初次申请时的验证方式进行验证，验证方可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E6.89.8B.E5.8A.A8-dns-.E9.AA.8C.E8.AF.81)。

6.单击【确认申请】，提交证书重颁发申请。

![](https://main.qcloudimg.com/raw/e218e49062a1365ffff9311e9cfbff69.png)

6.您可以单击【查看证书详情】查看重颁发证书详情并根据指引进行域名验证证。如下图所示：
![](https://main.qcloudimg.com/raw/5b59f0f4297987f326517ced6c665e43.png)

> 说明：
.
> - 提交成功后需要在三天时间内完成DNS解析记录或文件记录的添加，否则审核将会失败。
> - 证书重颁发中，该证书的重颁发功能关闭，不能再次申请重颁发。



