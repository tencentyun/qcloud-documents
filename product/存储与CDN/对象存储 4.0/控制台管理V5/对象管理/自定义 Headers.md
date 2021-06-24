## 简介
对象的 HTTP 头部（元数据头部 ）是服务器以 HTTP 协议传送 HTML 资料到浏览器前所送出的字符串。通过修改 HTTP 头部（元数据头部），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间。修改对象的 HTTP 头部不会修改对象本身。

例如：修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会出现解码错误。

>? 归档存储类型的对象不支持自定义 Headers。
>

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航栏中，单击【存储桶列表】，进入存储桶列表页面。
3. 找到对象所在的存储桶，单击其存储桶名称，进入存储桶管理页面。
4. 在左侧导航栏中，选择【文件列表】，进入文件列表页面。
5. 找到需要自定义头部的单个对象，在其右侧操作栏中，单击【更多操作】>【自定义头部】。
![](https://main.qcloudimg.com/raw/b424c94ad7dddd58dd6489cbb7cc43ee.png)
若您需要对多个对象自定义头部，可勾选多个对象，并单击上方的【更多操作】>【自定义头部】即可。
![](https://main.qcloudimg.com/raw/d579c8bf7ce332dcda4908bb94d0dab7.png)
6. 在弹出的窗口中，选择需要设置的元数据头部参数类型，输入对应的元数据值，单击【确定】即可。
COS 提供了以下6种对象 HTTP 头部标识供配置。头部配置说明如下：
![](https://main.qcloudimg.com/raw/cc85c6702c81f1af770dc04a23ae4bb7.png)
<table>
   <tr>
      <th>HTTP 头部</th>
      <th>说明</th>
      <th>示例</th>
   </tr>
   <tr>
      <td>Content-Type</td>
      <td>文件的 MIME 信息</td>
      <td>image/jpeg</td>
   </tr>
   <tr>
      <td>Cache-Control</td>
      <td>文件的缓存机制</td>
      <td>no-cache;max-age=200</td>
   </tr>
   <tr>
      <td>Content-Disposition</td>
      <td>MIME 协议的扩展</td>
      <td>attachment;filename="fname.ext"</td>
   </tr>
   <tr>
      <td>Content-Encoding</td>
      <td>文件的编码格式</td>
      <td>UTF-8</td>
   </tr>
   <tr>
      <td>Expires</td>
      <td>用来控制缓存的失效日期</td>
      <td>Wed, 21 Oct 2015 07:28:00 GMT</td>
   </tr>
   <tr>
      <td>x-cos-meta-[自定义后缀]</td>
      <td>用户自定义内容</td>
      <td>x-cos-meta-via: homepage</td>
   </tr>
</table>


## 示例

在 APPID 为 1250000000，创建存储桶名称为 examplebucket-1250000000。存储桶根目录下上传了对象 exampleobject.txt。

未自定义对象的 HTTP 头部时，浏览器或客户端下载时得到的对象头部范例如下：
#### 请求
```sh
GET /exampleobject.txt HTTP/1.1
Host: examplebucket-1250000000.file.myqcloud.com
Accept: */*
```

#### 响应
```http
HTTP/1.1 200 OK
Content-Language:zh-CN
Content-Type: text/plain
Content-Disposition: attachment; filename*="UTF-8''exampleobject.txt"
Access-Control-Allow-Origin: *
Last-Modified: Tue, 11 Jul 2017 15:30:35 GMT 
```

添加如下配置：
![](https://main.qcloudimg.com/raw/3df9e3628c6d8b429842807771ff547e.jpg)
再次发起请求，浏览器或客户端得到的对象头部范例如下：

#### 请求
```sh
GET /exampleobject.txt HTTP/1.1
Host: examplebucket-1250000000.file.myqcloud.com
Accept: */*
```

#### 响应
```http
HTTP/1.1 200 OK
Content-Language:zh-CN
Cache-Control: no-cache
Content-Type: image/jpeg
Content-Disposition: attachment; filename*="abc.txt"
x-cos-meta-md5: 1234
Access-Control-Allow-Origin: *
Last-Modified: Tue, 11 Jul 2017 15:30:35 GMT
```

