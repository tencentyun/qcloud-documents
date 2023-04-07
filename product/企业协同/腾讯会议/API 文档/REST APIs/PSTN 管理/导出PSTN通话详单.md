## 接口描述
- 描述：超管，企业管理员，拥有结算信息查看或编辑权限点的企业成员可以查询企业的通话详单信息，异步获取详单信息，可以订阅 [异步任务结果事件](https://cloud.tencent.com/document/product/1095/86417) 获得导出结果，也可以通过 [获取导出结果接口](https://cloud.tencent.com/document/product/1095/86453) 查询具体信息。
- 鉴权方式：JWT 鉴权
- 调用方法：GET
- 接口请求域名：
```html
https://api.meeting.qq.com/v1/meeting/phone/call_detail
```

## 输入参数
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="20%" >必选</td>
      <th width="20%" >参数类型</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>operator_id_type</td>
      <td>是</td>
      <td>Integer</td>
      <td>操作者 ID 的类型：<br>1：userid</td>
   </tr>
   <tr>
      <td>operator_id</td>
      <td>是</td>
      <td>String</td>
      <td>操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。</td>
   </tr>
   <tr>
      <td>meeting_id</td>
      <td>否</td>
      <td>String</td>
      <td>可以查询某次会议的数据，不传入则查询企业下全部会议的。</td>
   </tr>
   <tr>
      <td>start_date</td>
      <td>否</td>
      <td>String</td>
      <td>开始时间和结束时间需要同时传入，若开始与结束时间不传，则查询近一年的数据。<br>开始时间支持 yyyy-MM-dd 格式。</td>
   </tr>
   <tr>
      <td>end_date</td>
      <td>否</td>
      <td>String</td>
      <td>统计结束时间支持 yyyy-MM-dd 格式。<br>最多能查询到昨天的数据。</td>
   </tr>
</table>


## 输出参数
返回错误展示错误信息。
<table>
   <tr>
      <th width="0%" >参数名称</td>
      <th width="0%" >参数类型</td>
      <th width="0%" >参数描述</td>
   </tr>
   <tr>
      <td>job_id</td>
      <td>String</td>
      <td>任务 ID，可通过获取导出结果接口查询。</td>
   </tr>
</table>
	

## 示例
#### 输入示例
```plaintext
GET 
https://api.meeting.qq.com/v1/meeting/phone/call-detail?operator_id=user123&operator_id_type=1&meeting_id=12345678910&start_date=2023-01-16&end_date=2023-01-16
```
#### 输出示例
```plaintext
{
   "job_id":"e1234567-f123-4d12-123a-12346192e332"
}
```
