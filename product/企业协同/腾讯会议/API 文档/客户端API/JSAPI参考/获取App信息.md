## 接口描述
- 描述：调用 app.getAppInfo，获取当前客户端信息。
- 支持的版本：2.17.0
- 是否需要鉴权：否

## 参数说明
获取 App 版本信息，返回 promise ClientInfo。
<table>
   <tr>
      <th width="30%" >参数名称</td>
      <th width="30%" >参数类型</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>appVersion</td>
      <td>String</td>
      <td>App 版本</td>
   </tr>
   <tr>
      <td>clientLanguage</td>
      <td>String</td>
      <td>客户端当前语言</td>
   </tr>
   <tr>
      <td>instanceId</td>
      <td>Number</td>
      <td>App 对应的 instance id</td>
   </tr>
</table>
  
  
 
## 代码示例
```plaintext
const version = await app.getAppInfo()
```
