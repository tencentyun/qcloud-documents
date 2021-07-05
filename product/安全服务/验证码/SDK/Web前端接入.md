## 接入步骤
### 前提条件
接入验证码前，进入[图形验证](https://console.cloud.tencent.com/captcha/graphical)  页完成新建验证。可在【验证列表】查看 验证码接入所需的 CaptchaAppId 以及 AppSecretKey。
![](https://main.qcloudimg.com/raw/a15105526bbcf8c0b51b5cdafeefb92c.png)

### 快速接入
>!小程序插件 CaptchaAppId 仅限小程序插件接入方式使用，请勿使用在 Web 前端接入。

以下代码为图形验证功能的前端接入示例代码，根据应用场景，以此作为参考完成 Web 前端的接入。
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web 前端接入示例</title>
    <!-- 验证码程序依赖(必须)。请勿修改以下程序依赖，如使用本地缓存，或通过其他手段规避加载，会影响程序的正常使用。 -->
    <script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
</head>

<body>
    <!--点击此元素会自动激活验证码, 此例使用的button元素, 也可以使用div、span等-->
    <!--id :            (不可变) 元素的 ID, 值必须是 'TencentCaptcha'-->
    <!--data-appid :    (必须) 验证码CaptchaAppId, 从腾讯云的验证码控制台中获取, 验证码控制台页面内【图形验证】>【验证列表】进行查看 。如果未新建验证，请根据业务需求选择适合的验证渠道、验证场景进行新建-->
    <!--data-cbfn :     (必须) 回调函数名, 函数名要与 data-cbfn 相同-->
    <!--data-biz-state :(可选) 业务自定义透传参数, 会在回调函数内获取到 （res.bizState）-->
    <button id="TencentCaptcha" data-appid="你的验证码CaptchaAppId" data-cbfn="callbackName" data-biz-state="data-biz-state"
        type="button">验证</button>
</body>

<script>
    // 回调函数需要放在全局对象window下
    window.callbackName = function (res) {
        // 返回结果
        // ret         Int       验证结果，0：验证成功。2：用户主动关闭验证码。
        // ticket	  String	验证成功的票据，当且仅当 ret = 0 时 ticket 有值。
        // CaptchaAppId	   String	验证码应用ID。
        // bizState	Any	   自定义透传参数。
        // randstr	 String	本次验证的随机串，请求后台接口时需带上。
        console.log('callback:', res);


        // res（用户主动关闭验证码）= {ret: 2, ticket: null}
        // res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
        if (res.ret === 0) {
            // 复制结果至剪切板
            let str = `【randstr】->【${res.randstr}】      【ticket】->【${res.ticket}】`;
            let ipt = document.createElement('input');
            ipt.value = str;
            document.body.appendChild(ipt);
            ipt.select();
            document.execCommand("Copy");
            document.body.removeChild(ipt);
            alert('1. 返回结果（randstr、ticket）已复制到剪切板，ctrl+v 查看。\n2. 打开浏览器控制台，查看完整返回结果。');

        }
    }
</script>

</html>
```
>!验证码客户端接入完成后，验证码后台需二次核查验证码票据结果，请进行 [后台 API 接入](https://console.cloud.tencent.com/api/explorer?Product=captcha&Version=2019-07-22&Action=DescribeCaptchaResult&SignVersion=) 操作，确保验证安全性。更多详情请参见 [核查验证码票据文档](https://cloud.tencent.com/document/product/1110/36926) 。

### 定制接入
1. 如果不使用默认 id，可以通过实例化 TencentCaptcha 类，自定义参数来创建验证码组件。
>!绑定单击的元素不要使用`id="TencentCaptcha"`的元素，避免重复绑定单击。
>
2. TencentCaptcha 支持多种参数的重载，以下3种初始化方法，可根据具体情况选择其中一种。
 - **手动初始化。**
手动初始化的情况，一般是单击一个元素，执行一段逻辑，才调用验证码
```
new TencentCaptcha(CaptchaAppId, callback, options);
```
<table>
<thead><tr>
<th>参数名</th><th>值类型</th><th>说明</th></tr>
</thead>
<tbody><tr><td>CaptchaAppId</td><td>String</td>
<td>验证码应用 ID</td></tr><tr><td>callback</td><td>Function</td><td>回调函数</td>
</tr><tr><td>options</td><td>Object</td>
<td>更多配置参数, 请参见 <a href="#pzcs">配置参数</a></td>
</tr></tbody></table>
 - **绑定到一个元素。**
```
new TencentCaptcha(element);
```
<table>
<thead>
<tr>
<th>参数名</th>
<th>值类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>element</td>
<td>HTMLElement</td>
<td>验证码将绑定 click 事件到该元素上，该方式需要确保元素上有 data-appid 和 data-cbfn 属性。</td>
</tr>
</tbody></table>
 - **手动初始化并绑定到一个元素。**
```
new TencentCaptcha(element, CaptchaAppId, callback, options);
```
<table>
<thead>
<tr>
<th>参数名</th>
<th>值类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>element</td>
<td>HTMLElement</td>
<td>需要绑定<code>click</code>事件的元素</td>
</tr>
<tr>
<td>CaptchaAppId</td>
<td>String</td>
<td>验证码应用 ID</td>
</tr>
<tr>
<td>callback</td>
<td>Function</td>
<td>回调函数</td>
</tr>
<tr>
<td>options</td>
<td>Object</td>
<td>更多配置参数, 请参见 <a href="#pzcs">配置参数</a></td>
</tr>
</tbody></table>
 
 
- **示例代码**

```
//方法1: 直接生成一个验证码对象。
var captcha1 = new TencentCaptcha('CaptchaAppId', function(res) {/* callback */});
captcha1.show(); // 显示验证码

//方法2:绑定一个元素并自动识别场景id和回调。
// 验证码会读取dom上的`data-appid`和`data-cbfn`以及`data-biz-state`(可选)自动初始化
new TencentCaptcha(document.getElementById('TencentCaptchaBtn'));

//方法3：绑定一个元素并手动传入场景Id和回调。
new TencentCaptcha(
document.getElementById('TencentCaptchaBtn'),
'CaptchaAppId',
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
|CaptchaAppId|String|验证码应用 ID。|
|bizState|Any|自定义透传参数。|
|randstr|String|本次验证的随机串，请求后台接口时需带上。|

### 实例方法
TencentCaptcha 的实例提供一些操作验证码的常用方法：

| 方法名 | 说明 | 传入参数 |返回内容|
|---------|---------|---------|--------|
| show | 显示验证码，可以反复调用。 | 无 |无|
|destroy|隐藏验证码，可以反复调用。|无|无|
|getTicket|获取验证码验证成功后的 ticket。|无|`Object:{"CaptchaAppId":"","ticket":""}`|

### [配置参数](id:pzcs)
options 提供以下配置参数：
>!
- 验证码弹窗内部不支持调整样式大小，如果需要调整，可在弹窗最外层`id=tcaptcha_transform`的元素设置 `transform:scale();`。
- 如果手机原生端有设置左右滑动手势，需在调用验证码 show 方法前禁用，验证完成后再打开，防止与验证码滑动事件冲突。

|配置名	|值类型|	说明|
|---------|---------|---------|
|bizState|	Any|	自定义透传参数，业务可用该字段传递少量数据，该字段的内容会被带入 callback 回调的对象中。|
|enableDarkMode|	Boolean|	开启自适应深夜模式。|
|sdkOpts|	Object|	示例 {"width": 140, "height": 140}<br>移动端原生 webview 调用时传入，为设置的验证码弹框大小。<br>注意：手机原生端页面弹框通过 webview 加载验证码时须设置此值。若使用验证码 Web 的 loading，可设置一个小的值，然后在 ready 回调后重新设置尺寸。若自己实现 loading，此值可随意设置，等待 ready 回调后，再设置实际大小。|
|ready|	Function|	验证码加载完成的回调，回调参数为验证码实际的宽高：<br>{"sdkView": {<br>  "width": number,<br>  "height": number<br>}}<br>请勿使用此参数直接设定宽高，手机原生端可参考回调数值，设置弹框大小。|
|needFeedBack	|Boolean|	隐藏帮助按钮。<br>示例 { needFeedBack: false }|


## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击【快速咨询】，了解更多详细信息。
