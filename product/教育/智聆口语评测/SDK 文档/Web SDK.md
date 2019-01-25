## 概述
腾讯云智聆口语评测（英文版）（Smart Oral Evaluation-English，SOE-E）是腾讯云推出的语音评测产品，是基于英语口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的英语口语发音评测。腾讯云智聆口语评测（英文版）支持单词和句子模式的评测，多维度反馈口语表现，可广泛应用于英语口语类教学应用。
本 SDK 为智聆口语测评（英文版）的 Web 版本，封装了对智聆口语测评（英文版）网络 API 的调用及本地音频文件处理，并提供简单的录音功能，使用者可以专注于从业务切入，方便简洁地进行二次开发。
本文档只对 Web SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 使用说明
#### 依赖环境
请您使用支持录音功能的浏览器。
#### 引入 SDK
只需要在您的 Web 页面中添加如下代码即可：
```html
<script src="https://imgcache.qq.com/open/qcloud/soe/TencentSOE-0.0.1.js"></script>
```

#### 创建对象
使用`new TencentSOE`创建`TencentSOE`对象，参数说明如下：

|      参数      |  类型    |  说明    |  是否必填 | 默认值 |
|     :---:     | :---:    | :---    | :----: | :----  |
| InitUrl       | String   | 初始化接口地址 | 是 | 无 |
| TransUrl      | String   | 评分接口地址 | 是 | 无 |
| WorkMode      | Integer  | 上传方式：语音输入模式，0流式分片，1非流式一次性评估 | 否 | 0 |
| EvalMode      | Integer  | 评估模式，0：词模式，1：句子模式 | 否 | 0 |
| ScoreCoeff    | Float    | 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数<br>用于平滑不同年龄段的分数，1.0为最小年龄段，4.0为最高年龄段 | 否 | 3.5 |
| SoeAppId      | String   | 业务应用 ID，与账号应用 APPID 无关，是用来方便客户管理服务的参数 | 否 | 无 |
| StorageMode   | Integer  | 音频存储模式，0：不存储，1：存储到公共对象存储，<br>输出结果为该会话最后一个分片,TransmitOralProcess 返回结果 AudioUrl 字段 | 否 | 无 |
| success       | function | 创建成功回调 | 否 | 无 |
| error         | function | 创建失败回调 | 否 | 无 |


**用户需自行替换后台接口地址，NodeJS 版本可参考 [此 SDK](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)**

```
let recorder = new TencentSOE({
  InitUrl: 'http://127.0.0.1:3000/cgi/init',
  TransUrl: 'http://127.0.0.1:3000/cgi/trans',
  success() {
    // TODO
  },
  error(err) {
    console.log(err);
  }
});
```

#### 调用方法
- 初始化
```
/**
 * 调用初始化接口，设置测评文本
 * @param {
 *   success: function() {} // 成功回调
 *   error: function() {} // 失败回调
 * }
 */
recorder.init({
  RefText: 'about',
  success() {
    recorder.start();
  },
  error(err) {
    console.log(err);
  }
});
```

- 开始录音
```
/**
 * 开始录音
 * @param {
 *   error: function() {} // 录音过程出现错误时回调，选填
 * }
 */
recorder.start({
  error(err) {
    console.log(err);
  }
});
```

- 停止录音
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
    // 获取blob对象，创建audio进行回放
    let audio = document.createElement('audio');
    audio.setAttribute('controls', '');
    let blobUrl = URL.createObjectURL(res.blob);
    document.body.appendChild(audio);
   	
    // 输出测评得分
    console.log(res.PronAccuracy)
  },
  error(err) {
    console.log(err);
  }
});
```

- 重置参数
```
/**
 * 重置参数，用于修改请求参数
 * @param {Object} params
 */
recorder.reset({
  WorkMode: 1
});
```

## 使用示例
您可以通过单击 [示例](https://soe.cloud.tencent.com)，在线使用智聆口语测评（英文版）的 Web 版本。

## 错误码
|   code   | 错误说明                    |
|  :---:   | :---                    |
| 10000    | 参数格式错误              |
| 10001    | 当前浏览器不支持录音功能     |
| 10002    | 未开启麦克风访问权限        |
| 10003    | 未提供发音评估初始化接口     |
| 10004    | 未提供发音数据传输接口接口   |
| 10005    | 未提供测评文本             |
| 10020    | 接口错误                  |

> ?非本地环境必须使用 HTTPS 协议
