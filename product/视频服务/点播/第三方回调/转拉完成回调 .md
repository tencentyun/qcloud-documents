## 功能名称
转拉完成回调

## 功能说明
1. 转拉任务完成后，通知用户。

## 注意事项
1. 要启用回调，必须配置回调URL，并打开本条回调协议对应的开关；
2. 回调的方向是：腾讯云后台向APP后台发起HTTP POST请求。

## 可能触发该回调的场景
1. 转拉任务完成后。

## 回调发生时机
1. 转拉任务完成后。

## 接口说明

### 请求参数
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| status | String | 错误码, 0: 成功, 其他值: 失败 |
| message | Int | 错误信息  |
| file_id | String | 转拉生成的文件的id |
| file_url | String | 转拉生成的文件的url  |
| file_type | String | 转拉生成的文件的类型 |
| vodtask_id | String | 发起转拉请求后获取到的唯一id |
| imgUrl | Struct | 图片信息  |
| videoUrls | Struct | 视频信息 |
| player_code | Struct | 播放器代码 |

### HTTP请求方式
POST
### HTTP请求包体格式
JSON
### 回调请求包示例
```
{
    "image_video": {
        "code": 0,
        "duration": 10,
        "vid": "231414",
        "message": "success",
        "imgUrl": {
            "id": 3213,
            "url": "www.qcloud.com/templurl.png",
            "vheight": 21,
            "width": 32
        },
        "videoUrls": [
            {
                "url": "www.qcloucd.com/temp_video.mp4",
                "md5": "fdasfdsafsadf",
                "sha": "dasfdsfas",
                "size": 123,
                "update_time": "2015084912: 0: 0",
                "vbirate": 231,
                "vheight": 480,
                "vwidth": 800
            }
        ],
        "file_id": "12312314124",
        "ret": 0,
        "player_code": {
            "h5": "",
            "flash": "",
            "iframe": ""
        }
    }
}
```
### 回调请求包字段说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| status | Int | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息  |
### 回调应答包示例
```
{
    "code": 0,
	"message": "success"
}
```



