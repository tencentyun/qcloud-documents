[](id:sdkAPI)
TCCC SDK 提供 Call、Chat、Agent、Admin、UI 五个 namespace 分别对应电话客服、在线客服、坐席、管理和界面相关 API，使用 API 通过 tccc.namespace.api 的方式调用。
## Call
### 电话呼出
tccc.Call.startOutboundCall(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='2'>options</td>
      <td>phoneNumber</td>
      <td>string</td>
      <td>外呼号码</td>
   </tr>
   <tr>
      <td>phoneDesc</td>
      <td>string</td>
      <td>可选，替代号码显示</td>
   </tr>
</table>

### 接听会话
tccc.Call.accept(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 挂断会话
tccc.Call.hungUp(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 删除会话
tccc.Call.deleteCall(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 静音
tccc.Call.muteMic(options): void
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 取消静音
tccc.Call.unmuteMic(options): void
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 当前是否静音
tccc.Call.isMicMuted(options): boolean
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>

### 内部通话
tccc.Call.startInternalCall(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='2'>options</td>
      <td>calleeUserId</td>
      <td>string</td>
      <td>指定坐席</td>
   </tr>
   <tr>
      <td>useMobile</td>
      <td>boolean</td>
      <td>可选，表示是否呼叫对方手机</td>
   </tr>
</table>

### 转接
tccc.Call.transfer(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='3'>options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话Id</td>
   </tr>
   <tr>
      <td>skillGroupId</td>
      <td>string</td>
      <td>可选，转接到指定的技能组 Id</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>string</td>
      <td>可选，转接到指定的技能组 Id</td>
   </tr>
</table>
转接当前会话到指定技能组或坐席。

### 呼叫保持
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>
Name		Type	Description
options	sessionId	string	指定会话Id
给用户放音，坐席会进入静音状态，放音内容需在管理后台配置。

### 取消呼叫保持
tccc.Call.unHold(options)
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">Name</td>
      <th width="0px" style="text-align:center">Type</td>
      <th width="0px"  style="text-align:center">Description</td>
   </tr>
   <tr>
      <td style="text-align:center" >options</td>
      <td>sessionId</td>
      <td>string</td>
      <td>指定会话 Id</td>
   </tr>
</table>
取消给用户放音，坐席取消静音。

## Agent
### 上线
tccc.Agent.online()
### 下线
tccc.Agent.offline()

## Admin
### 获取技能组列表
`getSkillGroups(): { skillGroupName: string; skillGroupId: string; }[]`

## UI
### 隐藏SDK UI
`tccc.UI.hide(): void`
### 显示SDK UI
`tccc.UI.show(): void`

## Devices
### 检测当前浏览器是否支持
`tccc.Devices.isBrowserSupported(): boolean`
### 支持 Chrome 56+，Edge 80+
### 返回麦克风设备列表
`tccc.Devices.getMicrophones(): Promise<MediaDeviceInfo[]>`
### 返回扬声器设备列表
`tccc.Devices.getSpeakers(): Promise<MediaDeviceInfo[]>`
