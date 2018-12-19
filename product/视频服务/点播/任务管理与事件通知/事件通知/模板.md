## 事件说明
如果APP配置了事件通知，则在xxxxxxx任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见服务端事件通知简介。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| status | String | 错误码, 0: 成功, 其他值: 失败 |
| message | Int | 错误信息  |


## 示例
对于HTTP回调，以下内容为HTTP Post Body；对于基于消息队列的可靠通知，以下内容为PullEvent接口返回包体中eventList数组的元素。

```javascript
{
    "version": 4,
    "eventType": "PullComplete",
    "data": {
    }
}
```
