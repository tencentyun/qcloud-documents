## 背景

为了保障视频内容安全，防止视频被非法下载和传播，对象存储（Cloud Object Storage，COS）数据处理提供了对 HLS 视频内容进行加密的功能，拥有相比于私有读文件更高的安全级别。加密后的视频，无法分发给无访问权限的用户观看。即使视频被下载到本地，视频本身也是被加密的，无法恶意二次分发，从而保障您的视频版权不受非法侵犯。

本方案基于 [HLS 加密](https://cloud.tencent.com/document/product/436/59289) 流程，搭建一套基础的密钥管理服务，同时结合 [腾讯云点播超级播放器](https://cloud.tencent.com/document/product/266/58772)，一步步教您如何播放已被 COS HLS 转码加密的视频文件。

## 实践步骤

#### 步骤1：加密视频

参考 [通过 HLS 加密防止视频泄露](https://cloud.tencent.com/document/product/436/59289) 流程，对 COS 存储桶下的视频文件进行加密。

#### 步骤2：搭建密钥服务

1. 进入 [密钥相关接口](https://console.cloud.tencent.com/api/explorer?Product=kms&Version=2019-01-18&Action=Decrypt&SignVersion=)，根据自己的开发语言生成对应的 KMS API 调用示例代码。
![](https://qcloudimg.tencent-cloud.cn/raw/913d0d387824bfde5dd9fb086700bfe2.png)
2. 下面以 Node.js 为例，基于示例代码，结合 Koa 搭建一个密钥服务，调用 KMS API 获取解密密钥。
```
const Koa = require('koa')
const cors = require('koa2-cors')
const app = new Koa()
const tencentcloud = require("tencentcloud-sdk-nodejs")

app.use(cors()) // 跨域配置
app.use(async (ctx) => {
  // 生成的m3u8文件中的URI请求会默认带上参数
  const { Ciphertext, KMSRegion } = ctx.query

  const KmsClient = tencentcloud.kms.v20190118.Client
  const clientConfig = {
    credential: {
      // 账号API密钥，可前往https://console.cloud.tencent.com/cam/capi获取
      secretId: "SecretId",
      secretKey: "SecretKey",
    },
    
    region: KMSRegion, // 所在园区，eg："ap-guangzhou"
    profile: {
      httpProfile: {
      	endpoint: "kms.tencentcloudapi.com",
      },
    },
  };

  // 创建KMS对象实例
  const client = new KmsClient(clientConfig);
  const params = {
  	"CiphertextBlob": Ciphertext,
  };
  
	try {
    // 发起请求，获取解密密钥
    const res = await client.Decrypt(params)
    
    // 取出密钥，base64解密后返回其二进制数据
    const plaintext = res.Plaintext
    const plainBuff = Buffer.from(plaintext, 'base64');
    ctx.body = plainBuff
  } catch (error) {
    console.log(error);
  }
  
})

// 监听8080端口
app.listen('8080', () => {
  console.log('127.0.0.1:8080');
})
```

#### 步骤3：实现 Web 端播放加密视频

1. 在页面中引入播放器样式文件与脚本文件：
```
<!--播放器样式文件-->
<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.min.css" rel="stylesheet"/>
<!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.v4.2.2.min.js 之前引入 hls.min.0.13.2m.js。-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/libs/hls.min.0.13.2m.js"></script>
<!--播放器脚本文件-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.v4.2.2.min.js"></script>
```
建议在正式使用播放器 SDK 时，自行部署以上相关静态资源，[单击下载播放器资源](https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/release.zip)。
部署解压后的文件夹，不能调整文件夹里面的目录，避免资源互相引用异常。
2. 设置播放器容器节点
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playsinline>
</video>
```
>?
> - 播放器容器必须为 `<video>` 标签。
> - 示例中的 `player-container-id` 为播放器容器的 ID，可自行设置。
> - 播放器容器区域的尺寸，建议通过 CSS 进行设置，通过 CSS 设置比属性设置更灵活，可以实现例如铺满全屏、容器自适应等效果。
> - 示例中的 `preload` 属性规定是否在页面加载后载入视频，通常为了更快的播放视频，会设置为 `auto`，其他可选值：`meta`（当页面加载后只载入元数据），`none`（当页面加载后不载入视频），移动端由于系统限制不会自动加载视频。
> - `playsinline` 和 `webkit-playsinline` 这几个属性是为了在标准移动端浏览器不劫持视频播放的情况下实现行内播放，此处仅作示例，请按需使用。
> - 设置 `x5-playsinline` 属性在 TBS 内核会使用 X5 UI 的播放器。
> 
3. 在存储桶列表页面，获取步骤1加密视频的 **m3u8** 文件对象地址。
![](https://qcloudimg.tencent-cloud.cn/raw/e06464759ee54601fe4d07bd8b657a2c.png)
4. 初始化播放器，并传入 m3u8 对象地址。
```
var player = TCPlayer('player-container-id', {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
player.src(https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/path/example.m3u8); // m3u8对象地址
```

#### 步骤4：查看效果

1. 成功获取到 m3u8 文件和解密密钥。
![获取到m3u8文件](https://qcloudimg.tencent-cloud.cn/raw/4808069fd4269de39c6efff6c1af5908.png)
2. 成功解密并播放视频。
![播放视频](https://qcloudimg.tencent-cloud.cn/raw/2fc23e71f3675e0e98ce9a42c3a1d34c.png)

## 体验

以上实践，我们准备了一个 [线上体验 demo](https://ci-exhibition.cloud.tencent.com/tools/video/)，欢迎体验。
