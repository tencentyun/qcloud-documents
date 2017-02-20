
通过WeCOS，小程序项目中的图片资源会自动上传到 COS 上，且 WeCOS 自动替换代码中图片资源地址的引用为线上地址，移除项目目录中的图片资源，从而减小小程序包大小，解决包大小超过限制的烦恼。 


## 为什么需要 WeCOS

    
```
为了提升小程序体验流畅度，编译后的代码包大小需小于 1MB ，大于 1MB 的代码包将上传失败。
```

在开发小程序的过程中，图片资源通常会占用较大空间，很容易超出官方的 1MB 限制。这时候，使用 WeCOS，可以让你在开发过程中不需要关心图片资源占用多少空间的问题，专注于自己的逻辑开发。



## 准备工作
* 进入 [腾讯云官网](https://www.qcloud.com)，注册帐号
* 登录 [云对象存储服务（COS）控制台](https://console.qcloud.com/cos4)，开通COS服务，创建Bucket
* 下载 [WeCOS 工具](https://github.com/tencentyun/wecos)
* 安装 [Node.js](https://nodejs.org) 环境



## 安装

```js
npm install -g wecos
```



## 基本配置
在你的小程序目录同级下创建 `wecos.config.json` 文件

`wecos.config.json` 配置项例子：
```json
{
  "appDir": "./app",
  "cos": {
    "appid": "1234567890",
    "bucketname": "wxapp",
    "folder": "/", //资源存放在bucket的哪个目录下
    "region": "wx", //创建bucket时选择的地域简称
    "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "secret_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }
}
```

| 配置项 | 类型 | 说明 |
|:-- |:-- |:-- |
| appDir | **[String]** | 默认 `./app`，小程序项目目录 |
| cos | **[Object]** | 必填，填写需要上传到COS对应的配置信息，部分信息可在[COS控制台](https://console.qcloud.com/cos4/secret)查看 |


## 使用

在配置文件同级目录下命令行执行 
```js 
wecos
```
注意，执行前需要在该目录下创建 `wecos.config.json` 文件


## 高级配置

| 配置项 | 类型 | 说明 |
|:-- |:-- |:-- |
| backupDir | **[String]** | 默认 `./wecos_backup`，备份目录 |
| uploadFileSuffix | **[Array]** | 默认 `[".jpg", ".png", ".gif"]`，图片上传后缀名配置 |
| uploadFileBlackList | **[Array]** | 默认 `[]`，图片资源黑名单 |
| replaceHost | **[String]** | 默认 `''`，把指定域名替换成 targetHost |
| targetHost | **[String]** | 默认 `''`，使用自定义域名 |
| compress | **[Boolean]** | 默认 `false`，是否开启压缩图片 |
| watch | **[Boolean]** | 默认 `true`，是否开启实时监听项目目录 |

</br>
#### 设置备份目录

由于 WeCOS 在运行时会自动将项目下的图片上传至 COS 然后删除，这样可能存在丢失源文件的风险，因此我们也提供了备份源文件的功能，每上传一张图片，会在项目同级的某个目录下备份该文件

为了方便使用，可以通过以下配置来修改备份目录名，如果不需要使用该功能，可以设置为空值
```json
  "backupDir": "./wecos_backup"
```

#### 设置图片后缀

有些时候，我们需要限制上传图片的格式，例如只允许 `jpg` 格式，可以通过 WeCOS 提供的图片后缀配置项来定义

WeCOS默认支持 `jpg,png,gif` 三种格式，假如你还需要添加其他格式，例如 webp，可以在该配置项中添加

```json
  "uploadFileSuffix": [".jpg",".png",".gif",".webp"]
```

#### 设置图片黑名单

开发过程中，某些特定的图片我们不希望被上传，可以通过 WeCOS 的黑名单配置来解决这个问题，配置后上传程序会自动忽略掉这些图片

黑名单配置支持目录或具体到文件名的写法
```json
  "uploadFileBlackList": ["./images/logo.png","./logo/"]
```

#### 自定义域名

如果希望 COS 文件链接使用自定义的域名，可以配置 targetHost 代替默认域名，可以省略：`http://`：

```json
  "targetHost": "http://example.com"
```

如果代码中的图片链接想换一个域名，可以配置 replaceHost targetHost 来实现。

```json
  "replaceHost": "http://wx-12345678.myqcloud.com",
  "targetHost": "https://example.com"
```

#### 开启图片压缩

图片上传到 COS 之后虽然大大减轻了程序包的大小，但如果图片自身体积过大，访问速度也会影响到用户体验

令人激动的是，WeCOS在图片上云的基础功能上还额外提供了基于[腾讯云万象优图](https://www.qcloud.com/product/ci)的图片压缩功能。

首先，你需要在[万象优图控制台](https://console.qcloud.com/ci)创建 COS 的同名bucket

然后，开启该选项，资源将被压缩后上传（注：如果图片已经小到一定程度，压缩后大小可能不会变化）

```json
  "compress": true
```

#### 设置实时监听

WeCOS 默认实时监听项目目录变化，自动处理图片资源，在开发过程中，如果觉得实时监听不方便，或者只需要一次性处理就停止，可以修改该配置，程序将只会执行一次后退出
```json
  "watch": false
```


## 高级用法
如果你除了上述使用命令行来执行的方式外，还想使用其他的方式，例如定制化成自己的模块，我们也提供了直接引用的使用方法满足你个性化的需求

```js
var wecos = require('wecos');

/**
* option 可选 [String|Object]
* 传入 String，指定配置文件路径
* 传入 Object，指定配置项
*/
wecos([option]);

//指定配置文件路径
wecos('./wecos-config.js');

//指定配置项
wecos({
	appDir: './xxx',
	cos: {
		...
	}
});

```


## 相关

* [WeCOS-UGC-DEMO](https://github.com/tencentyun/wecos-ugc-upload-demo)——小程序用户资源上传COS DEMO

* [COS-AUTH](https://github.com/tencentyun/cos-auth)——COS鉴权服务器DEMO







