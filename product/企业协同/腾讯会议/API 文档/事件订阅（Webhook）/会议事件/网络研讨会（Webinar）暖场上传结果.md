## 事件描述
**事件名：**webinar.warm-up-uploaded
**事件说明：**通过 API 进行暖场配置上传暖场图片或视频时触发该事件。配置请参见 [设置网络研讨会（Webinar）暖场配置](https://cloud.tencent.com/document/product/1095/79824)。

## 示例
```plaintext
{
    "event":"webinar.warm-up-uploaded", //事件名
    "trace_id":"e7aa65dd-f7e6-4b62-912c-2035173b34a9",//事件的唯一序列值
    "payload":[
        {
            "operate_time":1609313201465,//毫秒级别事件操作时间戳，成功/失败时间点
			"warm_up_info":
			{
				"upload_status":true, //true：上传成功；false：上传失败
				"error_msg":"",//如果上传失败，则该字段返回失败原因
				"warm_up_picture":"",//url
				"warm_up_video":"",//url
			},
            "meeting_info":{//会议信息
                "meeting_id":"13339451618278424869",// 会议id
                "meeting_code":"445999969", // 会议code
                "subject":"tester的快速会议", // 会议主题
                "meeting_type":0,// 会议类型(0-一次性会议，1-周期性会议，2-微信专属会议，3-rooms投屏会议，5-个人会议号会议，6-网络研讨会)
                "start_time":1608522626,// 秒级别的会议开始时间戳
                "end_time":1609415039// 秒级别的会议结束时间戳
            }
        }
    ]
```
