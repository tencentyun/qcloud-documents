## 组件介绍

TUIRoom 是一个包含 UI 的开源音视频组件，通过集成 TUIRoom，您可以在业务中快速上线音视频房间，屏幕分享，聊天等功能。Web 端 TUIRoom 基础功能如下图所示：

>?TUIKit 系列组件同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信IM服务。即时通信 IM 服务详细计费规则请参见 [即时通信 - 价格说明](https://cloud.tencent.com/document/product/269/11673)，TRTC 开通会默认关联开通 IM SDK 的体验版，仅支持100个 DAU。
 
<table>
<tr>
<td><img width="460" src="https://web.sdk.qcloud.com/component/tuiroom/assets/page-home.png"/></td>
<td><img width="460" src="https://web.sdk.qcloud.com/component/tuiroom/assets/page-room.png"/></td>
</tr>
</table>

您可以单击 [TUIRoom 在线链接](https://web.sdk.qcloud.com/component/tuiroom/index.html) 体验 TUIRoom 更多功能。
您可以单击 [Github](https://github.com/tencentyun/TUIRoom) 下载 TUIRoom 代码，并参考 [TUIRoom Web 示例工程快速跑通](https://github.com/tencentyun/TUIRoom/tree/main/Web) 文档跑通 TUIRoom Web 示例工程。
如需在现有业务中集成 Web 端 TUIRoom 组件，请参考本文档。

## 组件集成
TUIRoom 组件使用 Vue3 + TS + Pinia + Element Plus + SCSS 开发，要求接入项目使用 Vue3 + TS 技术栈。

[](id:step1)
### 步骤一： 开通腾讯云实时音视频及即时通信服务
TUIRoom 基于腾讯云实时音视频和即时通信服务进行开发。

1. **创建实时音视频 TRTC 应用**
	- 如果您还没有腾讯云账号，请 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) ，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
	- 在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 单击 **应用管理 > 创建应用** 创建新应用。
![](https://qcloudimg.tencent-cloud.cn/raw/570a1d2db433f5b2429823f2c7ea9837.png)
2. **获取 TRTC 应用及密钥信息**
  1. 在 **应用管理 > 应用信息** 中获取 SDKAppID 信息。SDKAppID 为 TRTC 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话不能互通；
![](https://qcloudimg.tencent-cloud.cn/raw/f7915fbbeb48518c2b25a413960f3432.png)
  2. 在 **应用管理 > 快速上手** 中获取应用的 secretKey 信息。SecretKey 为 TRTC 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 TRTC 服务的鉴权用票据 UserSig。
![](https://qcloudimg.tencent-cloud.cn/raw/06d38bbdbaf43e1f2b444edae00019fa.png)
3. **签发 UserSig**
  UserSig 是腾讯云设计的一种安全保护签名，目的是为了阻止恶意攻击者盗用您的云服务使用权。TUIRoom 初始化需要您提供 UserSig 参数。
	- 调试跑通阶段签发 userSig 的方式请参见 [调试跑通阶段如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275#.E8.B0.83.E8.AF.95.E8.B7.91.E9.80.9A.E9.98.B6.E6.AE.B5.E5.A6.82.E4.BD.95.E8.AE.A1.E7.AE.97-usersig.EF.BC.9F)。
	- 生产环境签发 userSig 的方式参见 [正式运行阶段如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275#.E6.AD.A3.E5.BC.8F.E8.BF.90.E8.A1.8C.E9.98.B6.E6.AE.B5.E5.A6.82.E4.BD.95.E8.AE.A1.E7.AE.97-usersig.EF.BC.9F)。


[](id:step2)
### 步骤二：下载并拷贝 TUIRoom 组件
1. 单击 [Github](https://github.com/tencentyun/TUIRoom) , 克隆或下载 TUIRoom 仓库代码。
2. 打开业务侧已有 Vue3 + TS 项目，支持使用 Vite 及 Webpack 打包方式。如果无 Vue3 + TS 项目，可选择以下任意一种方式生成模版工程。
<dx-tabs>
::: 生成 Vue3 + Vite + TS 模版工程
```bash
npm create vite@latest TUIRoom-demo -- --template vue
```
>! 执行生成模板工程脚本的过程中，第一步直接回车，第二步选择 Vue，第三步选择 vue-ts。
>
成功生成 Vue3 + Vite + TS 模板工程后，执行以下脚本：
```
cd TUIRoom-demo
npm install
npm run dev
```
:::
::: 生成 Vue3 + Webpack + TS 模版工程
```bash
// 安装 vue-cli，注意 Vue CLI 4.x 要求 Node.js 为 v10 以上版本
npm install -g @vue/cli
// 创建 Vue3 + Webpack + TS 模版工程
vue create TUIRoom-demo
```
>! 执行生成模板工程脚本的过程中，生成模版的方式选择 Manually select features，其余配置选项参考图片。
> ![](https://qcloudimg.tencent-cloud.cn/raw/800412fb72b8e092f41fd06d5272601b.png)
> 
成功生成 Vue3 + Webpack + TS 模板工程后，执行以下脚本：
```
cd TUIRoom-demo
npm run serve
```
:::
</dx-tabs>
3. 复制 `TUIRoom/Web/src/TUIRoom` 文件夹到已有项目 src/ 目录下。

[](id:step3)
### 步骤三：引用 TUIRoom 组件

1. 在页面中引用 TUIRoom 组件。例如：在 `App.vue` 组件中引入 TUIRoom 组件。
	- TUIRoom 组件将用户分为主持人角色及普通成员角色。组件对外提供了 [init](#init)、[createRoom](#createroom)、[enterRoom](#enterroom) 方法。
	- 主持人及普通成员可通过 [init](#init) 方法向 TUIRoom 组件初始化应用及用户数据，主持人可通过 [createRoom](#createroom) 方法创建并加入房间，普通成员可通过 [enterRoom](#enterroom) 方法加入主持人已经创建好的房间。
```javascript
<template>
	<room ref="TUIRoomRef"></room>
</template>

<script setup lang="ts">
	import { ref, onMounted } from 'vue';
	// 引入 TUIRoom 组件，注意确认引入路径是否正确
	import Room from './TUIRoom/index.vue';
	// 获取 TUIRoom 组件元素，用于调用 TUIRoom 组件的方法
	const TUIRoomRef = ref();

	 onMounted(async () => {
		// 初始化 TUIRoom 组件
		// 主持人在创建房间前需要先初始化 TUIRoom 组件
		// 普通成员在进入房间前需要先初始化 TUIRoom 组件
		await TUIRoomRef.value.init({
			// 获取 sdkAppId 请您参考 步骤一
			sdkAppId: 0,
			// 用户在您业务中的唯一标示 Id
			userId: '',
			// 本地开发调试可在 https://console.cloud.tencent.com/trtc/usersigtool 页面快速生成 userSig, 注意 userSig 与 userId 为一一对应关系
			userSig: '',
			// 用户在您业务中使用的昵称
			userName: '',
			// 用户在您业务中使用的头像链接
			userAvatar: '',
			// 用户用于屏幕分享的唯一 Id，要求 shareUserId = `share_${userId}`, 无屏幕分享功能需求可不传入
			shareUserId: '',
			// 请您参考本文 步骤一 > 第三步 并使用 sdkAppId 及 shareUserId 签发 shareUserSig 
			shareUserSig: '',
		})
		 // 默认执行创建房间，实际接入可按需求择机执行 handleCreateRoom 方法
		await handleCreateRoom();
	})

	// 主持人创建房间，该方法只在创建房间时调用
	async function handleCreateRoom() {
		// roomId 为用户进入的房间号, 要求 roomId 类型为 number
		// roomMode 包含'FreeSpeech'(自由发言模式) 和'ApplySpeech'(举手发言模式) 两种模式，默认为'FreeSpeech'，注意目前仅支持自由发言模式
		// roomParam 指定了用户进入房间的默认行为（是否默认开启麦克风，是否默认开启摄像头，默认媒体设备Id)
		const roomId = 123456;
		const roomMode = 'FreeSpeech';
		const roomParam = {
			isOpenCamera: true,
			isOpenMicrophone: true,
		}
		await TUIRoomRef.value.createRoom(roomId, roomMode, roomParam);
	}

	// 普通成员进入房间，该方法在普通成员进入已创建好的房间时调用
	async function handleEnterRoom() {
		// roomId 为用户进入的房间号, 要求 roomId 类型为 number
		// roomParam 指定了用户进入房间的默认行为（是否默认开启麦克风，是否默认开启摄像头，默认媒体设备Id)
		const roomId = 123456;
		const roomParam = {
			isOpenCamera: true,
			isOpenMicrophone: true,
		}
		await TUIRoomRef.value.enterRoom(roomId, roomParam);
	}
</script>

<style>
html, body {
	width: 100%;
	height: 100%;
	margin: 0;
}

#app {
	width: 100%;
	height: 100%;
}
</style>
```

>! 在页面中复制以上代码之后，需要修改 TUIRoom 接口的参数为实际数据。

[](id:step4)
### 步骤四：配置开发环境
TUIRoom 组件引入之后，为了确保项目可以正常运行，需要进行以下配置：

<dx-tabs>
::: 配置 Vue3 + Vite + TS 项目开发环境
1. **安装依赖**
	- 安装开发环境依赖：
```bash
npm install sass typescript unplugin-auto-import unplugin-vue-components -S -D
```
	- 安装生产环境依赖：
```bash
npm install element-plus events mitt pinia rtc-beauty-plugin tim-js-sdk trtc-js-sdk tsignaling -S
```
2. **注册 Pinia**
TUIRoom 使用 Pinia 进行房间数据管理，您需要在项目入口文件中注册 Pinia，项目入口文件为 `src/main.ts` 文件。
```javascript
// src/main.ts 文件
import { createPinia } from 'pinia';

const app = createApp(App);
// 注册 pinia
app.use(createPinia()); 
app.mount('#app');
```
3. **配置 element-plus 按需引入**
	- TUIRoom 使用 element-plus UI 组件，为避免引入所有 element-plus组件，需要您在 `vite.config.ts` 中配置 element-plus 组件按需加载。
>! 以下配置项为增量配置，不要删除已经存在的 Vite 配置项。
>
```javascript
// vite.config.ts
import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers';

export default defineConfig({
	// ...
	plugins: [
		AutoImport({
			resolvers: [ElementPlusResolver()],
		}),
		Components({
			resolvers: [ElementPlusResolver({
				importStyle: 'sass',
			})],
		}),
	],
	css: {
		preprocessorOptions: {
			scss: {
				// ...
				additionalData: `
					@use "./src/TUIRoom/assets/style/element.scss" as *;
				`,
			},
		},
	},
});
```
	- 同时为了保证 element-plus 带 UI 组件能够正常显示样式，需要您在入口文件 `src/main.ts` 中加载 element-plus 组件样式。
```
// src/main.ts
import 'element-plus/theme-chalk/el-message.css';
import 'element-plus/theme-chalk/el-message-box.css';
```
:::
::: 配置 Vue3 + Webpack + TS 项目开发环境
1. **安装依赖**
	- 安装开发环境依赖：
```bash
npm install sass sass-loader typescript unplugin-auto-import unplugin-vue-components unplugin-element-plus @types/events -S -D
```
	- 安装生产环境依赖：
```bash
npm install element-plus events mitt pinia rtc-beauty-plugin tim-js-sdk trtc-js-sdk tsignaling -S
```
2. **注册 Pinia**
TUIRoom 使用 Pinia 进行房间数据管理，您需要在项目入口文件中注册 Pinia，项目入口文件为 `src/main.ts` 文件。
```javascript
// src/main.ts 文件
import { createPinia } from 'pinia';

const app = createApp(App);
// 注册 pinia
app.use(createPinia()); 
app.mount('#app');
```
3. **配置 element-plus 按需引入**
	- TUIRoom 使用 element-plus UI 组件，为避免引入所有 element-plus组件，需要您在 `vue.config.js` 中配置 element-plus 组件按需加载。
>! 以下配置项为增量配置，不要删除已经存在的 vue.config.js 配置项。
>
```javascript
// vue.config.js
const { defineConfig } = require('@vue/cli-service')
const AutoImport = require('unplugin-auto-import/webpack')
const Components = require('unplugin-vue-components/webpack')
const { ElementPlusResolver } = require('unplugin-vue-components/resolvers')
const ElementPlus = require('unplugin-element-plus/webpack')

module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      scss: {
        additionalData: '@use "./src/TUIRoom/assets/style/element.scss" as *;'
      }
    }
  },
  configureWebpack: {
    plugins: [
      AutoImport({
        resolvers: [ElementPlusResolver({ importStyle: 'sass' })]
      }),
      Components({
        resolvers: [ElementPlusResolver({ importStyle: 'sass' })]
      }),
      // 在按需导入时自定义主题颜色
      ElementPlus({
        useSource: true
      })
    ]
  }
})

```
	- 同时为了保证 element-plus 带 UI 组件能够正常显示样式，需要您在入口文件 `src/main.ts` 中加载 element-plus 组件样式。
```
// src/main.ts
import 'element-plus/theme-chalk/el-message.css';
import 'element-plus/theme-chalk/el-message-box.css';
```
4. **配置 ts 声明文件**
 在 `src/shims-vue.d.ts` 文件中添加以下配置：
```
declare module 'tsignaling/tsignaling-js' {
  import TSignaling from 'tsignaling/tsignaling-js';
  export default TSignaling;
}

declare module 'tim-js-sdk' {
  import TIM from 'tim-js-sdk';
  export default TIM;
}

declare const Aegis: any;
```
:::
</dx-tabs>

[](id:step5)
### 步骤五：开发环境运行
在控制台执行开发环境运行脚本，使用浏览器打开包含 TUIRoom 的页面，即可在页面中使用 TUIRoom 组件。

- **如果您是使用 [步骤二](#step2) 中的脚本生成 Vue + Vite + TS 项目**，您需要：
	1. 执行开发环境命令。
```bash
npm run dev
```
	2. 在浏览器中打开页面 `http://localhost:3000/`。
	>! 因 TUIRoom 按需引入 element-plus 组件，会导致开发环境路由页面第一次加载时反应较慢，等待 element-plus 按需加载完成即可正常使用。element-plus 按需加载不会影响打包之后的页面加载。
	3. 体验 TUIRoom 组件功能。
- **如果您是使用 [步骤二](#step2) 中的脚本生成 Vue + Webpack + TS 项目**，您需要：
	1. 执行开发环境命令
```bash
npm run serve
```
	2. 在浏览器中打开页面 `http://localhost:8080/`
	> ! 运行过程中若 src/TUIRoom 目录中有 eslint 报错，可在 .eslintignore 文件中添加 /src/TUIRoom 路径屏蔽 eslint 检查。
	3. 体验 TUIRoom 组件功能

## 附录：TUIRoom API
### TUIRoom 接口
#### init

初始化 TUIRoom 数据，任何使用 TUIRoom 的用户都需要调用 init 方法。
```javascript
TUIRoomRef.value.init(roomData);
```

参数如下表所示：

| 参数                  | 类型   | 含义                                                         |
| --------------------- | ------ | ------------------------------------------------------------ |
| roomData              | object |                                                              |
| roomData.sdkAppId     | number | 客户的 SDKAppId                                              |
| roomData.userId       | string | 用户的唯一 ID                                                |
| roomData.userSig      | string | 用户的 UserSig                                               |
| roomData.userName     | string | 用户的昵称                                                   |
| roomData.userAvatar   | string | 用户的头像                                                   |
| roomData.shareUserId  | string | 非必填，用户进行屏幕分享的 UserId，要求 shareUserId = `share_${userId}`，无屏幕分享功能可不传入 |
| roomData.shareUserSig | string | 非必填，用户进行屏幕分享的 UserSig                           |


#### createRoom

主持人创建房间。
```javascript
TUIRoomRef.value.createRoom(roomId, roomMode, roomParam);
```

参数如下表所示：

| 参数                          | 类型   | 含义                                                         |
| ----------------------------- | ------ | ------------------------------------------------------------ |
| roomId                        | number | 房间 ID                                                      |
| roomMode                      | string | 房间模式，'FreeSpeech'（自由发言模式）和 'ApplySpeech'（举手发言模式），默认为 'FreeSpeech'，注意目前仅支持自由发言模式 |
| roomParam                     | Object | 非必填                                                       |
| roomParam.isOpenCamera        | string | 非必填，进房是否打开摄像头，默认为关闭                       |
| roomParam.isOpenMicrophone    | string | 非必填，进房是否打开麦克风，默认为关闭                       |
| roomParam.defaultCameraId     | string | 非必填，默认摄像头设备 ID                                    |
| roomParam.defaultMicrophoneId | string | 非必填，默认麦克风设备 ID                                    |
| roomParam.defaultSpeakerId    | String | 非必填，默认扬声器设备 ID                                    |

#### enterRoom
普通成员加入房间。
```javascript
TUIRoomRef.value.enterRoom(roomId, roomParam);
```

参数如下表所示：

| 参数                          | 类型   | 含义                                   |
| ----------------------------- | ------ | -------------------------------------- |
| roomId                        | number | 房间 ID                                |
| roomParam                     | Object | 非必填                                 |
| roomParam.isOpenCamera        | string | 非必填，进房是否打开摄像头，默认为关闭 |
| roomParam.isOpenMicrophone    | string | 非必填，进房是否打开麦克风，默认为关闭 |
| roomParam.defaultCameraId     | string | 非必填，默认摄像头设备 ID              |
| roomParam.defaultMicrophoneId | string | 非必填，默认麦克风设备 ID              |
| roomParam.defaultSpeakerId    | String | 非必填，默认扬声器设备 ID              |


### TUIRoom 事件

#### onRoomCreate
创建房间回调。
```javascript
<template>
  <room ref="TUIRoomRef" @on-room-create="handleRoomCreate"></room>
</template>

<script setup lang="ts">
  // 引入 TUIRoom 组件，注意确认引入路径是否正确
  import Room from './TUIRoom/index.vue';
  
  function handleRoomCreate(info) {
    if (info.code === 0) {
      console.log('创建房间成功')
    }
  }
</script>
```

#### onRoomEnter

进入房间回调。
```javascript
<template>
  <room ref="TUIRoomRef" @on-room-enter="handleRoomEnter"></room>
</template>

<script setup lang="ts">
  // 引入 TUIRoom 组件，注意确认引入路径是否正确
  import Room from './TUIRoom/index.vue';
  
  function handleRoomEnter(info) {
    if (info.code === 0) {
      console.log('进入房间成功')
    }
  }
</script>
```

#### onRoomDestory

主持人销毁房间通知。
```javascript
<template>
  <room ref="TUIRoomRef" @on-room-destory="handleRoomDestory"></room>
</template>

<script setup lang="ts">
  // 引入 TUIRoom 组件，注意确认引入路径是否正确
  import Room from './TUIRoom/index.vue';
  
  function handleRoomDestory(info) {
    if (info.code === 0) {
      console.log('主持人销毁成功')
    }
  }
</script>
```

#### onRoomExit
普通成员退出房间通知。

```javascript
<template>
  <room ref="TUIRoomRef" @on-room-exit="handleRoomExit"></room>
</template>

<script setup lang="ts">
  // 引入 TUIRoom 组件，注意确认引入路径是否正确
  import Room from './TUIRoom/index.vue';
  
  function handleRoomExit(info) {
    if (info.code === 0) {
      console.log('普通成员退出房间成功')
    }
  }
</script>
```

#### onKickOff

普通成员被主持人踢出房间通知。

```javascript
<template>
  <room ref="TUIRoomRef" @on-kick-off="handleKickOff"></room>
</template>

<script setup lang="ts">
  // 引入 TUIRoom 组件，注意确认引入路径是否正确
  import Room from './TUIRoom/index.vue';
  
  function handleKickOff(info) {
    if (info.code === 0) {
      console.log('普通成员被主持人踢出房间')
    }
  }
</script>
```

## 联系我们

如果您在接入或使用过程有任何需要或者反馈，欢迎加入 TUI 组件使用交流 QQ 群（群号：592465424）进行技术交流和问题反馈。

<img src="https://main.qcloudimg.com/raw/1ea3ab1ff36d37c889f4140499585a4a.png" width="250">

同时，也希望您能抽出几分钟时间，将您接入和使用 Web TUIRoom 的感受和建议通过 [反馈问卷](https://wj.qq.com/s2/10508205/c03f/) 告诉我们，我们非常重视每位用户的宝贵意见，期待您的参与！