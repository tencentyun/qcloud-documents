## 接⼊准备
### 申请商户 ID 及获取 EidToken
详情请参考 [E证通小程序接入](https://cloud.tencent.com/document/product/1007/56643)。
#### 前置条件
1. 添加服务器域名⽩名单
⼩程序前端接⼝请求有域名⽩名单限制，未添加⽩名单的域名只能在调试模式下运⾏。您需要在⼩程序上线前需要将以下域名添加⾄服务器域名⽩名单
```
// request 合法域名
eid.faceid.qq.com
eid-enhance.faceid.qq.com
```
2. 添加业务域名⽩名单
在⼩程序配置业务域名中，将下载后的校验⽂件发给腾讯侧对接⼈员，待腾讯侧进⾏完相应的操作后，将以下域名添加⾄业务域名⽩名单
```
eid.faceid.qq.com
eid-enhance.faceid.qq.com
```

## uni-app 接⼊
### 步骤⼀：注册并创建 uni-app 开发环境
uni-app 开发接⼊具体参照 [uni 官⽹](https://uniapp.dcloud.net.cn/)。

### 步骤⼆：下载并配置 mp_ecard_sdk 源码
1. [下载 sdk 源码](https://faceid-ecard-1254418846.cos.ap-chengdu.myqcloud.com/uni/ecard-sdk-uni/cloud-mp-ecard-uni-sdk-release.zip)。
2. 配置 sdk 源码。
	- ⽅法⼀：项⽬根⽬录配置（推荐）
		1. 将 sdk 源码包 mp_ecard_sdk ⽂件夹拷⻉到项⽬根⽬录。
		2. 在 pages.json 中配置相关⻚⾯。
```
  "pages": [
 {
 "path": "mp_ecard_sdk/index/index",
 "style": {
 "navigationBarTitleText": "腾讯云E证通授权"
 }
 },
 {
 "path": "mp_ecard_sdk/protocol/eid/eid",
 "style": {
 "navigationBarTitleText": "eID数字身份⼩程序服务协议",
 "enablePullDownRefresh": false
 }
 },
 {
 "path": "mp_ecard_sdk/protocol/privacy/privacy",
 "style": {
 "navigationBarTitleText": "腾讯隐私政策",
 "enablePullDownRefresh": false
 }
 },
 {
 "path": "mp_ecard_sdk/protocol/service/service",
 "style": {
 "navigationBarTitleText": "腾讯云E证通服务协议",
 "enablePullDownRefresh": false
 }
 },
 {
 "path": "mp_ecard_sdk/protocol/userAccredit/userAccredit",
 "style": {
 "navigationBarTitleText": "⽤户授权协议",
 "enablePullDownRefresh": false
 }
 }
 ]
```
	- ⽅法⼆：任意位置⽂件夹配置
		1. 将 sdk 源码放置在其他⽂件夹下，例如 pagse/mp_ecard_sdk。
		2. 在 pages.json 中配置相关⻚⾯，pages 的 path 应为 mp_ecard_sdk 的相对位置路径，例如：pages/。
```
"pages": [
 {
 "path": "pages/mp_ecard_sdk/index/index",
 "style": {
 "navigationBarTitleText": "腾讯云E证通授权"
 }
 },
 {
 "path": "pages/mp_ecard_sdk/protocol/eid/eid",
 "style": {
 "navigationBarTitleText": "eID数字身份⼩程序服务协议",
 "enablePullDownRefresh": false
 }
 },
 {
 "path": "pages/mp_ecard_sdk/protocol/privacy/privacy",
 "style": {
 "navigationBarTitleText": "腾讯隐私政策",
 "enablePullDownRefresh": false
 }
 },
 {
 "path": "pages/mp_ecard_sdk/protocol/service/service",
 "style": {
 "navigationBarTitleText": "腾讯云E证通服务协议",
 "enablePullDownRefresh": false
 }
 },
 {
 "path":
"pages/mp_ecard_sdk/protocol/userAccredit/userAccredit",
 "style": {
 "navigationBarTitleText": "⽤户授权协议",
 "enablePullDownRefresh": false
 }
 }
 ],
```
		3. 修改 mp_ecard_sdk 下的 globalConfig.js 的 normalPath 参数,修改为对应相对路径，例如：'/pages'。注意，开头需要加'/'。
```
export default {
 normalPath: '/pages'
 }
```
3. 初始化
	- ⽅法⼀：可以在 App.vue 中全局初始化。
```
import { initEid } from './mp_ecard_sdk/main';
export default {
 onLaunch: function() {
 initEid();
 },
};
```
	- ⽅法⼆：在需要调⽤到的⻚⾯⽅法之前初识化即可。
4. 调⽤
在需要进⾏核身的地⽅引⼊调⽤ SDK 的⽅法 startEid。
>! startEid 调⽤需要在 initEid 初始化之后。
>
```
 import { startEid } from './mp_ecard_sdk/main'
 // 示例⽅法
 startEid({
 data: {
 token,
 },
 verifyDoneCallback(res) {
 const { token, verifyDone } = res;
 console.log('收到核身完成的res:', res);
 console.log('核身的token是:', token);
 console.log('是否完成核身:', verifyDone);
 },
 });
```
**startEid() 参数说明：**
	- `startEid(options)` ：进⼊实名认证⻚⾯。
	- `options` ：Object required 接⼊⽅传⼊的参数。
	- `options.data.token` ：String required 接⼊⽅⼩程序从接⼊⽅服务端获取EidToken。
	- `options.verifyDoneCallback` ：Function(res) required 核身完成的回调。res 包含验证成功的 token，是否完成的布尔值标志 verifyDone。请根据 res 返回的结果进⾏业务处理判断。

## 获取 E 证通核验结果信息
⽤户完成⼈脸核身后，会以回调形式返回 EidToken 以及其他信息，接⼊⽅⼩程序将 EidToken 传给接⼊⽅的服务端，接⼊⽅服务端即可凭借 EidToken 参数调⽤获取⼩程序核身结果信息 GetEidResult 接⼝去获取本次核身的详细信息，最后将核身结果返回给接⼊⽅⼩程序。
>? EidToken 作为⼀次核身流程的标识，有效时间为600秒；完成核身后，可⽤该标识获取3天内验证结果信息。

## 卸载 sdk
删除 `mp_ecard_sdk` ⽂件夹。

## 接⼊时序图
![](https://qcloudimg.tencent-cloud.cn/raw/62040b3b1c495342f8a31c68d1e34bfd.png)

## 完整示例参考
- [Vue2 Demo 示例](https://faceid-ecard-1254418846.cos.ap-chengdu.myqcloud.com/uni/ecard-sdk-uni/ecard-sdk-uniapp-demo-for-vue2.zip)
- [Vue3 Demo示例](https://faceid-ecard-1254418846.cos.ap-chengdu.myqcloud.com/uni/ecard-sdk-uni/ecard-sdk-uniapp-demo-for-vue3.zip)

## 注意事项
- 从 eID 数字身份⼩程序返回接⼊⽅⼩程序
当接⼊⽅⼩程序在初始化 E 证通 SDK 的时候，E 证通 SDK 会通过 wx.onAppShow 注册⼀个监听从 eID 数字身份⼩程序跳转回接⼊⽅⼩程序的事件，从⽽根据情况触发接⼊⽅传⼊的核身完成的回调函数，由于微信的机制，⽤户在 eID 数字身份⼩程序跳转回接⼊⽅⼩程序的时候，同时也会触发接⼊⽅⼩程序 app.js 中的 onShow ⽅法。为了避免冲突，如果接⼊⽅⼩程序在 onShow 中有执⾏逻辑的话，需要排除掉从 eID 数字身份⼩程序跳转回接⼊⽅⼩程序这个场景。
可通过以下⽅法实现：
```javascript
// app.vue
onShow(options) {
 const { referrerInfo, scene } = options;
 /* 判断是否从eID数字身份⼩程序返回 */
 const { appId } = referrerInfo;
 if (scene === 1038 && appId === 'wx0e2cb0b052a91c92') {
 return;
 } else {
 // 执⾏接⼊⽅⼩程序原本的逻辑
 }
},
```
