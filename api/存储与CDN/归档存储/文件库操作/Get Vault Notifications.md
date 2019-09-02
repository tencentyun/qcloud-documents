## 功能描述

Get Vault Notifications请求实现读取指定文件库通知回调策略

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/notification-configuration HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称           | 描述                                       | 类型     |
| ----------- | ---------------------------------------- | ------ |
| CallBackUrl | 回调的HTTP地址                                | String |
| Event       | 回调触发的事件，枚举值：` ArchiveRetrievalCompleted`，`InventoryRetrievalCompleted`，`PushToCOSCompleted`和`PullFromCOSCompleted` | String |

```JSON
{
	"CallBackUrl": "String",
	"Events": ["String", ...]
}
```

