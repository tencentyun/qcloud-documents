## 接口描述
**描述**：查询指定会议室（Rooms）下的会议列表，目前暂不支持 OAuth2.0 鉴权访问。
**调用方式**：GET
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/meeting-rooms/{operator_id}/meetings
```



## 输入参数
HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

<table>
   <tr>
      <th width="0px" style="text-align:center">参数名称</td>
      <th width="0px" style="text-align:center">是否必须</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td>operator_id</td>
      <td>是</td>
      <td>操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。</td>
   </tr>
   <tr>
      <td>operator_id_type</td>
      <td>是</td>
      <td>操作者 ID 的类型： <br>
			3：rooms 设备 rooms_id。<br>
			5：会议室ID meeting_room_id。</td>
   </tr>
   <tr>
      <td>instanceid</td>
      <td>是</td>
      <td>用户的终端设备类型： <br>
			1：PC。 <br>
			2：Mac。 <br>
			3：Android。<br>
			4：iOS。 <br>
			5：Web。 <br>
			6：iPad。 <br>
			7：Android Pad。 <br>
			8：小程序。 <br>
			9：voip、sip 设备。 <br>
			10：Linux。 <br>
			20：Rooms for Touch Windows。 <br>
			21：Rooms for Touch Mac。 <br>
			22：Rooms for Touch Android。 <br>
			30：Controller for Touch Windows。 <br>
			32：Controller for Touch Android。 <br>
			33：Controller for Touch iPhone。<br>
			</td>
   </tr>
   <tr>
      <td>start_time</td>
      <td>否</td>
      <td>Unix 时间戳。查询起始时间，时间区间不超过90天。</td>
   </tr>
   <tr>
      <td>end_time</td>
      <td>否</td>
      <td>Unix 时间戳。查询结束时间，时间区间不超过90天。</td>
   </tr>
   <tr>
      <td>page</td>
      <td>否</td>
      <td>当前页，页码起始值为1，默认为1。</td>
   </tr>
   <tr>
      <td>page_size</td>
      <td>否</td>
      <td>分页大小，默认20条，最大20条。</td>
   </tr>
</table>



## 输出参数

| 名称              | 类型         | 备注             |
| :---------------- | :----------- | :--------------- |
| current_page      | Integer      | 当前页。         |
| current_size      | Integer      | 当前实际页大小。 |
| total_count       | Integer      | 数据总条数。     |
| total_page        | Integer      | 数据总页数。     |
| meeting_info_list | 会议对象列表 | 会议对象列表。   |

**会议对象**

| 名称         | 类型    | 备注                                                         |
| ------------ | ------- | ------------------------------------------------------------ |
| meeting_id   | String  | 会议 ID。                                                    |
| meeting_code | String  | 有效会议 Code。                                              |
| subject      | String  | 会议主题。                                                   |
| status       | String  | 会议状态。                                                   |
| meeting_type | Integer | 会议类型：<br>0：一次性会议。<br>1：周期性会议。<br>2：微信专属会议。<br>4：rooms 投屏会议。<br>5：个人会议号会议。<br>6：络研讨会（Webinar）。|
| start_time   | Integer | 会议预订开始时间（Unix 秒）。                                |
| end_time     | Integer | 会议预订结束时间（Unix 秒）。                                |

