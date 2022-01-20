## 概述
目前有部分用户接入 TRTC（Tencent RTC）服务后，会有一些实时字幕、会议文字纪要的需求。本文档帮助 web 端用户在已经接入 TRTC 服务后，更方便的快速接入 ASR，完成语音转文字的需求。
## 准备工作
1. 需要在 [腾讯云语音识别控制台](https://console.cloud.tencent.com/asr) 已开通相关语音产品。
2. 在腾讯云控制台 [访问管理](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretID 和 SecretKey 。
3. 在腾讯云控制台 [账号信息](https://console.cloud.tencent.com/developer) 页面获取AppId。

## 接入流程
1. 首先需要接入 TRTC web 端 SDk，完成接入流程。
2. 引入语音识别的 [speechrecognizer.js](https://github.com/TencentCloud/tencentcloud-speech-sdk-js/blob/main/dist/speechrecognizer.js) 和 [asr.js](https://github.com/TencentCloud/tencentcloud-speech-sdk-js/blob/main/examples/trtc/asr.js) ，asr.js 中主要封装了从 TRTC web端 demo 中获取音轨，处理音频，以及调用 ASR 整个过程。
3. 在 TRTC web 端中的调用，（这里以 TRTC web端 demo 本地流为例）：
	- 参数说明
ASR 类的方法列表：
<table>
<thead>
<tr>
<th >方法</th>
<th >参数</th>
<th >说明</th>
</tr>
</thead>
<tbody>
<tr>
<td >start</td>
<td>-</td>
<td> 开始识别</td>
</tr><tr>
<td>stop</td>
<td>-</td>
<td>结束识别</td>
</tr><tr>
<td>OnRecognitionStart</td>
<td> callback</td>
<td>开始识别回调</td>
</tr><tr>
<td>OnSentenceBegin</td>
<td> callback</td>
<td>一句话开始时回调</td>
</tr><tr>
<td>OnRecognitionResultChange</td>
<td> callback</td>
<td>识别结果变化回调</td>
</tr><tr>
<td>OnSentenceEnd</td>
<td> callback</td>
<td>一句话结束时回调</td>
</tr><tr>
<td>OnRecognitionComplete</td>
<td> callback</td>
<td>识别完成回调</td>
</tr><tr>
<td>OnError</td>
<td> callback</td>
<td>识别错误回调</td>
</tr><tr>
<td>OnChange</td>
<td> callback</td>
<td>有识别结果回调</td>
</tr>
</tbody></table>
new ASR(options)说明：
<table>
<thead>
<tr>
<th >属性</th>
<th >必填</th>
<th >默认值</th>
<th >说明</th>
</tr>
</thead>
<tbody>
<tr>
<td >engine_model_type</td>
<td>是</td>
<td> 16k_zh</td>
<td> 引擎类型</td>
</tr><tr>
<td>voice_format</td>
<td> 是</td>
<td>1</td>
<td>语音编码方式</td>
</tr>
</tbody></table>

	其他参数和返回字段参考 [接口文档](https://cloud.tencent.com/document/product/1093/48982)。
>?目前 ASR 类将 TRTC 对应的音频默认处理为16k、16bit的 pcm 格式音频数据，所以 engine_model_type 目前只支持16k模型，voice_format 只能为1，若对音频数据有要求，可自行处理数据，具体可参考[speechrecognizer.js](https://github.com/TencentCloud/tencentcloud-speech-sdk-js/blob/main/dist/speechrecognizer.js) 中16k音频的处理方式。

	- 将生成 AppID、SecretID 和 SecretKey作为参数传入ASR类中，具体调用示例如下 ：
```javascript 
// this.localStream_.getAudioTrack() 为获取的本地流的音轨
const localStreamAsr = new ASR({
  secretKey: '',
  secretId: '',
  appId: 0,
    // 实时识别接口参数
  engine_model_type : '16k_zh', // 引擎
  voice_format : 1,
    // 以下为非必填参数，可跟据业务自行修改
  hotword_id : '08003a00000000000000000000000000',
  needvad: 1,
  filter_dirty: 1,
  filter_modal: 1,
  filter_punc: 1,
  convert_num_mode : 1,
  word_info: 2,,
  audioTrack: this.localStream_.getAudioTrack()
})
// 开始语音识别调用
localStreamAsr.start();

// 开始识别
localStreamAsr.OnRecognitionStart = (res) => {
  console.log('本地流：开始识别', res);
};
// 一句话开始
localStreamAsr.OnSentenceBegin = (res) => {
  console.log('本地流：一句话开始', res);
};
// 识别变化时
localStreamAsr.OnRecognitionResultChange = (res) => {
  console.log('本地流：识别变化时', res);
};
// 一句话结束
localStreamAsr.OnSentenceEnd = (res) => {
  console.log('本地流：一句话结束', res);
};
// 识别有结果时
localStreamAsr.OnChange = (res) => {
  console.log('本地流：识别中' ,res)
}
// 识别结束
localStreamAsr.OnRecognitionComplete = (res) => {
  console.log('本地流：识别结束', res);
};
// 识别错误
localStreamAsr.OnError = (res) => {
  console.log('本地流：识别失败', res);
};


// 关闭识别时
localStreamAsr.stop();

```
>! SecretID 和 SecretKey 作为敏感信息，不建议直接放在前端代码里运行，可以通过接口服务获取，同时建议采取临时密钥方案，具体可参考：[临时身份凭证](https://cloud.tencent.com/document/product/1312/48195) 。
