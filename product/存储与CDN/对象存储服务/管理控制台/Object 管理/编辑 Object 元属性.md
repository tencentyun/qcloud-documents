## 基本概念

更改 Object 的 HTTP Header 并不会改变Object的内容，只是增加了Object的 [元数据（Metadata）]() 键值组。Object头部 Header 是服务器以 HTTP 协议传 HTML 资料到浏览器前所送出的字串。通过修改 Header，可以改变页面的响应形式，或者传达配置信息。例如修改缓存时间。

## 配置详情

COS提供了 5 种头部标识可以配置：

|       Header        |                  解释                  |                示例                |
| :-----------------: | :----------------------------------: | :------------------------------: |
|    Cache-Control    |            指定请求和响应遵循的缓存机制            |       no-cache；max-age=200       |
|    Content-Type     |             返回内容的MIME类型              |            text/html             |
| Content-Disposition | Object控制用户请求所得的内容存为一个文件的时候提供一个默认的文件名 | attachment; filename="fname.ext" |
|  Content-Language   |                使用的语言                 |              zh-CN               |
|  x-cos-meta-自定义内容   |   用户按照自身业务场景，设置需要在 Header 中传输什么参数    |              自定义内容               |

## 配置方法

进入控制台，选择Bucket，选择Object，点击「Header设置」。![](//mccdn.qcloud.com/static/img/3bb5a7c32049a07d8077477f7106fcf7/image.jpg)

添加参数，并选择类型，如果是自定义内容则需要输入自定义的名称。

输入对应值，并按确定保存。


## 示例

在 APPID 为 10000 下创建了 Bucket 名称为 test。

在 Bucket 根目录上传了Object a.txt。

当不进行自定义 Header 时，浏览器或客户端下载时得到的Object头部范例如下：

```http
> GET /a.txt HTTP/1.1
> Host: test-10000.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Content-Type: text/plain
< Content-Disposition: attachment; filename*="UTF-8''a.txt"
< Access-Control-Allow-Origin: *
< Last-Modified: Wed, 20 Apr 2016 18:23:35 GMT
```

当添加了一些配置如下：

![](//mccdn.qcloud.com/static/img/3bb5a7c32049a07d8077477f7106fcf7/image.jpg)

再次发起请求，浏览器或客户端得到的Object头部范例如下：

```http
> GET /a.txt HTTP/1.1
> Host: test-10000.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Cache-Control: no-cache
< Content-Type: image/jpeg
< Content-Disposition: attachment; filename*="abc.txt"
< x-cos-meta-md5: 1234
< Access-Control-Allow-Origin: *
< Last-Modified: Wed, 20 Apr 2016 18:23:35 GMT
```

