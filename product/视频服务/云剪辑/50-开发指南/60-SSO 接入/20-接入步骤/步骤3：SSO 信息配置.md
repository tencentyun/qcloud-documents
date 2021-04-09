## 配置 SSO 信息到制作云
将认证服务（Authorization Server）的相关信息配置到制作云，当用户发起 SSO 登录时，制作云将使用该配置信息到认证服务进行授权认证。
### 配置信息
<table>
<tr>
  <th style = "width:20%">字段名	</th>
  <th>类型</th>
  <th>必填</th>
  <th>描述</th>
</tr>
<tr>
  <td>ClientId</td>
  <td>string</td>
  <td>是</td>
  <td>应用唯一标识，认证服务颁发给制作云的唯一标识。</td>
</tr>
<tr>
  <td>ClientSecret</td>
  <td>string</td>
  <td>是</td>
  <td>应用 Secret，认证服务颁发给制作云的 Secret。</td>
</tr>
<tr>
  <td>AuthorizationEndpoint</td>
  <td>string</td>
  <td>是</td>
  <td>认证服务的授权认证地址，在访问制作云平台且未登录时将会通过该地址发起授权登录。</td>
</tr>
<tr>
  <td>TokenEndpoint</td>
  <td>string</td>
  <td>是</td>
  <td>到认证服务获取 AccessToken 等信息的访问地址，制作云拿到授权 Code 后将通过该地址获取 AccessToken 信息。</td>
</tr>
<tr>
  <td>UserInfoEndpoint</td>
  <td>string</td>
  <td>是</td>
  <td>到认证服务获取用户信息的访问地址，制作云将通过该地址获取用户唯一标识等信息。</td>
</tr>
<tr>
  <td>Scope</td>
  <td>string</td>
  <td>是</td>
  <td>认证服务许可的应用授权作用域。</td>
</tr>
</table>

## 配置制作云的回调地址到开发者认证服务
制作云回调地址为：
```
https://api.vs.tencent.com/Oauth/Login/Callback
```

## 验证登录
至此，所有配置全部完成。可以通过访问创建制作云平台时获得的平台地址进行登录。
