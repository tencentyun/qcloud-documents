## 接口描述
- **描述**：
 - 会议创建者、主持人、联席主持人可以查询 PSTN 的 ms_open_id。
 - ms_open_id 是 PSTN 的识别标识，用户拨号进入后，在实时参会列表等 API 及 Webhook 中可以获取。
 - 由于可能出现一个座机号同时拨入的情况，所以同一个座机号可能对应多个 ms_open_id。
 - 仅当 PSTN 接通后，该接口会返回对应的 ms_open_id。
 - 支持查询会议下 PSTN 的历史 ms_open_id 列表。
- **调用方式**：POST
- **鉴权方式：**JWT 鉴权
- **接口请求域名**：
```plaintext
https://api.meeting.qq.com/v1/meetings/{meetingId}/phone/ms-open-id
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
      <td>operator_id</td>
      <td>String</td>
      <td>必须</td>
      <td>操作者 ID。会议创建者、主持人、联席主持人可以调用该接口。<br>operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。</td>
   </tr>
   <tr>
      <td>operator_id_type</td>
      <td>Number</td>
      <td>必须</td>
      <td>操作者 ID 的类型：<br>1：企业内用户 userid</td>
   </tr>
   <tr>
      <td>phone_numbers</td>
      <td>	Object []</td>
      <td>必须</td>
      <td>外呼的电话号码对象数组。</td>
   </tr>
</table>

**外呼的电话号码对象**
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>area</td>
      <td>Number</td>
      <td>必须</td>
      <td>国家/地区代码。（例如：中国是86）。</td>
   </tr>
   <tr>
      <td>phone</td>
      <td>String</td>
      <td>必须</td>
      <td>电话号码或固定电话总机号。</td>
   </tr>
   <tr>
      <td>extension_number</td>
      <td>String</td>
      <td>非必须</td>
      <td>固定电话分机号。</td>
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
      <td>meeting_id</td>
      <td>String</td>
      <td>必须</td>
      <td>会议的唯一 ID。 </td>
   </tr>
   <tr>
      <td>ms_open_id_list</td>
      <td>Array []</td>
      <td>必须</td>
      <td>	返回的 ms_open_id 对象数组。</td>
   </tr>
</table>


**返回的 ms_open_id 对象**
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >参数类型</td>
      <th width="20%" >是否必须</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>area</td>
      <td>Number</td>
      <td>必须</td>
      <td>国家/地区代码。（例如：中国是86）。 </td>
   </tr>
   <tr>
      <td>phone</td>
      <td>String </td>
      <td>必须</td>
      <td>	电话号码或固定电话总机号。</td>
   </tr>
   <tr>
      <td>extension_number</td>
      <td>String </td>
      <td>非必须</td>
      <td>	固定电话分机号。</td>
   </tr>
<tr>
      <td>ms_open_id</td>
      <td>String</td>
      <td>必须</td>
      <td>当场会议的用户临时 ID，可用于会控操作，适用于所有用户。</td>
   </tr>
</table>


## 示例
#### 输入示例
```plaintext
{
  "operator_id":"songe",
  "operator_id_type":2,
  "phone_numbers":[
    {
      "area":86,
      "phone":"13888888888",
    }
  ]
}
```

#### 输出示例
```plaintext
{
    "meeting_id":"1111111111111",
  "ms_open_id_list":[
    {
      "area":86,
      "phone":"13888888888",
      "ms_open_id":"xxxx"
    }
  ]
}
```
