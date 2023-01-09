## 简介

本文档提供关于通用文字识别的 API 概览和 SDK 示例代码。

| API           | 说明                 |
| ------------- |  ---------------------- |
| [通用文字识别](https://cloud.tencent.com/document/product/436/64324) | 通用文字识别功能将图片上的文字内容，智能识别为可编辑的文本。 |

## 通用文字识别

#### 功能说明

通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。


#### 请求示例

```javascript
function orc() {
  var config = {
    // 需要替换成您自己的存储桶信息
    Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
    Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
  };
  var key = '素材.jpeg';
  var host = config.Bucket + '.cos.' + config.Region + '.myqcloud.com/' + key;
  var url = 'https://' + host;
  cos.request({
      Method: 'GET',
      Key: key,
      Url: url,
      Query: {
        'ci-process': 'OCR', /* 必须，数据万象处理能力，图片文字识别固定为 OCR。	*/
        // type: '', /* 非必须，OCR 的识别类型 */
        // 'language-type': '', /* 非必须，type 值为 general 时有效，表示识别语言类型 */
        // ispdf: false, /* 非必须，type 值为 general、fast 时有效，表示是否开启 PDF 识别 */
        // 'pdf-pagenumber': '', /* 非必须，type 值为 general、fast 时有效，表示需要识别的 PDF 页面的对应页码 */
        // isword: false, /* 非必须，type 值为 general、accurate 时有效，表示识别后是否需要返回单字信息 */
        // 'enable-word-polygon': false, /* 非必须，type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出 */
      },
  },
  function(err, data){
      console.log(err || data);
  });
}
orc();
```

#### 参数说明

| 参数名称            | 描述                                                         | 类型    | 是否必选 |
| :------------------ | :----------------------------------------------------------- | :------ | :------- |
| Key           | 对象文件名，例如：folder/document.jpg。                      | String  | 是       |
| ci-process          | 数据万象处理能力，图片文字识别固定为 OCR。                   | String  | 是       |
| type                | OCR 的识别类型，有效值为 general，accurate，efficient，fast，handwriting。general 表示通用印刷体识别；accurate 表示印刷体高精度版；efficient 表示印刷体精简版；fast 表示印刷体高速版；handwriting 表示手写体识别。默认值为 general。 | String  | 否       |
| language-type       | type 值为 general 时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。可选值请参见 [可识别的语言类型](https://cloud.tencent.com/document/product/436/64324#language-type)。 | String  | 否       |
| ispdf               | type 值为 general、fast 时有效，表示是否开启 PDF 识别，有效值为 true 和 false，默认值为 false，开启后可同时支持图片和 PDF 的识别。 | Boolean | 否       |
| pdf-pagenumber      | type 值为 general、fast 时有效，表示需要识别的 PDF 页面的对应页码，仅支持 PDF 单页识别，当上传文件为 PDF 且 ispdf 参数值为 true 时有效，默认值为1。 | Integer | 否       |
| isword              | type 值为 general、accurate 时有效，表示识别后是否需要返回单字信息，有效值为 true 和 false，默认为 false。 | Boolean | 否       |
| enable-word-polygon | type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出，有效值为 true 和 false，默认值为 false。 | Boolean | 否       |

#### 返回结果说明

详情请参见 [通用文字识别](https://cloud.tencent.com/document/product/436/64324#.E5.93.8D.E5.BA.94)。

