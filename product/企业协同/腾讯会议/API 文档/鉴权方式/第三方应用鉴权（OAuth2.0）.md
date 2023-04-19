创建应用后即可获取应用凭证信息，具体可参见 [第三方应用接入指引](https://cloud.tencent.com/document/product/1095/83663)。

## 公共参数
公共参数是用于标识用户和接口鉴权目的的参数，如非必要，在每个接口单独的接口文档中不再对这些参数进行说明，但每次请求均需要携带这些参数，才能正常发起请求。
公共参数需要统一放到 HTTP Header 请求头部中。


| **参数名称**    | **类型** | **必选** | **描述**                                                     |
| --------------- | -------- | -------- | ------------------------------------------------------------ |
|Content-Type|String|是|内容类型，传入格式必须为 application/json。|
| X-TC-Action | String| 否 |操作的接口名称。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| X-TC-Region | String| 否 |地域参数，用来标识希望操作哪个地域的数据。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效**。 |
| X-TC-Timestamp  |  String   | 是       | 此参数参与签名计算。当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，单位为秒。<br>**注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。** |
| X-TC-Nonce      |  String  | 是       | 此参数参与签名计算，随机正整数。                               |
| X-TC-Version    | String   | 否       | 应用 App 的版本号，建议设置，以便灰度和查找问题。通过设置该字段，API 会把该版本信息传递给会议后台, 以控制一些和 App 版本有关的特性。 |
| AccessToken      | String   | 是       | OAuth2.0 鉴权成功后返回的 token 信息。                            |
| OpenId          | String   | 是       | OAuth2.0 鉴权成功后的用户信息。                                 |


>!构造请求头的时候，需注意自定义字段名的大小写。服务器端读取字段值时对大小写敏感。

## 授权方式
下面将为您介绍 OAuth 2.0的授权步骤，您可以使用 [Postman 模板调试](https://cloud.tencent.com/document/product/1095/83483)，按照步骤中描述的请求参数调用接口即可，具体如下：

### 步骤一：用户同意授权，获取 auth_code
#### 场景1：在浏览器中使用第三方应用，可通过此方法打开用户授权新页面，获取 auth_code。
**具体表现：**
- PC 端浏览器：
![](https://qcloudimg.tencent-cloud.cn/raw/79d5bd280eb134318a4c7b790763b5d9.png)
- 移动端浏览器：<br>
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/dc931b7ea069878294f547bf651937ae.png" />

**接口描述**
- **描述：**用户同意授权。
- **请求方法：**GET
- **请求域名：**
```html
https://meeting.tencent.com/marketplace/authorize.html?corp_id={corpId}&sdk_id={sdkId}&redirect_uri={redirect_uri}&state={state}
```

**输入参数**
Header 参数：不需要。

| 参数名称 | 必选 | 参数类型 |参数描述 |
|---------|---------|---------|---------|
|corp_id	|是	|String	OAuth |应用的企业 ID。|
|sdk_id	|是	|String	OAuth |应用 ID。|
|redirect_uri	|是|	String	|授权后重定向的回调链接地址，请使用 urlEncode 对链接进行处理。|
|state	|是|	String|	重定向后会带上 state 参数，开发者可以填写 a-zA-Z0-9 的参数值，最多64字节。|

**输出参数**

|参数名称	|参数类型	|参数描述|
|---------|---------|---------|
|auth_code	|String	|授权码。|
|state|	String	|入参的 state，接入方自行校验，防止 CSRF 攻击。|

**示例**
**输入示例**
接入方302重定向到授权 URL，例如：
```plaintext
https://meeting.tencent.com/marketplace/authorize.html?corp_id=200000999&sdk_id=10066660661&redirect_uri=https%3a%2f%2fqq.com%2fcallback%3fa%3d1%26b%3d2&state=123456789 
```
  
**输出示例**
```plaintext
HTTP/1.1 302 Found Location: https://qq.com/callback?a=1&b=2&auth_code=98187ecd****4846ac555a658dcc1122&state=123456789 Date: Wed, 02 Dec 2020 13:36:38 GMT Content-Length: 2 Content-Type: text/plain; charset=utf-8
```


#### 场景2：在腾讯会议会议客户端和 App 内，可通过 JS-API，在当前页面唤起用户授权弹框，获取 auth_code。
**具体表现：**在当前页面唤起授权弹框，实现发起授权。
- PC 客户端：
![](https://qcloudimg.tencent-cloud.cn/raw/8d6c337d3f6c3d686b252e29e4b9af65.png)
- 移动端 App：<br>
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9d84c467278bb003425255dd0feb1911.png" />

**接口描述**
- **描述：**调用 permission.authorize，实现第三方应用获取免登授权码。
- **支持的版本：**3.16.0
- **是否需要鉴权：**否
- **使用说明：**业务方在腾讯会议 App 或者客户端内需要获取用户的 authCode 以完成 Oauth 登录，当前用户尚未授权的情况下，也可通过此方法引导用户在当前页面弹框授权。

**参数说明**
授权请求入参如下，返回 Promise&lt;void&gt;。

| 参数名称 | 参数类型 | 参数描述 |
|---------|---------|---------|
|success	|	function	|成功回调|
|failure|	function	|失败回调|
|timeout	| number	|超时时间，默认为5s|

**代码示例**
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




### 步骤二：通过 auth_code 换取授权 access_token
**接口描述**：通过 auth_code 换取授权 access_token。
**接口请求方法**：POST 
**接口请求域名**：
```Plaintext
https://meeting.tencent.com/wemeet-webapi/v2/oauth2/oauth/access_token
```

>!由于授权的 secret 和获取到的 access_token 安全级别都非常高，必须只保存在服务器，不允许传给客户端。后续刷新 access_token、通过 access_token 获取用户信息等步骤时，也必须从服务器发起。

**Header 参数：**统一放到 HTTP Header 请求头部中。

| 参数名称| 类型 | 必选 |描述 |
|---------|---------|---------|---------|
| Content-Type | String | 是 |内容类型，传入格式必须为 application/json。 |


#### 输入参数

| 参数名称  | 必选 | 参数类型 | 参数描述      |
| --------- | ---- | -------- | ------------- |
| sdk_id    | 是   | String   | OAuth 应用 ID。   |
| secret    | 是   | String   | OAuth 应用密钥。 |
| auth_code | 是   | String   | 授权码，有效期五分钟。        |

#### 输出参数

| 参数名称      | 参数类型  | 参数描述                                        |
| ------------- | --------- | ----------------------------------------------- |
| access_token  | String    | 访问凭证（有效期6小时）。                           |
| refresh_token | String    | 用户刷新 access_token 凭证（有效期30天）。         |
| expires       | Int       | access_token 过期时间，时间戳（单位秒）。           |
| open_id       | String    | 用户唯一标识（同一 OAuth 应用，同一用户，值唯一）。 |
| scopes        | String | 用户授权的权限作用域，字符串数组。                |
| open_corp_id        | String | 授权用户的企业 ID，免费版用户返回为空。                |

#### 示例
**输入示例**
```Plaintext
{
  "sdk_id":"10066660661",    
  "secret":"fde85be844****13d2747d06313123fa", 
  "auth_code":"98187ecd****4846ac555a658dcc1122"
}
```


**输出示例**
```Plaintext
{
    "nonce" : "98187ecdebca4846",
    "data" : {
        "access_token" : "RRZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5h+Lm+pAoxuR",
        "expires" : 1606985243,
        "refresh_token" : "RZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5iO7r+pQoxu",
        "scopes" : [
            "VIEW_USER_INFO",
            "VIEW_VIDEO",
            "MANAGE_VIDEO"
        ],
        "open_id" : "xqGn7bYSD601jnq8xq0lCAlx5h12"
    },
    "message" : "SUCCESS",
    "code" : 0
}

```


### 步骤三：刷新 access_token（如有需要）
**接口描述**：通过 refresh_token，令牌续约。 
**接口请求方法**：POST
**接口请求域名**：
```Plaintext
https://meeting.tencent.com/wemeet-webapi/v2/oauth2/oauth/refresh_token
```
**Header 参数：**统一放到 HTTP Header 请求头部中。

| 参数名称| 类型 | 必选 |描述 |
|---------|---------|---------|---------|
| Content-Type | String | 是 |内容类型，传入格式必须为 application/json。 |

#### 输入参数

| 参数名称      | 必选 | 参数类型 | 参数描述                                            |
| ------------- | ---- | -------- | --------------------------------------------------- |
| refresh_token | 是   | string   | 刷新凭证。                                          |
| sdk_id        | 是   | string   | OAuth 应用 ID。                                     |
| open_id       | 是   | string   | 用户唯一标识（同一 OAuth 应用，同一用户，值唯一）。 |


#### 输出参数

| 参数名称      | 参数类型  | 参数描述                                            |
| ------------- | --------- | --------------------------------------------------- |
| access_token  | string    | 访问凭证（有效期6小时）。                           |
| refresh_token | string    | 用户刷新 access_token 凭证（有效期30天），刷新 access_token 时将同时自动续期30天。          |
| expires       | int       | access_token 过期时间，时间戳（单位秒）。           |
| open_id       | string    | 用户唯一标识（同一 OAuth 应用，同一用户，值唯一）。 |
| scopes        | string | 用户授权的权限作用域，字符串数组。                  |


#### 示例
**输入示例**

```Plaintext
{
   "sdk_id":"10066660661",
"refresh_token":"RZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5iO7r+pQoxu", "open_id":"xqGn7bYSD601jnq8xq0lCAlx5h12"
}
	 
```


**输出示例**

```Plaintext
{
    "nonce" : "98187ecdebca4846",
    "data" : {
        "access_token" : "RRZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5h+Lm+pAoxuR",
        "expires" : 1606985243,
        "refresh_token" : "RZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5iO7r+pQoxu",
        "scopes" : [
            "VIEW_USER_INFO",
            "VIEW_VIDEO",
            "MANAGE_VIDEO"
        ],
        "open_id" : "xqGn7bYSD601jnq8xq0lCAlx5h12"
    },
    "message" : "SUCCESS",
    "code" : 0
}

```


### 步骤四：拉取用户信息（检验凭证是否有效）
**接口描述**：拉取用户信息（检验凭证是否有效）。
**接口请求方法**：POST
**接口请求域名**：
```Plaintext
https://meeting.tencent.com/wemeet-webapi/v2/oauth2/oauth/user_info
```
**Header 参数：**统一放到 HTTP Header 请求头部中。

| 参数名称| 类型 | 必选 |描述 |
|---------|---------|---------|---------|
| Content-Type | String | 是 |内容类型，传入格式必须为 application/json。 |

#### 输入参数

| 参数名称     | 必选 | 参数类型 | 参数描述                                        |
| ------------ | ---- | -------- | ----------------------------------------------- |
| access_token | 是   | string   | 访问凭证。                                        |
| open_id      | 是   | string   | 用户唯一标识（同一 OAuth 应用，同一用户，值唯一）。 |


#### 输出参数

| 参数名称 | 参数类型  | 参数描述                                        |
| -------- | --------- | ----------------------------------------------- |
| expires  | string    | access_token 过期时间，时间戳（单位秒）。           |
| open_id  | string    | 用户唯一标识（同一 OAuth 应用，同一用户，值唯一）。 |
| scopes   | string| 用户授权的权限作用域，字符串数组。                |

#### 示例
**输入示例**


```Plaintext
{
"access_token":"RZ6+d8Y+JX2hwBtsmF9LpZwBi2gR/bBu3Wq8TmrGtYoV0FqvbnD985smoqkZ6SoV/IgP5iO7r+pQoxu", 
"open_id":"xqGn7bYSD601jnq8xq0lCAlx5h12"
}
```

**输出示例**
```Plaintext
{
    "nonce" : "98187ecdebca4846",
    "data" : {
        "expires" : 1606985243,
        "scopes" : [
            "VIEW_USER_INFO",
            "VIEW_VIDEO",
            "MANAGE_VIDEO"
        ],
        "open_id" : "xqGn7bYSD601jnq8xq0lCAlx5h12"
    },
    "message" : "SUCCESS",
    "code" : 0
}
```

## 鉴权错误返回参数
鉴权错误返回统一为400。
