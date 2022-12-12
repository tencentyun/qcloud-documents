
[](id:required)
## 开发环境要求
- React ≥ v18.0
- TypeScript
- node（12.13.0 ≤ node 版本 ≤ 17.0.0, 推荐使用 Node.js 官方 LTS 版本 16.17.0）
- npm（版本请与 node 版本匹配）

## chat-uikit-react 集成

### 步骤1：创建项目

1. 创建一个新的 React 项目，您可自行选择是否需要使用 ts 模板。
<dx-codeblock>
:::  shell
npx create-react-app sample-chat --template typescript
:::
</dx-codeblock>
2. 创建项目完成后，切换到项目所在目录。
<dx-codeblock>
:::  shell
cd sample-chat
:::
</dx-codeblock>

### 步骤2：下载 chat-uikit-react 组件

通过 npm 方式下载  [chat-uikit-react](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react) 并在项目中使用，另外在 GitHub 中也提供相关的 [开源代码](https://github.com/TencentCloud/chat-uikit-react)，您也可在此基础上进行开发您自己的组件库。
<dx-codeblock>
:::  shell
npm install @tencentcloud/chat-uikit-react
:::
</dx-codeblock>

[](id:step3)
### 步骤3：引入 chat-uikit-react 组件

替换 App.tsx 中的内容，或者您可以新建一个组件引入。
>! 以下代码中未填入 `SDKAppID`、`userID` 和 `userSig`，需在 [步骤4](#step4) 中获取相关信息后进行替换。

 <dx-codeblock>
:::  tsx
import React, { useEffect, useState } from 'react';
import { TUIKit } from '@tencentcloud/chat-uikit-react';
import '@tencentcloud/chat-uikit-react/dist/cjs/index.css';
import TIM, { ChatSDK } from 'tim-js-sdk/tim-js-friendship';
import TIMUploadPlugin from 'tim-upload-plugin';

// create tim instance && login
const init = async ():Promise<ChatSDK> => {
	return new Promise((resolve, reject) => {
		const tim = TIM.create({ SDKAppID: 0 });
		tim?.registerPlugin({ 'tim-upload-plugin': TIMUploadPlugin });
		const onReady = () => { resolve(tim); };
		tim.on(TIM.EVENT.SDK_READY, onReady);
		tim.login({
			userID: 'xxx',
			userSig: 'xxx',
		});
	});
}

export default function SampleChat() {
	const [tim, setTim] = useState<ChatSDK>();
	useEffect(() => {
		(async ()=>{
			const tim = await init()
			setTim(tim)
		})()
	}, [])

	return (
		<div style={{height: '100vh',width: '100vw'}}>
			<TUIKit tim={tim}></TUIKit>
		</div>
	);
}
:::
</dx-codeblock>

[](id:step4)
### 步骤4：获取 SDKAppID、userID 和 userSig

- SDKAppID：SDKAppID 是腾讯云 IM 服务区分客户帐号的唯一标识。我们建议每一个独立的 App 都申请一个新的 SDKAppID。不同 SDKAppID 之间的消息是天然隔离的，不能互通。
  您可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 查看所有的 SDKAppID，单击 **创建新应用**，可以创建新的 SDKAppID。
  ![](https://qcloudimg.tencent-cloud.cn/raw/d7f4bacfc440fe50cec41a48030a9928.png)
- userID：用户 ID。自行填写或者进入应用的账号管理页面，创建账号并获取 userID。
  <img style="width:870px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c6e76f750f11023d13b01ba8c2279a0e.png"/> 
- userSig：用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文。进入 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，选择辅助工具下的 [UserSig生成&校验](https://console.cloud.tencent.com/im/tool-usersig) ,userSig相关介绍参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。
  ![](https://qcloudimg.tencent-cloud.cn/raw/0295898f28bd7531024e0922d64cbf88.png)

### 步骤5：启动项目

<dx-codeblock>
:::  shell
 npm run start
:::
</dx-codeblock>

>!1. 请确保 [步骤三](#step3) 代码中  `SDKAppID`、`userID` 和 `userSig` 均已成功替换，如未替换将会导致项目表现异常。
>2. `userID` 和 `userSig`  为一一对应关系，具体参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。
>3. 如遇到项目启动失败，请检查 [开发环境要求](#required) 是否满足。

### 步骤6：发送您的第一条消息
1. 项目启动成功后，点击“+”图标，创建会话。
2. 在输入框中搜索另一个用户的 userID（参考：[步骤4 -> 创建账号并获取 `userID`](#step4)）。
3. 点击用户头像发起会话。
4. 在输入框输入消息，按下"enter"键发送。
   ![](https://web.sdk.qcloud.com/im/demo/TUIkit/react-static/images/chat-English.gif)

## 常见问题

#### 什么是 UserSig？

UserSig 是用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文。

#### 如何生成 UserSig？

UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向项目的接口，在需要 UserSig 时由您的项目向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

> !本文示例代码采用的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通功能调试**。 正确的 UserSig 签发方式请参见上文。


## 相关文档

- [SDK API 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
