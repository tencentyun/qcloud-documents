## Demo 体验
<input type="button" value="Windows 版" style="height: 30px;width: 150px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;margin-right:10px;"  onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education/TRTC_Education_Demo%20Setup%201.1.0.exe')" />

<input type="button" value="MacOS 版" style="height: 30px;width: 150px;margin-top: 5px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education/TRTC_Education_Demo-1.1.0.dmg')" />

## 效果展示
您可以下载安装我们的 Demo 体验实时互动课堂的能力效果，包括语音、视频、屏幕分享等上课方式，还封装了老师开始问答、学生举手、老师邀请学生上台回答、结束回答等相关能力。

<table>
<tr><th>教师端</th><th>学生端</th><tr>
<tr><td><img src="https://main.qcloudimg.com/raw/35d33cb6003bd3575ee6bbfb0cbe6450.png"/></td><td><img src="https://main.qcloudimg.com/raw/30e62d5c96c1ba31fc24c113ecfdb395.png"/></td><tr>
</table>

如需快速实现实时互动课堂功能，可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 [trtc-electron-education](https://cloud.tencent.com/document/product/647/45466) 组件并实现自定义 UI 界面。

## 复用 Demo 的 UI 界面
[](id:ui.step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择**开发辅助**>**[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如  `TestEduDemo`，单击**创建**。

>?本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。


[](id:ui.step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击**已下载，下一步**。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:ui.step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Electron/js/GenerateTestUserSig.js` 文件。
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
<ul>
 <li/>SDKAPPID：默认为0 ，请设置为实际的 SDKAppID。
 <li/>SECRETKEY：默认为空字符串 ，请设置为实际的密钥信息。</ul>
 <img src="https://main.qcloudimg.com/raw/c8ed13a3bc40c8b5d676e933adc402f9.png"/>
4. 粘贴完成后，单击**已复制粘贴，下一步**即创建成功。
5. 编译完成后，单击**回到控制台概览**即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：运行 Demo

```typescript
// 安装 yarn，demo 基于 yarn 管理
npm install yarn -g
// 安装所需依赖
yarn install
// 开发调试
yarn dev
// 打包
yarn package
```

>! 
- 安装依赖过程中，如遇到 Electron 下载慢甚至卡住不动等问题，您可以参考 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 文档解决。
- 只能使用 Mac 打包 Mac 包，使用 Windows 电脑打包 Windows 包。


### 步骤5：修改 Demo 源代码
Demo 所用框架技术如下：
- typescript
- react & react hooks
- electron & electron-react-boilerplate
- element-ui

如下表格列出了各个文件及其所对应的 UI 界面，以便于您进行二次调整：

| 文件 |功能描述|
| ----- | ----- |
| app/containers/HomePage.tsx|进入教室 UI 的实现代码|
| app/containers/ClassRoomPage.tsx|教室 UI 的实现代码|
| app/components/TeacherClass.tsx|教室-老师端 UI 的实现代码|
| app/components/StudentClass.tsx|教室-学生端 UI 的实现代码|
| app/components/Chat.tsx|教室-聊天室 UI 的实现代码|
| app/components/UserList.tsx|教室-成员列表 UI 的实现代码|

## 实现自定义 UI 界面
如果 Demo 中默认实现的 UI 不符合您的预期，您可以按需实现自己的用户界面，即只使用我们封装好的 [trtc-electron-education](https://www.npmjs.com/package/trtc-electron-education) 组件所提供的音视频能力，自行实现 UI 部分。
![](https://main.qcloudimg.com/raw/e00d38bf3869a41be809d8bf80cee248.png)

### 步骤1：集成 SDK

```
// yarn 方式引入
yarn add trtc-electron-education
// npm 方式引入
npm i trtc-electron-education --save
```

### 步骤2：初始化组件
初始化组件，其中几个必填的关键参数介绍如下表所示。

| 参数 |类型|说明|
| ----- | ----- | ----- |
|sdkAppId|number|必填参数，您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。|
|userID|string|必填参数，用户 ID，可以由您的帐号体系指定。|
|userSig|string|必填参数，身份签名（相当于登录密码），由 userID 计算得出，具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。|

```typescript
import TrtcElectronEducation from 'trtc-electron-education';
const rtcClient = new TrtcElectronEducation({
   sdkAppId: 1400***803,
   userID: '123'
   userSig: 'eJwtzM9****-reWMQw_'
 });
```

### 步骤3：实现老师端开课
1. 老师端调用组件 [createRoom](https://cloud.tencent.com/document/product/647/45466#createRoom) 方法创建教室。
```typescript
const params = {
      classId, // 教室 ID
      nickName // 昵称
}
rtcClient.createRoom(params).then(() => {
  //成功创建教室
})
```
2. 老师端调用组件的 [enterRoom](https://cloud.tencent.com/document/product/647/45466#enterRoom) 方法开始上课。
```typescript
rtcClient.enterRoom({
      role: 'teacher', // 角色
      classId // 教室 ID
})
```
3. 老师端调用组件的 [openCamera](https://cloud.tencent.com/document/product/647/45466#openCamera) 方法打开自己的摄像头。
```typescript
const domEle = document.getElementById('test');
rtcClient.openCamera(domEle)
```
4. 老师端可共享自己的屏幕给学生端观看，例如播放 PPT、课件等。
 a. 需要先调用组件的 [getScreenShareList](https://cloud.tencent.com/document/product/647/45466#getScreenShareList) 方法获取窗口列表。
```typescript
const screenList = rtcClient.getScreenShareList()
```
 b. 调用组件的 [startScreenCapture](https://cloud.tencent.com/document/product/647/45466#startScreenCapture) 开始推屏幕分享的流。
```typescript
rtcClient.startScreenCapture({
      type,// 采集源类型
      sourceId,// 采集源 ID，对于窗口，该字段指示窗口句柄；对于屏幕，该字段指示屏幕 ID
      sourceName // 采集源名称，UTF8 编码
 })
```
5. 上课过程中，老师如果想提问与学生互动，可以调用组件的 [startQuestionTime](https://cloud.tencent.com/document/product/647/45466#startQuestionTime) 方法开启问答时间，学生端收到该指令后，可以举手申请回答问题。
```typescript
rtcClient.startQuestionTime(classId) // classId 是教室 ID
```
6. 学生举手后，老师端可调用组件的 [inviteToPlatform](https://cloud.tencent.com/document/product/647/45466#inviteToPlatform) 方法邀请学生上台发言，被邀请的学生自动开麦。
```typescript
rtcClient.inviteToPlatform(userID) // 邀请学生上台的 userID
```
7. 老师端可调用组件的 [finishAnswering](https://cloud.tencent.com/document/product/647/45466#finishAnswering) 方法禁学生的麦克风。
```typescript
rtcClient.finishAnswering(userID)// 禁麦学生的 userID
```

### 步骤4：实现学生端听课
1. 学生端调用组件的 [enterRoom](https://cloud.tencent.com/document/product/647/45466#enterRoom) 方法进入教室，准备听课。
```typescript
rtcClient.enterRoom({
      role: 'student', // 角色
      classId // 教室 ID
})
```
2. 老师端开放举手问答后，学生端可调用组件的 [raiseHand](https://cloud.tencent.com/document/product/647/45466#raiseHand) 方法申请发言。
```typescript
rtcClient.raiseHand()
```

### 步骤5：实现聊天室功能

老师端和学生端可以使用聊天室互发一些文本消息。
```typescript
const params = {
   classId: classId, // 教室 ID
   message: '您好' // 消息文本
}
rtcClient.sendTextMessage(params) // 发送聊天室消息
```

[](id:QQ)
## 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">695855795</dx-tag-link>

## 参考文档

- [SDK API 手册](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/index.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/647/43117)
- [Simple Demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTCSimpleDemo)
- [API Example 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTC-API-Example)
- [Electron 常见问题](https://cloud.tencent.com/document/product/647/62562)
