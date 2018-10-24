## 基本概念

更改 Object 的 HTTP Header 并不会改变 Object 的内容，只是增加了 Object 的元数据键值组。Object 头部 Header 是服务器以 HTTP 协议传 HTML 资料到浏览器前所送出的字串。通过修改 Header，可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间，不会被修改文件本身。举例：修改了 Header 中的 content-encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会产生解码错误。

## 配置详情

COS提供了 5 种头部标识可以配置：

|       Header        |                  解释                  |                示例                |
| :-----------------: | :----------------------------------: | :------------------------------: |
|    Cache-Control    |            文件的缓存机制           |       no-cache；max-age=200       |
|    Content-Type     |             文件的 MIME 信息           |            text/html             |
| Content-Disposition | MIME 协议的扩展 | attachment; filename="fname.ext" |
|  Content-Language   |                文件的语言                 |              zh-CN               |
|  Content-Encoding   |  文件的编码格式   | UTF-8 |
|  x-cos-meta-自定义内容   |   自定义内容    |              自定义内容               |

## 配置方法

进入控制台，选择 Bucket，选择 Object，点击 **设置Header**。

![](https://mc.qcloudimg.com/static/img/dc304b8df347ff565f6424eb965ff8db/image.png)

在弹出来的设置 Header弹窗中添加参数，并选择类型，如果是自定义内容则需要输入自定义的名称。输入对应值，并按确定保存。

![](//mccdn.qcloud.com/static/img/3bb5a7c32049a07d8077477f7106fcf7/image.jpg)


## 示例

在 APPID 为 1250000000 下创建了 Bucket 名称为 test。

在 Bucket 根目录上传了Object a.txt。

当不进行自定义 Header 时，浏览器或客户端下载时得到的Object头部范例如下：

```http
> GET /a.txt HTTP/1.1
> Host: test-1250000000.file.myqcloud.com
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

再次发起请求，浏览器或客户端得到的 Object 头部范例如下：

```http
> GET /a.txt HTTP/1.1
> Host: test-1250000000.file.myqcloud.com
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

