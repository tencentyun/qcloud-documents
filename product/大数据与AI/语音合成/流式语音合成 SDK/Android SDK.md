## 开发相关

### 开发准备

- 支持 Android 4.0 以上版本 API LEVEL 16，支持手机与平板。
- 合成实时流式语音，需要手机能够连接网络（2/3/4G 或 Wi-Fi 网络等）。
- 建议使用最新版本 Android Studio 进行开发。
- 服务端 [API 文档](https://cloud.tencent.com/document/product/1073/37995)。

### 下载安装 SDK

- 语音合成 Android SDK [下载地址](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/tts/tts_sdk_android_v1.4.3.zip)。
- 解压后即是示例代码工程，工程目录 `libqcloudtts-demo/libs` 下的 aar 文件即 SDK 包。
- 用 Android Studio 打开此工程查看语音合成示例代码。
- 长文本接口：实例代码参考 LongTextTtsActivity 类，支持长文本，支持播放暂停与恢复。

### 参数说明

| 参数名称  | 类型   | 必填 | 说明                                                         |
| --------- | ------ | ---- | ------------------------------------------------------------ |
| appId     | int    | 是   | 腾讯云 ID，即 AppID，[获取地址](https://console.cloud.tencent.com/developer) |
| secretId  | String | 是   | 腾讯云安全凭证，[获取地址](https://console.cloud.tencent.com/cam/capi) |
| secretKey | String | 是   | 腾讯云安全凭证，获取地址同上                                 |
| sessionId | String | 否   | 一次请求对应一个 SessionId，会原样返回                       |
| projectId | String  | 否   | 项目 ID，用户自定义，默认为0，[获取地址](https://console.cloud.tencent.com/project) 
| speed     | int | 否   | 语速，范围：[-2，2]，分别对应不同语速：0.6倍、0.8倍、1.0倍、1.2倍、1.5倍，默认为0 |
| voiceType | int | 否   | tts 音色                                  |
| language  | int | 否   | 主语言类型，默认中文                                         |

## 快速入门
### 初始化 TtsController 示例
通过 LongTextTtsController 构造 ttsController。
```
LongTextTtsController mTtsController = new LongTextTtsController();
```
在使用云 API 之前，请前往腾讯云 API 密钥页面申请安全凭证。安全凭证包括 SecretId 和 SecretKey。
```
SecretId 用于标识 API 调用者身份。
SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。
```

>!这里只是示例，请根据用户实际申请的 SecretId 和 SecretKey 进行后续操作。

```
 /**直接鉴权**/
mTtsController.init(this,
	1257709062L,                           //腾讯云 appId
	“AKIDzlIbgVXMPC**QaT6TZOwDF1WktQr4”,   //腾讯云 secretId 
	“6xYsxngLo45sT**ORFuMZZLs9BzXt”        //腾讯云 secretKey
);

/**使用临时密钥鉴权
 1.通过sts 获取到临时证书,此步骤应在您的服务器端实现，详见https://cloud.tencent.com/document/product/598/33416
 2.通过临时密钥调用接口
**/
 mTtsController.init(this, 
	 1257709062L,					//腾讯云 appId
	“AKIDzlIbgVXMPC**QaT6TZOwDF1WktQr4”,   //腾讯云 临时的 secretId 
	“6xYsxngLo45sT**ORFuMZZLs9BzXt”  ,      //腾讯云 临时的 secretKey
	"sdfasdfdfds**fdgfgfdhghgjf"			//腾讯云 对应的token
);

```

### 设置自定义参数
```
//更多音色id可查看官网文档https://cloud.tencent.com/document/product/1073/37995
public enum VoiceType {
    VOICE_TYPE_Zhi_Yu(1001, "智瑜"),
    VOICE_TYPE_Zhi_yun(1004, "智云"),
    VOICE_TYPE_Zhi_Ling(1002, "智聆"),
    VOICE_TYPE_Zhi_Mei(1003, "智美"),
    VOICE_TYPE_We_Jack(1050, "WeJack，英文男声"),
    VOICE_TYPE_We_Rose(1051, "WeRose，英文女声"),
    VOICE_TYPE_Xiao_Yao( 10510000,"智逍遥，阅读男声"),
}

public enum VoiceSpeed {
    VOICE_SPEED_VERY_SLOW(-2, 0.6f, "0.6倍"),
    VOICE_SPEED_SLOWDOWN(-1, 0.8f, "0.8倍"),
    VOICE_SPEED_NORMAL(0, 1.0f, "正常语速(默认)"),
    VOICE_SPEED_ACCELERATE(1, 1.2f, "1.2倍"),
    VOICE_SPEED_VERY_FAST(2, 1.5f, "1.5倍"),
}

public enum VoiceLanguage {
    VOICE_LANGUAGE_CHINESE(1, "中文（默认）"),
    VOICE_LANGUAGE_ENGLISH(2, "英文"),
}
```

#### 示例
```
//设置语速
mTtsController.setVoiceSpeed(speed);

//设置音色
mTtsController.setVoiceType(voice);

//设置音量
mTtsController.setVoiceVolume(volume);

//设置语言
mTtsController.setVoiceLanguage(language);

//设置ProjectId
mTtsController.setProjectId(0);
```

### 语音合成
```
mTtsController.startTts(ttsText, mTtsExceptionHandler, new QCloudPlayerCallback() {
	//播放开始
	@Override
	public void onTTSPlayStart() {
 	   Log.d("tts", "onPlayStart");
	}

	//音频缓冲中
	@Override
	public void onTTSPlayWait() {
   	 Log.d("tts", "onPlayWait");
	}

	//缓冲完成，继续播放
	@Override
	public void onTTSPlayResume() {
	    Log.d("tts", "onPlayResume");
	}

	//连续播放下一句
	@Override
	public void onTTSPlayNext() {
	    Log.d("tts", "onPlayNext");
	}

	//播放中止
	@Override
	public void onTTSPlayStop() {
	    Log.d("tts", "onPlayStop");
	}

	//播放结束
	@Override
	public void onTTSPlayEnd() {
	    Log.d("tts", "onPlayEnd");
	}
});
```

### 接收异常
```
//接收接口异常
private final TtsController.TtsExceptionHandler mTtsExceptionHandler = new TtsController.TtsExceptionHandler() {
    @Override
    public void onRequestException(TtsController.TtsException e) {
        Log.e(TAG, "tts onRequestException");
        Toast.makeText(TtsActivity.this, e.getErrMsg(), Toast.LENGTH_SHORT).show();
    }
};
```


### 暂停、恢复或停止语音播放 
```
mTtsController.pause();
mTtsController.resume(); 
mTtsController.stop();
```

### 错误码
请参考 [语音合成 API 文档](https://cloud.tencent.com/document/product/1073/37995)。

