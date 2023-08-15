微搭外部资源加载功能指在帮助开发者在应用中加载外部的 JSSDK 或 CSS 样式等资源，方便开发者快速引用第三方 SDK 并在自己的应用中使用，这样可以方便扩展前端应用的能力和样式风格。

>!当前加载外部资源仅支持在 Web 端使用，暂不支持小程序。


## 操作步骤
### 步骤1：添加外部资源（JS/CSS）
1. 首先，在编辑器的**应用设置** > **开发设置**页面中，单击**添加外部资源**。
3. 在弹出的对话框中，输入要加载的资源的 URL。
3. 单击**添加**，即可完成资源的添加。

<img src = "https://qcloudimg.tencent-cloud.cn/raw/8693b209e7013f80d15920d731dfb6d1.png"  style = "width:80%">


### 步骤2：引用外部资源并调用方法
外部资源添加成功后，会在应用初始化时默认加载该资源，故只需打开 [代码编辑器](https://cloud.tencent.com/document/product/1301/57912) 在应用生命周期或页面生命周期直接调用即可，如图所示：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/c427fae85872e07516671562d264b272.png"  style = "width:80%">

进入 [代码编辑器](https://cloud.tencent.com/document/product/1301/57912)，在需要引用外部资源的位置输入以下代码（建议在应用周期的 `onAppShow() {...}` 、页面生命周期的 `onPageShow() {...}` 应用方法中或之后的方法中进行调用即可）：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/6ea1871102c2b0dddde388b0aa131139.png"  style = "width:80%"> 

保存代码，运行预览应用，即可在应用中使用外部资源中的方法。

#### 调用示例
例如我们引用了第三方的 [Tailwind CSS](https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css)。
利用 Tailwind 提供的标准 Class 进行样式的配置：
- 通过 rounded 控制边框圆角
- 通过 ml 控制元素左侧外间距
- 通过 space-x 控制子元素间距
- 通过 font-bold 控制字体的粗细

<dx-tabs>
::: 示例1
在页面中添加一个图片。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/1c6fb6d4cb63db3fbcd24e966cd81904.png"  style = "width:80%"> 
然后在图片的样式 > classname 绑定 rounded-3xl，可以查看绑定之后图片圆角的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/86959970961de1bb18466dc0f9b02ed9.png"  style = "width:80%"> 
:::
::: 示例2
在示例1的图片组件的 classname 绑定 ml-20，可以查看绑定之后图片组件的左侧外边距的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/6300184ceac39755afa56106d4a061df.png"  style = "width:80%"> 
:::
::: 示例3
在页面中添加一个普通容器，普通容器中添加几个按钮。然后在普通容器的样式 > classname 绑定 space-x-4，可以查看绑定之后子元素间距的变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/aa992b5dadd40890a840ec087a029fd8.png"  style = "width:80%"> 
:::
::: 示例4
示例3中添加的第一个按钮组件，在其样式 > classname 绑定 font-bold，可以查看绑定之后按钮组件的字体粗细变化。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/d02f9dbba72c6fe5decab8d7907a9fe1.png"  style = "width:80%"> 
:::
</dx-tabs>

## 注意事项
- 当前外部资源仅支持在 Web 端使用，暂不支持小程序。
- 当前外部 JS 资源仅支持无框架依赖的 JS 库，不建议直接使用依赖 vue/react 等框架的 JS 库。
- 请确保加载的资源 URL 是正确的，并且资源可以访问（某些资源是否支持跨域访问）。
- 如果使用的第三方资源，请遵循第三方资源提供商的使用规定，并确保不会侵犯任何第三方权益。
- 请确保您的应用与添加的外部资源兼容，以确保应用的正常运行。
- 请在开发过程中注意保护您的应用代码及数据安全，避免被第三方恶意访问。
