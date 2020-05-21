## 操作场景
Serverless 是近年来比较流行的架构，通过 Serverless 函数计算平台，您无需购买和管理服务器，只需要关注业务的核心逻辑，就能够便捷地运行代码。在 Serverless 模式下，使用 API 网关可以对外开放服务，并能实现安全防护、流量控制、日志监控、上架云市场、自动生成 SDK 和文档等高级功能。

腾讯云 API 网关与腾讯云云函数 SCF 高度整合，本文展示了以 API 网关为入口，通过 [云函数 SCF](https://cloud.tencent.com/document/product/583) 实现动态接口、 [对象存储 COS](https://cloud.tencent.com/document/product/628/11787) 存储静态资源，快速搭建 Web 站点。

您可以参考这种方式，在云上使用 API 网关快速开放 Serverless 服务，以体验到 Serverless 的魅力。

## 前提条件

在开始搭建网站前，您需要前往 [API 网关官方仓库](https://github.com/TencentCloud/apigateway-demo/tree/master/hello-website) 下载网站源码。源码包含一个骨架的 HTML 文件，以及常见的图片、CSS 文件、JS 文件等静态资源。

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

1. 登录 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos5/bucket) ，按下图填写信息，创建一个存储桶（参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档）。
![](https://main.qcloudimg.com/raw/1c820c445a74ebd57c97ea7ebfdcb55d.png)
2. 在存储桶中，上传网站源码（参考 [上传对象](https://cloud.tencent.com/document/product/436/13321)），目录结构与原文件保持一致。
![](https://main.qcloudimg.com/raw/f86586fffc201da9169ce5f055555d06.png)

### 步骤二：创建云函数，实现数据接口

1. 登录 [云函数 SCF 控制台](https://console.cloud.tencent.com/scf/list) 控制台，用 hello world 模板创建云函数（参考 [创建及更新函数](https://cloud.tencent.com/document/product/583/19806)）。
![](https://main.qcloudimg.com/raw/70813ce761854292233b92fc70873be3.png)
2. 修改云函数代码，返回简单的 JSON 数据。
![](https://main.qcloudimg.com/raw/bda30bde9cc024b9b2b6fe2ef5ee3660.png)

用到的云函数代码如下：
```JavaScript
'use strict';
exports.main_handler = async(event, context, callback) => {
	return {
		data: 'hello world' // hello world 可替换为您喜欢的任意内容
	}
};
```

### 步骤三：创建 API 网关服务

1. 登录 [ API 网关控制台](https://console.cloud.tencent.com/apigateway) ，按下图填写信息，创建一个API 网关服务（参考 [创建服务](https://cloud.tencent.com/document/product/628/11787)）。
![](https://main.qcloudimg.com/raw/0cf49ba223cc661cf6f6dac75253afb7.png)
2. 创建成功后，单击服务列表里的服务名称，进入服务详情页。
3. 在服务详情页单击【管理 API】，进入 API 管理页。接下来，您需要在 API 管理页创建三个API，分别指向对应的后端资源。

### 步骤四：配置三个 API

1. 单击【新建】按钮，创建第一个 API（参考 [创建通用 API](https://cloud.tencent.com/document/product/628/11797)），第一个 API 的作用是获取网站的 HTML 页面。前端路径配置为“/”：
![](https://main.qcloudimg.com/raw/d797a68003a6e01277fd36f2f0cbab28.png)
后端配置指向 COS 存储桶的“index.html”。
![](https://main.qcloudimg.com/raw/601fa75d0c7bcc6898cdd711ad2c403b.png)
2. 再次单击【新建】按钮，创建第二个 API，第二个 API 的作用是获取静态资源。前端路径配置为“^~/static”：
![](https://main.qcloudimg.com/raw/b3911b2ffd827765118b75c874395046.png)
后端配置指向COS存储桶的“/static”路径：
![](https://main.qcloudimg.com/raw/6ecc5aa906c3379e648999b591b7e5fc.png)
3. 再次单击【新建】按钮，创建第三个 API，第三个 API 的作用是获取动态数据。前端路径配置为“/fetchData”：
![](https://main.qcloudimg.com/raw/f8d2dc6e0acf2a640a3716b6598d8cfa.png)
后端配置指向对应的云函数：
![](https://main.qcloudimg.com/raw/eb5bab8b734149e5f54e49dfd8571191.png)

### 步骤五：发布服务并访问
1. 在服务详情页的【服务信息】Tab 页中，单击页面右上角的【发布】，将服务发布至“发布”环境。
![](https://main.qcloudimg.com/raw/d18ae93f6a8e24aab4c59048d3b44d05.png)
2. 在服务详情页的【服务信息】Tab 页中，查看“公网访问地址”，单击复制图标将地址复制到剪切板中。
![](https://main.qcloudimg.com/raw/5ea3316d9acaed82104cacb9ea2feaca.png)
3. 将“公网访问地址”粘贴至浏览器的地址栏，单击回车键，即可访问部署好的网站。
![](https://main.qcloudimg.com/raw/ffffd8d4c16b080003a103473ae14b25.png)
4. 单击【获取数据】，发起 XHR 调用，网站会通过云函数返回预先定义的 JSON 数据串。


## 说明
除了通过 API 网关提供的默认域名来访问搭建的站点之外，您可以将已有的自定义域名绑定到服务上。绑定之后，便可通过自定义域名来访问站点。详情可查看 [自定义域名配置](https://cloud.tencent.com/document/product/628/11791) 相关文档。
