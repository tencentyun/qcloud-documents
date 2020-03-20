## 单链接限速

COS 支持上传、下载文件时进行流量控制，以保证您其他应用的网络带宽，您可以在 [PutObject](https://cloud.tencent.com/document/product/436/7749)、[PostObject](https://cloud.tencent.com/document/product/436/14690)、[GetObject](https://cloud.tencent.com/document/product/436/7753)、[UploadPart](https://cloud.tencent.com/document/product/436/7750) 请求时携带 x-cos-traffic-limit 参数，并设置限速值，COS 会根据设置的限速值来控制本次请求的网络带宽。

## 使用说明

- 用户在 Object、PostObject、GetObject、UploadPart 请求时携带 x-cos-traffic-limit 参数来指定本次请求的限速值，该参数可以设置到 header、请求参数中，或者使用表单上传接口时在表单域中。
- x-cos-traffic-limit 参数的值必须为数字，单位默认为 bit/s。
- 限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，如果超出该范围将返回400错误。

## API 使用示例

如下为简单上传的 API 示例，限速值为1048576 bit/s，即128KB/s：

```sh
PUT /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Content-Length: 13
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1561109068;1561116268&q-key-time=1561109068;1561116268&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=998bfc8836fc205d09e455c14e3d7e623bd2****
x-cos-traffic-limit: 1048576
```

