

### 情况一：使用 cos v4 API 进行视频文件上传
使用 cos v4 API 进行视频文件上传的用户，在上传文件后的回包中，直接包含有 vid 信息，用户可直接记录该 vid 与源文件映射关系即可。

#### cos v4 API 上传文件后回包示例：

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 321
Connection: keep-alive
Date: Tue, 12 Sep 2017 07:36:45 GMT
Server: tencent-cos
x-cos-request-id: NTliNzhlOGRfMTliMjk0MGFfNDg0N18xMTdiY2E=

{
"code":0,
"message":"SUCCESS",
"request_id":"NTllOWQ2YjVfYzlhMzNiMGFfMTY0OV9jMzYwZTU=",
"data":
     {
    "access_url":"http://xy2-124566667.file.myqcloud.com/uploader1500000000",
    "resource_path":"/124566667/xy2/uploader1508497108630",
    "source_url":"http://xy2-124566667.cosgz.myqcloud.com/uploader1500000000",
    "url":"http://gz.file.myqcloud.com/files/v2/124566667/xy2/uploader1500000000",
    "vid":"4396314caa204d61f5d070d45248d9981508497077"
     }
}
```


### 情况二、使用 cos v5 API 进行视频文件上传
由于 cos v5 API 升级改版，用户使用新版 cos v5 API 进行视频文件上传后，回包中将不再包含 vid 信息，用户需要根据v5 回包中的 ```x-cos-request-id``` 及 ```date``` 信息进行计算后，记录 vid 信息与源文件的映射关系，具体映射规则如下：

#### cos v5 API 上传文件后回包示例：

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Mon, 26 Feb 2018 08:25:37 GMT 
ETag: "15c7565b15676b5f35ef85615c04dc19"
Server: tencent-cos
x-cos-request-id: NWE5M2M0N2ZfZDBhMDY4NjRfMWNhZmZfODE4OTEy
```

>!
- vid= md5(x-cos-request-id) + strtotime(Date)，其中，strtotime 表示把回包中的Date 在东八区下转换成时间戳格式。
- vid 中不包含 + 符号，如上示例中 vid 最终计算结果为：vid=421e6d34756e53814c99939ffeec49861519633537。

#### 备注
cos 中的 bucket 不区分 v4、v5 版本，即 cos v4 版本创建的 bucket，也可使用 v5 版本 API 进行上传；同理，cos v5 版本创建的 bucket，也可使用 v4 版本 API 进行上传。

更多 cos API 详细信息，请参见 [cos API 产品手册](https://cloud.tencent.com/document/product/436/7751) 。




