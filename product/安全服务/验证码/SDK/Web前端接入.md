## 接入步骤
### 前提条件
接入验证码前，进入[图形验证](https://console.cloud.tencent.com/captcha/graphical)  页完成新建验证。可在**验证列表**查看 验证码接入所需的 CaptchaAppId 以及 AppSecretKey。
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
	    // res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String",  errorCode: Number, errorMessage: "String"}
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


### 异常处理
以下为验证 JS 文件引入错误处理。

1. 定义错误处理函数
``` javascript
// 在脚本加载或初始化错误时 需手动绑定button元素的事件确保流程正常
// 函数定义需在script加载前
function TCaptchaLoadError(){
  var CaptchaAppId=''
  document.getElementById('TencentCaptcha').addEventListener('click', function () {
    var CaptchaAppId = ''
    /* 生成票据或自行做其它处理 */
    var ticket = 'terror_1001_' + CaptchaAppId + '_' + Math.floor(new Date().getTime()/1000)
    window.callback({
      ret: 0,
      randstr: '@'+Math.random().toString(36).substr(2),
     ticket: ticket,
      errorCode: 1001,
      errorMessage: 'jsload_error'
    })
  }, false)
}
```
2. 在 html 中加入以下代码引入验证 JS 文件。
```html
<!-- 如果script是在head中引入 onerror的函数需等domready再绑定元素事件 在body中加载无需等待 -->
<script src="https://ssl.captcha.qq.com/TCaptcha.js" onerror="TCaptchaLoadError()"></script>
```
3. 建议根据 ticket 和 errorCode 情况而非 ret 的值做处理，更精确和稳定。
```javascript
window.callback = function(res){
  /* res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
   res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String", 
                                         errorCode: Number, errorMessage: "String"}
   res（用户主动关闭验证码）= {ret: 2}
   */
  if (res.ticket){
    // 上传票据 可根据errorCode和errorMessage做特殊处理或统计
  }
}
```


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
try {
  var captcha1 = new TencentCaptcha('CaptchaAppId', callback);
  captcha1.show(); // 显示验证码
} catch (error) {
  loadErrorCallback();
}
//方法2:绑定一个元素并自动识别场景id和回调。
try {
// 绑定一个元素并自动识别场景id和回调
// 验证码会读取dom上的`data-appid`和`data-cbfn`以及`data-biz-state`(可选)自动初始化
  new TencentCaptcha(document.getElementById('TencentCaptcha'));
} catch (error) {
  loadErrorCallback();
}
//方法3：绑定一个元素并手动传入场景Id和回调。
try { 
  new TencentCaptcha(
    document.getElementById('TencentCaptcha'),
    'CaptchaAppId',
    callback,
    { bizState: '自定义透传参数' },
  );
} catch (error) {
  loadErrorCallback();
}

function callback(res) {
  /* res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
     res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String", errorCode: Number, errorMessage: "String"}
     res（用户主动关闭验证码）= {ret: 2}
  */
  if (res.ticket){
    // 上传票据 可根据errorCode和errorMessage做特殊处理或统计
  }
}
// 验证码js加载错误处理
function loadErrorCallback() {
  var CaptchaAppId = ''
   /* 生成票据或自行做其它处理 */
  var ticket = 'terror_1001_' + CaptchaAppId + Math.floor(new Date().getTime() / 1000);
  callback({
    ret: 0,
    randstr: '@'+ Math.random().toString(36).substr(2),
    ticket: ticket,
    errorCode: 1001,
    errorMessage: 'jsload_error',
  });
}
```


### 回调内容
前端验证成功后，验证码会调用业务传入的回调函数，并在第一个参数中传入回调结果。结果字段说明如下：

| 字段名       | 值类型 | 说明                                              |
| ------------ | ------ | ------------------------------------------------- |
| ret          | Int    | 验证结果，0：验证成功。2：用户主动关闭验证码。    |
| ticket       | String | 验证成功的票据，当且仅当 ret = 0 时 ticket 有值。 |
| CaptchaAppId | String | 验证码应用 ID。                                   |
| bizState     | Any    | 自定义透传参数。                                  |
| randstr      | String | 本次验证的随机串，请求后台接口时需带上。          |
| errorCode    | Number | 错误 code ，详情请参见 [回调函数 errorCode 说明](#errorCode)          |
| errorMessage | String | 错误信息                                          |

[](id:errorCode)
**回调函数errorCode说明**

| errorCode | 说明                    |
| --------- | ----------------------- |
| 1001      | TCaptcha.js 加载错误    |
| 1002      | 调用 show 方法超时        |
| 1003      | 中间 js 加载超时          |
| 1004      | 中间 js 加载错误          |
| 1005      | 中间 js 运行错误          |
| 1006      | 拉取验证码配置错误/超时 |
| 1007      | iframe 加载超时          |
| 1008      | iframe 加载错误          |
| 1009      | jquery 加载错误          |
| 1010      | 滑块 js 加载错误          |
| 1011      | 滑块 js 运行错误          |
| 1012      | 刷新连续错误3次         |
| 1013      | 验证网络连续错误3次     |




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
- 验证码弹窗内部不支持调整样式大小，如果需要调整，可在弹窗最外层用 `class=tcaptcha-transform` 的元素设置 `transform:scale();`。验证码更新可能会改变元素的 id，class 等属性，请勿依赖其他验证码元素属性值覆盖样式。
- 如果手机原生端有设置左右滑动手势，需在调用验证码 show 方法前禁用，验证完成后再打开，防止与验证码滑动事件冲突。


| 配置名         | 值类型          | 说明                                                         |
| :------------- | :-------------- | :----------------------------------------------------------- |
| bizState       | Any             | 自定义透传参数，业务可用该字段传递少量数据，该字段的内容会被带入 callback 回调的对象中。 |
| enableDarkMode | Boolean,'force' | 开启自适应深夜模式, 'force'将强制深夜模式。                  |
| sdkOpts        | Object          | 示例 {"width": 140, "height": 140}<br>仅支持移动端原生 webview 调用时传入，为设置的验证码元素 loading 弹框大小。 |
| ready          | Function        | 验证码加载完成的回调，回调参数为验证码实际的宽高：<br>{"sdkView": {<br>"width": number,<br>"height": number<br>}}<br>请勿使用此参数直接设定宽高。 |
| needFeedBack   | Boolean         | 隐藏帮助按钮。 示例 { needFeedBack: false }                  |
| userLanguage   | String          | 指定验证码提示文案的语言，优先级高于后台配置，暂时仅支持滑块拼图验证码。支持传入值同 navigator.language 用户首选语言，大小写不敏感。详情请参见 [userLaguage 配置参数](#userLanguage)。 |

**userLaguage 配置参数**[](id:userLanguage)

| 参数名 | 说明                 |
| :------- | :------------------- |
| zh-cn    | 简体中文             |
| zh-hk    | 繁体中文（中国香港） |
| zh-tw    | 繁体中文（中国台湾） |
| en       | 英文                 |
| ar       | 阿拉伯语             |
| my       | 缅甸语               |
| fr       | 法语                 |
| de       | 德语                 |
| he       | 希伯来语             |
| hi       | 印地语               |
| id       | 印尼语               |
| it       | 意大利语             |
| ja       | 日语                 |
| ko       | 朝鲜语               |
| lo       | 老挝语               |
| ms       | 马来语               |
| pl       | 波兰语               |
| pt       | 葡萄牙语             |
| ru       | 俄语                 |
| es       | 西班牙语             |
| th       | 泰语                 |
| tr       | 土耳其语             |
| vi       | 越南语               |




## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**，了解更多详细信息。
