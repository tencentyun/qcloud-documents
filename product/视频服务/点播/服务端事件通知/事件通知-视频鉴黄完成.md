## 事件名称
PorncheckComplete

## 事件说明
如果APP配置了事件通知，则在视频鉴黄任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 回调版本号，固定为4.0 |
| eventType | String | 回调类型，固定为PorncheckComplete |
| data | Object | 具体回调数据 |
| data.status | Integer | 错误码, 0: 成功, 其他值: 失败 |
| data.message | String | 错误信息  |
| data.vodTaskId | String | 鉴黄任务ID |
| data.fileId | String | 被鉴黄的文件ID |

## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

TODO：

协议需要完善，如下：

1. 不能直接返回is_porn，应该返回更加详细的信息；
2. 图片URL，是不是包含黄色、暴力等？不能直接叫porn_img_url

```javascript
{
    "version": "4.0",
    "eventType": "PorncheckComplete",
    "data": {
        "status": 0,
        "message": "",
        "vodTaskId": "Porncheck-1edb7eb88a599d05abe451cfc541cfbd",
        "fileId": "14508071098244931831",
        "pornImgUrl": [
            {
                "pic_time": "05:10:26",
                "pic_url": "http://125xx.vod2.myqcloud.com/vod125xx/12313213/pic.png"
            },
            {
                "pic_time": "05:10:29",
                "pic_url": "http://125xx.vod2.myqcloud.com/vod125xx/12313213/pic.png"
            }
        ]
    }
}
```