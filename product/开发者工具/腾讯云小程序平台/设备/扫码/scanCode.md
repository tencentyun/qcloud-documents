# scanCode

- 功能描述

调起客户端扫码界面进行扫码

- 参数

**Object object**

| 属性           | 类型           | 合法值及说明                                                 | 默认值                | 必填 | 说明                                             | 最低版本                                                     |
| :------------- | :------------- | ------------------------------------------------------------ | :-------------------- | :--- | :----------------------------------------------- | :----------------------------------------------------------- |
| onlyFromCamera | boolean        |                                                              | false                 | 否   | 是否只能从相机扫码，不允许从相册选择图片         |   |
| scanType       | Array.<string> | barCode：一维码<br>qrCode：二维码<br/>datamatrix：Data Matrix 码<br/>pdf417：PDF417 条码 | ['barCode', 'qrCode'] | 否   | 扫码类型                                         |   |
| success        | function       |                                                              |                       | 否   | 接口调用成功的回调函数                           |                                                              |
| fail           | function       |                                                              |                       | 否   | 接口调用失败的回调函数                           |                                                              |
| complete       | function       |                                                              |                       | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |                                                              |

**object.success 回调函数**

- 参数

**Object res**

| 属性     | 类型   | 合法值及说明                                                 | 说明                                                         |
| :------- | :----- | ------------------------------------------------------------ | :----------------------------------------------------------- |
| result   | string |                                                              | 所扫码的内容                                                 |
| scanType | string | QR_CODE：二维码<br/>AZTEC：一维码<br/>CODABAR：一维码<br/>CODE_39：一维码<br/>CODE_93：一维码<br/>CODE_128：一维码<br/>DATA_MATRIX：二维码<br/>EAN_8：一维码<br/>EAN_13：一维码<br/>ITF：一维码<br/>MAXICODE：一维码<br/>PDF_417：二维码<br/>RSS_14：一维码<br/>RSS_EXPANDED：一维码<br/>UPC_A：一维码<br/>UPC_E：一维码<br/>UPC_EAN_EXTENSION：一维码<br/>WX_CODE：二维码<br/>CODE_25：一维码 | 所扫码的类型                                                 |
| charSet  | string |                                                              | 所扫码的字符集                                               |
| path     | string |                                                              | 当所扫的码为当前小程序二维码时，会返回此字段，内容为二维码携带的 path |
| rawData  | string |                                                              | 原始数据，base64编码                                         |

- 示例代码

```js
// 允许从相机和相册扫码
wx.scanCode({
  success (res) {
    console.log(res)
  }
})

// 只允许从相机扫码
wx.scanCode({
  onlyFromCamera: true,
  success (res) {
    console.log(res)
  }
})
```