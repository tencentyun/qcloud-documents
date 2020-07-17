您可以对已经接入 CDN 的域名进行 HTTPS 证书配置。CDN 支持配置您已有的证书，或腾讯云 [SSL 证书管理](https://console.cloud.tencent.com/ssl) 控制台中托管或颁发的证书。

## 证书及私钥
若您要为您的域名配置已有证书，请先了解以下内容。若您配置的是腾讯云 [SSL 证书管理](https://console.cloud.tencent.com/ssl) 控制台中托管或颁发的证书，可跳过此部分内容，直接查阅后文配置证书流程。
CA 机构提供的证书一般包括以下几种，其中 CDN 使用的是 **Nginx**。
![](https://mc.qcloudimg.com/static/img/1d81ed6bea067ce28af930f6fd45f827/certificate.png)
进入 Nginx 文件夹，使用文本编辑器打开“.crt”（证书）文件和“.key”（私钥）文件，即可看到 PEM 格式的证书内容及私钥内容。
![](https://mc.qcloudimg.com/static/img/e96240a46e9837fdb8656d01a9cafd69/Nginx_certificate.png)
### 证书
证书扩展名一般为“.pem”，“.crt”或“.cer”，在文本编辑器中打开证书文件，可以看到与下图格式相似的证书内容。
证书 PEM 格式：以“-----BEGIN CERTIFICATE-----”作为开头， “-----END CERTIFICATE-----” 作为结尾。中间的内容每行 64 字符，最后一行长度可以不足 64 字符。
![](https://mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)
如果是通过中级 CA 机构颁发的证书，您拿到的证书文件包含多份证书，需要人为的将服务器证书与中间证书拼接在一起上传。拼接规则为：服务器证书放第一份，中间证书放第二份，中间不要有空行。一般情况下，机构在颁发证书的时候会有对应说明，请注意查阅规则说明。
> **注意**：
> 1. 证书之间不能有空行。
> 2. 每一份证书均为 PEM 格式。

中级机构颁发的证书链格式如下。
```
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
```
### 私钥
私钥扩展名一般为“.pem”或“.key”,在文本编辑器中打开私钥文件，可以看到与下图格式相似的私钥内容。
私钥 PEM 格式：以“-----BEGIN RSA PRIVATE KEY-----”作为开头， “-----END RSA PRIVATE KEY-----” 作为结尾。中间的内容每行 64 字符，最后一行长度可以不足 64 字符。
![](https://mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)
如果您得到是以“-----BEGIN PRIVATE KEY-----”作为开头， “-----END PRIVATE KEY-----” 作为结尾的私钥，建议您通过 openssl 工具进行格式转换，命令如下。
```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```

## 配置证书
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏【高级工具】下单击【证书管理】进入 **证书管理** 页面。页面中单击【配置证书】进入 **配置证书** 页面。
![](https://mc.qcloudimg.com/static/img/a50a78762a1cf10291b5c29c3bbd2cf9/certificate_manage.png)

### 1. 选择域名
在【域名】下拉菜单中选择您要配置证书的域名。
![](https://mc.qcloudimg.com/static/img/39d1926dc198d07d67e0da2b232cf211/certificate_domain.png)
> **注意：**
> + 配置证书的域名需要已接入腾讯云 CDN，且域名状态为 **部署中** 或 **已启动**。**已关闭** 状态的域名无法部署证书。
> + 使用腾讯云 **对象存储** 或 **万象优图** 服务开启 CDN 加速后，默认的 ```.file.myqcloud.com``` 或 ```.image.myqcloud.com``` 域名无法配置证书。

### 2. 选择证书
您可以选择使用自有证书或腾讯云托管证书。
#### 2.1 自有证书
选中【自有证书】，将证书内容、私钥内容粘贴入对文本框，您可以给证书添加备注信息以便区分。
![](https://mc.qcloudimg.com/static/img/5cb103f42460fdd84b3e383a73491695/own_certificate.png)
> **注意：**
> + 证书内容需要为 PEM 格式，非此格式证书请参考后文 **PEM 格式转换**。
> + 当您的证书有证书链时，请将证书链内容，转化为 PEM 格式内容，与证书内容合并上传，证书链补齐问题请参考后文 **证书链补齐**。

#### 2.2 腾讯云托管证书
您可以登录 [SSL 证书管理](https://console.cloud.tencent.com/ssl) 控制台，申请由亚洲诚信免费提供的第三方证书，或是将已有证书托管至腾讯云。
选中【腾讯云托管证书】，即可看到该域名可用的证书列表。从证书列表中选择要使用的证书，证书列表中展示格式为“证书 ID（备注）”。
![](https://mc.qcloudimg.com/static/img/91fd243506b64e3678ed60afa3da7b90/ssl_certificate.png)

### 3. 回源方式
配置证书后，您可以选择 CDN 节点回源站获取资源时的回源方式，CDN 支持 **HTTP** 和 **协议回源** 两种回源方式。
![](https://mc.qcloudimg.com/static/img/8abe8e23c18f5c374d8045f3b836020a/back_to_source.png)
> **注意：**
> + 选择 **HTTP** 回源配置成功后，用户至 CDN 节点请求支持 HTTPS/HTTP，CDN 节点回源站请求均为 HTTP。
> + 选择 **协议跟随** 回源配置，您的源站需要部署有效证书，否则将导致回源失败。配置成功后，用户至 CDN 节点请求为 HTTP 时，CDN 节点回源请求也为 HTTP。用户至 CDN 节点请求为 HTTPS 时，CDN 节点回源请求也为 HTTPS。
> + 若域名源站修改 HTTPS 端口为非 443 端口，会导致配置失败。
> + COS 源或 FTP 源域名仅支持 HTTP 回源。

#### 4. 配置成功
单击【提交】，您可以在【证书管理】页面看到已经配置成功的域名及证书信息。
![](https://mc.qcloudimg.com/static/img/40d0e02832523a3452809dd1f6eee7b9/certificate_ok.png)

## 批量配置证书
若您拥有多域名证书或泛域名证书，可适用于多个 CDN 加速域名，您可以通过批量配置，一次性为多个域名添加配置。
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏【高级工具】下单击【证书管理】进入 **证书管理** 页面。页面中单击【批量配置】进入 **批量管理** 页面。
![](https://mc.qcloudimg.com/static/img/ceb54fc1a4e6f4c9d0254325a5d84c64/batch_configuration.png)

### 1. 上传证书
将 PEM 编码的证书内容和私钥贴在页面对应文本框中，您可以通过修改备注名标识配置的证书，完成后单击【下一步】。
![](https://mc.qcloudimg.com/static/img/cbbbb8cafc85954a9a5d1749330d6df1/batch_certificate.png)

### 2. 关联域名和选择回源方式
CDN 系统会识别出可使用您上传证书的 CDN 加速域名（域名状态需要为 **部署中** 或 **已启动**），您可以勾选你需要关联的域名及选择回源方式。
![](https://mc.qcloudimg.com/static/img/78c62822e943392661134d68deaad2af/domain_source.png)
> **注意：**
> + 一次最多可勾选 10 个加速域名进行配置。
> + 选择 **HTTP** 回源配置成功后，用户至 CDN 节点请求支持 HTTPS/HTTP，CDN 节点回源站请求均为 HTTP。
> + 选择 **HTTPS** 回源配置，您的源站需要部署有效证书，否则将导致回源失败。配置成功后，用户至 CDN 节点请求为 HTTP 时，CDN 节点回源请求也为 HTTP。用户至 CDN 节点请求为 HTTPS 时，CDN 节点回源请求也为 HTTPS。
> + 若批量勾选的域名中，有源站修改 HTTPS 端口为非 443 端口，会导致配置失败。
> + 若批量勾选的域名中存在 COS 源或 FTP 源的域名，仅支持 HTTP 回源。

### 3. 提交配置
单击【提交】，CDN 会对所选域名配置证书，每一个域名配置需要 5 分钟左右，请耐心等待。您可以在【证书管理】页面查看证书配置状态。
![](https://mc.qcloudimg.com/static/img/3ba784eba97b08bc6d87cce25c6dcb2b/batch_ok.png)
> **注意：**
> + 若配置失败，您可以通过单击域名右侧的【编辑】按钮，重新进行证书配置。
> + 若批量配置的域名中存在已配置了证书的域名，则该操作会覆盖域名原有证书，若覆盖失败，该域名的证书状态会变为【更新失败】。此时原来配置的证书仍然有效，您可以通过单击域名右侧的【编辑】按钮，重新进行覆盖操作。

## 编辑证书
对于已经配置成功的证书，您可以通过单击域名右侧的【编辑】按钮更新证书。
![](https://mc.qcloudimg.com/static/img/ce4882ef77ee9812237e2d970e622aa2/edit_certificate.png)
你可以在自有证书和腾讯云托管证书之间进行切换，以及重新选择回源方式。单击【提交】即可完成部署。部署过程为无缝覆盖，不会影响您的业务使用。
![](https://mc.qcloudimg.com/static/img/1ecd5ff25b4d65d85eaa613dc7762ddb/edit.png)

## 删除证书
您可以通过单击域名右侧的【删除】按钮，将您部署的证书在 CDN 上删除。
![](https://mc.qcloudimg.com/static/img/4f08b2908790e364d0ebe00a86e4126c/del_certificate.png)

## 证书链补齐
在使用自有证书配置过程中，可能会出现 **证书链无法补齐** 的情况，如下图所示。
![](https://mc.qcloudimg.com/static/img/1720998f8386c793ced5d58151630f5b/image.png)
您可以通过将 CA 的证书（PEM 格式）内容贴入域名证书（PEM 格式）尾部，来补齐证书链。也可以提交工单联系我们。
![](https://mc.qcloudimg.com/static/img/53927ba56ceba5d0a3ed0c5d80257c8a/cer_add.png)

## PEM 格式转换
目前 CDN 只支持 PEM 格式的证书，其他格式的证书需要转换成 PEM 格式，建议通过 openssl 工具进行转换。下面是几种比较流行的证书格式转换为 PEM 格式的方法。

### DER 转换为 PEM
DER 格式一般出现在 java 平台中。
证书转换：
```
openssl x509 -inform der -in certificate.cer -out certificate.pem`
```
私钥转换：
```
openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem
```

### P7B 转换为 PEM
P7B 格式一般出现在 windows server 和 tomcat 中。
证书转换：
```
openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer
```
用文本编辑器打开 outcertificat.cer 即可查看 PEM 格式的证书内容。
私钥转换：私钥一般在IIS服务器里可导出。

### PFX 转换为 PEM
PFX 格式一般出现在 windows server 中。
证书转换：
```
openssl pkcs12 -in certname.pfx -nokeys -out cert.pem
```
私钥转换：
```
openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes
```
