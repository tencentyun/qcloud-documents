使用腾讯云提供的 HTTP Header 配置功能，当您的用户请求业务资源时，可以在返回的**响应消息**添加您配置的头部，以实现跨域访问等目的。
当资源在节点未命中时会进行回源，此时源站返回的头部信息会一起返回给用户。当资源在节点命中缓存时，静态内容加速、下载加速场景下，CDN 默认会将缓存的源站的 Access-Control-Allow-Origin、Timing-Allow-Origin、Content-Disposition、Accept-Ranges 头部信息返回给用户。
由于 HTTP Header 配置是针对域名，因此一旦配置生效，用户对该域名下任意一个资源的响应消息中均会加入所配置头部。配置 HTTP Header 仅影响客户端（如浏览器）的响应行为，不会影响到 CDN 节点的缓存行为。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 在【高级配置】中找到 **HTTP Header 配置**模块。默认情况下，**HTTP Header 配置**为关闭状态。
![img](https://main.qcloudimg.com/raw/8044e171d8626d8ff0d6072d6866fea9.png)
3. 单击开启 **HTTP Header** 开关，可添加头部：
![img](https://main.qcloudimg.com/raw/e0aa1b7333b2825f2cd4fce0274e0f38.png)
	CDN 提供以下常见的6类头部设置，也可支持自定义头部设置：
	- Access-Control-Allow-Origin：指定跨域请求时，允许访问资源的请求来源。
	- Access-Control-Allow-Methods： 指定跨域请求时，允许的跨域请求方法。
	- Access-Control-Max-Age：指定跨域请求时，对特定资源的预请求返回结果的缓存时间。
	- Access-Control-Expose-Headers：指定跨域请求时，客户端可见的头部集合。
	- Content-Disposition：激活客户端下载资源及设置默认的文件名。
	- Content-Language：用于定义页面所使用的语言代码。
	- 自定义：自定义头部。
4. 假设配置内容为：Access-Control-Allow-Origin，设置通配符`*`。确认提交后，开关为开启状态，下方显示正在生效的配置信息。单击【修改】可更改配置信息。单击【删除】可删该配置。
![img](https://main.qcloudimg.com/raw/f20db46cf30bcdc5060b4d5a7884d78a.png)
5. 关闭 **HTTP Header** 开关后，下方的配置信息失效，即 HTTP Header 配置未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/e04ce374d5b46284afda72a5b52bc07c.png)

### 通用配置
#### Content-Disposition
Content-Disposition 用来激活浏览器的下载，同时可以设置默认的下载的文件名。服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如 TXT、JPG 等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置 Content-Disposition 字段覆盖浏览器默认行为。常用的配置如下：
`Content-Disposition：attachment;filename=FileName.txt`

#### Content-Language
Content-Language 是用于定义页面所使用的语言代码，常用配置如下：
`Content-Language: zh-CN`
`Content-Language: en-US`

### 跨域配置
跨域是指某一个域名，如`www.abc.com`下的某资源，向另一个域名`www.def.com`下的某资源发起请求，此时由于资源所属域名不同，即出现**跨域**，不同的协议、不同的端口均会造成跨域访问的出现。此时必须在 Response Header 中增加跨域相关配置，才能让前者成功拿到数据。

#### Access-Control-Allow-Origin
- 功能介绍
Access-Control-Allow-Origin 用于解决资源的跨域权限问题，域值定义了允许访问该资源的域，若来源请求 Host 在域名配置列表之内，则直接填充对应值在返回头部中。也可以设置通配符`*`，允许被所有域请求。
![img](https://main.qcloudimg.com/raw/036e7f2988edcd7dfacd733400efeb12.png)
> ! 支持最多10个域名配置，一个一行，每个以回车分隔。
- 匹配模式介绍

| **匹配模式**   | **域值**                                                     | **说明**                                                     |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 全匹配         | *                                                            | 设置为`*`时，则返回 response-header 中添加头部：Access-Control-Allow-Origins，且值为：`*`。 |
| 固定匹配       | `http://www.test.com` `https://www.test.com` `http://www.b.com` | 若来源为`https://www.test.com`，在列表中命中，则返回 response-header 中添加头部：Access-Control-Allow-Origins，且值为：`https://www.test.com`。</br>若来源为`https://www.b.com`，未在列表中命中，因此返回 response-header 中无需添加头部：Access-Control-Allow-Origins。 |
| 二级泛域名匹配 | `http://*.test.com`                                          | 若来源为`http://www.test.com`，匹配，则返回 response-header 中添加头部：Access-Control-Allow-Origins，且值为：`http://www.test.com`。</br>若来源为`https://www.test.com`，不匹配，因此返回 response-header 中无需添加头部：Access-Control-Allow-Origins。 |
| 端口匹配       | `https://www.test.com:8080`                                  | 若来源为`https://www.test.com:8080`，匹配，则返回 response-header 中添加头部：Access-Control-Allow-Origins，且值为：`https://www.test.com:8080`。</br>若来源为`https://www.test.com`，不匹配，因此返回 response-header 中无需添加头部：Access-Control-Allow-Origins。 |

> !若存在特殊端口，则需要在列表中填写相关信息，不支持任意端口匹配，必须指定。

#### Access-Control-Allow-Methods

Access-Control-Allow-Methods 用于设置跨域允许的 HTTP 请求方法，可同时设置多个方法，如下：
Access-Control-Allow-Methods:`POST, GET, OPTIONS`

#### Access-Control-Max-Age
Access-Control-Max-Age 用于指定预请求的有效时间。
非简单的跨域请求，在正式通信之前，需要增加一次 HTTP 查询请求，称为“预请求”，用来查明这个跨域请求是不是安全可以接受的，如下请求会被视为非简单的跨域请求：
- 以 GET、HEAD 或者 POST 以外的方式发起，或者使用 POST，但是请求数据类型为 application/x-www-form-urlencoded、 multipart/form-data、text/plain 以外的数据类型，如 application/xml 或者 text/xml。
- 使用自定义请求头。

Access-Control-Max-Age 的单位为秒，设置示例如下：
Access-Control-Max-Age:`1728000`
表明在1728000秒（20天）内，对该资源的跨域访问不再发送另外一条预请求。

#### Access-Control-Expose-Headers
Access-Control-Expose-Headers 用于指定哪些头部可以作为响应的一部分暴露给客户端。默认情况下，只有6种头部可以暴露给客户端：
- Cache-Control
- Content-Language
- Content-Type
- Expires
- Last-Modified
- Pragma

如果想让客户端访问到其他的头部信息，可以进行如下设置，当输入多个头部时，需用`,`隔开。
Access-Control-Expose-Headers: `Content-Length,X-My-Header`
表明客户端可以访问到 Content-Length 和 X-My-Header 这两个头部信息。

### 自定义头部
1. 支持添加自定义 Header，用户可在参数列表选择“自定义”。
![img](https://main.qcloudimg.com/raw/fa7ffacae1c3c2dcb22c242f55a0cc25.png)
2. 填写自定义 key-value 值。
![img](https://main.qcloudimg.com/raw/e355d14afebc9943407156a44727603a.png)

暂不支持以下 Header 添加：
```
Date
Expires
Content-Type
Content-Encoding
Content-Length
Transfer-Encoding
Cache-Control
If-Modified-Since
Last-Modified
Connection
Content-Range
ETag
Accept-Ranges
Age
Authentication-Info
Proxy-Authenticate
Retry-After
Set-Cookie
Vary
WWW-Authenticate
Content-Location
Content-MD5
Content-Range
Meter
Allow
Error
```

>? 多条 Header 重复添加时，底部优先级高于顶部优先级，由最底部配置直接覆盖。
