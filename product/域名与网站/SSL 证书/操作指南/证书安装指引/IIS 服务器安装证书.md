## 操作场景
本文档指导您如何在 IIS 中安装 SSL 证书。
>?
>- 本文档以证书名称 `www.domain.com` 为例。
>- 本文档以操作系统 Windows10 为例。由于操作系统的版本不同，详细操作步骤略有区别。
>

## 操作步骤

### 证书安装
1. 已在 SSL 证书管理控制台 中下载并解压缩 `www.domain.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 IIS 文件夹和 CSR 文件：
 - 文件夹名称：IIS
 - 文件夹内容：
    - `www.domain.com.pfx` 证书文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
  - CSR 文件内容：	`www.domain.com.csr` 文件
  >?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 打开 IIS 服务管理器，选择计算机名称，双击打开 “服务器证书”。如下图所示：
![](https://main.qcloudimg.com/raw/6a9f8ec94639eb1258d05d08b4a74871.png)
3. 在服务器证书窗口的右侧 “操作” 栏中，单击【导入】。如下图所示：
![](https://main.qcloudimg.com/raw/fa246e41fc93a6039854ac1f55c8bbbb.png)
4. 在弹出的 “导入证书” 窗口中，选择证书文件存放路径，输入密码，单击【确定】。如下图所示：
>? 申请证书时若设置了私钥密码，输入密码时，请输入私钥密码。若申请证书时未设置私钥密码，输入密码时，请输入 IIS 文件夹中 keystorePass.txt 文件的密码。具体操作请参考 [私钥密码指引](https://cloud.tencent.com/doc/product/400/4461)。
>
![](https://main.qcloudimg.com/raw/39eb6694ce8b85659e66001bbb5317e4.png)
5. 选择网站下的站点名称，并单击右侧 “操作” 栏的【绑定】。如下图所示：
![](https://main.qcloudimg.com/raw/1ecd7c8d77ba107df4b9862b9246e81d.png)
6. 在弹出的 “网站绑定” 窗口中，单击【添加】。如下图所示：
![](https://main.qcloudimg.com/raw/84020faaf7c2899ff6290372acc4c608.png)
7. 在 “添加网站绑定” 的窗口中，将网站类型设置为 https，端口设置为443，并指定对应的 SSL 证书，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/88d92423869fd72104f6d29c4fe18649.png)
8. 添加完成后，即可在 “网站绑定” 窗口中查看到新添加的内容。如下图所示：
![](https://main.qcloudimg.com/raw/db2ab433f6868e775535bb20febf63db.png)

### HTTP 自动跳转 HTTPS 的安全配置（可选）

执行下列步骤前请下载安装 [rewrite 模块](https://www.iis.net/downloads/microsoft/url-rewrite)。
>?
>- 正常跳转可按照下列编辑规则。若您有其他需求可以自己设置。
>- HTTP 跳转 HTTPS 过程中，如果您的网站元素中存在外部链接或者使用的 http 协议，导致整个页面不完全是 https 协议。部分浏览器会因为这些因素报不安全的提示，例如链接不安全。您可以单击不安全页面中的 “详细信息” 查看报错原因。
>
1. 打开 IIS 服务管理器。
2. 选择网站下的站点名称，双击打开 “URL 重写”。如下图所示：
![](https://main.qcloudimg.com/raw/9f7acbeaf855a017a2af207e4f342cc3.png)
3. 进入 “URL 重写” 页面，并单击右侧 “操作” 栏的【添加规则】。如下图所示：
![](https://main.qcloudimg.com/raw/44bd6ad7bbaac642b1e5dd1dee226d82.png)
4. 在弹出的 “添加规则”窗口中，选择【空白规则】，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/7cbd21bda514331f55a1eaeab86b4328.png)
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
6. 单击 "操作" 栏的【应用】保存。
7. 返回网站首页，单击右侧 “管理网站” 栏的【重新启动】。即可使用 `http://www.domain.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。
