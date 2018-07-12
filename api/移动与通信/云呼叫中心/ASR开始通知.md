## 接口说明
仅在开启了智能外呼时会上报该通知。

## 请求
### 请求地址


### 请求方式
Post 请求

### 请求包体

| 属性     | 类型     | 必选   | 说明                  |
| ------ | ------ | ---- | ------------------- |
| appId  | String | 是   | 应用 ID               |
| callId | String | 是   | 呼叫 ID               |
| ssrc  |  String | 是  | 对应媒体 rtp 头部 ssrc  |
| event	| String | 是  | 通知事件类型 (asrStart)  |
| timeStamp | String | 是  | 时间戳  |


## 响应
### 响应包体

## 实际案例
### JSON 请求示例


### JSON 响应示例
