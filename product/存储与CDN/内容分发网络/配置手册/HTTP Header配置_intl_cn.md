HTTP 的消息通常包括以下两种：
+ 客户端向服务端发送的请求消息
+ 服务端向客户端发送的响应消息

以上两种类型的消息均由一个起始行，一个或多个头部，一个标明头部结束的空行和可选的消息体组成。
![](https://mc.qcloudimg.com/static/img/3e5f42e1cb78ef015967dda5f790f98c/http.png)
其中 HTTP 头部分为四种类型：通用头、请求头、响应头、实体头。每一个头部由域名、冒号（:）、域值组成，如： ```Connection:keep-alive```。

使用腾讯云提供的 HTTP header 配置功能，当您的用户请求业务资源时，可以在返回的 **响应消息** 添加您配置的头部，以实现跨域访问等目的。
> **注意**：
> + 当资源在节点未命中时会进行回源，此时源站返回的头部信息会一起返回给用户。当资源在节点命中缓存时，CDN 默认会将缓存的源站的 Access-Control-Allow-Origin、Timing-Allow-Origin、Content-Disposition、Accept-Ranges 头部信息返回给用户，如需缓存所有源站返回头部，可提交工单进行人工配置支持。
> + 由于 HTTP header 配置是针对域名，因此一旦配置生效，用户对该域名下任意一个资源的响应消息中均会加入所配置头部。
> + 配置 HTTP header 仅影响客户端（如浏览器）的响应行为，不会影响到 CDN 节点的缓存行为。

## 配置说明
CDN 提供以下 6 种头部的配置：
+ Content-Disposition：激活客户端下载资源及设置默认的文件名。
+ Content-Language：用于定义页面所使用的语言代码。
+ Access-Control-Allow-Origin：指定跨域请求时，允许访问资源的请求来源。
+ Access-Control-Allow-Methods： 指定跨域请求时，允许的跨域请求方法。
+ Access-Control-Max-Age：指定跨域请求时，对特定资源的预请求返回结果的缓存时间。
+ Access-Control-Expose-Headers：指定跨域请求时，客户端可见的头部集合。

### 通用配置
#### Content-Disposition
Content-Disposition 用来激活浏览器的下载，同时可以设置默认的下载的文件名。服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如 txt、jpg 等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置 Content-Disposition 字段覆盖浏览器默认行为。常用的配置如下：
> Content-Disposition：attachment;filename=FileName.txt

#### Content-Language
Content-Language 是用于定义页面所使用的语言代码，常用配置如下：
> Content-Language: zh-CN
> Content-Language: en-US

### 跨域配置
跨域是指某一个域名，如 ```www.abc.com``` 下的某资源，向另一个域名 ```www.def.com``` 下的某资源发起请求，此时由于资源所属域名不同，即出现 **跨域**，不同的协议、不同的端口均会造成跨域访问的出现。此时必须在 Response Header 中增加跨域相关配置，才能让前者成功拿到数据。

#### Access-Control-Allow-Origin
Access-Control-Allow-Origin 用于解决资源的跨域权限问题，域值定义了允许访问该资源的域，也可以设置通配符“*”，允许被所有域请求。常用配置如下：
> Access-Control-Allow-Origin: *
> Access-Control-Allow-Origin: ```http://www.test.com```

配置 Access-Control-Allow-Origin，有以下限制条件：
+ 不支持泛域名，如 ```*.qq.com```
+ 仅可配置为“*”，或指定一个 URI
+ 在配置指定域名时，需要加上 “http://” 或 “https://” 前缀

#### Access-Control-Allow-Methods 
Access-Control-Allow-Methods 用于设置跨域允许的 HTTP 请求方法，可同时设置多个方法，如下：
> Access-Control-Allow-Methods: POST, GET, OPTIONS

#### Access-Control-Max-Age
Access-Control-Max-Age 用于指定预请求的有效时间。
非简单的跨域请求，在正式通信之前，需要增加一次 HTTP 查询请求，称为“预请求”，用来查明这个跨域请求是不是安全可以接受的，如下请求会被视为非简单的跨域请求：
+ 以 GET、HEAD 或者 POST 以外的方式发起，或者使用 POST，但是请求数据类型为 application/x-www-form-urlencoded、 multipart/form-data、text/plain 以外的数据类型，如 application/xml 或者 text/xml。
+ 使用自定义请求头。

Access-Control-Max-Age 的单位为秒，设置示例如下：
> Access-Control-Max-Age: 1728000

表明在 1728000 秒（20 天）内，对该资源的跨域访问不再发送另外一条预请求。

#### Access-Control-Expose-Headers
Access-Control-Expose-Headers 用于指定哪些头部可以作为响应的一部分暴露给客户端。默认情况下，只有 6 种头部可以暴露给客户端：
- Cache-Control
- Content-Language
- Content-Type
- Expires
- Last-Modified
- Pragma

如果想让客户端访问到其他的头部信息，可以进行如下设置，当输入多个头部时，需用“,”隔开：
> Access-Control-Expose-Headers: Content-Length,X-My-Header

表明客户端可以访问到 Content-Length 和 X-My-Header 这两个头部信息。
### 配置流程
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【高级配置】，您可以看到 **HTTP header 配置** 模块，单击【添加 HTTP header】。
![](https://mc.qcloudimg.com/static/img/d65c06e0e68518fd406f37773c540b6b/header.png)
您可以在下拉菜单中选择需要添加的 HTTP header 及填写其对应配置，单击【添加参数】可以增加一个 header，每个 header 仅允许添加一次。
![](https://mc.qcloudimg.com/static/img/95e850c2d1c1aea01b603231ff1fb390/addheader.png)
单击【确定】，即可完成配置，配置生效时间大概 5 分钟。您也可以对已经添加的 HTTP header 进行【修改】或【删除】。
![](https://mc.qcloudimg.com/static/img/2925b1effc46253093f470f263dcca5d/addheaderok.png)