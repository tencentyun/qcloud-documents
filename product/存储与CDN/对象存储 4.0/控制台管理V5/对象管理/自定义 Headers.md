## 简介
对象的 HTTP 头部（Header ）是服务器以 HTTP 协议传送 HTML 资料到浏览器前所送出的字串。通过修改 HTTP 头部（Header ），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间。修改对象的 HTTP 头部不会修改对象本身。
例如：修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会出现解码错误。

## 配置详情
COS 提供了 6 种对象 HTTP 头部标识供配置：

|       HTTP 头部       |                  说明                  |                示例                |
| :-----------------: | :----------------------------------: | :------------------------------: |
|    Cache-Control    |            文件的缓存机制           |       no-cache;max-age=200       |
|    Content-Type     |             文件的 MIME 信息           |            text/html             |
| Content-Disposition | MIME 协议的扩展 | attachment;filename="fname.ext" |
|  Expires   |               用来控制缓存的失效日期                |     Wed, 21 Oct 2015 07:28:00 GMT         |
|  Content-Encoding   |  文件的编码格式   | UTF-8 |
|  x-cos-meta-[自定义内容]   |   自定义内容    |              自定义内容               |

## 配置步骤
1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos5)，选择左侧菜单栏【存储桶列表】，进入存储桶列表页面。单击需要配置 HTTP 头部的对象的存储桶（如 example-1253833564），进入存储桶。
![访问权限1](//mc.qcloudimg.com/static/img/d156619ab35a0e1195a70d0e8d8954ca/image.png)
2. 找到需要设置头部的对象（如 example.exe）,单击对象右侧的【详情】。
![设置HTTP头部1](//mc.qcloudimg.com/static/img/f9fe9cdf0d3535cc4bc93547ab7bd84c/image.png)
3. 在文件列表下面找到【自定义Header】,然后单击【添加 Header】，选择需要设置的参数类型（自定义内容需输入自定义名称），输入对应的值。单击【保存】即可。
![设置HTTP头部2](//mc.qcloudimg.com/static/img/e490a107dadd5d477584a8accbc746e9/image.png)

## 示例

在 APPID 为 1234567900 ，创建存储桶名称为 example。存储桶根目录下上传了对象 example.txt。

未自定义对象的 HTTP 头部时，浏览器或客户端下载时得到的对象头部范例如下：
```http
> GET /example.txt HTTP/1.1
> Host: example-1234567890.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Content-Type: text/plain
< Content-Disposition: attachment; filename*="UTF-8''example.txt"
< Access-Control-Allow-Origin: *
< Last-Modified: Tue, 11 Jul 2017 15:30:35 GMT 

```

添加如下配置：
![设置HTTP头部3](//mc.qcloudimg.com/static/img/bcba7754ca585143371935a9f4f0228a/image.png)
再次发起请求，浏览器或客户端得到的对象头部范例如下：
```http
> GET /example.txt HTTP/1.1
> Host: example-1234567890.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Cache-Control: no-cache
< Content-Type: image/jpeg
< Content-Disposition: attachment; filename*="abc.txt"
< x-cos-meta-md5: 1234
< Access-Control-Allow-Origin: *
< Last-Modified: Tue, 11 Jul 2017 15:30:35 GMT
```
