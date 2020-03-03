- OCR小程序完成人脸核身流程后，会携带唯一标识、订单号、验证结果、签名跳转回第三方小程序。
- 第三方小程序需在【小程序生命周期函数】>【监听小程序】显示 onShow 方法中监听结果返回，获得识别结果。
>!
>1. 第三方小程序在 onShow（options） 中可以通过 options.referrerInfo.extraData 拿到返回的结果参数。此部分为微信小程序提供的 API，详情请参见 [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)。
> 2. 合作方根据进行签名校验，确保返回结果的安全性。
> 3. 以上的基础库跳转时，需要在全局配置中加声明合作方参照 [微信文档](https://developers.weixin.qq.com/miniprogram/dev/framework/config.html) 加声明。

- **返回结果参数：**

| 参数        | 说明                                       | 类型   | 长度（字节） |
| --------- | ---------------------------------------- | ---- | ------ |
| code      | 活体验证结果的返回码，0表示活体验证成功，其他为错误码，表示验证失败，错误码详情请参见 [通用响应码](https://cloud.tencent.com/document/product/655/32309)  | String  |    -    |
| orderNo   | 订单号，由合作方上送，每次唯一，此信息为本次人脸核身上送的信息          | String    | 32     |
| signature | 对 URL 参数 AppID、oderNo 和 SIGN ticket 、code 的签名，详情请参见 [签名算法说明](https://cloud.tencent.com/document/product/655/31969) 和校验规则 | String    | 40     |



