## 前提条件
接入验证码前，需要先在 [验证码控制台](https://console.cloud.tencent.com/captcha) 中注册 AppID 和 AppSecret。注册完成后，您可以在控制台的 [基础配置](https://console.cloud.tencent.com/captcha/detail?appid=2043913615) 中查看 AppID 以及 AppSecret。
## 接入步骤
### 快速接入
以下为 Web 端快速接入流程，适用于每次都需要进行人机验证的场景（登录、注册、下发短信、活动等）。
1. 在 Head 标签的最后加入以下代码，引入验证 JS 文件（建议直接在 HTML 中引入）。
```
<script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
```
2. 在您需要激活验证码的 DOM 元素（button、div、span）内加入以下 ID 及属性。
```
<!--点击此元素会自动激活验证码-->
<!--id : 元素的 ID (必须)-->
<!--data-appid : AppID(必须)-->
<!--data-cbfn : 回调函数名(必须)-->
<!--data-biz-state : 业务自定义透传参数(可选)-->
<button id="TencentCaptcha"
        data-appid="appId"
        data-cbfn="callback"
        type="button"
>验证</button>
```
3. 为验证码创建回调函数。
>!函数名要与 data-cbfn 相同。
>
```
window.callback = function(res){
    console.log(res)
    // res（用户主动关闭验证码）= {ret: 2, ticket: null}
    // res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
    if(res.ret === 0){
        alert(res.ticket)   // 票据
    }
}
```

完成以上操作后，单击激活验证码的 DOM 元素，即可弹出验证码。至此，验证码客户端接入已完成，您可以进行 [后台 API 接入](https://cloud.tencent.com/document/product/1110/36926) 操作。
### 定制接入
验证码会在全局注册一个 TencentCaptcha 类，业务方可以使用 TencentCaptcha 类自行初始化验证码，并对验证码进行显示或者隐藏操作。
默认的验证码的 JS（TCaptcha.js）在加载完成后，会检测页面中是否存在`id="TencentCaptcha"`的元素，如果存在，则会自动将验证码的触发事件绑定在该元素上。如不希望默认绑定，请避免使用`id="TencentCaptcha"`的元素。
-  **构造函数**
TencentCaptcha 支持多种参数的重载，以下3种初始化方法，可根据具体情况选择其中一种。
	1. 手动初始化。
```
new TencentCaptcha(appId, callback, options);
```
**参数说明：**
		- appId：String，申请的场景 ID。
		- callback：Function，回调函数。
		- options：Object，更多配置参数, 请参见 [配置参数](#pzcs)。
		
 >!手动初始化的情况，一般是单击一个元素，执行一段逻辑，才调用验证码，绑定单击的元素不要使用`id="TencentCaptcha"`的元素，避免重复绑定单击。

	2. 绑定到一个元素。
```
new TencentCaptcha(element);
```
**参数说明：**
element： HTMLElement，验证码将绑定 click 事件到该元素上，该方式需要确保元素上有 data-appid 和 data-cbfn 属性。
>!手动绑定不要使用`id="TencentCaptcha" `的元素，避免重复绑定单击。
	3. 手动初始化并绑定到一个元素。
```
new TencentCaptcha(element, appId, callback, options);
```
**参数说明：**
		- element: HTMLElement, 需要绑定`click`事件的元素
>!手动绑定不要使用`id="TencentCaptcha"`的元素，避免重复绑定单击。
		- appId: String，申请的场景 ID。
		- callback: Function， 回调函数。
		- options: Object，更多配置参数, 请参见 [配置参数](#pzcs)。

- **示例代码**

```
//方法1: 直接生成一个验证码对象。
var captcha1 = new TencentCaptcha('appId', function(res) {/* callback */});
captcha1.show(); // 显示验证码

//方法2:绑定一个元素并自动识别场景id和回调。
// 验证码会读取dom上的`data-appid`和`data-cbfn`以及`data-biz-state`(可选)自动初始化
new TencentCaptcha(document.getElementById('TencentCaptchaBtn'));

//方法3：绑定一个元素并手动传入场景Id和回调。
new TencentCaptcha(
    document.getElementById('TencentCaptchaBtn'),
    'appId',
    function(res) {/* callback */},
    { bizState: '自定义透传参数' }
);
```
### 回调内容
前端验证成功后，验证码会调用业务传入的回调函数，并在第一个参数中传入回调结果。结果字段说明如下：

| 字段名 | 值类型 | 说明|
|---------|---------|---------|
| ret | Int | 验证结果，0：验证成功。2：用户主动关闭验证码。 |
|ticket|String|验证成功的票据，当且仅当 ret = 0 时 ticket 有值。|
|appid|String|场景 ID。|
|bizState|Any|自定义透传参数。|

### 实例方法
TencentCaptcha 的实例提供一些操作验证码的常用方法：

| 方法名 | 说明 | 传入参数 |返回内容|
|---------|---------|---------|--------|
| show | 显示验证码。 | 无 |无|
|destroy|隐藏验证码。|无|无|
|getTicket|获取验证码验证成功后的 ticket。|无|`Object:{"appid":"","ticket":""}`|

>?show 与 destroy 可以反复调用。
<span id="pzcs"></span>
### 配置参数
options 提供以下配置参数：

| 配置名 | 值类型 | 说明 |
|---------|---------|---------|
| bizState | Any | 自定义透传参数，业务可用该字段传递少量数据，该字段的内容会被带入 callback 回调的对象中。 |
