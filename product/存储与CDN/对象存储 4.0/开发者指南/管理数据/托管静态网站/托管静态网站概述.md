## 基本概念

静态网站指包含静态内容（如 HTML）或客户端脚本的网站，用户可以通过控制台对已绑定自定义域名的存储桶，配置静态网站。而动态网站的内容包含诸如 PHP、JSP 或 ASP.NET 等服务器端脚本，需要依赖服务器端处理。腾讯云 COS 支持静态网站的托管，不支持服务器端脚本编写。当您需要部署动态网站时，推荐使用云服务器 CVM 进行服务端代码部署。

## 示例

用户创建了名为 examplebucket-1250000000 的存储桶，上传了如下文件： 

```shell
index.html
404.html
403.html
test.html
docs/a.html
images/
```

### 静态网站

**开启前**：使用如下默认访问域名访问存储桶，弹出下载提示，可以保存 `index.html` 文件到本地。

```shell
https://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com/index.html
```

**开启后**：使用如下访问节点访问存储桶，可以直接在浏览器中查看 `index.html` 的页面内容。

```shell
https://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com/index.html
```

### 强制 HTTPS

**开启前**：请求来源为 HTTP 时，访问节点 URL 保持 HTTP 未加密的传输协议：

```shell
http://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com
```

**开启后**：无论请求来源为 HTTP 或 HTTPS，访问节点始终保持 HTTPS 加密的传输协议：

```shell
https://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com
```

### 索引文档

索引文档即静态网站的首页，是当用户对网站的根目录或任何子目录发出请求时返回的网页，通常此页面被命名为 `index.html`。
当用户使用存储桶访问域名（例如 `https://examplebucketbucket-1250000000.cos-website.ap-guangzhou.myqcloud.com`）访问静态网站时，且未请求特定的页面。在这种情况下，Web 服务器将返回首页。

您的用户访问存储桶包括根目录在内的任何目录，URL 地址以`/`为结尾的，会优先自动匹配该目录下的索引文档。根级 URL 的`/`是可选的，以下任意一个 URL 将返回索引文档。

```shell
http://www.examplebucket.com/
http://www.examplebucket.com
```

> !如果存储桶中创建了文件夹，则需要在每个文件夹层级上都添加索引文档。

### 错误文档

假设您在配置错误文档前，访问以下页面，将返回404状态码，页面上显示为默认的错误页面信息。

```shell
https://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com/webpage.html
```

配置错误文档后，访问以下页面，同样返回404状态码，但页面上将显示您所指定的错误页面信息。

```shell
https://examplebucket-1250000000.cos-website.ap-guangzhou.myqcloud.com/webpage.html
```

### 重定向规则

#### 配置错误码重定向

假设您为 webpage.html 这个文档设置了**私有读写**的公共访问权限，用户访问该文件时，将返回403错误。
配置403错误码重定向至 403.html 后：浏览器将返回 403.html 的内容。
如果您未配置 403.html 文档，浏览器将返回错误文档或默认错误信息。
![](https://main.qcloudimg.com/raw/7dc917ba95af42438b6ab2c7604666d3.png)

#### 配置前缀匹配

1. 当您将文件夹从`docs/`重命名为`documents/`后，用户在访问`docs/`文件夹会产生错误。所以，您可以将前缀`docs/`的请求重定向至` documents/`。
![](https://main.qcloudimg.com/raw/e3b5c9004a67d020928bd0035b820715.png)
2. 当您删除了`images/`文件夹（即删除了具有前缀`images/`的所有对象）。您可以添加重定向规则，将具有前缀`images/`的任何对象的请求重定向至`test.html`页面。
![](https://main.qcloudimg.com/raw/b6672acf43149267a837027911923f9b.png)
