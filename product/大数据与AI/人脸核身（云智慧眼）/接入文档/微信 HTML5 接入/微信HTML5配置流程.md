微信 H5 支持微信原生 H5 浮层模式和微信 H5 普通模式，微信原生 H5 浮层模式有行业限制，需要先审核，普通模式可以直接调用，两个模式配置流程相同。

1. 接入准备：
   - 登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid) ，申请 ruleid 参数，在自助接入中申请创建微信 H5（通用模式）或微信原生 H5（浮层模式）业务流程，ruleid 的申请，请参考 [微信 HTML5 接入准备](https://cloud.tencent.com/document/product/1007/42656)。
   - 登录官网控制台 [创建 API 密钥](https://console.cloud.tencent.com/cam/capi)（SecretId 和 SecretKey）
2. 接入方前端显示核身入口，调用接入方服务端接口。
3. 接入方服务端调用实名核身鉴权 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口，传入核身所需信息与业务回跳地址 RedirectUrl，获取到核身流程标识（BizToken）及核身入口 URL 。**[在线调试](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=)**。
4. 接入方前端通过地址跳转方式重定向至步骤3中获取的核身入口 URL，进入核身流程。
5. 用户完成人脸核身后，页面会跳转到 RedirectUrl 上，地址中会带上此次验证流程使用的 BizToken，接入方服务端即可凭借 BizToken 参数调用获取实名核身结果信息 [GetDetectInfo](https://cloud.tencent.com/document/api/1007/31331) 接口去获取本次核身的详细信息。 

### 接入流程示例图
![](https://main.qcloudimg.com/raw/8fd02af070e1d6fbbace09bc0839fb2c.png)
