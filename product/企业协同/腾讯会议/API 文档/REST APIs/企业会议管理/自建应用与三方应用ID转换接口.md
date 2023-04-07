## 接口描述
- **描述：**将三方应用获取到 open_id 转换为本企业用户的 userid。
- 鉴权方式：JWT 鉴权。
- **接口请求方法：** POST
- **接口请求域名：** 
```html
https://api.meeting.qq.com/v1/users/open-id-to-userid
```

## 输入参数
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>open_id_list</td>
      <td>String []	</td>
      <td>必须</td>
      <td>需要转换的 open_id 列表 。一次最多1000个。</td>
   </tr>
   <tr>
      <td>sdkid</td>
      <td>String</td>
      <td>必须</td>
      <td>第三方应用的 sdkid。需要转换的 open_id 应为腾讯会议为该三方应用提供的 open_id。</td>
   </tr>
</table>


## 输出参数
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>userid_list</td>
      <td>Object []</td>
      <td>必须</td>
      <td>转换成功的该自建应用所在企业下的 userid、open_id 对应关系列表。</td>
   </tr>
   <tr>
      <td>invalid_open_id_list</td>
      <td>String</td>
      <td>必须</td>
      <td>所有没有转换成功的 open_id 列表。 例如：open_id 和 sdkid 不一致、open_id 和自建应用不是同企业、open_id 非法等情况。</td>
   </tr>
</table>

**对应关系列表**
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>open_id</td>
      <td>String</td>
      <td>必须</td>
      <td>需要转换的 open_id。</td>
   </tr>
   <tr>
      <td>userid</td>
      <td>String</td>
      <td>必须</td>
      <td>转换成功后，该 open_id 所对应的本企业下用户的 userid。</td>
   </tr>
</table>

## 示例
### 输入示例

```plaintext
POST  https://api.meeting.qq.com/v1/users/open-id-to-userid
{
   "open_id_list":["123456"],
   "sdkid":"120001"
}
```


### 输出示例

```plaintext
{
   "userid_list":[
                          {
                               "open_id":"123456",
                               "userid":"user1"
                          }
                          ]
   "invalid_open_id_list":[]
}
```

