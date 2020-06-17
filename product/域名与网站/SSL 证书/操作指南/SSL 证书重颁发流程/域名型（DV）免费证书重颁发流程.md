## 操作场景  
本文档指导您重颁发域名型（DV）SSL 证书。

>?
>- 证书处于**已颁发状态且距过期时间大于90天**才可进行重颁发操作。
>- 1张免费域名型（DV）证书只能进行1次重颁发操作。
>-  相同主域名，若其中有1个子域名证书正在进行重颁发，该主域名下的其他子域名无法同时进行重颁发操作。

## 前提条件  
已登录 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)，且成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤
1. 选择您需要重颁发的域名型（DV）免费证书，选择【更多】，单击【重颁发】。如下图所示：
![](https://main.qcloudimg.com/raw/547a300d88112bfcb039321f3aac3be0.png)
2. 在弹出的窗口中，单击【确定】。如下图所示：  
![](https://main.qcloudimg.com/raw/dcffc9884db213c9804522c7efafcd83.png)
3. 进入【证书重颁发申请】页面，单击【下一步】。如下图所示：
>!
> - 如果填写了私钥密码，请您牢记该密码，该密码暂不支持找回和修改。
> - 如需部署腾讯云负载均衡、CDN 等云服务，请勿填写私钥密码。
> - 如果私钥密码不慎遗忘，请 [工单联系](https://console.cloud.tencent.com/workorder/category) 腾讯云工程师删除该证书，然后重新申请该域名证书。
> 
![](https://main.qcloudimg.com/raw/7a327a794549e0eb36d42565eee23be0.png)
4. 查看域名身份验证方式，系统会采用该证书首次申请时的域名验证方式，请您按照原来的方式进行验证即可。
例如，您之前申请该证书的域名验证方式为 “自动 DNS 验证”，重颁发过程则仍使用 “自动 DNS 验证”。验证方法可查看 [域名验证指引](https://cloud.tencent.com/document/product/400/4142)。
![](https://main.qcloudimg.com/raw/22fe4e45b4c936c41f563424ce798c37.png)
5. 单击【确认申请】，提交证书重颁发申请。

>! 证书重颁发中，该证书的重颁发功能关闭，不能再次申请重颁发。

