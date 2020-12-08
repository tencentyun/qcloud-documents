## 操作场景
HTTPS 协议是由 SSL + HTTP 协议构建的可进行加密传输和身份认证的网络协议，比 HTTP 协议安全。若需要开启 HTTPS 加速，可通过开启播放域名的 HTTPS 功能和配置正确有效的证书来实现。您可以在腾讯云 [SSL 证书](https://cloud.tencent.com/product/ssl) 购买相应证书，若您已有 HTTPS 证书，可上传至云直播控制台进行配置。直播目前仅支持 PEM 格式，若您的证书为其它格式，需要转化为 PEM 格式。证书的格式要求和配置方法如下：

## 前提条件
- 已登录 [云直播控制台](https://console.cloud.tencent.com/live)。
- 已 [添加播放域名](https://cloud.tencent.com/document/product/267/20381)。


## 操作步骤 
### 步骤1：编辑 HTTPS 配置
1. 进入[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)，单击需配置的**播放域名**或右侧的【管理】进入域名详情页。
2. 选择【高级配置】，查看【HTTPS 配置】标签。
3. 单击【编辑】进入 HTTPS 配置页，单击![](https://main.qcloudimg.com/raw/897761946b06e8f904bfa6301d282817.png)按钮选择开启 HTTPS 服务。
4. 选择证书来源，选择配置的证书来源，并填写相关信息，单击【保存】即可。
<table>
<tr><th>当选择证书来源类型为</th><th>需要填写</th></tr>
<tr>
<td>自有证书</td>
<td><ul style="margin:0">
<li>证书名称：可自定义，便于标识证书。</li>
<li>证书内容：填写 Nginx 文件中的<code>.crt</code> 文件内容，具体请参见 <a href="#content">证书内容</a>。</li>
<li>私钥内容：填写 Nginx 文件中的 <code>.key</code> 文件内容，具体请参见 <a href="#private_key">证书密钥</a>。</li><ul></td>
</tr><tr>
<td>腾讯云托管证书</td>
<td>证书列表：选择在腾讯云 <a href="https://console.cloud.tencent.com/ssl">SSL 证书服务</a> 中已经上传的证书。</td>
</tr></table>
<img src="https://main.qcloudimg.com/raw/2f38a79d4c4ccdbf0e14153a1b9b6603.png"></img>

#### 证书说明：
[CA](https://cloud.tencent.com/document/product/400/18504#354) 提供的证书包括 Apache、IIS、Nginx 以及 Tomcat。**云直播的加密服务使用 Nginx，故配置需选择 Nginx 文件中的内容**。 
进入【SSL 证书控制台】>【[证书管理](https://console.cloud.tencent.com/ssl)】，选择您需要查看的证书，单击操作栏的【下载】，并进行解压后即可获得以下文件：
  ![](https://main.qcloudimg.com/raw/f67e31bfa2c233cf8dc0c4a1e58cb6fc.png)
- <b id="content">证书内容</b>：选择 Nginx 中的 `.crt` 文件，输入框填写包含 `-----BEGIN CERTIFICATE-----` 和 `-----END CERTIFICATE-----` 的所有内容。
**内容示例：**
![](https://main.qcloudimg.com/raw/e6c61fda3637a2f11e56cec30f0f7bd3.png)
>?若您的证书为中级机构颁发，并包含多个证书，证书内容请按照下述方式拼接：
> -----BEGIN CERTIFICATE-----
> -----END CERTIFICATE-----
> -----BEGIN CERTIFICATE-----
> -----END CERTIFICATE-----
- <b id="private_key">证书私钥</b>：选择 Nginx 中的 `.key` 文件，输入框填写包含` -----BEGIN RSA PRIVATE KEY----- `和 `-----END RSA PRIVATE KEY----- `的所有内容。
**内容示例：**
![](https://main.qcloudimg.com/raw/1ca20b0021b49ccb407df43675be37ba.png)

### 步骤2：验证配置
HTTPS 配置生效时间约2小时，请于提交证书后2小时左右访问该域名，若浏览器地址栏显示为 HTTPS 则说明配置成功。
![](https://main.qcloudimg.com/raw/b1f54ec35855e5d2adbaeae96a04ef13.png)

### 步骤3：修改配置
HTTPS 功能支持开启和关闭。关闭此服务后，云直播将不再为该域名提供 HTTPS 服务。若证书已过期，需更新为新的有效证书。
 
>? 更多证书相关指引请参见 [SSL 证书操作指南](https://cloud.tencent.com/document/product/400/4141)。


## 常见问题
- [直播 HTTPS 配置要填写什么格式的证书？](https://cloud.tencent.com/document/product/267/45252#que5)
- [如何辨认证书是 PEM 格式还是 DER 格式？](https://cloud.tencent.com/document/product/267/45252#que6)







