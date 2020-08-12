## 操作场景
本文档指导您如何在 Weblogic 中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例，实际名称请以您申请的证书为准。
>- Weblogic 版本以 Weblogic/14.1.1 为例。
>- 本文档以操作系统 Windows Server 2012 R2 为例。由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 IIS 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>

## 操作步骤


### 证书安装
1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 Tomcat 文件夹和 CSR 文件：
 - 文件夹名称：Tomcat
 - 文件夹内容：
    - `cloud.tencent.com.jks` 证书文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
  - CSR 文件内容：	`cloud.tencent.com.csr` 文件
  
>?
>- CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
>- 当您申请 SSL 证书时选择了 “粘贴 CSR” 方式，或者购买的品牌证书为 Wotrus，则不提供 Tomcat 证书文件的下载，需要您通过手动转换格式的方式生成密钥库。操作方法如下：访问 [转换工具](https://myssl.com/cert_convert.html)。
>- 未提供 Tomcat 证书文件的情况下，您可以将 Nginx 文件夹中的证书文件和私钥文件上传至 “转换工具” 中，并填写密钥库密码，单击【提交】，即可转换为 jks 格式证书。
>
2. 请登录 Weblogic 服务管理后台（默认地址：`http://localhost:7001/console`），登陆 Weblogic 成功后，单击域配置中的【服务器】。如下图所示：
![](https://main.qcloudimg.com/raw/ffc8a6df5c09dd96680cdcf1bdb241cb.png)
3. 选择您要配置的 Web 服务器名称，以 `AdminiServer` 为例。 
![](https://main.qcloudimg.com/raw/aa01743bf9a8db4e4b56688069bd9906.png)
4. 进入`AdminiServer`的管理设置，勾选【启用 SSL 监听端口】并填写 SSL 监听端口为 `443`，单击【保存】，如下图所示：
![](https://main.qcloudimg.com/raw/c48f73608b825c6fd3d50fe5e2d1ddcb.png)
5. 单击【密钥库】，进行密钥库设置页面，设置完成后并单击【保存】。如下图所示：
![](https://main.qcloudimg.com/raw/9332b76bf9adac60781c2c87f3b605d8.png)
设置如下信息：
**密钥库**：选择 “定制身份和 JAVA 标准信任”。
**定制身份密钥库**：指定您的 JKS 证书文件路径。
**定制身份密钥库类型**：填写 JKS。
**定制身份密钥库密码短语**：输入您的 JKS 密码。
**确认定制身份密钥库密码短语**:再次输入确认您的密码。

>?【定制身份密钥库密码短语】与【确认定制身份密钥库密码短语】默认密码为空。此处密码可以和自己的 JKS 密码一致，也可以不做任何改动，此处设置不影响证书正常使用。
>
7. 单击【SSL】功能项，进入 SSL 设置页面，如下图所示：
![](https://main.qcloudimg.com/raw/332afb94b3add4447d1b0709ffaaddac.png)
设置如下信息：
**身份和信任位置**：更改为【密钥库】
**私有密钥别名**： JKS 的别名，默认为1。
**私有密钥密码短语**：输入您申请时设置的私有密码，如未设置可不填写。
**确认私有密钥密码短语**：再次输入私有密码。
8. 修改完成后，单击【保存】。
>?
>如果您的 Weblogic 版本在 10.3.6-12C 之间，请在 SSL 设置页面，高级选项中勾选 JSSE
>Weblogic 版本在10.3.6 以下不支持 sha2 算法证书，请升级后再试。
>
9. 修改完以上所有项目并且保存后，会自动激活，不需要进行重启。即可使用 `https://cloud.tencent.com` 进行访问。
![](https://main.qcloudimg.com/raw/6dac04176e3f1c33af5f7426619c1987.png)
