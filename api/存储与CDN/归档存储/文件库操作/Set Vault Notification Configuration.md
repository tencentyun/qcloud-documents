## 功能描述
Set Vault Notification Configuration 请求实现对指定文件库设置通知回调策略。配置成功后，相关任务状态变化为Completed，会向指定 URL 发送通知，通知内容与 Describle Job 返回内容一致。
请求成功，返回 204 No Content

## 请求
### 请求语法
```HTTP
PUT /<UID>/vaults/<VaultName>/notification-configuration HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```
### 请求参数
无特殊请求参数
### 请求头部
无特殊请求头部，其他头部请参见公共请求头部
### 请求内容
| 名称          | 描述                                       | 类型     | 必选   |
| ----------- | ---------------------------------------- | ------ | ---- |
| CallBackUrl | 回调的 HTTP 地址，地址必须以 http:// 或者 https:// 开头   | String | 是    |
| Event       | 可以配置一条或者多条回调触发的事件，枚举值：` ArchiveRetrievalCompleted`，`InventoryRetrievalCompleted`，`PushToCOSCompleted`和`PullFromCOSCompleted` | String | 是    |


```JSON
{
   "CallBackUrl": String,            // 必须以 http:// 或者 https:// 开头
   "Events":[String, ...] 
}
```

## 返回值
### 返回头部
无特殊返回头部，其他头部请参见公共返回头部。
### 返回内容
无返回内容。
