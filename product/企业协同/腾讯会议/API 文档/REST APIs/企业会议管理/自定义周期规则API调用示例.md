>?
>- recurring_type：0至4为常规周期性会议，5为自定义周期性会议。recurring_type 为5时，customized_recurring_type、customized_recurring_step、customized_recurring_days 才会生效，否则会被忽略。
- 修改会议与预定会议的 API 传参类似，需注意修改会议时 recurring_rule 中若填写了 sub_meeting_id，则表示修改该子会议时间，不可与周期性会议规则同时修改。如不填写，默认修改整个周期性会议时间。
- customized_recurring_days 指定哪些天重复，使用二进制表示，多选是二进制相加后的值。且需要包括预定会议日期（即第一个会议的日期），否则会返回如下报错信息：
```
{
  "error_info": {
    "error_code": 190004,
    "new_error_code": 1000190004,
    "message": "recurring_days no include firstStartTime"
  }
}
```
- customized_recurring_type 与 customized_recurring_days 可选值的对应关系：（注意：customized_recurring_type 为2时，customized_recurring_days 的值需选定周几+第几周。）
<table>
   <tr>
      <th width="0%" >customized_recurring_type 类型</td>
      <th width="0%" colspan="12" >customized_recurring_days 取值范围（多选即为对应值的加和）</td>
   </tr>
   <tr>
      <td>3（按月，以日期为粒度重复）</td>
      <td>1（1号）</td>
      <td>2（2号）</td>
      <td>4（3号）</td>
      <td>8（4号）</td>
	    <td>16（5号）</td>
	    <td>32（6号）</td>
	    <td>64（7号）</td>
	    <td>128（8号）</td>
	    <td>256（9号）</td>
	    <td>...</td>
	    <td>...</td>
	    <td>2^30次方（31号）</td>
</tr>
   <tr>
      <td>2（按月，以周为粒度重复）</td>
      <td>1（周日）</td>
      <td>2（周一）</td>
      <td>4（周二）</td>
      <td>8（周三）</td>
	    <td>16（周四）</td>
	    <td>32（周五）</td>
	    <td>64（周六）</td>
	    <td>128（第一周）</td>
	    <td>256（第二周）</td>
	    <td>...</td>
	    <td>2^11（第五周），没有第五周的月份跳过</td>
	    <td>-</td>
</tr>
   <tr>
      <td>1（按周）</td>
      <td>1（周日）</td>
      <td>2（周一）</td>
      <td>4（周二）</td>
      <td>8（周三）</td>
	    <td>16（周四）</td>
	    <td>32（周五）</td>
	    <td>64（周六）</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
</tr>
   <tr>
      <td>0（按天）</td>
      <td colspan="11" >忽略</td>
      <td>-</td>
</tr>
</table>
									
自定义周期规则传参的具体示例如下：
## 按天重复
### 每三天重复一次，共重复七次
>!按天重复时，customized_recurring_type = 0，使用 customized_recurring_step 指定每 [n] 天重复。customized_recurring_days 字段将被忽略。
#### 输入示例
```plaintext
{
	"userid": "tester",
	"instanceid": "1",
	"subject": "每三天重复一次，共重复七次",
	"type": "0",
	"start_time": "1664162868",
	"end_time": "1664163868",
	"meeting_type":1,
	"recurring_rule": {
		"recurring_type": "5",//自定义周期性会议
		"until_type": "1",//按次数结束重复
		"until_count": "7",//重复7次
		"customized_recurring_type":0,//按天重复
		"customized_recurring_step":3//每三天重复
	}
}
```
#### 输出示例
```plaintext
{
  "meeting_number": 1,
  "meeting_info_list": [
    {
      "subject": "每三天重复一次，共重复七次",
      "meeting_id": "10418246224797450687",
      "meeting_code": "78482137648",
      "type": 0,
      "join_url": "https://meeting.tencent.com/dm/uaa3D5n4vtjY",
      "hosts": [{"userid": "tester"}],
      "start_time": "1664185488",
      "end_time": "1664186488",
      "settings": {
        "mute_enable_join": true,
        "allow_unmute_self": true,
        "mute_all": true,
        "mute_enable_type_join": 1
      },
      "meeting_type": 1,
      "enable_live": false,
      "location": ""
    }
  ]
}
```
#### 客户端表现
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/478034ce4e5f9fecbb21f56b69deacbd.png" />

## 按周重复
### 每三周的周一、周二，默认结束重复
>!当不传入 until_type 和 until_date 时，默认按日期结束重复，结束日期默认为默认为当前日期往后推7天。
#### 输入示例
```plaintext
{
	"userid": "tester",
	"instanceid": "1",
	"subject": "每三周的周一、周二，默认结束重复",
	"type": "0",
	"start_time": "1664183361",
	"end_time": "1664184361",
	"meeting_type":1,
	"recurring_rule": {
		"recurring_type": "5",//自定义周期性会议
		"customized_recurring_type":1,//按周重复
		"customized_recurring_step":3,//每三周重复
		"customized_recurring_days":6 //2^1（周一）+2^2（周二）
	}
}
```
#### 客户端表现
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c84f06a4a1541f82dddc2a3eafab038a.png" />

## 按月，以周为粒度重复
>!此种重复类型下，周几暂不支持多选，仅支持预定会议的日期对应的星期，对应客户端上预定会议表现示例：

### 每三个月的第四周的周一，指定日期结束重复
#### 输入示例
```plaintext
{
	"userid": "tester",
	"instanceid": "1",
	"subject": "每三个月的第四周的周一，指定日期结束重复",
	"type": "0",
	"start_time": "1664204280",
	"end_time": "1664205280",
	"meeting_type":1,
	"recurring_rule": {
		"recurring_type": 5,//自定义周期性会议
		"until_type": 0,//按日期结束重复
		"until_date": 1695732877,//指定结束日期
		"customized_recurring_type":2,//按月，以周为粒度重复
		"customized_recurring_step":3,//每三个月重复
		"customized_recurring_days":1026 //2^1（周一）+2^10（第四周）
	}
}
```
#### 客户端表现
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4101905ecf4ceb627aab8d05d56e1576.png" />

## 按月，以日为粒度重复
>!此种重复类型下，日期支持多选，且必须包含预定会议对应的日期（即第一个会议的日期）。

### 每三个月的1日、26日，指定日期结束重复
#### 输入示例
```plaintext
{
	"userid": "tester",
	"instanceid": "1",
	"subject": "每三个月的1日、26日",
	"type": "0",
	"start_time": "1664199400",
	"end_time": "1664200400",
	"meeting_type":1,
	"recurring_rule": {
		"recurring_type": 5,//自定义周期性会议
		"until_type": 0,//按日期结束重复
		"until_date": 1695732877,//指定结束日期
		"customized_recurring_type":3,//按月，以日期为粒度重复。
		"customized_recurring_step":3,//每3个月重复
		"customized_recurring_days":33554433 //2^0（1日）+2^25（26日）
	}
}
```
#### 客户端表现
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4483aebe2093f4aa0b02e7442bd9e281.png" />
