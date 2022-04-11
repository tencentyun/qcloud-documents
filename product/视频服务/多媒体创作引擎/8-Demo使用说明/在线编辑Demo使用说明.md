## 使用须知

### Demo 功能介绍

本 Demo 以在云点播上传两个视频，以转场拼接并覆盖一张水印图片为例，介绍 Web Iframe 方式集成视频剪辑能力的方法。

### 架构和流程

业务架构图如下，虚线表示媒体创作引擎内部通信，实线表示与您的业务通信。

<img src="https://qcloudimg.tencent-cloud.cn/raw/83a7f4235f00cf2b2a85fe56989d2578.png" width="960">

整个业务系统涉及五部分，包括**多媒体创作引擎前端**、**业务前端**、**业务后端**、**多媒体创作引擎后端** 以及 **素材存储**。其中**多媒体创作引擎前端**与**业务前端**使用 Javascript API 进行通信，**多媒体创作引擎后端**与**业务后端**以云 API 进行通信。

具体业务流程：
1. 将待编辑的视频、音频、图片等媒体上传到腾讯云 VOD，前端拉取到待剪辑的音频、图片 。
2. 前端带上待剪辑的媒体 ID 创建剪辑项目，在业务前端将可以看到剪辑器界面，以及准备好的素材。
3. 在剪辑器中剪辑预览。
4. 发起云端视频合成，生成视频。
5. 轮询任务结果，成功后，在 VOD 上查看结果。

<img src="https://qcloudimg.tencent-cloud.cn/raw/b1322033d1d03c332f28cedf5b0fd93c.png" width="960">


### 案例中所用到的素材

- [视频1](https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/c20be6785285890809599844312/f0.mp4?download_name=视频1.mp4)：
<video width="540" controls>
  <source src="https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/c20be6785285890809599844312/f0.mp4" type="video/mp4">
  对不起，您的浏览器暂时不支持视频预览。
</video>
- [视频2](https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/f69747475285890810007930755/f0.mp4?download_name=视频2.mp4)：
<video width="540" controls>
  <source src="https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/f69747475285890810007930755/f0.mp4" type="video/mp4">
  对不起，您的浏览器暂时不支持视频预览。
</video>

- [水印图片](https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/91db8006387702291996843937/Pav7PiKcp3AA.png?download_name=水印图片.png)：
<img src="https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/91db8006387702291996843937/Pav7PiKcp3AA.png" width="540">


### 案例最终合成的视频成片
成片效果如下：
<video width="540" controls>
  <source src="https://1810000000.vod2.myqcloud.com/8d388654vodtranscq1810000000/d5f6138c387702292141915433/v.f100030.mp4" type="video/mp4">
  对不起，您的浏览器暂时不支持视频预览。
</video>



## 快速部署 Web Iframe 剪辑 Demo

