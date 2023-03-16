## 发起一起用
调用 wemeet.collaboration.start 发起**一起用**。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 示例
```plaintext
const { AppHandleRespType } = wemeet;
const callback = (resp) => {
  const { status, message } = resp;
  if (status === AppHandleRespType.SUCCESS) {
    console.log('startCollaboration success');
  } else if (status === AppHandleRespType.CANCELED) {
    console.log('user canceled');
  } else {
    // status === AppHandleRespType.FAILED
    console.log('startCollaboration failed');
  }
};

wemeet.collaboration.start({
  callback,
})
  .catch(err => {
    console.error('startCollaboration failed');
  })

```


## 结束一起用
调用 wemeet.collaboration.end 结束**一起用**。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 示例
```plaintext
const { AppHandleRespType } = wemeet;
const callback = (resp) => {
  const { status, message } = resp;
  if (status === AppHandleRespType.SUCCESS) {
    console.log('endCollaboration success');
  } else if (status === AppHandleRespType.CANCELED) {
    console.log('user canceled');
  } else {
    // status === AppHandleRespType.FAILED
    console.log('endCollaboration failed');
  }
};
wemeet.collaboration.end({
  callback,
})
  .catch(err => {
    console.error('endCollaboration failed');
  })

```


## 加入一起用
调用 wemeet.collaboration.join 加入**一起用**。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 示例

```plaintext
wemeet.collaboration.join()
  .then(() => {
    console.log('joinCollaboration success');
  })
  .catch(err => {
    console.error('joinCollaboration failed');
  })

```


## 离开一起用
调用 wemeet.collaboration.leave 离开**一起用**。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 示例
```plaintext
wemeet.collaboration.leave()
  .then(() => {
    console.log('leaveCollaboration success');
  })
  .catch(err => {
    console.error('leaveCollaboration failed');
  })

```


## 获取应用当前运行的场景值
调用 wemeet.app.getRunningContext 接口获取应用当前运行的场景值。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.11.0
- 是否需要鉴权：否

### 参数说明
返回 `Promise_\<RunningContextData\>`。
- scene：
 - "inmeeting"
 - "preMeetingDetail"
 - "inCollaboration"
 - "historyMeetingDetail"
 - "unknown"
- 运行场景：
 - inmeeting（会中）
 - inCollaboration（一起用模式）
 - preMeetingDetail（会前预定会议、会议详情等）
 - historyMeetingDetail（会后历史详情）
 - unknown（未知）


## 获取当前一起用相关信息
调用 wemeet.collaboration.getContext 接口获取当前**一起用**环节相关信息。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 参数说明
返回 `Promise_\<CollaborationContext\>`
<table>
   <tr>
      <th width="20%" >名称</td>
      <th width="40%" >类型</td>
      <th width="20%" >描述</td>
   </tr>
   <tr>
      <td>activeID</td>
      <td>String</td>
      <td>本次一起用 ID</td>
   </tr>
   <tr>
      <td>url</td>
      <td>String</td>
      <td>本次协作的 url</td>
   </tr>
</table>

### 示例
```plaintext
wemeet.collaboration.getContext()
  .then(() => {
    console.log('getCollaborationContext success');
  })
  .catch(err => {
    console.error('getCollaborationContext failed');
  })

```


## 设置一起用配置项
调用 wemeet.collaboration.setCollaborationConfig 接口设置**一起用**配置项。
- 客户端支持：Win、Mac、IOS、Android
- 支持的版本：3.12.0
- 是否需要鉴权：否

### 参数说明

| 参数 | 类型 | 说明 | 可选 |
| --- | --- | --- | --- |
| url | Undefined、String | 一起用 url，若不配置则发起时默认为当前页面 url | optional |
| visible | Undefined、False、True | 应用顶部栏显示一起用按键，若不配置默认为展示 | optional |

### 示例
```plaintext
wemeet.collaboration.setCollaborationConfig({
  visible: false,
  url: 'https://xxxxxxxx',
})
  .then(() => {
    console.log('setCollaborationConfig success');
  })
  .catch(err => {
    console.error('setCollaborationConfig failed');
  })

```


## 事件监听
事件注册方式参照客户端 API 事件监听部分。

**一起用环节发生变化**
collaboration-change
- 客户端支持：Win, Mac, IOS, Android
- 支持版本：3.12.0
- 是否需要鉴权：否

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| action | String | "start"、"join"、"leave"、"end" 一起用状态流转 |
| activeId | String | 一起用 ID |
| msOpenId | String | 临时用户 ID |
| openId | Undefined、String | optional，已授权的用户返回 |
| timestamp | Number | 时间戳 |
