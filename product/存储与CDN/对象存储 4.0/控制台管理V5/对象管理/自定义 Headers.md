## 简介
对象的 HTTP 头部（Header ）是服务器以 HTTP 协议传送 HTML 资料到浏览器前所送出的字符串。通过修改 HTTP 头部（Header），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间。修改对象的 HTTP 头部不会修改对象本身。

例如：修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前用 gz 压缩过，会出现解码错误。

>?归档存储类型的对象不支持自定义 Headers。

## 操作步骤
1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos5)，选择左侧菜单栏【存储桶列表】，进入存储桶列表页面。单击对象所在的存储桶，进入存储桶。
![](https://main.qcloudimg.com/raw/8dccbc7b536de784e46edbd8de3c2464.jpg)
2. 找到需要设置头部的对象，单击对象右侧的【详情】。
![](https://main.qcloudimg.com/raw/160b6e921d1e79de7b36f6533f4910c6.jpg)
3. 在对象属性页面找到【自定义 Headers】，然后单击【添加 Header】，选择需要设置的参数类型（自定义内容需输入自定义名称），输入对应的值。COS 提供了以下6种对象 HTTP 头部标识供配置。头部配置说明如下。配置完成后，单击【保存】即可。
![](https://main.qcloudimg.com/raw/babe4e3591b0d63a866537a34de12d94.jpg)
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
      <td>x-cos-meta-[自定义内容]</td>
      <td>自定义内容</td>
      <td>x-cos-meta-via: homepage</td>
   </tr>
</table>
4. 若您需要对多个对象进行批量自定义 Header 操作，可勾选多个对象，然后在【更多操作】下选择【自定义头部】即可。
![](https://main.qcloudimg.com/raw/f3c395a4cf1a8e29375c1722688642f3.png)

## 示例

在 APPID 为 1250000000 ，创建存储桶名称为 examplebucket-1250000000。存储桶根目录下上传了对象 exampleobject.txt。

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
