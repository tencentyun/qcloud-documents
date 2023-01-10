## 简介
[Ghost](https://ghost.org/docs) 是一个基于 Node.js 快速搭建博客类网站的框架，开发者可通过 Ghost 官方 cli 工具一键生成自己的个人网站，并支持部署到云服务器和 Docker 上。

作为一个博客类网站，上传附件是必不可少的功能，Ghost 默认会将附件存储在本地，本文将介绍如何通过插件将附件保存在 [腾讯云对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上，将论坛附件保存在 COS 上有以下好处：
- 附件将拥有更高的可靠性。
- 您的服务器无需为论坛附件准备额外的存储空间。
- 用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。
- 可配合 [腾讯云内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/product/cdn) 进一步提升论坛用户查看图片附件的速度。

## 准备工作

### 搭建 Ghost 网站

1. 安装 [Node.js](https://nodejs.org/en/download/) 环境。
2. 安装 ghost-cli。
```js
npm install ghost-cli@latest -g
```
3. 创建一个项目，在该项目的根目录下执行命令：
```js
ghost install local
```
创建成功后的项目结构如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/76e74eff7779379f2e40c5c9220453fc.jpg)
4. 打开浏览器，进入 localhost:2368，出现注册页面，注册后进入管理后台。
![](https://qcloudimg.tencent-cloud.cn/raw/16c412b34d8d9eda9525d12b7e34f5cf.jpg)


### 创建 COS 存储桶

1. 在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 创建一个访问权限为**公有读私有写**的存储桶，操作指引可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 单击**安全管理 > 跨域访问 CORS 设置**，添加一行跨域设置，为方便调试可使用以下配置，操作指引可参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318)。
![](https://qcloudimg.tencent-cloud.cn/raw/3fb3a428ec1b1d88fb8aa33f490e94a8.png)



## 将 Ghost 关联到 COS存储桶

>!建议使用子账号密钥，授权遵循 [最小权限指引](https://cloud.tencent.com/document/product/436/38618)，降低使用风险。子账号密钥获取可参考 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。


1. 修改 Ghost 项目根目录下的 config.development.json 配置文件，添加如下配置：
```json
  "storage": {
    "active": "ghost-cos-store",
    "ghost-cos-store": {      
      "BasePath": "ghost/", // 可修改为自己的目录名，不填写则默认根目录 
      "SecretId": "AKID*************",
      "SecretKey": "***************",
      "Bucket": "xxx-125********", 
      "Region": "**-*******"
    }
  }
```
参数说明如下：
<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
   <tr>
      <td>BasePath</td>
      <td>文件所存储的 COS 路径，可自行修改，不填写则默认根目录</td>
   </tr>
   <tr>
      <td>SecretId</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取</td>
   </tr>
   <tr>
      <td>SecretKey</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取。</td>
   </tr>
   <tr>
      <td>Bucket</td>
      <td>创建存储桶时自定义的名称，例如 examplebucket-1250000000。</td>
   </tr>
   <tr>
      <td>Region</td>
      <td>创建存储桶时所选择的地域。</td>
   </tr>
</table>
2. 创建自定义存储目录，在项目根目录下执行：
```js
mkdir -p content/adapters/storage
```
3. 安装腾讯云官方提供的 [ghost-cos-store](https://github.com/tencentyun/ghost-cos-store) 插件。
   1. 通过 npm 安装。
```js
npm install ghost-cos-store
```
   2. 在 storage 目录下创建 ghost-cos-store.js 文件，内容如下：
```js
//  content/adapters/storage/ghost-cos-store.js
module.exports = require('ghost-cos-store');
```
   3. 通过 git clone 安装。
```js
cd content/adapters/storage
git clone https://github.com/tencentyun/ghost-cos-store.git
cd ghost-cos-store  
npm i
```
   4. 安装完成后，需要重启 Ghost。
```js
ghost restart
```



## 发文并进行上传测试

1. 进入 Ghost 管理后台，单击发表一篇文章。
![](https://qcloudimg.tencent-cloud.cn/raw/27dc54b218009f64bd319707700dba71.jpg)
2. 单击上传图片，在浏览器抓包可以看到 upload 请求成功，并返回了图片对应的 COS 链接。
![](https://qcloudimg.tencent-cloud.cn/raw/a875407bd72738c5d2ddbfb4d41acd0a.jpg)




## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！

