## 操作场景
本文档指导您如何在 IIS 中安装 SSL 证书。
>?
>- 本文档以证书名称 `www.domain.com` 为例。
>- 本文档以操作系统 Windows10 为例。由于操作系统的版本不同，详细操作步骤略有区别。
>
## 前提条件
- 已在 SSL 证书管理控制台 中下载并解压缩 `www.domain.com` 证书文件包到本地目录。
解压缩后，可获得 IIS 文件夹和 CSR 文件：
 - 文件夹名称：IIS
 - 文件夹内容：
    - `www.domain.com.pfx` 证书文件
    - `keystorePass.txt` 密码文件
  - CSR 文件内容：	`www.domain.com.csr` 文件
- 已进入 IIS。
 
>!若您在申请 SSL 证书时已设置私钥密码，该文件夹下则无 keystorePass.txt 文件。

## 操作步骤

### 证书安装
1. 选择计算机名称，双击打开 “服务器证书”。如下图所示：
![3.2.1](https://main.qcloudimg.com/raw/7ad2099ee6123b2dc4c4dd507d26914c.png)
2. 在服务器证书窗口的右侧 “操作” 栏中，单击【导入】。如下图所示：
![3.2.2](https://main.qcloudimg.com/raw/b1b249dc14579a1e23e74d92489cdbad.png)
3. 在弹出的 “导入证书” 窗口中，选择证书文件存放路径，输入密码，单击【确定】。如下图所示：
>? 申请证书时若设置了私钥密码，输入密码时，请输入私钥密码。若申请证书时未设置私钥密码，输入密码时，请输入 IIS 文件夹中 keystorePass.txt 文件的密码。具体操作请参考 [私钥密码指引](https://cloud.tencent.com/doc/product/400/4461)。
>
![3.2.3](https://main.qcloudimg.com/raw/f05019f0d64429f8059941ea95c0b265.png)。
4. 选择网站下的站点名称，并单击右侧 “操作” 栏的【绑定】。如下图所示：
![3.2.4](https://main.qcloudimg.com/raw/fd844653ac645c9d57fff9a7a5d02b44.png)
5. 在弹出的 “网站绑定” 窗口中，单击【添加】。如下图所示：
![3.2.5](https://main.qcloudimg.com/raw/527b7e808e8e8f7ca45e9debaac066fc.png)
6. 在 “添加网站绑定” 的窗口中，将网站类型设置为 https，端口设置为443，并指定对应的 SSL 证书，单击【确定】。如下图所示：
![3.2.6](https://main.qcloudimg.com/raw/c19a3a6b3cc8315b1f1cb70fc8ac8ce7.png)
7. 添加完成后，即可在 “网站绑定” 窗口中查看到新添加的内容。如下图所示：
![3.2.7](//mccdn.qcloud.com/static/img/0748888723acf5671ba9a1ed7ef9ebd2/image.png)

### HTTP 自动跳转 HTTPS 的安全配置（不推荐）

执行下列步骤前请下载安装 [rewrite 模块](https://www.iis.net/downloads/microsoft/url-rewrite)。
>?正常跳转可按照下列编辑规则。若您有其他需求可以自己设置。
>
1. 进入 IIS。
2. 选择网站下的站点名称，单击 “URL 重写”，并单击右侧 “操作” 栏的【打开功能】。
3. 进入 “URL 重写” 页面，并单击右侧 “操作” 栏的【添加规则】。
4. 在弹出的 “添加规则”窗口中，选择【空白规则】，单击【确定】。
5. 进入 “编辑入站规则” 页面。
  - 名称：填写强制 HTTPS。如下图所示：
  ![](https://main.qcloudimg.com/raw/7d76a675f51ce23c8e090fa59923e980.png)
  - 匹配URL：在 “模式” 中手动输入`(.*)`。如下图所示：
  ![](https://main.qcloudimg.com/raw/712ae5173175b07d7ec78a2a850b1dc2.png)
  - 条件：
    - 单击 <img src="https://main.qcloudimg.com/raw/b55f713d199b5077dfa66fa960b08363.png" style="margin-bottom: -5px;"></img>展开，如下图所示：
    ![](https://main.qcloudimg.com/raw/3757992316f7cca69e68bd8c8e2abf5a.png)
    - 单击添加，弹出 “添加条件” 窗口。如下图所示：
    ![](https://main.qcloudimg.com/raw/033c4aa19ca6571a390ba691e2ae9f1f.png)
  - 服务器变量：无。
  - 操作：填写以下参数。如下图所示：
  ![](https://main.qcloudimg.com/raw/0e2d981173aec70e7aa6c74ac7586738.png)
	  - 操作类型：选择重定向。
	  - 重定向 URL：`https://{HTTP_HOST}.{R:1}`。
	  - 重定向类型：选择参阅其他（303）。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。
