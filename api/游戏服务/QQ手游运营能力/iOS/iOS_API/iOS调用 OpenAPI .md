
## 功能描述
iOS SDK 中具体支持的 API 种类和每条 API 的参数说明，请参照[ API 列表](http://wiki.connect.qq.com/api%E5%88%97%E8%A1%A8)。这里用设置用户头像举例说明。

### OpenAPI参数字典封装

在封装各接口的参数字典时，推荐使用为每个接口新增的参数封装辅助类，如：接口 (BOOL)addShareWithParams:(NSMutableDictionary *)params 对应辅助类 TCAddShareDic。

TCAddShareDic 辅助类中属性 @property (nonatomic, retain) TCRequiredStr paramTitle 对应于 CGI 请求中参数 title。

| 参数名 |  类型 |
|---------|---------|
| TCRequiredStr（必选） | String |
| TCOptionalStr（可选） | String |

### 使用增量授权

当第三方应用调用某个 API 接口时，如果服务器返回操作未被授权，则会触发增量授权逻辑。第三方应用需自行实现 tencentNeedPerformIncrAuth:withPermissions 协议接口才能够进入增量授权逻辑，否则默认第三方应用放弃增量授权。示例如下：

```
- (BOOL)tencentNeedPerformIncrAuth:(TencentOAuth *)tencentOAuth withPermissions: (NSArray *) permissions {
// incrAuthWithPermissions是增量授权时需要调用的登录接口
// permissions是需要增量授权的权限列表
[tencentOAuth incrAuthWithPermissions:permissions];
// 返回NO表明不需要再回传未授权API接口的原始请求结果，否则返回YES
return NO; 
}
```

>**注意：**
>在用户通过增量授权页重新授权登录后，第三方应用需更新自己维护的 token 及有效期限等信息。

用户在增量授权时是可以更换帐号进行登录的，强烈要求第三方应用核对增量授权后的用户 openid 是否一致，以添加必要的处理逻辑（用户帐号变更需重新拉取用户的资料等信息）。
- 增量授权成功时，会通过 tencentDidUpdate 协议接口通知第三方应用：

```
- (void)tencentDidUpdate:(TencentOAuth *)tencentOAuth {
_labelTitle.text = @"增量授权完成";
if (tencentOAuth.accessToken
            && 0 != [tencentOAuth.accessToken length]) {
// 在这里第三方应用需要更新自己维护的token及有效期限等信息
// **务必在这里检查用户的openid是否有变更，变更需重新拉取用户的资料等信息**
_labelAccessToken.text = tencentOAuth.accessToken;
    } else {
        _labelAccessToken.text = @"增量授权不成功，没有获取accesstoken";
}
}
```
- 增量授权失败时，会通过 tencentFailedUpdate 协议接口通知第三方应用：

```
- (void)tencentFailedUpdate:(UpdateFailType)reason {
    switch (reason) {
        case kUpdateFailNetwork:
            _labelTitle.text=@"增量授权失败，无网络连接，请设置网络";
            break;
        case kUpdateFailUserCancel:
            _labelTitle.text=@"增量授权失败，用户取消授权";
            break;
        case kUpdateFailUnknown:
        default:
            _labelTitle.text=@"增量授权失败，未知错误";
            break;
    }
}
```

## 返回数据说明

**APIResponse属性：**

|参数名 | 参数说明 | 
|---------|---------|
| retCode | 网络请求返回码，主要表示服务器是否成功返回数据。 | 
| seq | 请求的序列号，依次递增，方便内部管理。 | 
| errorMsg | 错误消息。 | 
| jsonResponse | 由服务器返回的 json 格式字符串转换而来的 json 字典数据（具体参数字段请参见对应 API 说明文档）。 | 
| message | 服务器返回的原始字符串数据。 | 
| detailRetCode |新增的详细错误码，以区分不同的错误原因（v1.2 以及之前的 SDK 接口无此参数）。 | 

## 返回码

retCode 网络请求返回码说明：

| 返回码 | 含义 | 
|---------|---------|
| 0 | 表示成功，请求成功发送到服务器，并且服务器返回的数据格式正确。 |
| 1 | 表示失败，可能原因有网络异常，或服务器返回的数据格式错误，无法解析。 |

detailRetCode 详细错误码说明：

| 错误码类别 | 返回码 | 含义 | 
|---------|---------|---------|
|**公共错误码：**| kOpenSDKInvalid | 无效的错误码 | 
|| kOpenSDKErrorSuccess| 成功 | 
||kOpenSDKErrorUnknown | 未知错误 | 
|| kOpenSDKErrorUserCancel | 用户取消 | 
||kOpenSDKErrorReLogin | token 无效或用户未授权相应权限需要重新登录 | 
|| kOpenSDKErrorOperationDeny | 第三方应用没有该 API 操作的权限 |
|**网络相关错误码：**| kOpenSDKErrorNetwork | 网络错误，网络不通或连接不到服务器 |
|| kOpenSDKErrorURL | URL 格式或协议错误 |
|| kOpenSDKErrorDataParse | 数据解析错误，服务器返回的数据解析出错 |
|| kOpenSDKErrorParam | 传入参数错误 |
|| kOpenSDKErrorConnTimeout | http 连接超时 |
|| kOpenSDKErrorSecurity | 安全问题 |
|| kOpenSDKErrorIO | 下载和文件 IO 错误 |
||kOpenSDKErrorServer | 服务器端错误 |
|**webview中特有错误：**|kOpenSDKErrorWebPage | 页面错误 |
|**设置头像自定义错误码段：**|kOpenSDKErrorUserHeadPicLarge | 图片过大 设置头像自定义错误码 |
