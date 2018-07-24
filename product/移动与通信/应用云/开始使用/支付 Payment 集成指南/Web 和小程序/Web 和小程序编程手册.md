## 集成说明

引入 JsApi：`<script src="https://midas.gtimg.cn/openmidas/jsapi/openMidas.js"></script>`
为了支持多域名情况，除了`openMidas.js`，还有一个额外的`openMidasConfig.js`路径为 `https://midas.gtimg.cn/openmidas/jsapi/config/openMidasConfig.xxx.js` 用于域名配置，在引入之前需要引入这个配置文件，默认情况下 openMidas 会走公有云的环境，可以不引入配置。

## 支付初始化

**说明**：初始化接口，使用 OpenMidas 其它接口之前必须调用本接口。

**接口**：`OpenMidas.init(env)`

**参数说明如下**： 

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
env | String | 是 | 环境，release 表示正式环境，test 表示测试环境

## 支付接口

### Web 支付接口

**说明**：本接口同时支持H5支付、公众号支付。

**接口 1**：弹框形式调用
```
OpenMidas.pay(payInfo, callback, appMetadata);
```

**参数说明如下**：

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
payInfo | String | 是 | 支付参数，详见 [服务器端 API](https://cloud.tencent.com/document/product/666/17994#.E5.95.86.E5.93.81.E4.B8.8B.E5.8D.95) 商品下单接口返回值里的 pay_info
callBack | Function | 是 | 支付完成回调函数，回调参数说明看下文“回调 url 示例”
appMetadata | String | 否 | 扩展字段，key=value 形式，最大长度 255。客户端回调时回传给调用方。

**调用方式示例**：

```javascript
someAsyncRequest(function(payInfo){
    OpenMidas.pay(payInfo, function(resultCode, innerCode, resultMsg, appMetadata){
        //业务处理代码
    }, appMetadata);//方式1调用
});
```

**接口 2**：页面跳转形式调用支付完成后会回调业务在下单时传入的 Web 回调地址。
```javascript
OpenMidas.pay(payInfo, appMetadata);
```

**参数说明如下**：

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
payInfo | String | 是 | 支付参数，详见 [服务器端 API](https://cloud.tencent.com/document/product/666/17994#.E5.95.86.E5.93.81.E4.B8.8B.E5.8D.95) 商品下单接口返回值里的 pay_info
appMetadata | String | 否 | 扩展字段，key=value 形式，最大长度 255。客户端回调时回传给调用方。

**调用方式示例**：

```javascript
someAsyncRequest(function(payInfo){
   OpenMidas.pay(payInfo, appMetadata);//方式2调用
});
```

**回调 url 示例**：
```
[callbackurl]?resultCode=0&innerCode=100-xxx&resultMsg=encode(支付成功)&appMetadata=xxxxx
```

### 小程序支付接口

**说明**：将 openMidas.js 文件放入工程目录，并通过如下方式引入

```javascript
var OpenMidas = require("openMidas");
```

为了支持多域名情况，除了`openMidas.js`还有一个额外的`openMidasConfig.js`用于域名配置，在 require jsapi 之前需要引入这个配置文件，默认情况下 openMidas 会走公有云的环境。

**说明**：初始化接口，使用 openMidas 其它接口之前必须调用本接口。

**接口**：`OpenMidas.init(env)`

**参数说明如下**： 

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
env | String | 是 | 环境，release 表示正式环境，test 表示测试环境

**接口**： 

```
OpenMidas.pay(String payInfo, Function callback, String appMetadata)
```

**参数说明如下**：

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
payInfo | String | 是 | 支付参数，详见 [服务器端 API](https://cloud.tencent.com/document/product/666/17994#.E5.95.86.E5.93.81.E4.B8.8B.E5.8D.95) 商品下单接口返回值里的 pay_info
callBack | Function | 是 | 支付完成回调函数，回调参数说明详见“小程序支付接口”
appMetadata | String | 否 | 扩展信息回传，透传支付时传入的参数。同支付时传入的 appMetadata

**调用方式示例**：

```
var OpenMidas=require("openMidas");
OpenMidas.init(env);
OpenMidas.pay(payInfo, function(resultCode, innerCode, resultMsg, appMetadata){
    //业务处理代码
}, appMetadata);
```

### 支付回调参数

属性 | 类型 | 取值
--- | --- | ---
resultCode | Int | 0(PAYRESULT_SUCC 支付流程成功),-1(PAYRESULT_ERROR 支付流程失败),-2(PAYRESULT_CANCEL 用户取消),-3(PAYRESULT_PARAMERROR 参数错误),-4(PAYRESULT_UNKNOWN 支付流程结果未知，如第三方渠道未回调米大师)
innerCode | String | 系统内部错误码，不直接展示给用户
resultMsg | String | 返回信息，不直接展示给用户
appMetadata | String | 扩展信息回传，透传支付时传入的参数。同支付时传入的 appMetadata

## 签约接口

### Web 签约接口

引入 JsApi：`<script src="https://midas.gtimg.cn/midas/open/openMidas.js"></script>`

**说明**：初始化接口，使用 OpenMidas 其它接口之前必须调用本接口。

**接口**：`OpenMidas.init(env)`

**参数说明如下**：

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
env | String | 是 | 环境，release 表示正式环境，test 表示测试环境

**说明**：签约接口

**接口**：
```
OpenMidas.signContract(Object params,Function errorCallback)
```

**参数说明如下**： 

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | --- |
params.appId | String | 是 | 米大师的应用 ID 
params.userId | String | 是 | 用户 ID
params.channel | String | 是 | 签约渠道，可选值：wechat（使用微信签约）
params.redirectUrl | String | 是 | 签约完成之后的回调 url，当用户从签约 url 返回时，会跳转到这个 url 上，url 参数会带上 appId、openId、channel、fromSign=1。
errorCallback | Function | 否 | 当内部参数校验不通过或者后台返回错误时，会执行回调，回调参数参见下表“错误回调参数说明”。

**错误回调参数说明**：
 
属性 | 类型 | 取值
--- | --- | ---
resultCode | Int | -1(PAYRESULT_ERROR 签约流程失败流程失败),-3(PAYRESULT_PARAMERROR 参数错误)
innerCode | String | 系统内部错误码，不直接展示给用户
resultMsg | String | 返回信息，不直接展示给用户

**说明**：签约接口事件

signContractDone 已经获取到相关签约参数，准备跳转到签约页面之前触发，调用方可以在这个事件内把自定义的 loading 取消。注意需要在调用了 signContract 接口之后才能注册这个事件。

**示例**：

```
OpenMidas.once('signContractDone',function(){
   //调用方代码
})
```


### 小程序签约接口

**说明**：将 openMidas.js 文件放入工程目录，并通过如下方式引入

```
var OpenMidas=require("openMidas");
```

为了支持多域名情况，除了 openMidas.js 还有一个额外的 openMidasConfig.js 用于域名配置，在 require jsapi 之前需要引入这个配置文件，默认情况下 openMidas 会走公有云的环境。

**接口**：

```
OpenMidas.init(env)
```

**参数说明如下**： 

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
env | String | 是 | 环境，release 表示正式环境，test 表示测试环境


**说明**：签约接口

**接口**：

```
OpenMidas.signContract(Object params,Function errorCallback)
```

**参数说明如下**：

参数名 | 参数类型 | 必填 | 参数说明
--- | --- | --- | ---
params.appId | String | 是 | 米大师的应用 ID 
params.userId | String | 是 | 用户 ID
errorCallback | Function | 否 | 当内部参数校验不通过或者后台返回错误时，会执行回调，回调参数参见下表“错误回调参数说明”。

**错误回调参数说明**：

属性 | 类型 | 取值
--- | --- | ---
resultCode | Int | -1 签约流程失败流程失败,-3 参数错误,-101 重复签约
innerCode | String | 系统内部错误码，不直接展示给用户，以下特殊 innerCode 需要调用方特殊处理：402-1-2-1 小程序签约接口不存在，原因是微信客户端版本未满足 Android：6.5.10，IOS：6.5.9。402-1-2-2 未成功跳转到小程序签约，此时 resultMsg 透传微信侧返回的错误。 
resultMsg | String | 返回信息，不直接展示给用户

**说明**：签约接口事件

signContractDone 已经获取到相关签约参数，准备跳转到签约页面之前触发，调用方可以在这个事件内把自定义的 loading 取消。注意需要在调用了 signContract 接口之后才能注册这个事件。

```
var OpenMidas=require("openMidas");
OpenMidas.once('signContractDone',function(){
   //调用方代码
})
```

### 签约回调

小程序签约回调是由微信侧回调到App层的，详见微信文档  [小程序纯签约](https://pay.weixin.qq.com/wiki/doc/api/pap.php?chapter=18_14&index=2)。

![签约回调](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/payment/web_sign_callback.png)
