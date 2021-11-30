## 注册帐号
腾讯云平台申请证书首先需要注册腾讯云账号并且完成实名认证。
1. 新用户请单击 [腾讯云官网](https://cloud.tencent.com/) 右上角的**免费注册**，进入注册页面。
2. 请您 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)，即可登录腾讯云控制台。
3. 完成 [实名认证](https://console.cloud.tencent.com/developer/auth)，方可继续申请证书。
![](https://main.qcloudimg.com/raw/966974bf6f78e4a719a5e130254ecea9.png)

## 申请免费证书
>?
>- 免费证书仅提供二级域名及其子域名证书申请，不支持 IP 与泛域名申请。例如 `dnspod.cn`、`docs.dnspod.cn`。
>- 亚洲诚信范围内（不一定在腾讯云申请）的同一主域最多只能申请20张免费证书，申请时请注意该域名是否在其他服务商平台存在亚洲诚信下的证书，避免申请达到上限无法申请。更多详情可参考 [免费证书名额相关问题](https://cloud.tencent.com/document/product/400/46849)。
>- 免费证书到期后如需继续使用证书，请重新申请并安装。
>
1. 登录 [SSL证书管理控制台](https://console.cloud.tencent.com/ssl)，进入 “我的证书” 管理页面，并单击**申请免费证书**。如下图所示：
![](https://main.qcloudimg.com/raw/7fb2560e501edab5c8ccc162a8ea5f18.png)
2. 在弹出的**确认证书类型**窗口中，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/b97b630532f223b5628e86577fd7f55a.png)
3. 填写证书申请内容，例如 `qcloud.com`，`cloud.tencent.com`，`demo.test.qlcoud.com`，并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/b7142c496f76d90c0922b918434ee588.png)
 - **算法选择**：勾选所需证书的加密算法。加密算法具体内容可查看 [RSA 加密算法与 ECC 加密算法的区别？](https://cloud.tencent.com/document/product/400/54179)
 - **证书绑定域名**：即绑定证书的域名，请填写单个域名。例如 `tencent.com`、`ssl.tencent.com`。
 - **申请邮箱**：请输入您的邮箱地址。
 - **证书备注名**：可选，请输入证书的备注名称，不可超过200字。
 - **私钥密码**：可选，为了保障私钥安全，目前**不支持密码找回**功能，请您牢记私钥密码。
>!如需部署腾讯云负载均衡、CDN 等云服务，请勿填写私钥密码。
 - **标签**：请选择您的标签键和标签值，方便您管理腾讯云已有的资源分类。
>?如需添加标签，请参考 [管理标签](https://cloud.tencent.com/document/product/651/36480)。
 - **所属项目**：请选择您证书所属项目，方便您通过项目管理您的证书。
4. 选择域名验证方式，并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/c69d7ca9df2d0951e7790abf839f03e1.png)
 - **选择自动添加 DNS**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54499)。
>?若申请的域名已成功托管在 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns/domains)，可支持自动添加 DNS。
 - **选择 DNS 验证**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54500)。
 - **选择文件验证**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54501)。
5. 根据【验证操作】提示，完成域名身份验证。
>?单击**查看域名验证状态**，即可查看当前域名验证的状态。
>- 验证中：系统正在进行验证检查。
>- 等待验证：等待添加域名验证操作。
>- 验证超时：系统进行验证检查超过30s未成功检查将显示验证超时。
>- 已通过：已通过域名验证所有权认证。
>- 验证失败：验证期内未完成验证域名显示验证失败。
6. 域名验证通过后，CA 机构将在24小时内完成签发证书操作，请您耐心等待。

>!提交域名未通过 CA 机构安全审核，具体原因参考 [安全审核失败原因](https://cloud.tencent.com/document/product/400/5439)。
>
## 下载和部署
完成域名审核后，颁发的证书即可单击**下载**到本地进行安装部署或部署到腾讯云相关云服务上。相关操作请参见：[如何选择 SSL 证书安装部署类型？](https://cloud.tencent.com/document/product/400/4143)

## 相关问题
- [免费 SSL 证书名额相关问题](https://cloud.tencent.com/document/product/400/46849)
- [SSL 证书配置的 TXT 解析是否可以删除？](https://cloud.tencent.com/document/product/400/46864)
- [忘记私钥密码怎么办？](https://cloud.tencent.com/document/product/400/7421)
- [免费 SSL 证书一直在待验证怎么办？](https://cloud.tencent.com/document/product/400/46870)


