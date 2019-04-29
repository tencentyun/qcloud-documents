## 背景说明
为了支持已有App的合作伙伴，小微平台支持使用自有App来实现用户身份和设备的绑定。

对于合作伙伴的自有App，需要使用**腾讯open体系**的登录态，以及**通道层SDK**来实现绑定，详细介绍和使用步骤如下文。

## 用户身份获取
我们支持使用QQ/微信登录来关联小微设备。

如果您希望打通QQ账户，请到[QQ互联](https://connect.qq.com/)完成基于OAuth的登录对接，拿到openid/appid/accessToken。

如果您希望打通微信账户，请到[微信开放平台](https://open.weixin.qq.com/)完成同样的登录对接，拿到openid/appid/accessToken。

获取用户身份后，如果希望减少用户重复登录的操作频率，可以参考以上两个平台，实现自动续期的逻辑，保证accessToken的可用状态。

## 设备端绑定
进行用户身份和设备的绑定，需要您自行把用户登录态传递到设备上，并且调用相关接口，完成流程。</div>

### 设备端接口
`com.tencent.device.TXAudioManager.init`方法中，参数`accountData`是专门用于用户身份传递的，它指向`com.tencent.device.audio.Account`类型。

### 参数说明
`com.tencent.device.audio.Account`共支持4种类型的设置：

```
    public static final int AccountNull   = 0;    //默认值，使用小微App时使用
    public static final int AccountQQ     = 1;    //QQ账户绑定
    public static final int AccountWX     = 2;    //WX账户绑定
    public static final int Account3rd    = 3;    //第三方账户云接口绑定
```

关于这4种类型分别对应的参数意义说明如下：

| type        | account    | token       | appid  | 说明                             |
|:------------|:-----------|:------------|:-------|:---------------------------------|
| AccountNull | 无意义     | 无意义      | 无意义 | 默认值，无需传递用户登录态时使用 |
| AccountQQ   | openid     | accessToken | appid  | QQ账户登录态                     |
| AccountWX   | openid     | accessToken | appid  | 微信账户登录态                   |
| Account3rd  | 三方账户ID | 无意义      | 无意义 | 第三方账户云接口绑定身份(不建议) |

> *   `com.tencent.device.audio.Account.Account3rd`由于接入步骤相对繁琐，不建议使用。

### 调用时机

`com.tencent.device.TXAudioManager.init`方法是支持重复调用的，当有必要更新绑定账户时，进行调用，下次query生效。

同理，如果要清空绑定者信息，只要在传入`accountData`时，置空帐号信息相关的字段即可。

## 其他说明
按照QQ音乐版权方面的要求，同一个用户身份最多支持3个设备绑定，如果超过这个数量，按照绑定顺序，靠后的设备体检可能会得不到保证。
