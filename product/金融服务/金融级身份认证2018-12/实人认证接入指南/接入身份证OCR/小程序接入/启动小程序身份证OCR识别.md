## 启动小程序身份证 OCR 识别
合作方小程序上送 sign，调用微信打开小程序 API 启动人脸核身小程序。
**请求方法：**使用 navigator 组件打开，navigatot 使用方法示例如下。
```
<navigator target="miniProgram"open-type="navigate" app-id=""path="" extra-data="" version="release">打开绑定的小程序</navigator>
```
此方法是微信小程序提供的 API，信息详情请参考 [微信小程序官方文档 ](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)。
**说明：**
  1. navigator 组件无回调函数，无法得知跳转结果。且该组件只能触发跳转事件，在跳转前应先获取到 sign 等参数。
  2. 由于 sign 存在有效期，若跳转到刷脸小程序后用户长时间未进行操作，合作方小程序应再次获取 sign 后执行跳转（每次调起刷脸小程序都应获取一次）。
  3. 由于 navigator 组件目前无回调函数，所以执行跳转后合作方小程序应清除当前缓存，保证异常退出后用户可以再次获取 sign 后跳转。

>!
>- 由于微信修改了小程序调起第三方小程序方式，老的方式 wx.navigateToMiniProgram（OBJECT） 已于2018年7月5日废弃，目前在基础库2.0.7以上（对应微信6.6.6）的微信将无法使用此接口调起小程序。
>- 由于 navigator 组件仅在基础库2.0.7（对应微信6.6.6）以上可用，合作方跳转的逻辑仍需兼容旧方式，即低版本的微信。可以使用 wx.getSystemInfo（OBJECT） 获取到当前微信的基础库版本，判断其小于2.0.7版本使用旧的跳转方式。
>  信息详情请参考 [wx.getSystemInfo（OBJECT） 文档](https://developers.weixin.qq.com/miniprogram/dev/api/wx.getSystemInfo.html)。

- **请求参数：**

| 参数       | 说明                                                         | 类型   | 默认值             | 是否必填 |
| ---------- | ------------------------------------------------------------ | ------ | ------------------ | -------- |
| target     | 默认发生跳转的小程序为当前小程序                             | String | -                  | 是       |
| open-type  | 跳转方式                                                     | String | navigate           | 是       |
| app-id     | 要打开的小程序 AppID                                         | String | wxb9b6a64ddce80154 | 是       |
| path       | 打开小程序的页面路径，如果为空则打开首页                     | String | pages/index          | 是       |
| extra-data | 需要传递给目标小程序的数据，目标小程序可在`App.onLaunch()`，`App.onShow()`中获取到这份数据 | Object | -                  | 是       |
| version    | 要打开的小程序版本，分别有：develop（开发版）、trial（体验版）、release（正式版），仅在当前小程序为开发版或体验版时此参数有效；如果当前小程序是体验版或正式版，则打开的小程序必定是正式版 | String | release            | 是       |

**extra-data 中需要传递的参数：**

| 参数        | 说明                                                         | 类型   | 长度                     | 是否必填 |
| ----------- | ------------------------------------------------------------ | ------ | ------------------------ | -------- |
| webankAppId | WebankAppId，由腾讯指定                                      | String | 由腾讯指定、腾讯服务分配 | 是       |
| version     | 接口版本号，默认值：1.0.0                                    | String | 20                       | 是       |
| nonce       | 随机数，32位随机串，由字母+数字组成                          | String | 32                       | 是       |
| orderNo     | 订单号，由合作方上送，每次唯一，此信息为本次人脸核身上送的信息 | String | 32                       | 是       |
| userId      | 用户 ID ，用户的唯一标识（不要带有特殊字符）                 | String | -                        | 是       |
| sign        | 使用上文生成的签名                                           | String | 40                       | 是       |
| OCRFlag     | 人像面、国徽面识别配置 参数值为 “1”、null 时，人像面必须识别，国徽面可选识别 参数值为 “2” 时，人像面、国徽面都必须识别）返回示例 | String | -                        | 否       |
