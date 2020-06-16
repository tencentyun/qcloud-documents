## 操作场景  
本文档指导您重颁发域名型（DV）SSL 证书。

>?
>- 证书处于已颁发状态且距过期时间大于90天才可进行重颁发操作。
>- 一张免费域名型（DV）证书只能进行一次重颁发操作。
>-  相同主域名，其中有一个子域名证书正在进行重颁发，该主域名下的其他子域名无法同时进行重颁发操作。

## 前提条件  
已登录 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)，且成功申请获取证书（参考 [如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)）。

## 操作步骤

1. 选择您需要重颁发的域名型（DV）免费证书，选择【更多】，单击【重颁发】。如下图所示：
![](https://main.qcloudimg.com/raw/632e64d7cac2650469018cde0624a2ce.png)
2. 在弹出的窗口中，单击【确定】。如下图所示：  
![](https://main.qcloudimg.com/raw/b1bb53c5c9952b4e374248b0db94418d.png)
3. 进入【证书重颁发申请】，单击【下一步】。如下图所示：
>!
> - 如果填写了私钥密码，请您牢记该密码，该密码暂不支持找回和修改。
> - 如需部署腾讯云负载均衡、CDN 等云服务，请勿填写私钥密码。
> - 如果私钥密码不慎遗忘，请 [工单联系](https://console.cloud.tencent.com/workorder/category) 腾讯云工程师删除该证书，然后重新申请该域名证书。
> 
![](https://main.qcloudimg.com/raw/2874854ea0e30182307011d70a928b82.png)
4. 系统会根据您的域名解析是否在腾讯云自行判断解析验证方式。
 - 域名解析在腾讯云，使用 “自动 DNS 验证方式”，验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E8.87.AA.E5.8A.A8-dns-.E9.AA.8C.E8.AF.81)。
![](https://main.qcloudimg.com/raw/22fe4e45b4c936c41f563424ce798c37.png)
 - 域名解析不在腾讯云，使用 “手动 DNS 验证方式”,验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/4142#.E6.89.8B.E5.8A.A8-dns-.E9.AA.8C.E8.AF.81)。
![](https://main.qcloudimg.com/raw/1ef7b8341d2a8a09def6d9181d0704a1.png)

5. 单击【确认申请】，提交证书重颁发申请。

>? 证书重颁发中，该证书的重颁发功能关闭，不能再次申请重颁发。

