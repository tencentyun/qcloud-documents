## 接口描述
- **描述：**调用 permission.config，实现企业自建应用 JSAPI 鉴权配置。
- **支持的版本：**2.17.0
- **是否需要鉴权：**否


## 参数说明
授权请求入参（param：AuthConfigParam）：
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>corpId</td>
      <td>String</td>
      <td>应用的企业 ID</td>
   </tr>
   <tr>
      <td>nonceStr</td>
      <td>String</td>
      <td>生成签名的随机串</td>
   </tr>
   <tr>
      <td>sdkId</td>
      <td>String</td>
      <td>应用 ID</td>
   </tr>
   <tr>
      <td>signature</td>
      <td>String</td>
      <td>签名</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>Undefined、Number</td>
      <td>超时时间</td>
   </tr>
   <tr>
      <td>timestamp</td>
      <td>String</td>
      <td>生成签名的时间戳</td>
   </tr>
</table>

返回 Promise void。

## 代码示例
```plaintext
wemeet.permission.config()
```
