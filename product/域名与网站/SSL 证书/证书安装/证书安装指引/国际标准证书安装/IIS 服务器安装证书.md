## 操作场景
本文档指导您如何在 IIS 中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例，实际名称请以您申请的证书为准。
>- 本文档以操作系统 Windows Server 2012 R2 为例。由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 IIS 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
>

## 操作步骤

### 证书安装
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **IIS**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 `cloud.tencent.com.iis` 文件夹：
 - 文件夹名称： `cloud.tencent.com.iis`
 - 文件夹内容：
    - `cloud.tencent.com.key` 密钥文件
    - `cloud.tencent.com.pfx` 证书文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
3. 打开 IIS 服务管理器，选择计算机名称，双击打开 “服务器证书”。如下图所示：
![](https://main.qcloudimg.com/raw/f81cfa90c5bed2470837ab1e04dd029e.png)
4. 在服务器证书窗口的右侧 “操作” 栏中，单击**导入**。如下图所示：
![](https://main.qcloudimg.com/raw/b1b6d531d89ea5b70a348521a9568740.png)
5. 在弹出的 “导入证书” 窗口中，选择证书文件存放路径，输入密码，单击**确定**。如下图所示：
>? 
>- 申请证书时若设置了私钥密码，输入密码时，请输入私钥密码。若申请证书时未设置私钥密码，输入密码时，请输入 `cloud.tencent.com.iis` 文件夹中 keystorePass.txt 文件的密码。
>- 如果私钥密码不慎遗忘，请 [工单联系](https://console.cloud.tencent.com/workorder/category) 腾讯云工程师删除该证书，然后重新申请该域名证书。
>
![](https://main.qcloudimg.com/raw/b3084eae5e0502d1ea730e130adc6b61.png)
6. 选择网站下的站点名称，并单击右侧 “操作” 栏的**绑定**。如下图所示：
![](https://main.qcloudimg.com/raw/d9a68b79c3130e3cf19ffc89fb60472b.png)
7. 在弹出的 “网站绑定” 窗口中，单击**添加**。如下图所示：
![](https://main.qcloudimg.com/raw/83570ec33b564a66f2fd29c46f727016.png)
8. 在 “添加网站绑定” 的窗口中，将网站类型设置为 https，IP 地址设置为全部未分配，端口设置为443，主机名请填写您当前申请证书的域名，并指定对应的 SSL 证书，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/ba1575aa633cd1d6960aa5ffe510af57.png)
9. 添加完成后，即可在 “网站绑定” 窗口中查看到新添加的内容。
10. 请使用 `https://cloud.tencent.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）

>?
>- 正常跳转可按照下列编辑规则。若您有其他需求可以自己设置。
>- HTTP 跳转 HTTPS 过程中，如果您的网站元素中存在外部链接或者使用的 HTTP 协议，导致整个页面不完全是 HTTPS 协议。部分浏览器会因为这些因素报不安全的提示，例如链接不安全。您可以单击不安全页面中的 “详细信息” 查看报错原因。
>
1. 打开 IIS 服务管理器。
2. 选择网站下的站点名称，双击打开 “URL 重写”。如下图所示：
>!执行该步骤前请下载安装 [rewrite 模块](https://www.iis.net/downloads/microsoft/url-rewrite)。
>
![](https://main.qcloudimg.com/raw/1598d33791e582e133e847ed5a79e129.png)
3. 进入 “URL 重写” 页面，并单击右侧 “操作” 栏的**添加规则**。如下图所示：
![](https://main.qcloudimg.com/raw/2c9ac65d66166b8618e3bb58aa237db4.png)
4. 在弹出的 “添加规则”窗口中，选择**空白规则**，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/26df81828a18a24198ccc8136f836dfb.png)
5. 进入 “编辑入站规则” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/13ee58091b5b006f00dbe004f2740564.png)
  - 名称：填写强制 HTTPS。
  - 匹配URL：在 “模式” 中手动输入`(.*)`。
  - 条件：展开 <img src="https://main.qcloudimg.com/raw/b55f713d199b5077dfa66fa960b08363.png" style="margin-bottom: -5px;"></img>，单击添加，弹出 “添加条件” 窗口。
    - 条件输入：`{HTTPS}`。
    - 检查输入字符串是否：默认选择与模式匹配。
    - 模式：手动输入`^OFF$`。
  - 操作：填写以下参数。
	  - 操作类型：选择重定向。
	  - 重定向 URL：`https://{HTTP_HOST}/{R:1}`。
	  - 重定向类型：选择参阅其他（303）。
6. 单击 "操作" 栏的**应用**保存。
7. 返回网站首页，单击右侧 “管理网站” 栏的**重新启动**。即可使用 `http://cloud.tencent.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。

