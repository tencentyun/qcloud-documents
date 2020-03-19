微信HTML5 接入分原生 HTML5（浮层模式）和通用 HTML5 模式
 - 微信原生 HTML5（浮层模式）是基于微信原生的体验，可选择读数字、光线、光线+数字自动切换模式。
 - 微信通用 HTML5 模式是腾讯云人脸核身产品提供的用于微信公众号的通用 HTML5 模式，支持数字、动作、静默模式

1. 接入准备：
   - 登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid) ，申请 ruleid 参数，在自助接入中申请创建微信 H5（通用模式）或微信原生 H5（浮层模式）业务流程，ruleid 的申请，请参考 [微信 HTML5 接入准备](https://cloud.tencent.com/document/product/1007/30999)
   - 登录官网控制台[创建 API 密钥](https://console.cloud.tencent.com/cam/capi)（SecretId 和 SecretKey）
2. 客户后端调用实名核身鉴权 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口进行核身流程开启前鉴权，获取到业务流程标识（BizToken）及微信跳转 URL。**[在线调试](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=)**
3. 客户前端通过地址跳转方式重定向至步骤2中获取的 URL 地址
4. 用户完成人脸核身后，页面会跳转回核身鉴权 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 中参数 RedirectUrl 传入的地址，地址中会传递此次验证流程使用的 BizToken，客户后端即可凭借参数中提供的 BizToken 调用获取实名核身结果信息  [GetDetectInfo](https://cloud.tencent.com/document/api/1007/31331) 接口去获取本次核身的详细信息。

### 接入流程示例图
![](https://main.qcloudimg.com/raw/e6140897733e231526aae3c5aae4a701.png)

