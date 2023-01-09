## 功能介绍
CDN SaaS 证书功能提供域名证书的全生命周期管理服务，包括 ssl/tls 证书的批量申请、绑定、证书过期自动更新等服务，对于已接入腾讯云 CDN 的域名，支持通过控制台、API 的方式进行一键申请使用，助力网站建站等 SaaS 服务提供商降低运维成本，提供安全的域名访问。
>! 该功能当前处于内测中，如需使用，请联系腾讯云技术支持开通使用。

## 适用场景
**1. 域名证书批量申请、绑定**
用户加速域名具有 HTTPS 访问诉求时，需要为该域名申请绑定 ssl 证书，此时需要完成证书申请（提交资料-验证域名-等待机构签发证书）、绑定域名等操作。面对10w+级别的域名接入时（集中在泛互出海建站用户），此时使用传统的证书、申请步骤批量操作域名流程繁琐、用时较长。

**2. 域名证书批量自动续签，代维**
使用传统托管证书、证书存在有效期，过期后，可能会造成访问异常，需要为域名重新申请并绑定证书，若需要管理大量的域名，此时运维难度较大巨大，通过 SaaS 证书功能， 会实时检测证书过期时间，并自动完成续签和部署的动作。

## 使用流程
### 步骤一：开通插件中心-SAAS 证书功能
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择**插件中心**，单击 **SaaS 证书**插件功能卡片的开关按钮。
![](https://qcloudimg.tencent-cloud.cn/raw/92c455a0fbf20076919c3d3154a2ea55.png)
![](https://qcloudimg.tencent-cloud.cn/raw/bcdf918539037de8ffaf230a7b8afccc.png)
2. 开通 SaaS 证书功能，功能开通之后，可通过证书管理-SaaS 证书管理进入配置页面。
![](https://qcloudimg.tencent-cloud.cn/raw/d383b40832d65fafac524b74c8c8ccc0.png)

### 步骤二：为需要绑定证书的域名申请证书
1. 选择您要绑定证书的域名，可单选或者多选
<img src="https://qcloudimg.tencent-cloud.cn/raw/e882883e1d56fbdcdff6060545d4c4cf.png" width="70%">
2. 选择证书算法
	- RSA 加密算法：国际标准算法，应用较早的算法之一，普遍性更强，同比 ECC 算法的适用范围更广，兼容性更好，一般采用2048位的加密长度，服务端性能消耗较高。
	- ECC 加密算法：椭圆加密算法，新一代算法趋势主流，一般采用256位加密长度（相当于 RSA 3072 位加密强度）更安全，抗攻击型更强，同比 RSA 算法加密速度快，效率更高，服务器资源消耗更低。
3. 自动进行域名验证
SaaS 证书通过 HTTP 验证的方式进行域名归属验证，请您签发证书前，先确保域名 CNAME 解析正常，否则可能导致证书签发失败。
![](https://qcloudimg.tencent-cloud.cn/raw/5f87845e972d2c27ff43b4ad980ae986.png)
4. 单击**确认**，进入 SaaS 证书管理页面

### 步骤三：等待证书签发、部署
证书签发部署过程约5 - 10分钟，您可通过状态记录查看进度
![](https://qcloudimg.tencent-cloud.cn/raw/67cbd9c6afa4da0dc16441bc141bdc22.png)
<img src="https://qcloudimg.tencent-cloud.cn/raw/ade958ac8b86ebbc115b316b072ff5cc.png" width="70%">


## 费用说明
**SAAS证书** 在内测期间暂不收取费用。
