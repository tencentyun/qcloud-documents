## 操作场景
本文档指导您如何在 IIS 服务器中安装 SSL 证书。

## 前提条件
由于操作系统的版本不同，详细操作步骤略有区别。以下条件仅针对当前服务器说明：
- 当前服务器的操作系统 Windows10。
- 已进入 IIS 服务管理器。

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

下载安装 [rewrite 模块](https://www.iis.net/downloads/microsoft/url-rewrite)。
1. 选择网站下的站点名称，单击 “URL 重写”，并单击右侧 “操作” 栏的【打开功能】。
2. 进入 “URL 重写” 页面，并单击右侧 “操作” 栏的【添加规则】。
3. 在弹出的 “添加规则”窗口中，选择【空白规则】，单击【确定】。
4. 进入 “编辑入站规则” 页面。
![](https://main.qcloudimg.com/raw/adab7ac787fa1cef7e093ebe58445a78.png)
![](https://main.qcloudimg.com/raw/2d2e989eac6e7cd59d4416e5e3ad1c59.png)

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。
