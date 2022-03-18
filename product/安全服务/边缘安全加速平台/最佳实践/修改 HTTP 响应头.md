## 功能简介
支持自定义变更/增加/删除 HTTP 响应头（从节点响应客户端用户时的 HTTP 响应头），不会影响节点缓存。若您需要实现跨域访问，可使用此功能。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需配置修改 HTTP 响应头规则。
>!目前仅支持匹配条件为 全部（任意请求） 或 Host 时配置修改 HTTP 请求头操作

参数说明：

| 类型 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| 变更 | 变更指定头部参数的取值为设置后的值<br/>注意：<br/>1. 若指定头部不存在，则会增加该头部<br/>2. 若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部） |
| 增加 | 增加指定的头部<br/>注意：<br/>若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部） |
| 删除 | 删除指定的头部                                               |

| 头部参数                      | 说明                                                         |
| :---------------------------- | :----------------------------------------------------------- |
| Access-Control-Allow-Origin   | 用于解决资源的跨域权限问题，域值定义了允许访问该资源的域。若来源请求 Host 在域名配置列表之内，则直接填充对应值在返回头部中。也可以设置通配符 “*”，允许被所有域请求。更多说明请见 Access-Control-Allow-Origin 匹配模式介绍。 <br>支持输入`*` ，或多个域名 / IP / 域名与 IP 混填（必须包含 `http://` 或 `https://`，填写示例：`http://test.com,http://1.1.1.1`， 逗号隔开）（注意：输入框最多可输入1000字符）。 |
| Access-Control-Allow-Methods  | 用于设置跨域允许的 HTTP 请求方法，可同时设置多个方法，如下： Access-Control-Allow-Methods: `POST, GET, OPTIONS`。 |
| Access-Control-Max-Age        | 用于指定预请求的有效时间，单位为秒。 非简单的跨域请求，在正式通信之前，需要增加一次 HTTP 查询请求，称为“预请求”，用来查明这个跨域请求是不是安全可以接受的，如下请求会被视为非简单的跨域请求： 以 GET、HEAD 或者 POST 以外的方式发起，或者使用 POST，但是请求数据类型为 application / x-www-form-urlencoded、 multipart / form-data、text / plain 以外的数据类型，如 application / xml 或者 text / xml。 使用自定义请求头为：Access-Control-Max-Age:`1728000`，表明在1728000秒（20天）内，对该资源的跨域访问不再发送另外一条预请求。 |
| Access-Control-Expose-Headers | 用于指定哪些头部可以作为响应的一部分暴露给客户端。 默认情况下，只有6种头部可以暴露给客户端：Cache-Control、Content-Language、Content-Type、Expires、Last-Modified、Pragma。 如果想让客户端访问到其他的头部信息，可以进行如下设置，当输入多个头部时，需用 “,” 隔开，如：`Access-Control-Expose-Headers: Content-Length,X-My-Header`，表明客户端可以访问到 Content-Length 和 X-My-Header 这两个头部信息。 |
| Content-Disposition           | 用来激活浏览器的下载，同时可以设置默认的下载的文件名。 服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如 TXT、JPG 等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置 Content-Disposition 字段覆盖浏览器默认行为。常用的配置如下： `Content-Disposition：attachment;filename=FileName.txt` |
| Content-Language              | 用于定义页面所使用的语言代码。常用配置如下： `Content-Language: zh-CN` `Content-Language: en-US` |
| 自定义                        | 支持自定义头部： <br/>参数名：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成<br/>参数值：1 - 1000个字符，不支持中文 |

### Access-Control-Allow-Origin 匹配模式介绍

| **匹配模式**   | **域值**                                                     | **说明**                                                     |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 全匹配         | *                                                            | 设置为 * 时，则响应添加头部： `Access-Control-Allow-Origin:*` |
| 固定匹配       | `http://cloud.tencent.com` `https://cloud.tencent.com` `http://www.b.com` | 来源`https://cloud.tencent.com`，命中列表，则响应添加头部： `Access-Control-Allow-Origin: https://cloud.tencent.com` 来源为 `https://www.qq.com`，未命中列表，响应无变化。 |
| 二级泛域名匹配 | `https://*.tencent.com`                                      | 来源 `https://cloud.tencent.com`，命中列表，则响应添加头部： `Access-Control-Allow-Origin: https://cloud.tencent.com` 来源为 `https://cloud.qq.com`，未命中列表，响应无变化。 |
| 端口匹配       | `https://cloud.tencent.com:8080`                             | 来源为 `https://cloud.tencent.com:8080`，命中列表，则响应添加头部： `Access-Control-Allow-Origin:https://cloud.tencent.com:8080` 来源为 `https://cloud.tencent.com`，未命中列表，响应无变化。 |

>!若存在特殊端口，则需要在列表中填写相关信息，不支持任意端口匹配，必须指定。
>

## 注意事项

- 一个修改 HTTP 响应头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：

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
