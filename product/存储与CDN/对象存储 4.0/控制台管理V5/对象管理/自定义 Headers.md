## 简介
对象的 HTTP 头部（Header ）是服务器以 HTTP 协议传送 HTML 资料到浏览器前所送出的字串。通过修改 HTTP 头部（Header ），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间。修改对象的 HTTP 头部不会修改对象本身。
例如：修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会出现解码错误。

## 操作步骤
1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos5)，选择左侧菜单栏【存储桶列表】，进入存储桶列表页面。单击对象所在的存储桶，进入存储桶。
  ![访问权限1](https://main.qcloudimg.com/raw/b90ad17947a0ec530db87210f4b9027d.png)
2. 找到需要设置头部的对象，单击对象右侧的【详情】。
  ![设置HTTP头部1](https://main.qcloudimg.com/raw/4282ea6ea80d720a6f76604f1c2bf62f.png)
3. 在文件列表下方找到【自定义 Header】，然后单击【添加 Header】，选择需要设置的参数类型（自定义内容需输入自定义名称），输入对应的值。COS 提供了以下 6 种对象 HTTP 头部标识供配置。头部配置说明如下。配置完成后，单击【保存】即可。

|        HTTP 头部        |          说明          |              示例               |
| :---------------------: | :--------------------: | :-----------------------------: |
|      Content-Type       |    文件的 MIME 信息    |           image/jpeg            |
|      Cache-Control      |     文件的缓存机制     |      no-cache;max-age=200       |
|   Content-Disposition   |    MIME 协议的扩展     | attachment;filename="fname.ext" |
|    Content-Encoding     |     文件的编码格式     |              UTF-8              |
|         Expires         | 用来控制缓存的失效日期 |  Wed, 21 Oct 2015 07:28:00 GMT  |
| x-cos-meta-[自定义内容] |       自定义内容       |           自定义内容            |

![](https://main.qcloudimg.com/raw/ce52b4ffee10a75eb12b1e780f678768.png)


## 示例

在 APPID 为 1250000000 ，创建存储桶名称为 example。存储桶根目录下上传了对象 exampleobject.txt。

未自定义对象的 HTTP 头部时，浏览器或客户端下载时得到的对象头部范例如下：
```http
> GET /exampleobject.txt HTTP/1.1
> Host: examplebucket-1250000000.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Content-Type: text/plain
< Content-Disposition: attachment; filename*="UTF-8''exampleobject.txt"
< Access-Control-Allow-Origin: *
< Last-Modified: Tue, 11 Jul 2017 15:30:35 GMT 

```

添加如下配置：
![设置HTTP头部3](//mc.qcloudimg.com/static/img/bcba7754ca585143371935a9f4f0228a/image.png)
再次发起请求，浏览器或客户端得到的对象头部范例如下：
```http
> GET /exampleobject.txt HTTP/1.1
> Host: examplebucket-1250000000.file.myqcloud.com
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
