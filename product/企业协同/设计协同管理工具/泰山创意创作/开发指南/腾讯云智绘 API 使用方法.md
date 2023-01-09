在使用所有的腾讯云智绘 API，都需要通过鉴权，从而获取 access_token，最后再通过 access_token 来调用 腾讯云智绘 API。鉴权流程接入如下：
### 步骤1：注册获取智绘泰山的用户信息
通过 [腾讯云控制台](https://console.cloud.tencent.com/taidc/api ) 获取以下信息：Uin、userId、secretId、secretKey。
### 步骤2：通过 secretId 和 secreKey 获取 access_token
 - 调用地址：
 ```plaintext
 https://zhihui.qq.com/account/api/auth/secret
 ```
 - 请求方式：POST
 - 返回类型：JSON
 - 请求参数：
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>id</td>
      <td>string</td>
      <td>是</td>
      <td>用户 userId。</td>
   </tr>
   <tr>
      <td>secretId</td>
      <td>string</td>
      <td>	是</td>
      <td>分配的密钥 ID（secretId）。</td>
   </tr>
   <tr>
      <td>sig</td>
      <td>string</td>
      <td>是</td>
      <td>签名，计算方法请参见 <a href="https://cloud.tencent.com/document/product/1351/77421">腾讯云智绘签名 Sig 加密计算方法</a>。<b>注意：</b>加密密钥使用 secretKey。</td>
   </tr>
</table>	
 - 请求示例：
```plaintext
// 请求参数
let param = {
  id: 'xxxxxxx',
  secretId: 'xxxxxxx',
  sig: 'xxxxxx'
}
 
// 获取 access_token 以及用户信息
const userData = await request('/api/auth/secret', {
  method: 'post',
  data: param,
})
```
 - 返回示例：
 ```plaintext
{
  "statusCode":200,
  "data": {
    "access_token": "iIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTE0NjU1MzRjZjE5ZjJmZmQ2NzlmNxxxxxxxxxxxxxxx"
    "name": "taidc",
    "avatar": "",
    "email": "taidc@tencent.com",
     ......
  }
}
```

