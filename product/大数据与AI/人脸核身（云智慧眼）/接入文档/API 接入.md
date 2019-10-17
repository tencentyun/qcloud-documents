腾讯云人脸核身除了 SaaS 化的接入方式，还提供了多个 API 接口，您可根据场景和需求自定义开发。

API 接入详情请参见 [人脸核身 API 文档](https://cloud.tencent.com/document/product/1007/31320)。
## 腾讯云人脸核身接口

| 功能              | 说明                                |
| --------------- | ----------------------------------- |
|[活体人脸核身](https://cloud.tencent.com/document/api/1007/31818)|上传视频与公安权威库比对。 |
| [活体人脸比对](https://cloud.tencent.com/document/api/1007/31819)|传入视频和照片，对视频中的人与上传照片进行比对。 |
| [活体检测](https://cloud.tencent.com/document/product/1007/35330)| 传入视频，判断视频中的人是否为真人录制。 |
| [获取动作顺序](https://cloud.tencent.com/document/api/1007/31822)| 活体检测使用动作模式时，需先调用该接口获取动作顺序。 |
| [获取数字验证码](https://cloud.tencent.com/document/api/1007/31821) | 活体检测使用数字模式时，需先调用该接口获取数字验证码。 |
| [自拍照+身份信息识别	](https://cloud.tencent.com/document/product/1007/35918)   |上传照片与公安权威库比对（照片人脸核身）  |
|[身份信息核验](https://cloud.tencent.com/document/api/1007/33188)| 传入姓名和身份证号，验证真实性和一致性 |
|[银行卡二要素核验](https://cloud.tencent.com/document/api/1007/35776)  | 传入姓名和银行卡号，验证真实性和一致性 |
|[银行卡三要素核验](https://cloud.tencent.com/document/api/1007/33848)  | 传入姓名、开户证件号、银行卡号，验证真实性和一致性 |
|[银行卡四要素核验](https://cloud.tencent.com/document/api/1007/35775)  | 传入姓名、开户证件号、银行卡号、手机号，验证真实性和一致性 |
