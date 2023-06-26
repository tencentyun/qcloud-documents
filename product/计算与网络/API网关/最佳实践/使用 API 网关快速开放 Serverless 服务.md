## 操作场景
Serverless 是近年来比较流行的架构，通过 Serverless 函数计算平台，您无需购买和管理服务器，只需要关注业务的核心逻辑，就能够便捷地运行代码。在 Serverless 模式下，使用 API 网关可以对外开放服务，并能实现安全防护、流量控制、日志监控、上架云市场、自动生成 SDK 和文档等高级功能。

腾讯云 API 网关与腾讯云云函数 SCF 高度整合，本文展示了以 API 网关为入口，通过 [云函数 SCF](https://cloud.tencent.com/document/product/583) 实现动态接口、 [对象存储 COS](https://cloud.tencent.com/document/product/436) 存储静态资源，快速搭建 Web 站点。

您可以参考这种方式，在云上使用 API 网关快速开放 Serverless 服务，以体验到 Serverless 的魅力。

## 前提条件

在开始搭建网站前，您需要前往 [API 网关官方仓库](https://github.com/TencentCloud/apigateway-demo/tree/master/hello-website) 下载网站源码。使用其中一个文件夹 `hello-website` 作为本示例的项目源码，源码包含一个骨架的 HTML 文件，以及常见的图片、CSS 文件、JS 文件等静态资源。

下载后文件的目录结构如下所示：
```
├── client                                      // 项目根目录
│   ├── static                                  // 静态资源
│   │   ├── background.jpg                      // 网站背景图片
│   │   ├── favicon.ico                         // 网站 icon
│   │   ├── index.js                            // 脚本文件
│   │   ├── style.css                           // 样式文件
│   ├── index.html                              // 网站首页
```

## 操作步骤

### 步骤一：创建 COS 存储桶，存储静态资源

1. 登录 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos/bucket) ，按下图填写信息，创建一个存储桶（参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档）。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7e53b315d6df8c540c5e07f3e13fdec5.png" width=600/>
2. 在存储桶中，上传网站源码（参考 [上传对象](https://cloud.tencent.com/document/product/436/13321)），目录结构与原文件保持一致。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1dacddde2a6dba9e773d06305f9b4db3.png" width=900/>



### 步骤二：创建云函数，实现数据接口

1. 登录 [云函数 SCF 控制台](https://console.cloud.tencent.com/scf/list) ，用 hello world 模板创建云函数（参考 [创建及更新函数](https://cloud.tencent.com/document/product/583/19806)）。
<img src="https://main.qcloudimg.com/raw/70813ce761854292233b92fc70873be3.png" width=600/>

2. 修改云函数代码，返回简单的 JSON 数据。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c7d9dc804539d2cf5de88682b7cd4c13.png" width=900/>

用到的云函数代码如下：
```JavaScript
'use strict';
exports.main_handler = async(event, context, callback) => {
	return {
		data: 'hello world' // 此处可替换为您喜欢的任意内容
	}
};
```

### 步骤三：创建 API 网关服务

1. 登录 [ API 网关控制台](https://console.cloud.tencent.com/apigateway) ，按下图填写信息，创建一个API 网关服务（参考 [创建服务](https://cloud.tencent.com/document/product/628/11787)）。
2. 创建成功后，单击服务列表里的服务名称，进入服务详情页。
3. 在服务详情页单击**管理 API**，进入 API 管理页。接下来，您需要在 API 管理页创建三个API，分别指向对应的后端资源。

### 步骤四：配置三个 API

1. 单击**新建**按钮，创建第一个 API（参考 [创建通用 API](https://cloud.tencent.com/document/product/628/11797)），第一个 API 的作用是获取网站的 HTML 页面。前端路径配置为“/”：
后端路径指向 COS 存储桶的“index.html”。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5a0375511c8719b1adfd125df43fea08.png" width=900/>

2. 再次单击**新建**按钮，创建第二个 API，第二个 API 的作用是获取静态资源。前端路径配置为“^~/static”：
<img src="https://qcloudimg.tencent-cloud.cn/raw/483df176d74379a54af348e4ecccbfcb.png" width=900/>

	后端路径指向COS存储桶的“/static”路径：
<img src="https://qcloudimg.tencent-cloud.cn/raw/77bbb5d07c320a786ab1a1b6c1d19cab.png" width=900/>

3. 再次单击**新建**按钮，创建第三个 API，第三个 API 的作用是获取动态数据。前端路径配置为“/fetchData”：
<img src="https://qcloudimg.tencent-cloud.cn/raw/76d217e5b700bc131f10791602982f67.png" width=900/>

	后端路径指向上面第二步中创建的云函数：
<img src="https://qcloudimg.tencent-cloud.cn/raw/94edf09d75d1adfddd4a1429a3671b2e.png" width=900/>

### 步骤五：发布服务并访问
1. 在服务详情页中，单击页面右上角的**发布服务**，将服务发布至“发布”环境。
<img src="https://qcloudimg.tencent-cloud.cn/raw/03fbaeafb99b6b5471f6d7058560cfa7.png"  width=900/>
2. 在服务详情页的**基础配置** Tab 页中，查看“公网访问地址”，复制该地址（可直接单击复制按钮）。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d9ea331f180b729f239408c34a4f4a0a.png" width=900/>
3. 将“公网访问地址”粘贴至您的浏览器的地址栏，单击回车键，即可访问部署好的网站，效果如下。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e71766b7cbe7ac8ca5604aa2162e89e1.png" width=700/>
4. 单击**获取数据**，发起 XHR 调用，网站会通过云函数返回预先定义的 JSON 数据串，效果如下。
<img src="https://qcloudimg.tencent-cloud.cn/raw/66b86cf2b6d6bd75cefbe60f44633ba7.png" width=700/>

## 说明
除了通过 API 网关提供的默认域名来访问搭建的站点之外，您可以将已有的自定义域名绑定到服务上。绑定之后，便可通过自定义域名来访问站点。详情可查看 [自定义域名配置](https://cloud.tencent.com/document/product/628/11791) 相关文档。
