### 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。腾讯云智聆口语评测支持单词和句子模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。

本 SDK 为智聆口语测评的 Web 版本，封装了对智聆口语测评网络 API 的调用及本地音频文件处理，并提供简单的录音功能，使用者可以专注于从业务切入，方便简洁地进行二次开发。
本文档只对 Web SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

### 使用说明

#### SDK 引入
只需要在您的 Web 页面中添加如下代码即可：
```html
<script src="https://imgcache.qq.com/open/qcloud/soe/TencentSOE-0.0.4.js"></script>
```

#### 创建对象
new TencentSOE

|      参数      |  类型    |  说明    |  是否必填 | 默认值 |
|     :---:     | :---:    | :---    | :----: | :----  |
| SecretId      | String   | 用户 SecretId | 否| 无 |
| SecretKey     | String   | 用户 SecretKey | 否 | 无 |
| TransInitUrl  | String   | 发音数据传输附带初始化接口地址 | 否 | 无 |
| WorkMode      | Integer  | 上传方式：语音输入模式，0流式分片（微信端无效），1非流式一次性评估 | 否 | 0 |
| EvalMode      | Integer  | 0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式 | 否 | 0 |
| ScoreCoeff    | Float    | 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数<br>用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段 | 否 | 3.5 |
| SoeAppId      | String   | 业务应用ID，与账号应用 AppID 无关，是用来方便客户管理服务的参数 | 否 | 无 |
| StorageMode   | Integer  | 音频存储模式，0：不存储，1：存储到公共对象存储，<br>输出结果为该会话最后一个分片 TransmitOralProcess 返回结果 AudioUrl 字段 | 否 | 无 |
| ServerType    | Integer  | 评估语言，0：英文，1：中文 | 否 | 0 |
| TextMode      | Integer  | 输入文本模式，0: 普通文本，1: 音素结构文本 | 否 | 0 |
| MediaUrl      | String  | 获取高清语音素材获取接口（微信端） | 是 | 0 |
| success       | function | 创建成功回调 | 否 | 无 |
| error         | function | 创建失败回调 | 否 | 无 |
> 必须同时提供 SecretId 和 SecretKey 或者 TransInitUrl

