>! tccc 是加载 SDK 后的全局变量，可直接访问。
## 通用结构
### CommonSDKResponse
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>status</td>
      <td>'success' |
'error'</td>
      <td>是</td>
      <td>SDK API 调用结果，成功时返回 success，失败返回 error</td>
   </tr>
   <tr>
      <td>errorMsg</td>
      <td>string</td>
      <td>否</td>
      <td>错误信息，当 status 为 error 时返回</td>
   </tr>
</table>

## Call（电话客服和音频客服相关接口函数）
### 电话呼出
**tccc.Call.startOutboundCall(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='6'>options</td>
      <td>phoneNumber</td>
      <td>string</td>
      <td>是</td>
      <td>被叫号码</td>
   </tr>
   <tr>
      <td>phoneDesc</td>
      <td>string</td>
      <td>否</td>
      <td>号码备注，可替代号码显示</td>
   </tr>
   <tr>
      <td>uui</td>
      <td>string</td>
      <td>否</td>
      <td>用户自定义数据，传入后可通过 <a href="https://cloud.tencent.com/document/product/679/67257">电话 CDR 事件</a> 推送返回</td>
   </tr>
   <tr>
      <td>skillGroupId</td>
      <td>string</td>
      <td>否</td>
      <td>指定技能组内绑定的外呼号码</td>
   </tr>
   <tr>
      <td>callerPhoneNumber</td>
      <td>string</td>
      <td>否</td>
      <td>指定外呼号码</td>
   </tr>
   <tr>
      <td>servingNumberGroupIds</td>
      <td>string[]</td>
      <td>否</td>
      <td>指定号码 id 列表</td>
   </tr>
</table>

### 接听会话
**tccc.Call.accept(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID，从 tccc.events.callIn 事件中获取</td>
   </tr>
</table>

### 挂断会话
**tccc.Call.hungUp(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 删除会话
**tccc.Call.deleteCall(options)**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 静音
**tccc.Call.muteMic(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 取消静音
**tccc.Call.unmuteMic(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 当前是否静音
**tccc.Call.isMicMuted(options): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 发起内部通话
**tccc.Call.startInternalCall(): Promise<CommonSDKResponse>**
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>calleeUserId</td>
      <td>string</td>
      <td>是</td>
      <td>被叫坐席账号</td>
   </tr>
   <tr>
      <td>useMobile</td>
      <td>boolean</td>
      <td>否</td>
      <td>是否呼叫对方手机</td>
   </tr>
	 </table>

### 转接会话
#### tccc.Call.transfer(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='3'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
   <tr>
      <td>skillGroupId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定技能组</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定坐席</td>
   </tr>
</table>

### 呼叫保持
#### tccc.Call.hold(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 取消通话保持
#### tccc.Call.unHold(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 发送分机号
#### tccc.Call.sendDigits(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
   <tr>
      <td>dtmfText</td>
      <td>string</td>
      <td>否</td>
      <td>需要发送的分机号</td>
   </tr>
</table>

## Chat（在线客服相关接口函数）
### 接听会话
#### tccc.Chat.accept(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 结束会话
#### tccc.Chat.end(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 转接会话
#### tccc.Chat.transfer(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='3'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
   <tr>
      <td>skillGroupId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定技能组</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定坐席</td>
   </tr>
</table>

## Video（视频客服相关接口函数）
### 接听会话
#### tccc.Video.accept(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 挂断会话
#### tccc.Video.end(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 静音
#### tccc.Video.muteMic(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 取消静音
#### tccc.Video.unmuteMic(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 关闭摄像头
#### tccc.Video.muteVideo(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 开启摄像头
#### tccc.Video.unmuteVideo(options): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 转接会话
#### tccc.Video.transfer(): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='3'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
   <tr>
      <td>skillGroupId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定技能组</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>否</td>
      <td>转接到指定坐席</td>
   </tr>
</table>

## Agent（坐席状态相关接口函数）
### 上线
#### tccc.Agent.online(): void 

### 下线
#### tccc.Agent.offline(): void

### 设置坐席状态
#### tccc.Agent.setStatus(optoins): Promise<CommonSDKResponse>
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>status</td>
      <td>string</td>
      <td>是</td>
      <td><li>坐席状态，可选值：</li><li>free: 空闲</li><li>rest: 小休</li><li>arrange: 话后整理</li><li>notReady: 示忙</li><li>stopNotReady: 停止示忙</li></td>
   </tr>
   <tr>
      <td>restReason</td>
      <td>string</td>
      <td>否</td>
      <td>小休原因</td>
   </tr>
</table>

## Devices（设备相关接口函数）
### 检测当前浏览器是否支持
#### tccc.Devices.isBrowserSupported(): boolean
>? TCCC Web SDK 支持 Chrome 56、Edge80以上的浏览器。

### 返回麦克风设备列表
#### tccc.Devices.getMicrophones(): Promise<<a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDeviceInfo">MediaDeviceInfo</a> []>


### 返回扬声器设备列表
#### tccc.Devices.getSpeakers(): Promise<<a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDeviceInfo">MediaDeviceInfo</a> []>

## UI（用户界面相关接口函数）
### 隐藏 SDK UI
#### tccc.UI.hide(): void

### 显示 SDK UI
#### tccc.UI.show(): void

## Events（事件）
### SDK 初始化完成
#### tccc.events.ready
当 SDK 初始化完成时触发，此时可安全调用API


### 会话呼入
#### tccc.events.callIn
会话呼入类型包括
- phone: 电话会话
- im: 在线会话
- voip: 音频会话
- video: 视频会话
- internal: 内线会话

#### 电话会话呼入
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='8'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>会话 ID</td>
   </tr>
   <tr>
      <td>type</td>
      <td>'phone'</td>
      <td>是</td>
      <td>电话会话类型</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>number</td>
      <td>是</td>
      <td>会话接入超时时长，0代表不超时</td>
   </tr>
   <tr>
      <td>calleePhoneNumber</td>
      <td>string</td>
      <td>是</td>
      <td>被叫号码</td>
   </tr>
   <tr>
      <td>callerPhoneNumber</td>
      <td>string</td>
      <td>否</td>
      <td>主叫号码</td>
   </tr>
   <tr>
      <td>callerLocation</td>
      <td>string</td>
      <td>否</td>
      <td>主叫号码归属地</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>string</td>
      <td>否</td>
      <td>备注</td>
   </tr>
   <tr>
      <td>ivrPath</td>
      <td>{key: string, label: string}[]</td>
      <td>-</td>
      <td>用户的 IVR 按键路径，key 表示对应按键，label 表示对应的按键标签</td>
   </tr>
</table> 

#### 在线会话呼入
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='9'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>会话 ID</td>
   </tr>
   <tr>
      <td>type</td>
      <td>'phone'</td>
      <td>是</td>
      <td>电话会话类型</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>number</td>
      <td>是</td>
      <td>会话接入超时时长，0代表不超时</td>
   </tr>
   <tr>
      <td>nickname</td>
      <td>string</td>
      <td>是</td>
      <td>用户昵称</td>
   </tr>
   <tr>
      <td>avatar</td>
      <td>string</td>
      <td>否</td>
      <td>用户头像</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>string</td>
      <td>否</td>
      <td>备注</td>
   </tr>
   <tr>
      <td>peerSource</td>
      <td>string</td>
      <td>否</td>
      <td>渠道来源</td>
   </tr>
   <tr>
      <td>channelName</td>
      <td>string</td>
      <td>否</td>
      <td>自定义参数</td>
   </tr>
   <tr>
      <td>clientData</td>
      <td>string</td>
      <td>否</td>
      <td>用户自定义参数</td>
   </tr>
</table> 

#### 音频会话呼入
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='11'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>会话 ID</td>
   </tr>
   <tr>
      <td>type</td>
      <td>'voip'</td>
      <td>是</td>
      <td>音频会话类型</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>number</td>
      <td>是</td>
      <td>会话接入超时时长，0代表不超时</td>
   </tr>
   <tr>
      <td>callee</td>
      <td>string</td>
      <td>是</td>
      <td>渠道入口</td>
   </tr>
   <tr>
      <td>calleeRemark</td>
      <td>string</td>
      <td>否</td>
      <td>渠道入口备注</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>是</td>
      <td>用户的 openId</td>
   </tr>
   <tr>
      <td>nickname</td>
      <td>string</td>
      <td>否</td>
      <td>用户授权后可获得微信昵称</td>
   </tr>
   <tr>
      <td>avatar</td>
      <td>string</td>
      <td>否</td>
      <td>用户授权后可获得微信头像</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>string</td>
      <td>否</td>
      <td>备注</td>
   </tr>
   <tr>
      <td>peerSource</td>
      <td>string</td>
      <td>否</td>
      <td>主叫号码归属地</td>
   </tr>
   <tr>
      <td>ivrPath</td>
      <td>{key: string, label: string}[]</td>
      <td>否</td>
      <td>用户的 IVR 按键路径，key 表示对应按键，label 表示对应的按键标签</td>
   </tr>
</table> 

#### 视频会话呼入
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='8'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>会话 ID</td>
   </tr>
   <tr>
      <td>type</td>
      <td>'video'</td>
      <td>是</td>
      <td>视频会话类型</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>number</td>
      <td>是</td>
      <td>会话接入超时时长，0代表不超时</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>是</td>
      <td>用户的 openId</td>
   </tr>
   <tr>
      <td>nickname</td>
      <td>string</td>
      <td>否</td>
      <td>用户授权后可获得微信昵称</td>
   </tr>
   <tr>
      <td>avatar</td>
      <td>string</td>
      <td>否</td>
      <td>用户授权后可获得微信头像</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>string</td>
      <td>否</td>
      <td>备注</td>
   </tr>
</table> 

#### 内部会话呼入
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='8'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>会话 ID</td>
   </tr>
   <tr>
      <td>type</td>
      <td>'internal'</td>
      <td>是</td>
      <td>内部会话类型</td>
   </tr>
   <tr>
      <td>timeout</td>
      <td>number</td>
      <td>是</td>
      <td>会话接入超时时长，0代表不超时</td>
   </tr>
   <tr>
      <td>peerUserId</td>
      <td>string</td>
      <td>是</td>
      <td>主叫坐席的账号</td>
   </tr>
</table> 

### 坐席接入会话
#### tccc.evens.userAccessed
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 会话超时转接事件
#### tccc.events.autoTransfer
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 会话结束事件
#### tccc.events.sessionEnded
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 外呼成功事件
#### tccc.events.callOuted
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 外呼对方接听事件
#### tccc.events.calloutAccepted
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

### 会话话转接事件
#### tccc.events.transfer
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>是</td>
      <td>指定会话 ID</td>
   </tr>
</table>

