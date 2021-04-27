## 注册帐号
腾讯云平台申请证书首先需要注册腾讯云账号并且完成实名认证。
1. 新用户请单击 [腾讯云官网](https://cloud.tencent.com/) 右上角的【免费注册】，进入注册页面。
2. 请您 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)，即可登录腾讯云控制台。
3. 完成 [实名认证](https://console.cloud.tencent.com/developer/auth)，方可继续申请证书。
![](https://main.qcloudimg.com/raw/966974bf6f78e4a719a5e130254ecea9.png)

## 申请免费证书
>?
>- 免费证书提供二级域名证书申请。
>- 亚洲诚信范围内（不一定在腾讯云申请）的同一主域最多只能申请20张免费证书，申请时请注意该域名是否在其他服务商平台存在亚洲诚信下的证书，避免申请达到上限无法申请。更多详情可参考 [免费证书名额相关问题](https://cloud.tencent.com/document/product/400/46849)。
>- 如需要给二级域名进行配置证书，请您单独对该二级域名进行申请证书。
>- 免费证书到期后如需继续使用证书，请重新申请并安装。
>
1. 登录 [SSL证书管理控制台](https://console.cloud.tencent.com/ssl)，选择【证书管理】>【证书列表】，单击【申请免费证书】。如下图所示：
![](https://main.qcloudimg.com/raw/7fb2560e501edab5c8ccc162a8ea5f18.png)
2. 在弹出的【确认证书类型】窗口中，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/b97b630532f223b5628e86577fd7f55a.png)
3. 填写证书申请内容，例如 `qcloud.com`，`cloud.tencent.com`，`demo.test.qlcoud.com`，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/94b5d0af2af5a11d5eb7a0c8f11a54bd.png)
 - **算法选择**：勾选所需证书的加密算法。加密算法具体内容可查看 [RSA 加密算法与 ECC 加密算法的区别？](https://cloud.tencent.com/document/product/400/54179)
 - **证书绑定域名**：即绑定证书的域名，请填写单个域名。例如 tencent.com、ssl.tencent.com。
 - **申请邮箱**：请输入您的邮箱地址。
 - **证书备注名**：可选，请输入证书的备注名称，不可超过200字。
 - **私钥密码**：可选，为了保障私钥安全，目前**不支持密码找回**功能，请您牢记私钥密码。
>!如需部署腾讯云负载均衡、CDN 等云服务，请勿填写私钥密码。
 - **标签**：请选择您的标签键和标签值，方便您管理腾讯云已有的资源分类。
 >?如需添加标签，请参考 [管理标签](https://cloud.tencent.com/document/product/651/36480)。
 - **所属项目**：请选择您证书所属项目，方便您通过项目管理您的证书。
4. 选择域名验证方式，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/9adc3968c25a0745988d015a4c1ed1ca.png)
 - **选择自动添加 DNS**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54499)。
>?如果所申请域名成功添加 [DNS 解析平台](https://console.cloud.tencent.com/cns/domains)，可以支持自动添加 DNS。
 - **选择 DNS 验证**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54500)。
 - **选择文件验证**：验证方法可查看 [详情](https://cloud.tencent.com/document/product/400/54501)。
5. 根据【验证操作】提示，完成域名身份验证即可获取证书。
>?单击【查看域名验证状态】，即可查看当前域名验证的状态。
>- 验证中：系统正在进行验证检查。
>- 等待验证：等待添加域名验证操作。
>- 验证超时：系统进行验证检查超过30s未成功检查将显示验证超时。
>- 已通过：已通过域名验证所有权认证。
>- 验证失败：验证期内未完成验证域名显示验证失败。

>!提交域名未通过 CA 机构安全审核，具体原因参考 [安全审核失败原因](https://cloud.tencent.com/document/product/400/5439)。
>
## 下载和部署
完成域名审核后，颁发的证书可下载到本地，或者部署到腾讯云相关云服务。如下图所示：
![](https://main.qcloudimg.com/raw/5c3b23c2abb7e3dfa75e5847a8945987.png)


