## 操作场景
本文档指导您如何在 Weblogic 中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例，实际名称请以您申请的证书为准。
>- Weblogic 版本以 Weblogic/14.1.1 为例。
>- 本文档以操作系统 Windows Server 2012 R2 为例。由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Weblogic 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
>

## 操作步骤
>?下述步骤中的目录皆是测试环境的目录，具体路径请根据您的实际环境与需求进行确定。
>
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **JKS**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 `cloud.tencent.com_jks` 文件夹：
 - 文件夹名称：`cloud.tencent.com_jks`
 - 文件夹内容：
    - `cloud.tencent.com.jks` 证书文件
    - `cloud.tencent.com.key` 私钥文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
  
>?
>- 当您申请 SSL 证书时选择了 “粘贴 CSR” 方式，或者购买的品牌证书为 Wotrus，则不提供 JKS 证书文件的下载，需要您通过手动转换格式的方式生成密钥库。操作方法如下：访问 [转换工具](https://myssl.com/cert_convert.html)。
>- 未提供 JKS 证书文件的情况下，您可以将 Nginx 文件夹中的证书文件和私钥文件上传至 “转换工具” 中，并填写密钥库密码，单击**提交**，即可转换为 jks 格式证书。
>
3. 请登录服务器，请在 C 盘中创建新的文件夹，以 `temp` 为例。
4. 将本地解压缩后的证书文件与密码文件上传至 `temp` 文件夹中。
5. 请登录 Weblogic 服务管理后台（默认地址：`http://localhost:7001/console`），输入您的用户名及密码，即可进入 WebLogic Server 管理控制台。
6. 单击**域配置 > 服务器**。进入 “服务器概要” 管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/ffc8a6df5c09dd96680cdcf1bdb241cb.png)
7. 选择您要配置的服务器名称，以 `AdminiServer` 为例。 如下图所示：
![](https://main.qcloudimg.com/raw/aa01743bf9a8db4e4b56688069bd9906.png)
8. 进入 `AdminiServer` 的管理设置页面，勾选**启用 SSL 监听端口**并填写 SSL 监听端口为 `443`，单击**保存**。如下图所示：
![](https://main.qcloudimg.com/raw/c48f73608b825c6fd3d50fe5e2d1ddcb.png)
9. 在 `AdminiServer` 的管理设置页面，单击**密钥库**，设置完成后并单击**保存**。如下图所示：
![](https://main.qcloudimg.com/raw/cd19bfe757e62b3dc0763d2d979a7cf5.png)
设置如下信息：
**密钥库**：选择 “定制身份和 JAVA 标准信任”。
**定制身份密钥库**：请填写您的 JKS 证书文件路径，例如：`C:\temp\cloud.tencent.com.jks`。
**定制身份密钥库类型**：请填写 JKS。
**定制身份密钥库密码短语**：请输入您的 JKS 密码。
**确认定制身份密钥库密码短语**：请再次输入您的密码。
>?**定制身份密钥库密码短语**与**确认定制身份密钥库密码短语**默认密码为空。此处密码可以和自己的 JKS 密码一致，也可以不做任何改动，此处设置不影响证书正常使用。
>
10. 在 `AdminiServer` 的管理设置页面，单击 **SSL**，设置完成后并单击**保存**。如下图所示：
![](https://main.qcloudimg.com/raw/729e4accbfbcc70dd198d6c1ad11c7e7.png)
设置如下信息：
**身份和信任位置**：请更改为**密钥库**。
**私有密钥别名**： 请填写 JKS 的别名。
>?默认为证书域名，例如为 \*.dnspod.cn，则填写 \*.dnspod,cn；如为 dnspod.cn，则填写 dnspod.cn。
>
**私有密钥密码短语**：请输入您申请时设置的私有密码，如未设置可不填写。
**确认私有密钥密码短语**：请再次输入私有密码。
>?
>- 如果您的 Weblogic 版本在 10.3.6-12C 之间，请在 **SSL** 设置页面，高级选项中勾选 JSSE。
>- Weblogic 版本在10.3.6 以下不支持 SHA2 算法证书，请升级后再试。
>
11. 修改内容后，单击**保存**，即可自动激活，不需要进行重启。如下图所示：
![](https://main.qcloudimg.com/raw/6dac04176e3f1c33af5f7426619c1987.png)
12. 请使用 `https://cloud.tencent.com` 进行访问。

