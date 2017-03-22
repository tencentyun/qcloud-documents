## 功能介绍
HTTP的消息通常包括以下两种：

+ 客户端向服务端发送的请求消息
+ 服务端向服务端发送的响应消息

以上两种类型的消息均由一个起始行，一个或多个头域，一个标明头域结束的空行和可选的消息体组成。其中HTTP头域分为四种类型：通用头、请求头、响应头、实体头。每一个头域由一个域名（Key）、冒号（：）、阈值（Value）组成。

腾讯云提供的HTTP Header配置功能，当您的用户请求业务资源时，在返回的**响应消息**中<font color="red">添加</font>配置的头域，以实现跨域访问等目的。

**注意：**
+ 当资源在节点未命中时会进行回源，此时源站返回头部信息会一起返回给用户；当资源在节点命中缓存时，CDN 默认会将缓存的源站 Access-Control-Allow-Origin、Timing-Allow-Origin、Content-Disposition、Accept-Ranges头部信息返回给用户，如需缓存所有源站返回头部，可提交工单进行人工配置支持；
+ 由于HTTP Header配置是针对域名，因此一旦配置生效，用户对该域名下任意一个资源的响应消息中均会加入所配置头域；
+ 配置HTTP Header 仅影响客户端（如浏览器）的响应行为，不会影响到CDN节点的缓存行为；



## 配置说明

CDN提供以下5种头域的配置：
+ Content-Disposition：激活自定资源下载设置，以及下载时默认文件名；
+ Content-Language：指定资源在客户端（如浏览器）响应的语言；
+ Access-Control-Allow-Origin：指定跨域请求时，允许访问资源的请求来源；
+ Access-Control-Allow-Methods： 指定跨域请求时，允许的跨域请求方法；
+ Access-Control-Max-Age：指定跨域请求时，对特定资源的预请求返回结果的缓存时间。


### 通用配置

#### Content-Disposition
Content-Disposition 用来激活浏览器的下载，同时可以设置默认的下载的文件名。服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如txt、jpg等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置Content-Disposition字段覆盖浏览器默认行为。常用的配置如下：

> Content-Disposition：attachment;filename=FileName.txt

#### Content-Language
Content-Language 是用于定义页面所使用的语言代码，常用配置如下：

> Content-Language: zh-CN
> Content-Language: en-US


### 跨域配置
跨域是指某一个域名，如 www.abc.com 下的某资源，向另一个域名 www.def.com 下的某资源发起请求，此时由于资源所属域名不同，即出现**跨域**，不同的协议不同的端口均会造成跨域访问的出现。此时必须在 Response Header 中增加跨域相关配置，才能让前者成功拿到数据。

#### Access-Control-Allow-Origin
Access-Control-Allow-Origin 用于解决资源的跨域权限问题，域值定义了允许被引用该资源的域，也可以设置通配符 * ，允许被所有域引用。常用配置如下：

>Access-Control-Allow-Origin: *
>Access-Control-Allow-Origin: http://www.test.com

**注意**：

+ 不支持泛域名，如 *\.qq.com
+ 仅可配置为 * ，或指定一个URI
+ 在配置指定域名时，需要加上 http://  或 https:// 前缀;



#### Access-Control-Allow-Methods 
Access-Control-Allow-Methods 允许的跨域请求方式，可以设置多个：

> Access-Control-Allow-Methods: POST, GET, OPTIONS


#### Access-Control-Max-Age
Access-Control-Max-Age 指定了预请求的有效时间。

非简单的跨域请求，在正式通信之前，需要增加一次HTTPS查询请求，称为“预请求”，用来查明这个跨站请求是不是安全可以接受的，如下情况会被当成预请求：

+ 以GET、HEAD 或者 POST以外的方式发起，或者使用POST，但是请求数据类型为 application/x-www-form-urlencoded、 multipart/form-data、text/plain 以外的数据类型，如 application/xml 或者 text/xml；
+ 使用自定义请求头。

Access-Control-Max-Age 的单位为秒，设置示例如下：

>Access-Control-Max-Age: 1728000

表明在1728000（20天）内，对该资源的跨域访问不再发送另外一条预请求。

### 配置流程
登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

在【高级配置】中找到 HTTP Header 配置，点击添加：

![](https://mccdn.qcloud.com/static/img/96846833b3f6e4830ad3323da43415ea/image.png)

可以选择需要添加的header及填写其对应配置，支持批量添加，**一个header仅允许添加一次**：

![](https://mccdn.qcloud.com/static/img/e7673fae30256b95d445e134b84de36f/image.png)

点击确定，即可完成配置，配置生效时间大概5分钟：

![](https://mccdn.qcloud.com/static/img/6e8d29c43503eca11650068ea6042744/image.png)

也可以对已经添加的header进行修改或删除。






