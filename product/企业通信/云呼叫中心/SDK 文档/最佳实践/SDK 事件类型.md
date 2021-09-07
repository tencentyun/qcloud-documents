## 如何监听事件
```
function onCallIn(data) { //可以直接传入事件字符串监听事件
    console.log('会话呼入',data)
}
tccc.on('callIn',onCallIn)
tccc.off('callIn', onCallIn) //可以通过off注销某个事件监听
tccc.on(tccc.events.sessionEnded, function(data) { //也可以通过tccc.events枚举避免字符串typo
    console.log('会话结束',data)
})
```

## 事件类型
为了同步 SDK 的状态给前端页面, SDK 暴露了以下事件：

<dx-tabs>
::: 1.\sSDK\s初始化完成事件
**tccc.events.ready**
SDK 的加载通常需要数秒钟时间，以完成加载和登录，在此之前调用 SDK 的其他功能可能会导致发生异常。请确保监听 SDK 的 ready 事件，并在 ready 后调用 SDK 的相关功能。
```
// 调用腾讯云 API 获取 token, sdkUrl
// API 接口连接 https://cloud.tencent.com/document/api/679/49227
// 自己需要补充 sdkAppId 和 userId
function injectTCCC({token, sdkAppId, userId, sdkUrl}) {
    const scriptDom = document.createElement('script')
    scriptDom.dataset.token =token
    scriptDom.dataset.sdkAppId =sdkAppId
    scriptDom.dataset.userid = userId
    scriptDom.src = sdkUrl
    scriptDom.onload = () => {
        tccc.on('ready', () => { //监听ready事件
            tccc.callOut({phoneNumber: '186xxxxxxxx'}) //此时可以安全的调用外呼功能
        }
    }
    document.body.appendChild(scriptDom)
}
injectTCCC({token: "xxx", userId: 'xxx', sdkAppId: 'xxx'})

```
:::
::: 2.\sToken\s过期事件
**tccc.events.tokenExpired**
SDK 初始化时 Token 已过期，则触发此事件，此时需要重新从云 API 获取最新的 Token 并且重新初始化SDK。
:::
::: 3.\s会话接入询问事件
**tccc.events.callIn**
当客户的转人工请求到达呼叫中心后，呼叫中心会根据当前配置的调度算法以及优先级询问可能的坐席，此时该事件触发，当前坐席需要作出应答。

| Props             | Type                             | Description                      |
| ----------------- | -------------------------------- | -------------------------------- |
| sessionId         | string                           | 当前会话的 Id                          |
| calleePhoneNumber | string                           | 被叫号码                             |
| callerPhoneNumber | string                           | 可选，主叫号码                          |
| protectedCaller   | string                           | 可选，主叫映射 Id                        |
| callerLocation    | string                           | 主叫号码归属地                          |
| ivrPath           | {key: string; label: string}\[\] | 用户的 IVR 按键路径，key 表示按键，label 表示分支标签文字 |
| remark            | string                           | 可选，主叫备注                          |
| timeout           | number                           | 会话呼入超时时间                         |

```
{
    "sessionId": "9657eeb1-25ac-4bef-9168-a172ba721ed9",
    "callerPhoneNumber": "0086075586013388",
    "calleePhoneNumber": "0086075586013388",
    "protectedCaller": ""
    "callerLocation": "广东深圳固话",
    "ivrPath": [
        {
            "key": "0",
            "label": "hello world"
        }
    ],
    "remark": "Tencent",
    "timeout": 8
}

```
:::
::: 4.\s会话开始事件
**tccc.events.userAccessed**
坐席接听后通话开始则触发此事件。

| Props     | Type   | Description |
| --------- | ------ | ----------- |
| sessionId | string | 当前会话的Id     |

```
{
    "sessionId": "9657eeb1-25ac-4bef-9168-a172ba721ed9"
}
```
:::
::: 5.\s超时转接事件
**tccc.events.autoTransfer**
坐席收到会话接入时，如果在管理端中超时转接功能处于开启状态，同时坐席没有在指定时间内接入，当前会话会触发超时转接至其他坐席。此事件触发。

| Props     | Type   | Description |
| --------- | ------ | ----------- |
| sessionId | string | 当前会话的 Id     |

```
{
    "sessionId": "9657eeb1-25ac-4bef-9168-a172ba721ed9"
}
```
:::
::: 6.\s会话结束事件
**tccc.events.sessionEnded**
当坐席或者客户挂断或者结束会话时, 触发此事件。

| Props     | Type   | Description |
| --------- | ------ | ----------- |
| sessionId | string | 当前会话的Id     |
| type      | string | 会话类型        |
| duration  | number | 通话持续时长，单位为秒 |
|closeBy|string|挂断方，可选值有<li>"seat"：坐席挂断</li><li>"client": "客户挂断</li><li>"admin": 系统挂断</li>|

```
{
    "sessionId": "027d802c-8b55-4a00-8541-70dd6648cac9",
    "type": "phone",
    "duration": 9.614,
    "closeBy": "client"
}

```
:::
::: 7.\s会话完成事件
**tccc.events.sessionCompleted**
当坐席整理会话列表时，点击完成会话时（该会话会从坐席的服务列表中清除）触发此事件。

| Props     | Type   | Description |
| --------- | ------ | ----------- |
| sessionId | string | 当前会话的 Id     |

```
{
    "sessionId": "9657eeb1-25ac-4bef-9168-a172ba721ed9"
}
```
呼入事件流程：
![](https://main.qcloudimg.com/raw/b4ad4ceac252feb5e1a0b91823d8e80f.png)
:::
::: 8.\s外呼事件
**tccc.events.callOuted**
当坐席点击呼出按钮外呼成功或使用 tccc.Call.callOut() 成功时，会触发该事件，此事件表明当前外呼已经发起，早于对端振铃。

| Props             | Type   | Description |
| ----------------- | ------ | ----------- |
| sessionId         | string | 当前会话的Id     |
| calleePhoneNumber | string | 可选，被叫号码     |
| callerPhoneNumber | string | 主叫号码        |
| protectedCallee   | string | 可选，被叫映射 Id   |
| remark            | string | 可选，被叫号码备注   |

```
{
    "sessionId": "d8615e3a-d850-490b-b7b3-db2edd8a9d8e",
    "callerPhoneNumber": "008602066247697",
    "calleePhoneNumber": "0086075586013388",
    "protectedCallee": "",
    "remark": "Tencent"
}

```
:::
::: 9.\s外呼接听事件
**tccc.events.calloutAccepted**
当坐席外呼, 对方接听时会收到此事件。

| Props     | Type   | Description |
| --------- | ------ | ----------- |
| sessionId | string | 当前会话的 Id     |

```
{
    "sessionId": "d8615e3a-d850-490b-b7b3-db2edd8a9d8e"
}

```

呼出事件流程：
![](https://main.qcloudimg.com/raw/bbc97db34ef49692bd5e49e9bd45e93b.png)
:::
::: 10.\s会话转接事件
**tccc.events.transfer**
坐席可以在服务过程中, 将当前服务的会话转接给指定技能组或坐席，转接完成时，会触发此事件。

| Props        | Type   | Description |
| ------------ | ------ | ----------- |
| sessionId    | string | 当前会话的Id     |
| skillGroupId | string | 可选，转接的技能组id |
| userId       | string | 可选，转接的坐席    |

```
{
    "sessionId": "d8615e3a-d850-490b-b7b3-db2edd8a9d8e"
    "skillGroupId": "334",
    "userId": ""
}

```
:::
</dx-tabs>
