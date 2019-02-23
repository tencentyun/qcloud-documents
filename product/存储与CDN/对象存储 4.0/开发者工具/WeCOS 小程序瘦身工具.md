## 功能说明
为了提升小程序体验流畅度，微信限制编译后的代码包大小需小于 1MB ，大于 1MB 的代码包将上传失败。实际上，在开发小程序的过程中，图片资源通常会占用较大空间，容易超出官方的 1MB 限制要求。

通过使用对象存储的 WeCOS 工具，小程序项目中的图片资源会自动上传到 COS 上，并且 WeCOS 可以自动替换代码中图片资源地址的引用为线上地址，移除项目目录中的图片资源，从而减小代码包大小。

下面将介绍使用 WeCOS 的相关准备工作和安装操作等配置。
## 准备工作
1. 进入 [腾讯云官网](https://cloud.tencent.com/)，注册腾讯云账户，指引请参考 [注册腾讯云](/doc/product/378/9603) 页面。
2. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos4)，开通对象存储服务，[创建存储桶](/doc/product/436/6232)。
3. 在 GitHub 中 [获取 WeCOS 工具](https://github.com/tencentyun/wecos) 。
4. 在 [Node.js 官网](https://nodejs.org/) 下载环境并安装。

## 开始安装
使用以下命令安装 WeCOS 工具：

```js
npm install -g wecos
```

## 基本配置
在您的小程序目录同级下创建 `wecos.config.json` 文件，文件配置示例如下：

```json
{
  "appDir": "./app",
  "cos": {
    "secret_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "bucket": "wxapp-1251902136",
    "region": "ap-guangzhou", 
    "folder": "/"
  }
}
```

region：创建 bucket 时选择的地域简称。
folder： 资源存放在 bucket 的哪个目录下。

### 配置项说明

| 配置项    | 类型           | 说明                                       |
| ------ | ------------ | ---------------------------------------- |
| appDir | String | 默认 `./app`，小程序项目目录                       |
| cos    | Object | 必填。COS 的存储桶、地域等配置信息，请查看 [存储桶概述](https://cloud.tencent.com/document/product/436/13312) 文档，密钥等信息请在 [云API密钥控制台](https://console.cloud.tencent.com/cos4/secret) 中获取查看 |


## 开始使用
在配置文件同级目录下执行以下使用命令：
```
wecos
```

>!执行使用命令前，需要在配置文件同级目录下创建 `wecos.config.json` 文件。

## 高级配置

| 配置项                 | 类型            | 说明                                      |
| ------------------- | ------------- | --------------------------------------- |
| backupDir           | String  | 默认 `./wecos_backup`，备份目录                |
| uploadFileSuffix    | Array  |  默认 `[".jpg", ".png", ".gif"]`，图片上传后缀名配置  |
| uploadFileBlackList |Array |  默认 `[]`，图片资源黑名单    |
| replaceHost         | String  |  默认 `''`，把指定域名替换成 targetHost   |
| targetHost          | String | 默认 `''`，使用自定义域名    |
| compress            | Boolean |  默认 `false`，是否开启压缩图片       |
| watch               | Boolean | 默认 `true`，是否开启实时监听项目目录   |

#### 设置备份目录
由于 WeCOS 在运行时会自动将项目下的图片上传至 COS 然后删除，这样可能存在丢失源文件的风险，我们提供了备份源文件的功能，每上传一张图片，会在项目同级的某个目录下备份该文件。您可通过以下配置来修改备份目录名，若不需要使用该功能，可以设置为空值：
```
  "backupDir": "./wecos_backup"
```
#### 设置图片后缀
当需要限制上传图片的格式（例如只允许 `jpg` 格式）时，可通过 WeCOS 提供的图片后缀配置项来定义。WeCOS 默认支持 jpg、png、gif 三种格式，若您还需要添加其他格式（例如 webp），可在该配置项中添加，示例如下：

```
  "uploadFileSuffix": [".jpg",".png",".gif",".webp"]
```

#### 设置图片黑名单
开发过程中，不希望上传某些特定的图片时，可通过 WeCOS 的黑名单配置来实现，配置后上传程序会自动忽略掉这些图片。黑名单配置支持目录或具体到文件名的写法。

```
  "uploadFileBlackList": ["./images/logo.png","./logo/"]
```

#### 自定义域名
当您希望 COS 文件链接使用您的自有域名时，可配置 targetHost 代替默认域名（配置时可省略`http://`）：

```
  "targetHost": "http://example.com"
```

想为代码中的图片链接替换域名时，可通过配置 replaceHost targetHost 来实现。

```
  "replaceHost": "http://wx-12345678.myqcloud.com",
  "targetHost": "https://example.com"
```

#### 开启图片压缩
图片上传到 COS 之后虽然大大减轻了程序包的大小，但如果图片自身体积过大导致访问延迟，也会影响到用户体验。
WeCOS 在图片上云的基础功能上还额外提供了基于 [腾讯云数据万象](https://cloud.tencent.com/product/ci) 的图片压缩功能。您在 [数据万象控制台](https://console.cloud.tencent.com/ci) 创建与 COS 同名的存储桶后，进入存储桶，在样式页面开启图片压缩功能后，资源将被压缩后上传。

```
  "compress": true
```

#### 设置实时监听
WeCOS 默认实时监听项目目录变化，自动处理图片资源。在开发过程中，若觉得实时监听不方便，或只需要一次性处理就停止，可以按照如下命令行修改该配置，程序将只执行一次后退出。

```
  "watch": false
```

## 高级用法
如上述使用方式无法满足您的需求，WeCOS 还提供了定制化模块的配置操作，通过直接引用的方式，满足您的个性化需求。配置示例如下：

```
var wecos = require('wecos');

// option 可选 (String|Object)
// 传入 String，指定配置文件路径
// 传入 Object，指定配置项
wecos([option]);

// 指定配置文件路径
wecos('./wecos-config.js');

// 指定配置项
wecos({
    appDir: './xxx',
    cos: {
        ...
    }
});
```

## 相关资源
- [WeCOS-UGC-DEMO](https://github.com/tencentyun/wecos-ugc-upload-demo) —— 小程序用户资源上传 COS DEMO
- [COS-AUTH](https://github.com/tencentyun/cos-auth) —— COS 鉴权服务器 DEMO