### 步骤1：开通腾讯云 VOD 服务
请参见 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 开通云点播服务，并创建一个 [子应用](https://cloud.tencent.com/document/product/266/14574)。

>?若已开通云点播服务，请忽略此步骤。

### 步骤2：创建多媒体创作引擎平台

请参见 [管理端使用指南 - 创建开发型平台](https://cloud.tencent.com/document/product/1156/64111) 创建平台，并拿到平台 ID。

>!
>- 创建平台时，必须指定存储为上一步创建的云点播子应用。
>- 如果您后续使用到 **视频编辑模板** 等功能，请 [创建标准型平台](https://cloud.tencent.com/document/product/1156/64110)。


### 步骤3：获取 API 密钥
请求云 API 需要使用到开发者的 API 密钥（ SecretId 和 SecretKey）。如果还未创建过密钥，请参见 [创建密钥文档](https://cloud.tencent.com/document/product/598/40488#.E5.88.9B.E5.BB.BA.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 生成新的 API 密钥；如果已创建过密钥，请参见 [查看密钥文档](https://cloud.tencent.com/document/product/598/40488#.E6.9F.A5.E7.9C.8B.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 获取 API 密钥。

### 步骤4：准备视频
将上文提到的两个示例视频和一个示例图片下载到本地，上传到云点播。分以下几步操作：

1. 先登录 [云点播控制台](https://console.cloud.tencent.com/vod/overview)，在云点播控制台创建视频分类，选择 **上传存储设置**，再选择 **分类管理**，**添加分类**。输入分类名称，创建完成后，得到分类 ID。如图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/4e5d7cf84d2791abf3c541d36210b6de.png" width="960">
2. 上传视频。将示例视频上传到云点播，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/fc6656958d0342ff60564e044aaf3d00.png" width="960">
3. 上传图片。将示例图片上传到云点播，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/caf66537d817ce90e1e75bd1eed4b1d2.png" width="960">

>!
>- 上传视频及图片时，请注意一定要上传到创建多媒体创作引擎平台所使用的云点播子应用下。同时上传视频及图片时请选择**步骤1**创建的分类名称。
>- 这里上传视频及图片指定分类，主要是为了 Demo 能在前端拉取到待剪辑的媒体，实际应用中是非必要步骤。


### 步骤5：部署 Demo 服务[](id:p4)
1. 下载 [**项目源码**](https://vs-cdn.tencent-cloud.com/resources/cme-node-demo-feature-iframe-2.0.zip)。
2. **配置文件**
配置文件在 config.js 上，按如下方式进行配置：
```javascript
const config = {
    port: 9090,  // demo 端口号，开发者可以替换为自己的端口号
    secretId: "You SecretId",  // 配置准备工作中 步骤3 获取到的 SecretId 
    secretKey: "You SecretKey",  // 配置准备工作中 步骤3 获取到的 SecretKey
    vodSubAppId: 140****274 ,  // 配置创建多媒体创作引擎平台时使用的云点播子应用 Id
    platform: "14****274 ",  // 配置准备工作中 步骤2 创建的平台 Id 
    vodFileClassId: 8****1  // 云点播的媒资分类Id
}
```
>!这里的配置文件仅用于 Demo 展示，开发者可以根据自身业务需求调整和进行管理。
3. **搭建环境**
<dx-tabs>
::: Linux 下安装 Node.js
1. Node 官网下载已经编译好的版本，直接解压安装：
```text
wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.xz
tar xf node-v10.9.0-linux-x64.tar.xz
```
2. 配置软链接或环境变量(这里根据自己的解压路径设置)：
```text
ln -s /usr/local/nodejs/bin/npm /usr/local/bin/
ln -s /usr/local/nodejs/bin/node /usr/local/bin/
```
3. 执行 node、npm 命令查看版本，如果出现版本号，说明已经安装成功：
```text
node -v
npm -v
```
:::
::: Windows 下安装 Node.js 
1. [下载](https://nodejs.org/en/download/ ) 您系统对应的 Node.js 版本。
2. 选择安装目录进行执行安装。
3. 执行 node 、npm 命令查看版本，如果出现版本号，说明已经安装成功。
```text
node -v 
npm -v
```
:::
</dx-tabs>
4. **部署服务**
	1. 官网 [下载 Demo](https://vs-cdn.tencent-cloud.com/resources/cme-node-demo-feature-iframe-2.0.zip)。
	2. 运行命令 npm install 自动安装依赖包 。
	3. 运行命令 npm start，启动服务。
	4. 访问地址 `http://localhost:9090`，即可进入 Demo 的登录页面（如配置了其它服务地址及端口，替换即可），可看到如下登录界面：
![](https://qcloudimg.tencent-cloud.cn/raw/5527e084ff1ea8f88e3c4db48c2f93d9.png)


### 步骤6：测试 Demo
#### 登录
输入任意账号和密码即可登录，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/9de21a8e7484cafee9bb3dd9e7567f91.png)

#### 编辑视频
在编辑页将待剪辑的视频拖到轨道，并在中间加上转场。同时设置上水印，如下图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b9b4d64da68dedce26cba6ef571c7827.png" width="960">

#### 导出视频
编辑完成后，点播导出按键，发起导出任务，如下图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/3cceaeda30e892435bdb3479f024cfa9.png" width="960">

#### 在云点播查看导出视频
登录云点播控制台，如果任务完成后，可以看到剪辑导出的视频：
<img src="https://qcloudimg.tencent-cloud.cn/raw/06a2df1eda92ee958facf8d51e3d481f.png" width="960">

## 系统设计说明[](id:design)
### 框架
本 Demo 基于 [node.js](https://nodejs.org/zh-cn/) 以及 [koa](https://github.com/koajs/koa) 框架进行开发（您也可以替换成您熟悉的编程语言与框架）。也可以使用腾讯云轻量应用服务器（Lighthouse）或无服务器云函数（SCF）快速部署，参见：
- Lighthouse：[搭建 Node.js 开发环境](https://cloud.tencent.com/document/product/1207/60266)。
- SCF：[快速部署 Koa 框架](https://cloud.tencent.com/document/product/583/59231)。

### Demo 后台实现解读

本教程中约定，后端暴露的接口形式如下：
- 后端服务的域名为 `http://localhost`。
- 以 HTTP GET 或者 POST 方式发起请求，通过 QueryString 或者 BODY 传递业务参数。
- 以 `localhost` 域的 Cookie `UserId` 传递用户 ID（暂时不考虑鉴权）。

#### 接口列表 
- **登录接口（Login）**[](id:Login)
本接口实现登录逻辑，接收来自前端传过来的用户 ID，登录成功后设置上名称为 UserId，值为登录用户 Id 的 Cookie。
>?目前 Demo 实现的登录逻辑并未做密码等安全验证，业务实现过程中一定要按业务实际的登录方式进行用户权限验证。

- **获取媒体接口（DescribeMedias）** [](id:DescribeMedias)
本接口获取在准备工作中上传到云点播的媒体，供页面端选择进行编辑。该接口有使用到云点播的 [搜索媒体](https://cloud.tencent.com/document/product/266/31813) 接口。
>?业务实现时，前端选择待编辑的媒体由业务自行决定，该接口是非必须的，也可以由业务后台直接指定待剪辑的媒体列表。

- **创建项目接口（CreateProject）** [](id:CreateProject)
本接口实现获取从前端传过来的项目名称、待剪辑的媒体列表等参数。调用多媒体创作引擎的 [创建项目](https://cloud.tencent.com/document/product/1156/40350) 接口创建项目，同时将待剪辑的媒体调用多媒体创作引擎的 [在项目中导入媒体](https://cloud.tencent.com/document/product/1156/40352) 接口导入到项目中，返回前端项目 ID 及打开项目的签名。
>?本 Demo 将创建项目及导入媒体到项目操作在一个接口实现，业务可以选择先创建项目，再分次导入媒体到项目中。

- **导出视频接口（ExportVideo）** [](id:ExportVideo)
本接口实现调用多媒体创作引擎的 [导出视频编辑项目](https://cloud.tencent.com/document/product/1156/40353) 接口导出视频，获取到任务 ID。

- **查看导出结果接口（GetTaskInfo）** [](id:GetTaskInfo)
本接口实现调用多媒体创作引擎的 [获取任务详情](https://cloud.tencent.com/document/product/1156/40359) 接口获取任务状态，如果任务成功，则可获取到导出的视频 URL 及云点播 FileId。
>!因云创多媒体引擎暂时未提供导出任务回调的功能，发起导出任务后，依赖业务轮询任务状态来获取到最终的导出结果。

-  **获取项目列表接口（DescribeProjects）**[](id:DescribeProjects)
本接口实现调用多媒体创作引擎的 [获取项目列表](https://cloud.tencent.com/document/product/1156/40348) 接口获取到项目详情及打开剪辑项目的签名，方便实现用户登录后获取到历史创建的项目功能。

- **导入媒体到项目接口（ImportMediaToProject）** [](id:ImportMediaToProject)
本接口实现调用多媒体创作引擎的 [在项目中导入媒体](https://cloud.tencent.com/document/product/1156/40352) 接口，将云点播媒体导入到剪辑项目中。

- **申请上传签名接口（ApplyUploadSign）**[](id:ApplyUploadSign)
本接口实现生成到云点播上传媒体的签名，前端直接上传媒体到云点播中。用于在剪辑过程中上传新的媒体到项目中。


### Demo 前端实现解读

业务前端主要完成以下三部分工作：
- 实现用户交互。
- 调用后端接口完成操作。
- 调用 jssd，监听事件与云创 iframe 交互，重点参考 editor.ts 文件内 CMD 相关事件注册。
