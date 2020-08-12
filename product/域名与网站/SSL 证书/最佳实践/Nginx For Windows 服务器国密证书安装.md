## 操作场景
本文档指导您如何在国密版 Nginx 服务器中安装国密标准 SSL 证书。
>?
>- 国密标准 SSL 证书仅支持安装在国密版本的 Nginx 服务器上。
>- 目前仅提供64位 nginx/1.16.0 国密版与32位 nginx/1.17.0 国密版 ，如需其他版本，请您 [提交工单](https://console.cloud.tencent.com/workorder/category) ，腾讯云工程师将为您提供其他版本与帮助。
>- Nginx 版本以国密版 nginx/1.16.0 为例。
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- 当前服务器的操作系统为 Windows Server 2012 R2，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您开启服务器上 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)

### 下载 Windows For Nginx 国密版
| Nginx 版本 | 34位 | 64位 |
|---------|---------|---------|
| 1.16.0 | 暂无 | [单击下载](https://www.wotrus.com/download/gm_nginx-1.16.0.zip) |
| 1.17.0 | [单击下载](https://www.wotrus.com/download/gm_nginx-1.17.0.zip ) | 暂无 |

## 前提条件
- 已在云服务器上下载国密版 Nginx 压缩包。
- 已购买国密标准（SM2）SSL 证书。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<td>名称</td>
<td>说明</td>
</tr>
<tr>
<td>服务器的 IP 地址</td>
<td>服务器的 IP 地址，用于 PC 连接到服务器。</td>
</tr>
<tr>
<td>用户名</td>
<td>登录服务器的用户名。</td>
</tr>
<tr>
<td>密码</td>
<td> 登录服务器的密码。</td>
</tr>
</table>


>?在腾讯云官网购买的云服务器，您可以登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)  获取服务器 IP 地址、用户名及密码。

## 操作步骤
### 安装证书
>?
> 下述步骤中的目录皆是测试环境的目录，具体路径，请根据您的实际环境与需求进行确定。

1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。 其中包含 Nginx 目录和 CSR 文件：
 - **文件夹名称**：Nginx
 - **文件夹内容**：

    - `1_cloud.tencent.com_sign_bundle.crt` 证书文件
    - `2_cloud.tencent.com_encrypt_bundle.crt` 证书文件
    - `3_cloud.tencent.com.key` 私钥文件
  - **CSR 文件内容**：
    -   `cloud.tencent.com_sign.csr` 文件
    - 	`cloud.tencent.com_encrypt.csr` 文件

>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。

2. 解压已下载的国密版 Nginx 压缩包到相应的目录，如 `c:\gmssl`

![](https://main.qcloudimg.com/raw/cb70ea46a24278cafa562a554d87ca75.png)

3. 在 nginx-1.16.0 目录下(如 conf 目录)创建存放证书的目录，如`ssl` 目录。

![](https://main.qcloudimg.com/raw/b329f134789f71f9d5993d1f7cdda575.png)

4. 将解压缩后的 crt 证书文件与 key 私钥文件放在创建的 ssl 目录中，如下图所示

![](https://main.qcloudimg.com/raw/0e34c64fcea588cdb25843f9347260e3.png)

5. 编辑 `nginx/conf` 目录下 `nginx.conf` 文件，在 `http{}` 中，添加 `include ssl.conf` 文件内容。如下图所示

![](https://main.qcloudimg.com/raw/a4b041d00009d77ca3170649b2555106.png)

6. 在 `nginx/conf` 目录下，新建 `ssl.conf` 文件。如下图所示

![](https://main.qcloudimg.com/raw/7af804d184fdd24eecb6eed9f11f9a4c.png)

7. 编辑新建的 `ssl.conf` 文件，添加证书配置，如下所示

```
server { 
listen 443ssl; 
server_name domain.com; 

ssl_certificate d:/gmssl/nginx-1.16.0/conf/ssl/1_cloud.tencent.com_sign_bundle.crt; 
ssl_certificate_key d:/gmssl/nginx-1.16.0/conf/ssl/3_cloud.tencent.com.key;

ssl_certificate d:/gmssl/nginx-1.16.0/conf/ssl/domain.com_en.crt; 
ssl_certificate_key d:/gmssl/nginx-1.16.0/conf/ssl/domain.com_sm2.key; 

#先配置签名证书，再配置加密证书，签名加密证书私钥 key 为同一个！
ssl_session_timeout 5m; 
ssl_protocols TLSv1TlSv1.1TLSv1.2;
ssl_ciphers SM2-WITH-SMS4-SM3:ECDH:AESGCM:HIGH:MEDIUM:!RC4:!DH:!MD5:!aNULL:! eNULL; 
ssl_prefer_server_ciphers on;

Location/{ 
		root html; 
		index index.html index.htm; 
	} 
} 
```

>?
>- 建议用 Administrator 账户配置证书，若用非管理员权限账户配置，可能出现找
不到证书的错误。
- 以上配置仅为参考，具体的`server_name`，证书名称，证书存放目录，`location`等配
置请根据实际环境配置。


7. 配置完成后，您可以通过在服务器 `dos` 命令下， `cd` 进入 `nginx-1.16.0` 目录，如`cd c:\gmssl\nginx-1.16.0`， 输入`nginx-t`，检测 `Nginx` 配置是否正常，正常显示如下图:

![](https://main.qcloudimg.com/raw/3d865472a7963f65330619a6d4537aab.png)

- 若提示`Syntax OK`，则表示配置正常，可以启动  Nginx 服务器。
- 若提示非`Syntax OK`，请您重新配置或者根据提示修改存在问题。


9. 启动 Nginx 服务器，进入 nginx-1.16.0 目录，双击运行 `nginx.exe` 即可使用 `https://cloud.tencent.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


