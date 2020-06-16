## OAuth2.0 概述
OAuth2.0 是一个开放授权标准，它允许用户让**第三方应用**访问该用户在某服务的**特定私有资源**但是**不提供账号密码信息**给第三方应用。
>?OAuth2.0 是一个授权协议，不是认证协议。

### OAuth2.0 角色说明
OAuth2.0 有以下四个角色： 
- Resource Owner：资源拥有者。
- Resource Server：资源服务器。
- Client：第三方应用客户端，指任何可以消费资源服务器的第三方应用。
- Authorization Server：授权服务器，管理上述三个角色的中间层。

### 授权流程
![](https://main.qcloudimg.com/raw/27814a835f31fd1511ef3247764ee1c7.png)
（A）：客户端请求资源所有者的授权。
（B）：资源所有者同意授权。
（C）：客户端获得了资源所有者的授权之后，向授权服务器申请授权令牌。
（D）：授权服务器验证客户端无误后发放授权令牌。
（E）：客户端拿到授权令牌之后请求资源服务器发送用户信息。
（F）：资源服务器验证令牌无误后将用户信息发放给客户端。


## API 网关 OAuth2.0 操作方法
   腾讯云API 网关对外提供了 OAuth2.0 功能，为了能够快速的使用该功能，首先提供简化版的使用方式，准备以下：
 - 分发 token 的授权服务器（当前提供python3的Demo），
 - API网关配置，同一个服务下创建一个授权API，一个业务API，其中授权API是用来校验请求业务API中携带的 token 是否合法，以及提供获取token的链接，

### 授权服务器的搭建
[代码路径 >>]( https://github.com/TencentCloud/apigateway-demo/tree/master/apigateway-oauth-python-demo)
1. 生成 RSA 公钥和私钥。使用 Python3 运行 produce_key.py，生成三个文件：
 - public_pem ：pem 格式的公钥
 - priv_pem ：pem 格式的私钥
 - pulic ：json 格式的公钥，该文件的内容用于配置 API 网关的授权 API。具体格式如下：：
```
{"e":"AQAB","kty":"RSA","n":"43nSuC6lmGLogEPgFVwaaxAmPDzmZcocRB4Jed_dHc-sV7rcAcNB0iHyuGfNkfOAE2uhHVjdXuO6DBYGz4pnTwRZ5_wFrW0DlrlJQAXSvg6B2N1uda_aqySNw3rrvdh38rVG7HxFmyPbLXcpJtyfkiRNyZ1WhSpH0NciIRrFbW2mKRtOZsBGfBgmNqPGcGrMA71cuqNAQ9RMKmAF37iGXkx0tWMBQ_PL2aviHhtsiPbT3zIO7qUG3cleBHnS61kid3K8F38z9-5Hj-1zdTIP8iS4rAt4FmhvKvtOocRPYGq0W_dLLxmi4DYgIV2GJE93WyZ1EUvgRGhpcHvyT65z4w"}
```

2. 启动服务。安装 bottle 库、pip3 install bottle 后，使用 Python3 运行 server.py。
首先执行 produce_key.py 生成三个文件后，再执行 server.py，用于提供 token，执行后可以简单验证生成 token是否成功。
```
curl localhost:8080/token 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIyNzgwODksImZvbyI6ImJhciIsImlhdCI6MTU5MjI3Nzc4OSwianRpIjoibFY1TS10S2oxMEdtV0pJcHotM01GUSIsIm5iZiI6MTU5MjI3Nzc4OSwid3VwIjo5MH0.aHyZo2jgkNxVRDMtEiRBU4-n0pMfa0gocu92KQBe-nmbFoeI_5EWTJ8XFNnSIuoCAIFvrd9MSUX2DNVTg0woXukjoKOTjZSx4txknaXs1aApdvW74FVddCrMtdLrKh_VlwPOrEaOGesmtfcR3RN8xWnj1oedPW-HKPEqVpIAIIWO8ilCBFF-5yffcnFGIbfYO0t7OeBBviCQnQjWAmQHnteOZm0CBeG22k7rlnjH96qE_kyq7DHQqGmURjlpGxoXRC6E-AiV-3mYrCGnsAosEltuIUtq8VIbTZabSobFDE92C8us4GFtIVJQB2NWgeB3Hxgpz3Dlb4NCCcCkZbryEQ
```

### 配置腾讯云 API 网关的授权 API 和 业务 API

前提条件：已经创建一个 API 网关服务（参考 [创建服务](https://cloud.tencent.com/document/product/628/11787)）

#### 配置腾讯云 API 网关的授权 API 
1. 创建授权 API（参考 [创建通用 API](https://cloud.tencent.com/document/product/628/11797)），前端配置时，鉴权类型选择 OAuth2.0，OAuth 模式选择授权 API。
![](https://main.qcloudimg.com/raw/15e1037c697b18395be29a7520d7f403.png)
2. 后端配置时，认证服务器选择自己的个人服务器地址，token 位置选择 Header，公钥为4.1中执行文件produce_key.py 生成的 public 文件中的内容，创建完成后单击【完成】。
![](https://main.qcloudimg.com/raw/2cd37daa0975fd88cbddf0eddc722a38.png)

#### 配置腾讯云 API 网关的业务 API 
1. 创建授权 API（参考 [创建通用 API](https://cloud.tencent.com/document/product/628/11797)），前端配置时，鉴权类型选择 OAuth2.0，OAuth 模式选择业务 API，关联授权API选择刚刚创建的授权API。
![](https://main.qcloudimg.com/raw/51e5340d331fb6b75cd0cf79115ebd82.png)
2. 后端配置时，后端类型选择 Mock 类型，返回 hello world。
![](https://main.qcloudimg.com/raw/1f9d8c12673aacf852c4d618d518c933.png)



### 示例演示
 先获取 token ，本文直接从授权服务器快速获取 token。
 >?为保护授权服务器本身，您也可以请求 API 网关的授权 API 地址来获取 token。

- 请求授权 API，获取 token：
```
curl http://service-cmrrdq86-1251890925.gz.apigw.tencentcs.com:80/token
```
返回结果：
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIyNzk3MTAsImZvbyI6ImJhciIsImlhdCI6MTU5MjI3OTQxMCwianRpIjoiZlBGYlFZRkR4REx3d0lXTFl0aHBBQSIsIm5iZiI6MTU5MjI3OTQxMCwid3VwIjo5MH0.0JQquNRVCQ8n9hPV-mJi6Mku_7G3T1jFp68Sk2AYBijpzzBMQ1KOcREyo9G6QOpvdctynGOAPkL3cwqeTzkFhWgGj633pu_MdLjlectEBMGyVQIv6pL8OBMCHMQzTUTpHWJ_NoUkLpRLKGqZFFcXW8q7v4KeCbf8xHUa9OCH5VF2JxYOnFWDVgucSqao06r0Jaq64LDwKIhLw77ujheKpcBjRrf1kqoIpqk2qhb8CzxM36g_DawMadzKmX49dT-k7auNnI2xUtu5CZdXZ3lSmLeicXfGjc66rrH_acqUqipZRKeeQ5F3Ma467jPQaTeOKiCMHwS2_yp-sXNU2GzxOA
```
- 请求业务 API：
```
curl http://service-cmrrdq86-1251890925.gz.apigw.tencentcs.com:80/work -H'Authorization:Bearer id_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIyNzk3MTAsImZvbyI6ImJhciIsImlhdCI6MTU5MjI3OTQxMCwianRpIjoiZlBGYlFZRkR4REx3d0lXTFl0aHBBQSIsIm5iZiI6MTU5MjI3OTQxMCwid3VwIjo5MH0.0JQquNRVCQ8n9hPV-mJi6Mku_7G3T1jFp68Sk2AYBijpzzBMQ1KOcREyo9G6QOpvdctynGOAPkL3cwqeTzkFhWgGj633pu_MdLjlectEBMGyVQIv6pL8OBMCHMQzTUTpHWJ_NoUkLpRLKGqZFFcXW8q7v4KeCbf8xHUa9OCH5VF2JxYOnFWDVgucSqao06r0Jaq64LDwKIhLw77ujheKpcBjRrf1kqoIpqk2qhb8CzxM36g_DawMadzKmX49dT-k7auNnI2xUtu5CZdXZ3lSmLeicXfGjc66rrH_acqUqipZRKeeQ5F3Ma467jPQaTeOKiCMHwS2_yp-sXNU2GzxOA"'
```
返回结果：
```
hello world
```

### 使用授权码的方式获取 token
以上示例中可以看到，获取 token 时并没有使用授权码进行获取，为了确保指定的用户才能获取到 token，根据授权流程，需要有一个步骤需去资源拥有者那里获取授权码，从 server.py 文件中可以看到，可以第一步请求 code 路径获取授权码，而同时获取 token 的时候，需要对发放的 code 进行登记，判断是否合法。