- 方式一（推荐）：自行替换后台接口地址（可参考[Tencent Cloud API 3.0 SDK](https://cloud.tencent.com/document/product/884/32828)），提供TransInitUrl
```
let recorder = new TencentSOE({
  TransInitUrl: 'https://soe.cloud.tencent.com/cgi/transInit',
  success() {
    // TODO
  },
  error(err) {
    console.log(err);
  }
});
```
- 方式2（不推荐）：前端使用固定密钥计算授权凭证，该方式适用于前端调试，若使用此方式，请避免泄露密钥
```
let recorder = new TencentSOE({
  SecretId: 'your secretid',
  SecretKey: 'your secretkey',
  success() {
    recorder.start({});
  },
  error(err) {
    console.log(err);
  }
});
```

#### 调用方法
开始录音：
```
/**
 * 开始录音
 * @param {
 *   RefText: 'string', // 测评文本，必填
 *   error: function() {}, // 录音过程出现错误回调，选填
 *   complete: function() {}, // 录音1分钟自动停止回调（微信端），选填
 *   success: function() {}, // 录音1分钟自动测评回调（微信端），建议填写，否则超时后无法获取测评结果
 * }
 */
recorder.start({
  RefText: 'about',
  error: function(err) {
    console.log(err);
  },
  complete: function() {
    console.log('录音超过1分钟未停止触发此回调')
  },
  success: functin(res) {
    console.log(res);
  }
});
```

停止录音：
```
/**
 * 停止录音，返回测评结果
 * @param {
 *   success: function() {} // 成功回调
 *   error: function() {} // 失败回调
 * }
 */
recorder.stop({
  success(res) {
    // 获取blob对象，创建audio进行回放 (PC端)
    let audio = document.createElement('audio');
    audio.setAttribute('controls', '');
    let blobUrl = URL.createObjectURL(res.blob);
    document.body.appendChild(audio);
    
    // 获取localId，进行回放（微信端）
    // let localId = res.localId;
    // wx.playVoice({
    //  localId: localId
    // });
   	
    // 输出测评结果
    console.log(res);
  },
  error(err) {
    console.log(err);
  }
});
```

本地上传文件测评（微信端暂未支持）：
```
/**
 * 上传本地文件进行测评，支持wav、mp3、speex格式
 * @param {
 *   RefText: 'about', // 测评文本
 *   load: function() {} // 文件加载完成回调
 *   success: function() {} // 成功回调
 *   error: function() {} // 失败回调
 * }
 */
 recorder.uploadLocalFile({
   RefText: 'about',
   load() {
     console.log('文件加载完成');
   }
   success(res) {
     console.log(res); // 输出测评结果
   },
   error(err) {
     console.log('err', err);
   }
 });
```

重置参数：
```
/**
 * 重置参数，用于修改请求参数
 * @param {Object} params
 */
recorder.reset({
  WorkMode: 1
});
```

### 示例 Demo
您可以通过单击 [示例](https://soe.cloud.tencent.com)，体验在线使用智聆口语测评（英文版）的 Web 版本。
sdk调试可单击[这里](https://soe.cloud.tencent.com/demo)


### 微信端说明
只支持一次性测评，录音最长时长为一分钟，超过一分钟会自动触发停止录音。使用前必须引入[微信 js-sdk](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421141115)，
wx 接口列表 jsApiList 需要加入['startRecord','stopRecord','playVoice','stopVoice','onVoicePlayEnd','uploadVoice']，TencentSOE 对象的创建需在 wx 成功验证后，如下：
```js
wx.ready(function() {
  var recorder = new TencentSOE({
    TransInitUrl: 'https://yourdomain/transInit',
    MediaUrl: 'https://yourdomain/getMedia',
    success() {
      recorder.start({ RefText: 'about' });
    },
    error(err) {
      console.log(err);
    }
  });
});
```
用户需提供 MediaUrl 接口用于获取高清语音素材，接受 mediaId 作为传入参数，通过 mediaId 和 token 调用微信高清语音素材获取接口，返回文件流。
接口实现参考微信[获取临时素材](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727)中的"附录：高清语音素材获取接口"部分。
下面提供 nodejs 版的示例：
```js
module.exports = async function(req, res, next) {
  var id = req.query.mediaId; // 获取请求的参数mediaId
  var token = await getToken(); // 用户后台存储的token
  var mediaUrl= `https://api.weixin.qq.com/cgi-bin/media/get/jssdk?access_token=${token}&media_id=${id}`; // 拼接url
  request.get(mediaUrl).pipe(res); // 从微信后台获取音频并返回给前端
};
```

### 错误码
|   code   | 错误说明                  |
|  :---:   | :---                    |
| 10000    | 参数格式错误              |
| 10001    | 当前浏览器不支持录音功能     |
| 10002    | 未开启麦克风访问权限        |
| 10003    | 未提供发音评估初始化接口     |
| 10004    | 未提供发音数据传输接口接口   |
| 10005    | 未提供测评文本             |
| 10006    | 上传文件必须是mp3类型       |
| 10007    | 未引入微信JS-SDK          |
| 10008    | 用户拒绝用户拒绝授权录音     |
| 10009    | 上传文件必须是mp3类型       |
| 10010    | 网络异常                  |
| 10011    | TransInitUrl接口不正确     |
| 10012    | MediaUrl接口不正确         |
| 10013    | 录音失败，请重新录音         |
| 10020    | 接口错误，具体看返回信息      |


### 平台和兼容性
| 操作系统平台	  | 浏览器/webview                  | 版本要求 | 备注|
|  :---:      | :---                           | :---   | :--- |
| iOS         | Safari ( 只支持Safari )         | 11.1.2 | |
| Android     | TBS （微信和手机QQ的默认Webview）  | 43600  | 微信和手机 QQ 默认内置的浏览器内核为 TBS。[TBS介绍](https://x5.tencent.com/) |
| Android     | Chrome                         | 60+    | |
| Mac         | Chrome                         | 47+    | |
| Mac         | Safari                         | 11+    | |
| Windows(PC) | Chrome                         | 52+    | |
| Windows(PC) | QQ浏览器                        | 10.2   | |
| 微信端       | 微信默认 webview                  | 无     | 需引入微信 JS-SDK|

> Tip：
非本地环境必须使用 https 协议
