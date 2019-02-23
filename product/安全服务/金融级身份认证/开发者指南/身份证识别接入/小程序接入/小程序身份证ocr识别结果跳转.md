1. OCR 小程序完成识别流程后，会携带唯一标识、订单号、验证结果、签名跳转回第三方小程序。
2. 第三方小程序需在【小程序生命周期函数】>【监听小程序】显示 onShow 方法中监听结果返回，获得识别结果。
> !
>- 第三方小程序在 onShow（options） 中可以通过 options.referrerInfo.extraData 拿到返回的结果参数。此部分为微信小程序提供的 API，详情可以参考 [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)。
>- 合作方根据进行签名校验，确保返回结果的安全性。
>- 2.0.4以上的基础库跳转时，需要在全局配置中加声明合作方参照 [微信文档加声明](https://developers.weixin.qq.com/miniprogram/dev/framework/config.html)。
3. **返回结果参数：**

| 参数        | 说明                                       | 类型   | 长度（字节） |
| --------- | ---------------------------------------- | ---- | ------ |
| code      | 身份证识别结果的返回码，0表示识别成功，其他错误码表示失败 | String  |    -    |
| orderNo   | 订单号，由合作方上送，每次唯一，此信息为本次身份证识别上送的信息      | String    | 32     |
|Signature | 对 URL 参数 App ID、oderNo 和 SIGN ticket 的签名。具体见 [签名生成](https://cloud.tencent.com/document/product/655/13817) 和校验规则 | String    | 40     |



