## 简介
对象的 HTTP 头部（Header ）是服务器以 HTTP 协议传 HTML 资料到浏览器前所送出的字符串。通过修改 HTTP 头部（Header ），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间。修改对象的 HTTP 头部不会修改对象本身。
例如，修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会出现解码错误。

## 配置详情
COS 提供了 5 种对象 HTTP 头部标识供配置：

|       HTTP 头部       |                  说明                  |                示例                |
| :-----------------: | :----------------------------------: | :------------------------------: |
|    Cache-Control    |            文件的缓存机制           |       no-cache;max-age=200       |
|    Content-Type     |             文件的 MIME 信息           |            text/html             |
| Content-Disposition | MIME 协议的扩展 | attachment;filename="fname.ext" |
|  Content-Language   |                文件的语言                 |              zh-CN               |
|  Content-Encoding   |  文件的编码格式   | UTF-8 |
|  x-cos-meta-[自定义内容]   |   自定义内容    |              自定义内容               |

## 配置步骤
1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos4/index)，选择左侧菜单栏【 Bucket 列表】，进入 Bucket 列表页面。单击需要配置回源的存储桶（如 example），进入存储桶。
![访问权限1](//mc.qcloudimg.com/static/img/b51d5a77d53c3416324ea3eb283c788c/image.png)
2. 找到需要设置头部的对象（例如 example.exe）,单击对象右侧的【更多】>【设置 Header】，弹出设置 header 对话框。
![设置HTTP头部1](//mc.qcloudimg.com/static/img/5edf2ba97d32dd82b9c1be1e59379deb/image.png)
3. 单击【+添加参数】，选择需要设置的参数类型（自定义内容需输入自定义名称），输入对应的值。单击【确定】保存即可。
![设置HTTP头部2](//mc.qcloudimg.com/static/img/2a2ee4acd84b10baaa4c27a5b3118ebc/image.png)

## 示例

在 APPID 为123456790 ，创建存储桶名称为 example。存储桶根目录下上传了对象 example.txt。

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
![设置HTTP头部3](//mc.qcloudimg.com/static/img/0d8bb1be135a68204f19f3ea187a75ab/image.png)
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
