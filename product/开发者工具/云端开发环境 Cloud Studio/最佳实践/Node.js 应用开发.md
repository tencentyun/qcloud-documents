Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行环境。Node.js 使用了一个事件驱动、非阻塞式 I/O 的模型，使其轻量又高效。Node.js 的包管理器 npm，是全球最大的开源库生态系统。

## JavaScript 程序开发
1. 新建一个 Node.js 预置环境工作空间。
![](https://qcloudimg.tencent-cloud.cn/raw/c15037bd8db8848b20af9c4f8b65cf8b.png)
2. 新建文件，编写 JavaScript 代码。
![](https://qcloudimg.tencent-cloud.cn/raw/d21f0ac7d0209a993845cce62b89e219.png)
3. 运行和调试代码。
![](https://qcloudimg.tencent-cloud.cn/raw/08bddaac85d74a1aba6da99554da8c67.png)
![](https://qcloudimg.tencent-cloud.cn/raw/b379a1b1b3ef3940aead71fb1d361cc0.png)

## 前端框架应用开发
### 以一个 Vue 的 demo 为例
1. 新建一个 Vue.js 预置环境工作空间, 该模板已默认安装 Vue 脚手架。
2. 在终端，通过 Vue CLI 初始化项目 vue create my-project。
![](https://qcloudimg.tencent-cloud.cn/raw/7d6e0c59361b6340e25f4428cc95e0a3.png)
3. 使用 yarn run serve 启动项目。
![](https://qcloudimg.tencent-cloud.cn/raw/01c0f28d160a0e2a52aa79f2737797ad.png)
4.	单击右下角弹窗打开内置预览或打开浏览器，或者在端口的就可以实时预览前端啦。
![](https://qcloudimg.tencent-cloud.cn/raw/381a9a4cffb1fb8d9f9aaec7239a663d.png)

### 解决 Vue 项目中的 “Invalid Host header”
在根目录下创建文件 vue.config.js，然后填入如下内容，重新启动项目即可。
![](https://qcloudimg.tencent-cloud.cn/raw/01f0a80f87d9784b84f7de9c50383b70.png)
![](https://qcloudimg.tencent-cloud.cn/raw/52ecbe470f0241cb16844b7b281e1808.png)
