## 使用说明
腾讯会议提供的 JSAPI 有很多是需要进行鉴权才能调用的，需要 wemeet.permission.config 或者 wemeet.permission.agentConfig 先进行鉴权，然后再调用。

## 鉴权步骤

### 步骤一：获取第三方应用 auth code（免登码）
调用 permission.authorize，实现第三方应用获取免登授权码。
- **支持的版本：**3.16.0
- **是否需要鉴权：**否

#### 功能描述
- 使用场景：业务方在需要获取用户的 authCode 以完成 Oauth 登录，当前用户尚未授权的情况下，也可通过此方法引导用户在当前页面弹框授权。
- 具体表现：在当前页面唤起授权弹框，实现发起授权。
 - PC 端：
![](https://qcloudimg.tencent-cloud.cn/raw/38842ac33a75a03c0662f9cc78cc0ba9.png)
 - 移动端：<br>
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c1c14d1dee686f1d5553a1b695ef57fe.png" />

#### 参数说明
授权请求入参如下，返回 Promise&lt;void&gt;。


| 参数名称 | 参数类型 |参数描述  |
|---------|---------|---------|
|success	|	function	|成功回调|
|failure|	function	|失败回调|
|timeout	| number	|超时时间，默认为5s|


#### 代码示例
```plaintext
permission.authorize({
  success: ({ authCode }) => { console.log(authCode) },
  // bizCode: 授权业务场景状态码，主要场景有以下几类：
  // 授权成功【0】：AuthorizeBizCode.SUCCEEDED
  // 申请授权成功【1】：AuthorizeBizCode.APPLY_SUCCEED 
  // 用户选择关闭授权弹框【2】 AuthorizeBizCode.CLOSED
  // 用户选择拒绝授权【3】 AuthorizeBizCode.REJECTED
  // 其他异常【4】，请根据bizMessage获知原因 AuthorizeBizCode.UN_KNOW
  fail: ({ bizCode, bizMessage }) => { 
     console.log(bizCode, bizMessage)
  },
}).catch(err => {
   console.error('authorize error', err);
 });
```



### 步骤二：通过 auth_code（免登码）换取账号 access_token
- **接口描述：**
 - 通过 auth_code（免登码）换取账号 access_token。
 - 切记 access_token 只可以存储在应用后台，不要暴露到前端页面，否则会有安全风险。
- **调用方法：**POST
- **接口请求域名：**
```plaintext
https://meeting.tencent.com/wemeet- webapi/v2/oauth2/oauth/access_token
```


#### 输入参数

| 参数名称 | 必选 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| sdk_id | 是 | String | OAuth 应用 ID |
| secret | 是 | String | OAuth 应用密钥 |
| auth_code | 是 | String | 免登码，有效期五分钟 |

#### 输出参数
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="60%" >参数描述</td>
   </tr>
   <tr>
      <td>code</td>
      <td>Int</td>
      <td>响应码</td>
   </tr>
   <tr>
      <td>message</td>
      <td>String</td>
      <td>响应描述</td>
   </tr>
   <tr>
      <td>nonce</td>
      <td>String</td>
      <td>请求 TracelD，可用于链路追踪</td>
   </tr>
   <tr>
      <td>data</td>
      <td>Object</td>
      <td>响应数据</td>
   </tr>
</table>

**data 内数据结构**
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="60%" >参数描述</td>
   </tr>
   <tr>
      <td>access_token</td>
      <td>String</td>
      <td>访问凭证（有效期6小时）</td>
   </tr>
   <tr>
      <td>refresh_token</td>
      <td>String</td>
      <td>用户刷新 access token 凭证（有效期30天）。刷新 access_token 时将同时自动续期30天。</td>
   </tr>
   <tr>
      <td>expires</td>
      <td>Int</td>
      <td>过期时间，时间戳（单位秒）</td>
   </tr>
   <tr>
      <td>open_id</td>
      <td>String</td>
      <td>用户唯一标识（同一 OAuth 应用，同一用户，值唯一）</td>
   </tr>
   <tr>
      <td>scopes</td>
      <td>String</td>
      <td>（后续废弃）用户授权的权限作用域，字符串数组。</td>
   </tr>
   <tr>
      <td>scopes_v2</td>
      <td>String</td>
      <td>用户授权的权限作用域，字符串数组。</td>
   </tr>
</table>


#### 示例
**输入示例**
```plaintext
{
"sdk_id":"10066660661",
 "secret":"fde85be844**13d2747d06313123fa", 
"auth_code":"98187ecd**4846ac555a658dcc1122 
}
```

**输出示例**
```plaintext
{
"sdk_id":"10066660661",
 "secret":"fde85be844**13d2747d06313123fa", 
"auth_code":"98187ecd**4846ac555a658dcc1122 
}
```


### 步骤三：获取 jsapi_ticket
- **接口描述：**
 - 根据 openid，accessToken 获取 jsticket。
 - jsapi_ticket 是一次性的，不可重复使用。
 - 当前用户获取的 jsapi_ticket，其他用户无法使用。
- **调用方式：** GET
- **接口请求域名：**
```plaintext
https://api.meeting.qq.com/v1/jsapi/ticket
```
- **header：**参见文档 [第三方应用鉴权（OAuth2.0）](https://cloud.tencent.com/document/product/1095/51257)。

#### 入参
无

#### 出参
| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| ticket | string | jsticket票据 |
| timestamp | string | 时间戳 |
| expired_time | string | 过期时间 |

#### 示例
输出参数：
```plaintext
{ 
  "code":0, 
  "message”: "SUCCESS"
  "nonce":"98187ecdebca4846",
  "data":{ 
     "access_token": "RRZ6+d8Y+JX2hwBtsmF9LpZwBi2qR/bBu3Wq8TmrGtYoV0FgvbnD985smogkZ6So/IgP5h+Lm+pAoxuR",
     "expires":1606985243,
     "refresh_token": "RZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wg8TmrGtYoV0FqvbnD985smogkZ6SoV IgP5i07r+pQoxu",
    "open_id" : "xqGn7bYSD601jnq8xq01CAlx5h12",
    "scopes":[
        "VIEW_USER_INFO", 
        "VIEW_VIDEO", 
        "MANAGE_VIDEO" 
    ]， 
    "scopes_v2" :[ 
       "personal-user-view", 
       "personal-recording-view",
       "personal-recording-edit" 
        ]，
    },   
}
```


### 步骤四：获取签名参数
在前端进行鉴权之前，需要获取以下签名所需的参数：

| **参数** | **字段类型** | **描述** |
| --- | --- | --- |
| corp_id | string | 企业 ID，企业在会议平台备案的 ID |
| sdk_id | string | 应用 ID, 接入方在会议平台备案的应用 ID |
| timestamp | string | 生成前面的时间对应秒级时间戳 |
| nonce_str | string | 接入方后台随机生成的字符串 |
| url | string | **当前需要初始化 JS_SDK 的页面地址，需在腾讯会议客户端内打开该地址** 。地址的 **域名** 必须是在会议平台备案的 **可信域名** 。（例如：`https://meeting.tencent.com/`，注意最后的符号；）（推荐从 header 的 refer 里面去获取，或者通过 location.href 去获取，不要写死） |
| ticket | string | 步骤二中的获取到的 JS_SDK Ticket |

### 步骤五：计算签名
接入方服务端生成 JS_SDK Config 给到自己的前端。

计算签名的示例代码（包含 go、java、python）可参见：[前端 JS-API 签名示例代码](https://cloud.tencent.com/document/product/1095/83774)；如遇问题，可通过 [JS-API 签名工具](https://meeting.tencent.com/marketplace/tools/jsapi-sigin) 进行自检。

JS_SDK Config 包含的字段：
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="60%" >参数描述</td>
   </tr>
   <tr>
      <td>corp_id</td>
      <td>String</td>
      <td>企业 ID</td>
   </tr>
   <tr>
      <td>sdk_id</td>
      <td>String</td>
      <td>应用 ID</td>
   </tr>
   <tr>
      <td>timestamp</td>
      <td>String</td>
      <td>生成前面的时间对应秒级时间戳</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>String</td>
      <td>接入方后台随机生成的字符串</td>
   </tr>
   <tr>
      <td>sign</td>
      <td>String</td>
      <td>配置参数签名</td>
   </tr>
</table>
上面参数中的 sign 是对多个参数的签名。签名规则如下：

 - 签名对应明文的字段
<table>
   <tr>
      <th width="20%" >字段顺序</td>
      <th width="20%" >参数名称</td>
      <th width="60%" >参数描述</td>
   </tr>
   <tr>
      <td>1</td>
      <td>corp_id</td>
      <td>企业 ID</td>
   </tr>
   <tr>
      <td>2</td>
      <td>sdk_id</td>
      <td>应用 ID</td>
   </tr>
   <tr>
      <td>3</td>
      <td>timestamp	</td>
      <td>生成前面的时间对应秒级时间戳</td>
   </tr>
   <tr>
      <td>4</td>
      <td>nonce_str	</td>
      <td>接入方后台随机生成的字符串</td>
   </tr>
   <tr>
      <td>5</td>
      <td>url</td>
      <td>需要初始化 JS_SDK 的当前页面地址（不要转码）</td>
   </tr>
   <tr>
      <td>6</td>
      <td>ticket</td>
      <td>接入方后台请求会议后台获取的 JS_SDK Ticket</td>
   </tr>
</table>

- 签名明文拼接
以下是样例明文，注意**字段顺序不可更改** ,字段间使用"&"间隔：
```plaintext
"corp_id=12345&sdk_id=67890&timestamp=1622517702&nonce_str=abcde&url=https://www.test.com/search?a=1&b=2&ticket=ABCDEFXX"
```
>!
>- url 字段包含协议头、域名、路径、Query 参数，不包含位置参数。例如：`https://www.test.com/search?a=1&b=2`。
>- 若当前 url 最后带有#号，例如：`https://www.test.com/search/#/`。

 由于#号是代表一个锚点，计算签名的时候，腾讯会议侧会忽略#号和#号后面的，故接入方也需要用代码处理，忽略掉#号和#号后面的，最终 url 应该为：`https://www.test.com/search/`。

- 签名方法
sha256

### 步骤六：引入使用的 JS
引入方法请参见：[引用方法](https://cloud.tencent.com/document/product/1095/83770)。

### 步骤七：JSAPI 鉴权
>!wemeet.permission.agentConfig 中所有的参数必须直接来自服务端，不能直接在前端定义。

调用 permission.agentConfig，实现第三方应用 JSAPI 鉴权。
- **支持的版本：**2.17.0
- **是否需要鉴权：**否

#### 参数说明
授权请求入参：
param：AuthConfigParam
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="60%" >参数描述</td>
   </tr>
   <tr>
      <td>sdkId </td>
      <td>String </td>
      <td>应用 ID</td>
   </tr>
   <tr>
      <td>corpId</td>
      <td>String</td>
      <td>企业 ID</td>
   </tr>
   <tr>
      <td>signature </td>
      <td>String</td>
      <td>签名</td>
   </tr>
   <tr>
      <td>nonceStr</td>
      <td>String</td>
      <td>生成签名的随机串</td>
   </tr>
   <tr>
      <td>timestamp</td>
      <td>String</td>
      <td>生成签名的时间戳</td>
   </tr>
</table>
返回 Promise&lt;void&gt;。

#### 代码示例
```plaintext
wemeet.permission.agentConfig({
  sdkId: SDKID,
  corpId: CROPID,
  signature: SINGATURE,
  nonceStr: NONCE_STR,
  timestamp: TIMESTAMP,
})
  .then(() => {
  })
  // success
  .catch((err) => {
    // failed
  });

```

### 步骤八：调用 JSAPI
步骤七鉴权通过以后就可以调用 JSAPI 了。
