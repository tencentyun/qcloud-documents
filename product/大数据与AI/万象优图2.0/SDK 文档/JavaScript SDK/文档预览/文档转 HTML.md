## 简介

本文档提供关于文档预览同步请求的 API 概览以及 SDK 示例代码。

| API  |	说明  |
|----|-----|
| [文档转 HTML](https://cloud.tencent.com/document/product/436/54059)  | 文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。 | 


## 文档转 HTML

#### 功能说明

支持对多种文档类型的文件生成 HTML 格式预览。

#### 请求示例

```javascript
function getDocHtmlUrl() {
  var config = {
    // 需要替换成您自己的存储桶信息
    Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
    Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
  };
  cos.getObjectUrl({
    Bucket: config.Bucket,
    Region: config.Region,
    Key: '文档.docx',
    Query: {
      'ci-process': 'doc-preview', /* 必须，数据万象处理能力，文档预览固定为 doc-preview */
      dstType: 'html',
    },
  }, function(err, data) {
    if (err) {
      console.log(err);
    } else {
      // 使用浏览器打开 url 即可预览
      var url = data.Url;
      console.log(url);
    }
  });
}
getDocPreviewUrl();
```

#### 参数说明


| 名称        | 参数说明                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | -------- |
| dstType   | 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）  | String  | 是       |  
| srcType | 指定目标文件类型，支持的文件类型请见 [文档转 HTML](https://cloud.tencent.com/document/product/436/54059) 文档   | String | 否 |
| sign          | 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档</br>注意：需要进行 urlencode  | String | 否      | 
| copyable          | 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0     | String   | 否      | 
| htmlParams          | 自定义配置参数，json结构，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true } }，支持的配置参考 [自定义配置项说明](https://cloud.tencent.com/document/product/436/59408#.E8.87.AA.E5.AE.9A.E4.B9.89.E9.85.8D.E7.BD.AE.E9.80.89.E9.A1.B9)    | String   | 否   |
| htmlwaterword          | 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为空     | String  | 否      | 
| htmlfillstyle          | 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：rgba(192,192,192,0.6)  | String   | 否      | 
| htmlfront          | 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：bold 20px Serif    | String   | 否      | 
| htmlrotate          | 水印文字旋转角度，0 - 360，默认315度  | String   | 否      | 
| htmlhorizontal          | 水印文字水平间距，单位 px，默认为50  | String | 否      | 
| htmlvertical          | 水印文字垂直间距，单位 px，默认为100  | String | 否      | 


#### 返回结果说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档 | Object |
| - statusCode | 请求返回的 HTTP 状态码，例如200、403、404等                  | Number |
| - headers    | 请求返回的头部信息                                           | Object |
| data   | 请求成功时返回的对象，如果请求发生错误，则为空               | Object |
| - RequestId | 请求的唯一 ID                                                | String |
| - Url  | 文档预览的 Url                                               | String |
