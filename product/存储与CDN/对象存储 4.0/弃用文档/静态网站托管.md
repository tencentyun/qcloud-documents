## 基本概念

通过为网站托管配置 Bucket，可以在腾讯云 COS 上托管静态网站（仅限进行了自定义域名的 Bucket）。静态网站是指只包含静态内容（如 HTML ）或客户端脚本的网站，而动态网站的内容包含诸如 PHP、JSP 或 ASP.NET 等服务器端脚本，依赖服务器端处理。腾讯云 COS 支持静态网站的托管，不支持服务器端脚本编写。

> 需要部署动态网站，请使用腾讯云云服务器 CVM 进行服务端代码部署。

若要托管静态网站，用户需要首先创建 Bucket，然后将网站内容上传到 Bucket 并进行自定义域名后，即可通过特定的地址访问静态网站上的不同资源：

假设用户创建了 Bucket，进行自定义域名（假设为`www.example.com`)并为其开启了静态网站功能。 以下示例 URL 将提供对不同网站内容的访问。

`http://www.example.com/` 或 `http://example.com`将返回用户为该网站配置的默认索引文档；


`http://example.com/photo.jpg` 将请求位于 Bucket 根目录下的 photo.jpg 文件，若无此文件则将返回 404 错误对应的错误文件；


`http://example.com/docs/doc1.html ` 将请求位于 Bucket 下的 docs/doc1.html 文件，若返回错误，则将返回相应错误码对应的错误文件。

若要为静态网站托管配置 Bucket，则要将网站配置添加到存储桶。该配置包含以下配置项。

## 静态访问

通过自定义域名（CNAME 或 CDN 绑定）访问 Bucket 文件资源时，默认使用浏览器直接打开文件，可支持图片浏览和 html 静态文件托管等。

