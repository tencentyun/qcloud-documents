
TUIKit 组件具备单人视频通话和语音通话功能，并且实现了小程序端和 Web 端、App 端全平台的互通。

> ?**2022年8月以后，TUIKit 组件升级了音视频通话功能，采用了全新的 TUICallKit，新版本音视频通话功能需要加购专属的 IM 音视频通话能力包后解锁**，具体购买方法请参考 [**步骤1：开通音视频服务**](#step1)，如已开通，则可忽略该步骤。

音视频通话界面如下图所示：

<table style="text-align:center;vertical-align:middle;width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">语音通话<br></th>
    <th style="text-align:center;" width="500px">视频通话<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b412c178178c0052254f4f800559d7d4.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6b2b6878e714e77e578e3c962659e36b.jpg" />     </td>
	 </tr>
</table>


## 操作步骤
[](id:step1)
### 步骤1：开通音视频通话能力

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 在页面的右下角找到**开通腾讯实时音视频服务**功能区。
   1. 若您需要体验音视频通话功能，可单击卡片内的 **免费体验** 开通 TUICallKit 的 7 天免费试用服务。
      ![image](https://qcloudimg.tencent-cloud.cn/raw/a7caebe5a773c93fb23d00b4488003b1.png)
   2. 您可参见 [音视频通话能力版本说明](https://cloud.tencent.com/document/product/269/84296#step2) 确认所需要使用的版本，单击 **[购买正式版](https://buy.cloud.tencent.com/avc)** 以购买正式的音视频通话能力。在购买页内的增值服务中勾选“音视频通话能力”，并选择所需版本即可。![](https://qcloudimg.tencent-cloud.cn/raw/c0d6f96d96a1d10a6422f143b620c94b.png)
      ![](https://qcloudimg.tencent-cloud.cn/raw/79e1c65b1cc44442b9f83ea2f62e7683.png)

### 步骤2：下载并集成 TUICallKit 组件
通过 [npm](https://www.npmjs.com/package/@tencentcloud/call-uikit-wechat) 方式下载 TUICallKit 组件，为了方便您后续的拓展，建议您通过以下命令将 TUICallKit 组件复制到自己项目的根目录 wxcomponents 目录下，并在根目录 pages.json 文件中引入组件，在 TUIChat 组件中集成。
 <dx-tabs>
:::  npm 下载
```shell
# macOS
npm i @tencentcloud/call-uikit-wechat
```
```shell
mkdir -p ./wxcomponents/TUICallKit && cp -r ./node_modules/@tencentcloud/call-uikit-wechat/ ./wxcomponents/TUICallKit
```
```shell
# windows
npm i @tencentcloud/call-uikit-wechat
```
```shell
xcopy .\node_modules\@tencentcloud\call-uikit-wechat .\wxcomponents\TUICallKit /i /e
```
成功后目录结构如图所示：  
<img width="300" src="https://qcloudimg.tencent-cloud.cn/raw/a2f115d1b8cbd85bca9f6c6edd7e31f2.png"/>
:::  
:::   pages.json 文件
请在 TUIChat 页面引入 tuicallkit 组件。
```javascript
    "usingComponents": {
     "tuicallkit": "/wxcomponents/TUICallKit/TUICallKit/TUICallKit"
    }
```
如图所示：

<img width="700" src="https://qcloudimg.tencent-cloud.cn/raw/2c120eed8aa66cfcc0833b7e6a369a67.png"/>
:::
:::  index.vue 文件
#### 步骤1. 引入 tuicallkit 组件并初始化:
在 TUIChat [index.vue](https://github.com/TencentCloud/chat-uikit-uniapp/blob/main/TUIPages/TUIChat/index.vue) 文件中引入 tuicallkit 组件并初始化
```javascript
 <!-- #ifdef MP-WEIXIN -->
   <tuicallkit
     ref="TUICallKit"  //用于获取组件对象方法       
   ></tuicallkit>
 <!-- #endif -->
```

如图所示：
<img width="700" src="https://qcloudimg.tencent-cloud.cn/raw/6fdaf89311a33eb57d80d29726dc349a.png"/>

#### 步骤2. 获取 TUICallKit 组件:
```javascript
 const TUICallKit = shallowRef(null);
 // vue3 语法
 return {
    ...toRefs(data),
    TUICallKit,
};
```
#### 步骤3. 初始化 TUICallKit 组件:
```javascript
//  初始化组件
  onReady(() => {
	  // #ifdef MP-WEIXIN
    const options = {
     sdkAppID: uni.$chat_SDKAppID, // 开通实时音视频服务创建应用后分配的 SDKAppID
     userID: uni.$chat_userID, // 用户 ID，可以由您的帐号系统指定
     userSig: uni.$chat_userSig, // 身份签名，相当于登录密码的作用
     tim: uni.$TUIKit, //  tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
    }
    uni.$TUICallKit = TUICallKit;
    nextTick(() => {
     uni.$TUICallKit.value.init(options)
    })
    // #endif
   });
```
#### 步骤4. 回收 TUICallKit 组件
```javascript
   onUnload(() => {
    // #ifdef MP-WEIXIN
    //回收 TUICallKit
    uni.$TUICallKit.value.destroyed();
    // #endif
    TUIServer.destroyed();
   });
```

::: 
</dx-tabs>

> ?
> - **为了减少小程序体积，建议您使用 TUICallkit 内部  tim-wx-sdk (600kb)，具体路径：wxcomponents/TUICallKit/lib/tim-wx-sdk，故请修改** [TUIKit](https://github.com/TencentCloud/chat-uikit-uniapp/blob/main/debug/tim.js) 中 sdk 引用路径改为：
```javascript
const TIM = require("../../../wxcomponents/TUICallKit/lib/tim-wx-sdk");
```
> - **为减少小程序体积，请确保整个项目中只使用了一份  tim-wx-sdk，具体路径：wxcomponents/TUICallKit/lib/tim-wx-sdk**

### 步骤3：发起您的第一次通话

<img width="1015" src="https://qcloudimg.tencent-cloud.cn/raw/3efc84f4a97fbfb74baeb767da487dea.png"/>

您可以通过小程序订阅消息，实现小程序平台的“离线推送”能力，请参考文档 [小程序离线推送](https://cloud.tencent.com/document/product/269/79050)。


## 常见问题

#### 1.  错误提示“The package you purchased does not support this ability”？

如遇以上错误提示，是由于您当前应用的**音视频通话能力包过期**或**未开通**，请参见 [步骤一：开通服务](#step1)，领取或者开通音视频通话能力，进而继续使用 TUICallKit 组件。

#### 2. 如何购买套餐？

请参考购买链接：[音视频通话 SDK 购买指南](https://cloud.tencent.com/document/product/1640/79968)，如有其他问题，请点击页面右侧，进行售前套餐咨询。

#### 3.  通话邀请的超时时间默认是多久？
通话邀请的默认超时时间是30s。

#### 4. 如何全局监听，在所有页面都可以唤起通话界面？

小程序无法直接将一个组件挂载为全局组件。可行的方案如下：
**方案**：通话界面为单独的页面，里面使用 TUICallKit，收到邀请后，跳转到通话页面

1. 通话界面为一个单独的页面，里面引入 TUICallKit。在 app.json 中配置通话界面页面。
2. 在 app.js 中监听 TSignaling 事件。
3. 收到邀请信息则跳转到通话界面，通话结束后，返回到原来的页面。

#### 4. 小程序集成 TUICallKit 体积过大，如何优化？
1. 建议使用 [分包集成](https://cloud.tencent.com/document/product/269/64507) 方案
 - 客户线上环境，如果不需要本地换算 userSig ，可删除 debug 文件（节省 150kb)
 - 打包小程序端，有体积限制需求，分包集成（分包可节约 170kb）
2. **建议您使用 TUICallkit 内部  tim-wx-sdk (600kb)，具体路径：wxcomponents/TUICallKit/lib/tim-wx-sdk，故请修改 [TUIKit](https://github.com/TencentCloud/chat-uikit-uniapp/blob/main/debug/tim.js) 中 sdk 引用路径改为：**
```javascript
const TIM = require("../../../wxcomponents/TUICallKit/lib/tim-wx-sdk");
```
如图所示：
<img width="800" src="https://qcloudimg.tencent-cloud.cn/raw/3fce50809c73d701082192d30880d6c9.png"/> 
3. 为减少小程序体积，**请自检项目其他引用 tim-wx-sdk  (600kb) 的地方，确保整个项目中只使用了一份  tim-wx-sdk**，具体路径：`wxcomponents/TUICallKit/lib/tim-wx-sdk`
4. 运行在小程序端：选择运行时压缩代码
<img width="400" src="https://qcloudimg.tencent-cloud.cn/raw/a00a2eabbaea401f854cda0c58d835cf.png"/> 

## 相关文档
- [TUICallkit  API（小程序） 文档](https://cloud.tencent.com/document/product/647/78912)
- [TUICallkit  API（客户端） 文档](https://cloud.tencent.com/document/product/647/78732)
- [TUIKit (uni-app)](https://cloud.tencent.com/document/product/269/64506)
- [小程序离线推送](https://cloud.tencent.com/document/product/269/79588)

## 交流与反馈
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">309869925</dx-tag-link>

<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-app-qq.png" width = "300"/>
 

