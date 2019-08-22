## 操作场景
HTTPS 协议是由 SSL + HTTP 协议构建的可进行加密传输和身份认证的网络协议，比 HTTP 协议安全。若需要开启 HTTPS 加速，可通过开启播放域名的 HTTPS 功能和配置正确有效的证书来实现。您可以在腾讯云 [SSL 证书](https://cloud.tencent.com/product/ssl) 购买相应证书，若您已有 HTTPS 证书，可上传至云直播控制台进行配置。直播目前仅支持 PEM 格式，若您的证书为其它格式，需要转化为 PEM 格式。证书的格式要求和配置方法如下：


## 操作步骤
### 第一步：进入控制台
 登录 [云直播控制台](https://console.cloud.tencent.com/live)，选择左侧菜单栏的【域名管理】，单击【管理】或需配置的播放域名进入域名管理。
 ![](https://main.qcloudimg.com/raw/ba9fa1cab68838873a319f10729a1657.png)

### 第二步：编辑 HTTPS 配置
在**高级配置**菜单栏下，单击 **HTTPS 配置**模块的【编辑】，开启 HTTPS 服务并输入证书名称、证书内容和私钥内容，保存后就可以开启 HTTPS 服务。
![](https://main.qcloudimg.com/raw/679034a43612bd5bcb01d72d8b5eebd6.png)
- **证书名称**：自定义证书名称，便于标识证书。
- **证书内容**：CA 提供的证书包括 Apache、IIS、Nginx 以及 Tomcat，云直播的加密服务使用 Nginx，故配置需选择 Nginx 文件中的内容。
  ![](https://main.qcloudimg.com/raw/f67e31bfa2c233cf8dc0c4a1e58cb6fc.png)
	其中 .crt 文件是证书内容：
	![](https://main.qcloudimg.com/raw/dc6e10861dbe5c4043e07073240cf3b0.png)
  请在 HTTPS 证书内容输入框填写包含 -----BEGIN CERTIFICATE----- 和 -----END CERTIFICATE----- 的所有内容。
	>?若您的证书为中级机构颁发，并包含多个证书，证书内容请按照下述方式拼接：
	> -----BEGIN CERTIFICATE-----
	> -----END CERTIFICATE-----
	> -----BEGIN CERTIFICATE-----
	> -----END CERTIFICATE-----
- **证书私钥**：Nginx 文件中 .key 文件内容为证书私钥：
  ![](https://main.qcloudimg.com/raw/fdfe6829c5910da0742e2c3d845a8447.png)
  请在 HTTPS 私钥内容输入框填写包含 -----BEGIN RSA PRIVATE KEY----- 和 -----END RSA PRIVATE KEY----- 的所有内容。

### 第三步：验证配置
HTTPS 配置生效时间约2小时，请于提交证书后2小时左右访问该域名，若浏览器地址栏显示为 HTTPS 则说明配置成功。
![](https://main.qcloudimg.com/raw/b1f54ec35855e5d2adbaeae96a04ef13.png)

### 第四步：修改配置
HTTPS 功能支持开启和关闭。关闭此服务后，云直播将不再为该域名提供 HTTPS 服务。若证书已过期，需更新为新的有效证书。
  
