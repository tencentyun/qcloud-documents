## 开发环境要求
- TypeScript
- sass（sass-loader 版本 ≤ 10.1.1）
- node（12.13.0 ≤ node 版本 ≤ 17.0.0, 推荐使用 Node.js 官方 LTS 版本 16.17.0）
- npm（版本请与 node 版本匹配）

### 步骤1：创建项目

推荐使用 vue-cli 方式创建项目， 配置 Vue3 + TypeScript + sass。
如果您尚未安装 vue-cli ，可以在 terminal 或 cmd 中采用如下方式进行安装：
<dx-codeblock>
::: shell
npm install -g @vue/cli@4.5.0 sass sass-loader@10.1.1
:::
</dx-codeblock>

通过 vue-cli 创建项目，并选择下图中所选配置项。
依赖的选项有：**`Choose Vue version`**、**`Babel`**、**`TypeScript`**、**`Router`**、**`Vuex`**、**`Css Pre-processors`**、**`Linter/Formatter`**。
<dx-codeblock>
::: shell
vue create chat-example
:::
</dx-codeblock>

<img style="width:600px;" src="https://qcloudimg.tencent-cloud.cn/raw/bcb071ef63661f70b9387987318e1f01.png">

创建项目完成后，切换到项目所在目录
<dx-codeblock>
::: shell
cd chat-example
:::
</dx-codeblock>

### 步骤2：下载 UIKit 组件

通过 [npm](https://www.npmjs.com/package/@tencentcloud/chat-cs-vue) 方式下载 UIKit 组件
<dx-codeblock>
::: shell
npm install @tencentcloud/chat-cs-vue
:::
</dx-codeblock>

###  步骤3：修改main.ts
在 main.ts 中，引入chatCsVueUIKit并抛出app实例
<dx-codeblock>
:::  js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { chatCsVueUIKit } from "@tencentcloud/chat-cs-vue" //引入uikit插件

const app = createApp(App);

app.use(router).use(chatCsVueUIKit).mount('#app'); //安装uikit插件

export default app; //抛出app实例
:::
</dx-codeblock>

### 步骤4：调用 UIKit 组件
首先，请从云呼叫中心座席工作台中获取webAppId，具体操作可见[参考《快速配置》获取网页ID](https://cloud.tencent.com/document/product/679/84672)

在需要展示的页面，调用 UIKit 的组件即可使用。

例如：在 App.vue 页面中，使用 UIKit 快速搭建聊天界面（以下示例代码同时支持 Web 端与 H5 端）。
代码示例如下：
```js
<template>
  // webAppId 为从云呼叫中心座席工作台中获取的webAppId
  <TCCCWebChat webAppId="8d11d9c3d8d7687a072e1e1578bfd0bf"></TCCCWebChat>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {};
  },
});
</script>
```
### 步骤5：启动项目

执行以下命令启动项目：
<dx-codeblock>
::: shell
npm run serve
:::
</dx-codeblock>

### 步骤6： 打开UIKit
在浏览器端输入编译完成后的网站地址即可。
<img style="width:600px;" src="https://qcloudimg.tencent-cloud.cn/raw/b4a31a50051f57a685f8424d2976364d.png">

## 自定义消息样式

我们在UIKit中提供了不同种类的slot，便于您自定义消息的样式。

slot与消息类型的对应关系如下表所示：

| slot名称     | 消息类型                                              |
| ------------ | ----------------------------------------------------- |
| tcccText     | 文本消息                                              |
| tcccImage    | 图片消息                                              |
| tcccVideo    | 视频消息                                              |
| tcccAudio    | 语言消息                                              |
| tcccFile     | 文件消息                                              |
| tcccFace     | 表情消息                                              |
| tcccLocation | 位置消息                                              |
| tcccCustom   | 自定义消息                                            |
| tcccMerger   | 合并消息                                              |
| tcccMultiple | 多element消息（message中\_elements的长度大于1的消息） |

### 使用案例
message为消息对象，用于描述一条消息具有的属性，如类型、消息的内容、所属的会话 ID 等。不同类型消息的具体结构可见[文档](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html)。
conversation为会话对象，用于描述会话具有的属性，如类型、消息未读计数、最新消息等。会话对象的具体结构可见[文档](https://web.sdk.qcloud.com/im/doc/zh-cn/Conversation.html)

自定义文本消息渲染的代码案例如下所示:

```js
<template>
  <TCCCWebChat>
	// slot名称为tcccText代表使用文本消息的插槽
    <template #tcccText="{ message,conversation }">
	  // 在插槽中使用文本消息的内容渲染自定义的文本消息
      <p :style="{ color: 'blue' }">{{ message.payload.text }}</p>
    </template>
  </TCCCWebChat>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "Home",
});
</script>
```
效果图如下所示:
<img style="width:600px;" src="https://qcloudimg.tencent-cloud.cn/raw/29a53ecc0bec14789a338d1614ab5674.png">

> !1. slot的参数提供了当前message与当前conversation的属性。
> 2. 您可以根据此案例的代码对其他类型的消息进行自定义渲染。

## UIKit参数[](id:uikitQuery)
UIKit提供的参数名称与参数类型的对应关系如下表所示：

| 参数名称   | 参数类型 |
| ---------- | -------- |
| webAppId   | string   |
| clientData | string   |
| userSig    | string   |
| hideHeader | boolean  |

> ! uikit的参数也可以通过url参数进行传入，但是通过组件传参的优先级高于url参数。

### webAppId
首先，请从云呼叫中心座席工作台中获取webAppId，具体操作可见[参考《快速配置》获取网页ID](https://cloud.tencent.com/document/product/679/84672)

代码示例如下：
```html
<TCCCWebChat webAppId="8d11d9c3d8d7687a072e1e1578bfd0bf"></TCCCWebChat>
```

### clientData与userSig
clientData与userSig的使用方法可见[App 参数对接](https://cloud.tencent.com/document/product/679/76164)

代码示例如下：
```html
<TCCCWebChat clientData="clientData" userSig="userSig"></TCCCWebChat>
```

### hideHeader
hideHeader用于强制隐藏uikit的页面标题。

代码示例如下：
```html
<TCCCWebChat :hideHeader="true"></TCCCWebChat>
```
