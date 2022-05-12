## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 除了可以通过 [MD5 和自定义属性](https://cloud.tencent.com/document/product/436/36427) 验证数据完整性外，还可以通过 CRC64 检验码来进行数据校验。

COS 会对新上传的对象进行 CRC64 计算，并将结果作为对象的属性进行存储，随后在返回的响应头部中携带 x-cos-hash-crc64ecma，该头部表示上传对象的 CRC64 值，根据 [ECMA-182标准](https://www.ecma-international.org/publications/standards/Ecma-182.htm) 计算得到。对于 CRC64 特性上线前就已经存在于 COS 的对象，COS 不会对其计算 CRC64 值，所以获取此类对象时不会返回其 CRC64 值。

## 操作说明

目前支持 CRC64 的 API 如下：

- 简单上传接口
	- [PUT Object](https://cloud.tencent.com/document/product/436/7749) 和 [POST Object](https://cloud.tencent.com/document/product/436/14690)：用户可在返回的响应头中获得文件 CRC64 校验值。
- 分块上传接口
	- [Upload Part](https://cloud.tencent.com/document/product/436/7750)：用户可以根据 COS 返回的 CRC64 值与本地计算的数值进行比较验证。
	- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：如果每个分块都有 CRC64 属性，则会返回整个对象的 CRC64 值，如果某些分块不具备 CRC64 值，则不返回。
- 执行 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) 时，会返回对应的 CRC64 值。
- 执行 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 时，如果源对象存在 CRC64 值，则返回 CRC64，否则不返回。
- 执行 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 和 [GET Object](https://cloud.tencent.com/document/product/436/7753) 时，如果对象存在 CRC64，则返回。用户可以根据 COS 返回的 CRC64 值和本地计算的 CRC64 进行比较验证。

## SDK 示例

#### 功能说明

用于在对象上传和下载的时候对对象数据做 CRC64 一致性校验。

#### 请求示例

这里只用简单上传举例，其它接口也是同样使用方式。

[//]: # (.cssg-snippet-put-object)
```js
cos.putObject({
    Bucket: 'examplebucket-1250000000', /* 必须 */
    Region: 'COS_REGION',     /* 存储桶所在地域，必须字段 */
    Key: 'exampleobject',              /* 必须 */
    StorageClass: 'STANDARD',
    Body: fileObject, // 上传文件对象
    onProgress: function(progressData) {
        console.log(JSON.stringify(progressData));
    }
}, function(err, data) {
    if (err) {
      console.log(err);
    } else {
      // 需要给Expose-Headers添加字段x-cos-hash-crc64ecma字段才可正确返回
      // 参考文档：https://cloud.tencent.com/document/product/436/13318
      var crc64 = data.headers['x-cos-hash-crc64ecma'];
      console.log(crc64);
    }
});
```

