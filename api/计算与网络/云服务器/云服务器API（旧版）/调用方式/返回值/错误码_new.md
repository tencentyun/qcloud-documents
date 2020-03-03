>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1、公共错误码

注：本页展示的是改版后接口的错误码。如需查看旧接口对应的错误码，请参考 [公共错误码](https://cloud.tencent.com/document/api/213/6982) 信息。

返回结果中如果存在 Error 这个 key，则表示调用 API 接口失败。Error 底下的 Code 字段表示错误码，当调用失败后，用户可以根据下表确定公共错误原因并采取相应措施。

<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>错误类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> InvalidParameter
</td><td> 请求参数非法
</td><td> 缺少必要参数，或者参数值格式不正确，具体错误信息请查看错误描述 message 字段。
</td></tr>
<tr>
<td> InvalidParameter.SignatureFailure
</td><td> 身份认证失败
</td><td> 身份认证失败，一般是由于签名计算错误导致的。
</td></tr>
<tr>
<td> AuthFailure
</td><td> 未授权访问接口
</td><td> 子账号未被主账号授权访问该接口，请联系主账号管理员开通接口权限。
</td></tr>
<tr>
<td> AuthFailure
</td><td> 未授权访问资源
</td><td> 子账号未被主账号授权访问特定资源，请联系主账号管理员开通资源权限。
</td></tr>
<tr>
<td> AuthFailure
</td><td> 未授权访问当前接口所操作的资源
</td><td> 子账号没有被主账户授权访问该接口中所操作的特定资源，请联系主账号管理员开通资源权限。
</td></tr>
<tr>
<td> InvalidParameter.SecretIdNotFound
</td><td> 密钥不存在
</td><td> 用于请求的密钥不存在，请确认后重试。
</td></tr>
<tr>
<td> InvalidRequest.TokenCheckFailed
</td><td> token 错误
</td><td> token 错误。
</td></tr>
<tr>
<td> InvalidRequest.MFACheckFailed
</td><td> MFA 校验失败
</td><td> MFA 校验失败。
</td></tr>
<tr>
<td> InternalError.CAMInnerError
</td><td> 其他 CAM 鉴权失败
</td><td> 其他 CAM 鉴权失败。
</td></tr>
<tr>
<td> InvalidRequest.Forbidden
</td><td> 拒绝访问
</td><td> 账号被封禁，或者不在接口针对的用户范围内等。
</td></tr>
<tr>
<td> InvalidRequest.LimitExceeded
</td><td> 超过配额
</td><td> 请求的次数超过了配额限制。
</td></tr>
<tr>
<td> InvalidRequest.ReplayAttack
</td><td> 重放攻击
</td><td> 请求的 Nonce 和 Timestamp 参数用于确保每次请求只会在服务器端被执行一次，所以本次的 Nonce 和上次的不能重复，Timestamp 与腾讯服务器相差不能超过5分钟。
</td></tr>
<tr>
<td> InvalidRequest.UnsupportedProtocol
</td><td> 协议不支持
</td><td> 协议不支持，当前 API 仅支持 HTTPS 协议，不支持 HTTP 协议。
</td></tr>
<tr>
<td> InternalError.ResourceOpFailed
</td><td> 资源操作失败
</td><td> 对资源的操作失败，具体错误信息请查看错误描述 message 字段，稍后重试或者联系客服人员帮忙解决。
</td></tr>
<tr>
<td> InternalError
</td><td> 服务器内部错误
</td><td> 服务器内部出现错误，请稍后重试或者联系客服人员帮忙解决。
</td></tr>
<tr>
<td> InvalidAction.NotFound
</td><td> 版本暂不支持
</td><td> 本版本内不支持此接口或该接口处于维护状态等。注意：出现这个错误时, 请先确定接口的域名是否正确, 不同的模块，域名可能不一样。
</td></tr>
<tr>
<td> InvalidAction.ActionUnavailable
</td><td> 接口暂时无法访问
</td><td> 当前接口处于停服维护状态，请稍后重试。
</td></tr>
<tr>
<td> InvalidRequest.RequestConcurrencyExceeded
</td><td> 接口请求超过并发限制
</td><td> 当前接口请求量超过 qps 限制，请稍后重试。
</td></tr>
</tbody></table>
