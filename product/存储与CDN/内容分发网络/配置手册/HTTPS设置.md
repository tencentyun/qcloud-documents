HTTPS 是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

>?
-  **对象存储**或**万象优图**服务开启 CDN 加速后，默认的```.file.myqcloud.com```后缀域名，或```.image.myqcloud.com```后缀域名，可直接支持 HTTPS 请求，无需配置证书。
- 腾讯云 CDN 目前针对 HTTP2.0 协议支持已经全面公测，可直接开启使用。

## 配置指引
腾讯云 CDN 目前支持两种方式部署证书。
- 自有证书：将自有证书、私钥内容上传至 CDN 进行部署，全程加密传输，证书不落地，保障您的证书安全。
- 腾讯云托管证书：您可以通过 [SSL 证书管理](https://console.cloud.tencent.com/ssl)，将已有证书托管至腾讯云，以用于多个云产品，您也可以在该平台申请由亚洲诚信免费提供的第三方证书，将其直接部署至 CDN。

### 配置 HTTPS 证书
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧导航栏的【域名管理】进入**域名管理**页面。单击域名右侧【管理】按钮，进入管理页面：
![](https://main.qcloudimg.com/raw/8a395bd78a46d6d957efbef3e428ff0c.png)
2. 单击 【高级配置】，找到 **HTTPS 配置**模块。单击【前往配置】，跳转至**证书管理**页面配置证书。配置流程请参阅 [证书管理](https://cloud.tencent.com/document/product/228/6303)。
![](https://main.qcloudimg.com/raw/57ff3b542eee49cf03d7ccb4cf06cb1a.png)
3. 证书**配置成功**后，会出现【强制跳转 HTTPS】开关。开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 请求进行访问：
![](https://main.qcloudimg.com/raw/d29b36ebc42d3d18214bf3eb4aaefa49.png)

### HTTP2.0 配置
在成功为域名配置了 HTTPS 证书后，可以开启 HTTP2.0。
![](https://main.qcloudimg.com/raw/8c62180a82aa84bfb3c15247e70a0e59.png)
了解更多 HTTP2.0 相关特性，请参见 [HTTP2.0 的新特性](https://cloud.tencent.com/community/article/541321)。
>?file.myqcloud.com 后缀域名暂不支持 HTTP2.0。

## HTTPS 回源支持的算法
目前 HTTPS 回源可支持的算法如下表所示（顺序无先后之分）：

<table ><tbody>
<tr><td >ECDHE-RSA-AES256-SHA</td>
<td >ECDHE-RSA-AES256-SHA384</td>
<td >ECDHE-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >ECDHE-ECDSA-AES256-SHA</td>
<td >ECDHE-ECDSA-AES256-SHA384</td>
<td >ECDHE-ECDSA-AES256-GCM-SHA384</td></tr>
<tr><td >SRP-AES-256-CBC-SHA</td>
<td >SRP-RSA-AES-256-CBC-SHA</td>
<td >SRP-DSS-AES-256-CBC-SHA</td></tr>
<tr><td >DH-RSA-AES256-SHA</td>
<td >DH-RSA-AES256-SHA256</td>
<td >DH-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >DH-DSS-AES256-SHA</td>
<td >DH-DSS-AES256-SHA256</td>
<td >DH-DSS-AES256-GCM-SHA384</td></tr>
<tr><td >DHE-RSA-AES256-SHA</td>
<td >DHE-RSA-AES256-SHA256</td>
<td >DHE-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >DHE-DSS-AES256-SHA</td>
<td >DHE-DSS-AES256-SHA256</td>
<td >DHE-DSS-AES256-GCM-SHA384</td></tr>
<tr><td >CAMELLIA256-SHA</td>
<td >DH-RSA-CAMELLIA256-SHA</td>
<td >DHE-RSA-CAMELLIA256-SHA</td></tr>
<tr><td >PSK-3DES-EDE-CBC-SHA</td>
<td >DH-DSS-CAMELLIA256-SHA</td>
<td >DHE-DSS-CAMELLIA256-SHA</td></tr>
<tr><td >ECDH-RSA-AES256-SHA</td>
<td >ECDH-RSA-AES256-SHA384</td>
<td >ECDH-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >ECDH-ECDSA-AES256-SHA</td>
<td >ECDH-ECDSA-AES256-SHA384</td>
<td >ECDH-ECDSA-AES256-GCM-SHA384</td></tr>
<tr><td >AES256-SHA</td><td >AES256-SHA256</td>
<td >AES256-GCM-SHA384</td></tr>
<tr><td >ECDHE-RSA-AES128-SHA</td>
<td >ECDHE-RSA-AES128-SHA256</td>
<td >ECDHE-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >ECDHE-ECDSA-AES128-SHA</td>
<td >ECDHE-ECDSA-AES128-SHA256</td>
<td >ECDHE-ECDSA-AES128-GCM-SHA256</td></tr>
<tr><td >SRP-AES-128-CBC-SHA</td>
<td >SRP-RSA-AES-128-CBC-SHA</td>
<td >SRP-DSS-AES-128-CBC-SHA</td></tr>
<tr><td >DH-RSA-AES128-SHA</td>
<td >DH-RSA-AES128-SHA256</td>
<td >DH-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >DH-DSS-AES128-SHA</td>
<td >DH-DSS-AES128-SHA256</td>
<td >DH-DSS-AES128-GCM-SHA256</td></tr>
<tr><td >DHE-RSA-AES128-SHA</td>
<td >DHE-RSA-AES128-SHA256</td>
<td >DHE-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >DHE-DSS-AES128-SHA</td>
<td >DHE-DSS-AES128-SHA256</td>
<td >DHE-DSS-AES128-GCM-SHA256</td></tr>
<tr><td >ECDH-RSA-AES128-SHA</td>
<td >ECDH-RSA-AES128-SHA256</td>
<td >ECDH-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >ECDH-ECDSA-AES128-SHA</td>
<td >ECDH-ECDSA-AES128-SHA256</td>
<td >ECDH-ECDSA-AES128-GCM-SHA256</td></tr>
<tr><td >CAMELLIA128-SHA</td>
<td >DH-RSA-CAMELLIA128-SHA</td>
<td >DHE-RSA-CAMELLIA128-SHA</td></tr>
<tr><td >PSK-RC4-SHA</td>
<td >DH-DSS-CAMELLIA128-SHA</td>
<td >DHE-DSS-CAMELLIA128-SHA</td></tr>
<tr><td >AES128-SHA</td>
<td >AES128-SHA256</td>
<td >AES128-GCM-SHA256</td></tr>
<tr><td >SEED-SHA</td>
<td >DH-RSA-SEED-SHA</td>
<td >DH-DSS-SEED-SHA</td></tr>
<tr><td >DES-CBC3-SHA</td>
<td >DHE-RSA-SEED-SHA</td>
<td >DHE-DSS-SEED-SHA</td></tr>
<tr><td >IDEA-CBC-SHA</td>
<td >PSK-AES256-CBC-SHA</td>
<td >PSK-AES128-CBC-SHA</td></tr>
<tr><td >EDH-RSA-DES-CBC3-SHA</td>
<td >ECDH-RSA-DES-CBC3-SHA</td>
<td >ECDHE-RSA-DES-CBC3-SHA</td></tr>
<tr><td >EDH-DSS-DES-CBC3-SHA</td>
<td >ECDH-ECDSA-DES-CBC3-SHA</td>
<td >ECDHE-ECDSA-DES-CBC3-SHA</td></tr>
<tr><td >RC4-SHA</td>
<td >ECDH-RSA-RC4-SHA</td>
<td >ECDHE-RSA-RC4-SHA</td></tr>
<tr><td >RC4-MD5</td>
<td >ECDH-ECDSA-RC4-SHA</td>
<td >ECDHE-ECDSA-RC4-SHA</td></tr>
<tr><td >SRP-3DES-EDE-CBC-SHA</td>
<td >SRP-RSA-3DES-EDE-CBC-SHA</td>
<td >SRP-DSS-3DES-EDE-CBC-SHA</td></tr>
<tr><td >DH-DSS-DES-CBC3-SHA</td>
<td >DH-RSA-DES-CBC3-SHA</td>
<td >-</td></tr>
</tbody></table>
