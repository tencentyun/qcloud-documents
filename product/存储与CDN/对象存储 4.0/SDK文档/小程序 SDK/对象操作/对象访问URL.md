## 简介

本文档提供获取已上传到存储的对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明

查询对象访问的 URL，该接口不会判断对象是否真实存在。

>?
> - 如何使生成的对象URL在浏览器中打开是预览，而不是下载：在获取的url后拼接参数 response-content-disposition=inline
> - 如何使生成的对象URL在浏览器中打开是下载，而不是预览：在获取的url后拼接参数 response-content-disposition=attachment

#### 使用示例

获取在浏览器默认下载的url：

[//]: # (.cssg-snippet-get-presign-download-url)
```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION',  /* 存储桶所在地域，例如ap-beijing，必须字段 */
    Key: '1.jpg',  /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），必须字段 */
    Sign: true,    /* 获取带签名的对象URL */
}, function(err, data) {
    if (err) return console.log(err);
    /* url为对象访问url */
    var url = data.Url;
    /* 复制downloadUrl的值到浏览器打开会自动触发下载 */
    var downloadUrl = data.Url + (data.Url.indexOf('?') > -1 ? '&' : '?') + 'response-content-disposition=attachment'; // 补充强制下载的参数
});
```

#### 参数说明

| 参数名  | 参数描述                                                     | 类型    | 是否必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | 存储桶的名称，命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Region  | 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) | String  | 是   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，详情请参见 [对象概述](https://cloud.tencent.com/document/product/436/13324) | String  | 是   |
| Sign    | 是否返回带有签名的 Url，默认为 true，当对象为私有读时，获取到不带签名的url依然没有权限访问                          | Boolean | 否   |
| Protocol    | 可选填为`http:`或`https:`，默认为`http:`（带冒号）                          | String | 否   |
| Domain    | 存储桶访问域名，默认为 {BucketName-APPID}.cos.{Region}.myqcloud.com     | String | 否   |
| Method  | 操作方法，例如 GET，POST，DELETE，HEAD 等 HTTP 方法，默认为 GET | String  | 否   |
| Query     | 签名中要签入的请求参数，{key: 'val'} 的格式                                        | Object | 否   |
| Headers   | 签名中要签入的请求头部，{key: 'val'} 的格式                                       | Object | 否   |
| Expires | 签名几秒后失效，默认为900秒                                  | Number  | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档 | Object |
| data   | 请求成功时返回的对象，如果请求发生错误，则为空               | Object |
| - Url  | 计算得到的 Url                                               | String |
