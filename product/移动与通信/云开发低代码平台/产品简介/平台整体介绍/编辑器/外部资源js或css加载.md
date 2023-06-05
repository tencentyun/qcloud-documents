**微搭外部资源加载功能旨在帮助开发者在应用中加载外部的 JSSDK 或 CSS 样式等资源，方便开发者快速引用第三方 SDK 并在自己的应用中使用。这样可以极大地扩展前端应用的能力和样式风格。**（当前外部资源仅支持在 Web 端使用，暂不支持小程序）


## 使用说明
### 步骤1：添加外部资源（JS/CSS）
1. 首先，在编辑器的**应用设置** > **开发设置**页面中，单击**添加外部资源**。
3. 在弹出的对话框中，输入要加载的资源的 URL。
3. 单击**添加**，即可完成资源的添加。

<img src = "https://qcloudimg.tencent-cloud.cn/raw/8693b209e7013f80d15920d731dfb6d1.png"  style = "width:80%">

![]()
### 步骤2：引用外部资源并调用方法
外部资源添加成功后，会在应用初始化时默认加载该资源，故只需在代码编辑器的应用生命周期或页面生命周期是直接调用即可，如图所示：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/db0bf82854aa359af2be6568a52f71fd.png"  style = "width:50%"> 
进入**代码编辑器**，在需要引用外部资源的位置输入以下代码（建议在应用周期的 `onAppShow() {...}` 或者页面生命周期的 `onPageShow() {...}` 应用方法中或之后的方法中进行调用即可）：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/6ea1871102c2b0dddde388b0aa131139.png"  style = "width:80%"> 
保存代码，运行预览应用，即可在应用中使用外部资源中的方法。

**调用示例：**
例如我们引用了第三方的 Tailwind css（https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css）。
在 Tailwind 中：
- 通过 rounded 控制边框圆角
- 通过 ml 控制元素左侧外间距
- 通过 space-x 控制子元素间距
- 通过 font-bold 控制字体的粗细
- 通过 tracking-widest 控制字母间的间距

**示例1：**
在页面中添加一个图片。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/652e8b5efbd08ed5fca6f4b9d4650d0b.png"  style = "width:80%">
然后在图片的样式 > classname 绑定 rounded-3xl，可以查看绑定之后图片圆角的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/773d8e34c426e298ba5a0148611a06e6.png"  style = "width:80%">

**示例2：**
在示例1的图片组件的 classname 绑定 ml-20，可以查看绑定之后图片组件的左侧外边距的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/4924c8c13d9ee01c2eaa566519d06235.png"  style = "width:80%">

**示例3：**
在页面中添加一个普通容器，普通容器中添加几个按钮。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ed9c3335ded7ae7563c1f4693ea7b7f8.png"  style = "width:80%">
然后在普通容器的样式 > classname 绑定 space-x-4，可以查看绑定之后子元素间距的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/5f005a98a617dcae3d9dbe8674c8d807.png"  style = "width:80%">

**示例4：**
示例3中添加的第一个按钮组件，在其样式 > classname 绑定 font-bold，可以查看绑定之后按钮组件的字体粗细的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/c83d7181037335b420766b68040f31d5.png"  style = "width:80%">

**示例5：**
在页面中添加一个文本组件，文本内容输入字母。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/576870a8063c5b3a1c1d46ed3ef76337.png"  style = "width:80%">
然后在文本的样式 > classname 绑定 tracking-widest，可以查看绑定字母之间间距的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0f724679e7f54042a7e7344ef531ee40.png"  style = "width:80%">

## 注意事项
- 当前外部资源仅支持在 Web 端使用，暂不支持小程序。
- 请确保加载的资源 URL 是正确的，并且资源可以访问（某些资源是否支持跨域访问）。
- 如果使用的第三方资源，请遵循第三方资源提供商的使用规定，并确保不会侵犯任何第三方权益。
- 请确保您的应用与添加的外部资源兼容，以确保应用的正常运行。
- 请在开发过程中注意保护您的应用代码及数据安全，避免被第三方恶意访问。
