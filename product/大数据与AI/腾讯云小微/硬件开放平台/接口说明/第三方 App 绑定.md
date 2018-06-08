## 背景说明
为了支持已有 App 的合作伙伴，小微平台支持使用自有 App 来实现用户身份和设备的绑定。
对于合作伙伴的自有 App，需要使用 ** 腾讯 open 体系 ** 的登录态，以及 ** 通道层 SDK** 来实现绑定，详细介绍和使用步骤如下文。

## 用户身份获取
我们支持使用 QQ / 微信登录来关联小微设备。
- 如果您希望打通 QQ 账户，请到 [QQ 互联](https://connect.qq.com/) 完成基于 OAuth 的登录对接，获得 OpenId、AppId 和 AccessToken。
- 如果您希望打通微信账户，请到 [微信开放平台](https://open.weixin.qq.com/) 完成同样的登录对接，获得 OpenId、AppId 和 AccessToken。

获取用户身份后，如果希望减少用户重复登录的操作频率，可以参考以上两个平台，实现自动续期的逻辑，保证 accessToken 的可用状态。

## 设备端绑定
进行用户身份和设备的绑定，需要您自行把用户登录态传递到设备上，并且调用相关接口，完成流程。

### 设备端接口
在 `com.tencent.xiaowei.sdk.XWSDK.init` 方法中，参数 `accountInfo` 是专门用于用户身份传递的，它指向 `com.tencent.xiaowei.info.XWAccountInfo` 类型。

```
/**
 * 初始化语音服务
 *
 * @param context     上下文对象，不能为null
 * @param accountInfo 账户信息，使用小微 App 对接传null即可
 */
public int init(Context context, XWAccountInfo accountInfo)
```

### 参数说明

`com.tencent.xiaowei.info.XWAccountInfo` 共支持 4 种类型的设置：

```
public static final int AccountNull   = 0;    //默认值，使用小微 App 时使用
public static final int AccountQQ     = 1;    //QQ 账户绑定
public static final int AccountWX     = 2;    //WX 账户绑定
public static final int Account3rd    = 3;    //第三方账户云接口绑定
```

关于这 4 种类型分别对应的参数意义说明如下：

| type        |     account      |  token  |  appid  |  说明  |
| :--------       | :-----    | :----  | :----  | :----  | :----  |
| AccountNull      |  无意义  |  无意义  |  无意义  |  默认值，无需传递用户登录态时使用  |
| AccountQQ        |  openid  |  accessToken  |  appid  |  QQ 账户登录态  |
| AccountWX        |  openid  |  accessToken  |  appid  |  微信账户登录态  |
| Account3rd       |  三方账户ID  |  无意义  |  无意义  |  第三方账户云接口绑定身份(不建议)  |


### 调用时机

`com.tencent.xiaowei.sdk.XWSDK.init` 方法是支持重复调用的，当有必要更新绑定账户时，进行调用，下次 query 生效。
同理，如果要清空绑定者信息，只要在传入`accountInfo `时，置空帐号信息相关的字段即可。

## 其他说明
按照 QQ 音乐版权方面的要求，同一个用户身份最多支持3个设备绑定，如果超过这个数量，按照绑定顺序，靠后的设备体检可能会得不到保证。
