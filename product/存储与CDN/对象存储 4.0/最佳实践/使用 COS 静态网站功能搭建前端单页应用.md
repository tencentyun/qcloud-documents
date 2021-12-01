## 什么是单页应用？

单页应用（single-page application，SPA）是一种网络应用程序或网站的模型，它通过动态重写当前页面与用户进行交互，而非传统的从服务器重新加载整个新页面。这种方法避免了页面之间切换打断用户体验，使应用程序更像一个桌面应用程序。在单页应用中，所有必要的代码（HTML、JavaScript 和 CSS）都通过单个页面的加载而检索，或者根据需要（通常是为响应用户操作）动态装载适当的资源并添加到页面。

目前在前端开发领域，常见的单页应用开发框架有 React、Vue、Angular 等。

本文将使用目前较为热门的2个框架，一步步教您使用**腾讯云对象存储（Cloud Object Storage，COS）**提供的**静态网站**功能快速搭建一个线上可用的单页应用，并提供一些常见问题的解决方案。


## 准备工作

1. 安装 [Node.js](https://nodejs.org/zh-cn/download/) 环境。
2. 注册腾讯云账户，并完成实名认证，确保能正常登录 [腾讯云 COS 控制台](https://console.cloud.tencent.com/cos5)。
3. 创建一个存储桶（为了方便测试可将权限设置为**公有读私有写**）。

## 编写前端代码

>! 如果已经自行实现了代码，可直接跳至 [开启存储桶静态网站配置](#configuration) 步骤查看。
>

### 使用 Vue 快速搭建一个单页应用

1. 执行如下命令，安装 vue-cli：
```
npm install -g @vue/cli
```
2. 执行如下命令，使用 vue-cli 快速生成一个 vue 项目，可参考 [官方文档](https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create)。
```
vue create vue-spa
```
3. 执行如下命令，在项目根目录下安装 vue-router：
```
npm install vue-router -S  （Vue2.x）
```
或者
```
npm install vue-router@4 -S  （Vue3.x）
```
4. 修改项目里的 main.js 和 App.vue 文件。
main.js 如下图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/aa25c6be5a57a7fcfe786e48c0a31ef2.png" style="width: 70%" /></br>
App.vue 主要修改组件的 template，如下图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/5be1dfb77701e071ef7829237396d481.png" style="width: 70%" /></br>
>? 由于篇幅有限，这里仅节选部分关键代码，完整代码可 [单击此处](https://cos-code-demo-1253960454.cos.ap-shanghai.myqcloud.com/vue-spa.zip) 下载。
>
5. 修改好代码后，执行如下命令，进行本地预览。
```
npm run serve
```
6. 调试并预览检查无误后，执行如下命令，打包生产环境代码。
```
npm run build
```
此时，将会在项目根目录下生成 dist 目录。至此，Vue 的程序代码已经准备完毕。


### 使用 React 快速搭建一个单页应用

1. 执行如下命令，安装 create-react-app：
```
npm install -g create-react-app
```
2. 使用 create-react-app 快速生成一个 react 项目，可参考 [官方文档](https://create-react-app.dev/docs/getting-started)。
3. 执行如下命令，在项目根目录下安装 react-router-dom：
```
npm install react-router-dom -S
```
4. 修改项目里的 App.js 文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c35e3011b1c4f083782bcc11834673f4.png" style="width: 70%" /></br>
>? 由于篇幅有限，这里仅节选部分关键代码，完整代码可 [单击此处](https://cos-code-demo-1253960454.cos.ap-shanghai.myqcloud.com/react-spa.zip) 下载。
>
5. 修改好代码后，执行如下命令，进行本地预览。
```
npm run start
```
6. 调试并预览检查无误后，执行如下命令，打包生产环境代码。
```
npm run build
```
此时将会在项目根目录下生成 build 目录。至此，React 的程序代码已经准备完毕。


<span id="configuration"></span>
## 开启存储桶静态网站配置

1. 进入创建好的存储桶详情页面，并在左侧导航栏中，单击**基础配置** > **静态网站**。
2. 在静态网站管理页面，参考下图，进行配置。操作详情请参见 [设置静态网站](https://cloud.tencent.com/document/product/436/14984)。
![](https://qcloudimg.tencent-cloud.cn/raw/1643fe5b1aa0e9b4dec08579ff38a160.png)


## 部署至 COS

1. 找到之前已经配置了静态网站的存储桶，进入文件列表页面。
2. 将编译目录（Vue 默认为 dist 目录，react 默认为 build 目录）下的所有文件上传至存储桶的根目录下。操作详情请参见 [上传对象](https://cloud.tencent.com/document/product/436/13321)。
![](https://qcloudimg.tencent-cloud.cn/raw/e21c7145a09aaf03125139aaf56e1a0a.png)
3. 访问存储桶的静态网站域名（如下图中的访问节点）。
![](https://qcloudimg.tencent-cloud.cn/raw/5cc44a50b5e3cfd34223242915279351.png)
即可看到已经部署完成的应用主页，这里以 Vue 应用举例。
![](https://qcloudimg.tencent-cloud.cn/raw/e4be083f712287f399051d84ceea866c.png)
4. 尝试切换路由（Home、Foo、Bar），并刷新页面，验证是否符合预期（即在路由下刷新不会出现404报错）。

## 常见问题

### 我不想使用静态网站的默认域名怎么办？可以使用我自己的域名吗？

除了上面使用的默认静态网站域名，COS 还提供了默认 CDN 加速域名、自定义 CDN 加速域名、自定义源站域名等其他选择。

具体可参考 [域名管理概述](https://cloud.tencent.com/document/product/436/18424#.E7.9B.B8.E5.85.B3.E6.93.8D.E4.BD.9C) 文档进行配置，配置成功后即可使用自己想要的域名来访问应用。


### 部署好应用之后，切换路由能成功渲染，但页面一刷新就出现404报错，是什么原因？

原因可能是配置静态网站的时候，缺失配置或错误配置了**错误文档**导致，请再次回顾本文开头提供的标准配置截图，可以看到错误文档和索引文档均配置为 `index.html` 。

由于单页应用的特性，我们需要保证在任何情况下都要成功访问到应用入口（一般为`index.html`），这样才能触发后续路由的一系列内部逻辑。


### 切换路由之后，页面能正常显示，但 HTTP 状态码依然为404，怎样才能正常返回200？

这里原因是配置静态网站的时候，缺少了配置**错误文档响应码**导致，可参考开头的配置截图，将其配置为200即可解决。

### 配置了错误文档之后，访问错误的路径还需要展示404的功能，应该如何处理？

这里推荐在前端代码里实现404逻辑，在路由配置最底部设置一个底层的匹配规则，当前面所有规则都匹配失败的时候则渲染一个404组件，组件内容可根据自行需求来设计实现。具体可参考本文提供的代码 demo 里的路由配置的最后一个配置。


### 访问页面出现 403 Access Denied 报错是什么原因？

原因可能是存储桶的权限设置了**私有读写**，可以修改为**公有读私有写**解决。

另外，如果使用 CDN 加速域名访问**私有读写**的存储桶，还需注意开启**回源鉴权**配置，这样才能授权 CDN 服务正常访问到 COS 下的资源。