![](https://mc.qcloudimg.com/static/img/fe07f2899c8e418414776cebed904b9b/image.png)

静态网站功能帮助用户设置文件的打开方式，开启此功能时，下载文件后会默认使用浏览器打开而不是保存在本地。

**注意**：此功能仅在用户为 Bucket 设置了自定义域名时有意义，使用默认提供的域名（ CDN加速域名和 COS 直接访问域名）访问资源时将 **始终** 弹出下载框，只有 [绑定自定义域名](/doc/product/436/6252) 并开启静态网站功能后，才可以直接在浏览器中打开文件资源。

假设用户创建 Bucket，在根目录上传了 test.html，并将自定义域名 ` www.example.com ` 通过 CNAME 或 CDN 控制台绑定到了该 Bucket 。在未开启静态网站功能时，访问 `http://www.example.com/test.html ` 将弹出下载框，可选择保存文件到本地；开启静态网站功能后，使用自定义域名访问文件 ` http://www.example.com/test.html ` 可以直接在浏览器中呈现 test.html 的页面内容。

## 索引文档

当您键入诸如 http://example.com 的 URL 时，您不是在请求特定的页面。在这种情况下，Web 服务器将提供默认页面，该页面包含存储了请求的网站内容的目录。此默认页面称为索引文档，被命名为 index.html。

通过自定义域名（CNAME 或 CDN 绑定）访问 Bucket 包括根目录在内的任何目录，URL 地址以 / 为结尾的，会优先自动匹配该目录下的 index.html，其次匹配 index.htm。如果两个文件都不存在，则返回 404 错误。

索引文档是当对网站的根或任何子目录发出请求时返回的网页。例如，如果用户在浏览器中输入 `http://www.example.com`，则该用户没有请求任何特定页面。在这种情况下，在 COS 中开启静态网站服务并提供索引页，可将此访问指向至您指定的页面。用户可以上传名称为 `index.html` 或 `index.htm` 的对象并将其配置为公开读。开启静态网站功能的具体内容请参考[配置静态访问](/doc/product/436/6249)。

![](//mccdn.qcloud.com/static/img/e56e0999c45bd38601b5e29316fee84c/image.jpg)

根级 URL 的尾部斜杠是可选的。例如，如果您将具有 index.html 的网站配置为索引文档，以下任意一个 URL 将返回 index.html。

`http://example.com/`

`http://example.com`

如果用户在 Bucket 中创建了文件夹结构（请参考[Bucket 概述 - Bucket 内的文件夹和对象](/doc/product/436/6244)），可能需要在每个层级上都添加索引文档。通过自定义域名（CNAME 或 CDN 绑定）访问 bucket 包括根目录在内的任何目录，URL 地址以 / 为结尾的，会优先自动匹配该目录下的 index.html，其次匹配 index.htm。如果两个文件都不存在，则返回 404 错误。

> 注：使用 [CDN 加速地址](/doc/product/436/6252) 或 [COS 直接访问地址](/doc/product/436/6252) 访问以` / `结尾的资源，将返回错误。

## 错误文档

通过自定义域名（CNAME 或 CDN 绑定）访问 Bucket 时，若触发了 404 或 403 错误，用户可以选择性地提供自定义错误文档，可以在该文档中向客户提供其他指引。

目前只支持指定 Bucket  **根目录** 下的文件，请使用 .html / .htm 等浏览器可识别的文件。若使用了浏览器不可识别的文件，通常浏览器会报错 `INVALID_RESPONSE`。

使用了自定义域名功能后，在页面发生错误时，用户可以自定义腾讯云 COS 返回的特定页面，下表列出了当前自定义页面支持的 HTTP 错误码。

| HTTP 错误码 | 说明                                       |
| -------- | ---------------------------------------- |
| 403      | Forbidden。可以理解为用户没有权限访问此站，服务器收到请求但拒绝提供服务。通常在对象设置了特定的[访问权限](/doc/product/436/6259)时导致此错误发生。 |
| 404      | Not Found。服务器没有找到请求的资源。通常可能发生在以下场景：<br>- 请求的对象不存在<br>- 请求 COS 根目录或文件夹目录时，没有指定索引页<br> - URL 中指定的 Bucket 不存在。 |

用户可以为 403 和 404 错误指定返回的自定义页面。确保该页面已上传到配置为网站的 Bucket，并且将权限设置为***公共读***。这样，当通过自定义域名（CNAME 或 CDN 绑定）访问 Bucket 并触发了 404 或 403 错误时，可以返回指定的内容。

如果使用 CDN 加速地址或 COS 直接访问地址访问并出现 403/404 错误时，设置的错误页面将没有任何效果。

> 注：如果错误状态码指向使用了浏览器不可识别的文件，例如 .zip 文件，大部分浏览器将显示错误无法访问或拒绝访问请求。

![](//mccdn.qcloud.com/static/img/efd9fd50380bcdb575772622a4ecffea/image.jpg)

## 示例

### 配置静态访问

用户创建了 Bucket，并将自定义域名 www.example.com 通过 CNAME 或 CDN 控制台绑定到了该 bucket 。在根目录下放置了一个 index.htm 文件。

**开启前**

> 使用自定义域名访问文件 http://www.example.com/index.htm 将弹出下载框，可以保存 index.htm 文件到本地。

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**开启后**

> 使用自定义域名访问文件 http://www.example.com/index.htm 可以直接在浏览器中呈现 index.htm 的页面内容。

![](//mccdn.qcloud.com/static/img/42eac89413e3916d7c160020037b6783/image.png)

### 配置索引文档

用户创建了 bucket，并将自定义域名 www.example.com 通过 CNAME 或 CDN 控制台绑定到了该 bucket 。放置了如下文件：

> index.html
>
> dir/index.htm
>
> dir/index.html
>
> dir2/
>
> dir3/index.htm

**开启前**

> 访问 http://www.example.com 返回 404 错误。
>
> 访问 http://www.example.com/dir 返回 404 错误，因为根目录下没有 dir 这个文件。
>
> 访问 http://www.example.com/dir/ 返回 404 错误。
>
> 访问 http://www.example.com/dir2/ 返回 404 错误。
>
> 访问 http://www.example.com/dir3/ 返回 404 错误。

**开启后**

> 访问 http://www.example.com 返回 index.html 文件内容。
>
> 访问 http://www.example.com/dir 返回 404 错误，因为根目录下没有 dir 这个文件。
>
> 访问 http://www.example.com/dir/ 返回 dir/index.html 文件内容，因为 index.html 优先级比 index.htm 高。
>
> 访问 http://www.example.com/dir2/ 返回 404 错误，因为要匹配的 index 文件都不存在。
>
> 访问 http://www.example.com/dir3/ 返回 dir3/index.htm 文件内容。

### 配置错误文档

用户创建了 bucket，并将自定义域名 www.example.com 通过 CNAME 或 CDN 控制台绑定到了该 bucket 。

在根目录下放置了一个 404.htm 文件，并配置 404 为 404.html。假设根目录下不存在 abcd.txt 这一文件。

**开启前**

> 访问 http://www.example.com/abcd.txt 返回 404 状态码，并包含默认的错误信息。

**开启后**

> 访问 http://www.example.com/abcd.txt 返回指定的 404.htm 的页面，HTTP 状态码仍为 404。

