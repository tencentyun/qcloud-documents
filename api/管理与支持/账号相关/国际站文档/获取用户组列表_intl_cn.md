## 1. 接口描述
域名:account.api.qcloud.com
接口名:DescribeUserGroup

获取用户组列表

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| groupIds.n  | 否 | String |用户组Id |


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 描述（待补充） |
|groupId | Int | 用户组ID| 
| groupName | String | 用户组名称| 
|channel | Int |消息接收渠道 0:无 1: 短信 2：邮件 3：短信+邮件| 
| remark | String  |备注| 
| createTime | String | 创建时间| 


## 4. 示例
输入
<pre>
https://account.api.qcloud.com/v2/index.php?Action=DescribeUserGroup
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
		  "totalCount": 2,
        "groupSet":[
            {
                "groupId":1155,
                "groupName":"监控接收组",
                "channel":3,
                "remark":"test",
                "createTime":"2015-07-09 10:26:20"
            }
        ]
    }
}
```

