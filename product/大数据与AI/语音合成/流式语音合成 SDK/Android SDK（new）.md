>? 
>- 当前页面为新版（V2.0.0及以上）SDK 开发文档。新客户可直接按当前文档接入新版 SDK。
>- 旧版（V1.5.3版本及以下）开发文档已于2022年9月5日下线。正在使用旧版 SDK 的客户，可前往 [控制台](https://console.cloud.tencent.com/tts/download)  查看开发文档。
>- 新版 SDK 在稳定性、功能健全性、接口自由度等方面都有所优化。我们将继续支持旧版（V1.5.3版本及以下）SDK，但建议正在使用旧版 SDK 的客户及时升级到新版，以获取更好的使用体验。

## 开发相关
### 开发准备
- 支持 Android 4.1 以上版本 API LEVEL 16，支持手机与平板。
- 合成实时流式语音，需要手机能够连接网络（3/4/5G 或 Wi-Fi 网络等）。
- 建议使用最新版本 Android Studio 进行开发。
- 服务端 [API 文档](https://cloud.tencent.com/document/product/1073/37995)。

### 下载安装 SDK
- 语音合成 [Android SDK](https://console.cloud.tencent.com/tts/download)。
- 解压后即是示例代码工程，目录 `sdk` 下的 aar 文件即 SDK 包。
- 用 Android Studio 打开此工程查看语音合成示例代码。

### 环境配置
- 添加实时语音识别 SDK aar 包 放在 libs 目录下，在 App 的 build.gradle 文件中添加以下代码。
```
 implementation(name: 'libqcloudtts-release', ext: 'aar')
```
- 在 AndroidManifest.xml 添加如下权限：
```
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### 接口说明
#### 获得 TTS 合成器实例
```java
//获得实例
TtsController mTtsController = TtsController.getInstance();  

//销毁实例
TtsController.release();
```

#### 初始化引擎
```java
//第二个参数固定传入 TtsMode.ONLINE
//TtsResultListener: 合成监听器，用于获取合成结果
mTtsController.init(Context context,TtsMode.ONLINE,TtsResultListener listener) 
```

#### 合成监听器，用于获取合成结果
实例化 *TtsResultListener* 时，默认需要重写 *onSynthesizeData()* 和 *onError()* 方法。
**onSynthesizeData()方法签名说明**

| 参数               | 说明                                                  |
| ------------------ | ----------------------------------------------------- |
| byte[] bytes       | 语音数据                                              |
| String utteranceId | 语句 ID                                                |
| String text        | 文本                                                  |
| int engineType     | 引擎类型；0：在线，1：离线；当前是纯在线 SDK，请忽略此参数 |

**onError()方法签名说明**

| 参数               | 说明                     |
| ------------------ | ------------------------ |
| TtsError error     | 错误信息，无错误返回 null |
| String utteranceId | 语句 ID（如果有则返回）   |
| String text        | 文本（如果有则返回）      |

**示例**
```java
TtsResultListener listener = new TtsResultListener() {

    @Override
    public void onSynthesizeData(byte[] bytes, String utteranceId, String text, int engineType) {
    	// 您可以在这里将音频保存或者送入播放接口播放，可调用播放器入参接口入参
    }
    
    @Override
    public void onError(TtsError error, String utteranceId, String text) {
      // 您可以在这里添加错误后处理
    }
  
    @Override
    public void onOfflineAuthInfo(QCloudOfflineAuthInfo offlineAuthInfo) {
      //离在线SDK保留接口，请忽略，如果您后续升级为离线SDK或者离在线SDK，此接口将用于返回授权信息
   }
}
```

#### 合成文本入参接口

| 接口                                        | 说明                                                         |
| ------------------------------------------- | ------------------------------------------------------------ |
| synthesize(String text, String utteranceId) | text 为需要合成的文本；utteranceId 为标记该文本的 ID，将随合成结果返回宿主层 |
| synthesize(String text)                     | text 为需要合成的文本                                         |

**示例**
```java
//内部有维护队列，可持续添加语句，SDK内将依次合成
TtsError error = null;
//当返回的error不为null时，入参失败
error = mTtsController.synthesize("今天天气不错","第1句");
error = mTtsController.synthesize("腾讯云语音合成","第2句");
error = mTtsController.synthesize("腾讯云AI","第3句");
error = mTtsController.synthesize("腾讯云AI","第4句");

//取消未合成的任务并清空内部队列
mTtsController.cancel();
```

#### TtsController 配置参数方法

| 接口                          | 说明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| setSecretId(String s)         | 腾讯云安全凭证，[获取地址](https://console.cloud.tencent.com/cam/capi) |
| setSecretKey(String s)        | 腾讯云安全凭证，获取地址同上                             |
| setToken(String s)            | 若 STS 临时证书鉴权时需要设置 Token，请参见 [获取联合身份临时访问凭证](https://cloud.tencent.com/document/product/598/33416) |
| setOnlineVoiceSpeed(float f)  | 设置在线所合成音频的语速,语速，范围：[-2，2]，分别对应不同语速：0.6倍、0.8倍、1.0倍、1.2倍、1.5倍，默认为0<br>如果需要更细化的语速，可以保留小数点后一位，例如0.5、1.1、1.8等。 |
| setOnlineVoiceVolume(float f) | 设置在线所合成音频的音量                     |
| setOnlineVoiceType(int i)     | 设置在线所合成音频的音色 ID，完整的音色 ID 列表请参见 [基础语音合成](https://cloud.tencent.com/document/product/1073/37995) |
| setOnlineVoiceLanguage(int i) | 主语言类型：1-中文（默认），2-英文                             |
| setOnlineCodec(String s)      | 在线模式编码格式，**非业务必要不建议更改：默认 mp3**，目前支持 mp3、wav、pcm，如更改为 pcm 不支持播放 |
| setConnectTimeout(int i)      | 连接超时，范围：[500,30000]，单位ms，默认15000ms        |
| setReadTimeout(int i)         | 读取超时，范围：[2200,60000]，单位ms，默认30000ms        |

**示例**
```java
mTtsController.setSecretId("AKIDs*********LbFHp7");
mTtsController.setSecretKey("D9tdAM******Lmxvc2");
mTtsController.setOnlineVoiceSpeed(0.0); //配置语速
mTtsController.setOnlineVoiceVolume(1.0);//配置音量
mTtsController.setOnlineVoiceType(1001); //配置音色id 
mTtsController.setOnlineVoiceLanguage(1);//配置主语言
mTtsController.setOnlineCodec("mp3"); //配置合成格式
mTtsController.setConnectTimeout(15 *1000); //连接超时时间
mTtsController.setReadTimeout(30 *1000); //读取超时时间
```

### 播放接口
#### 初始化播放器
如果 SDK 的内置播放器无法满足您的需求，您也可以使用自己实现的播放器替换。demo 中也额外提供了一份播放器源码，您可以修改播放器逻辑，源代码位于 MediaPlayerDemo.java，与 SDK 内置播放器一致。
```java
//使用SDK中提供的播放器
QCloudMediaPlayer mediaPlayer = new QCloudMediaPlayer(new QCloudPlayerCallback() { 
    
    @Override
    public void onTTSPlayStart() {
        Log.d(TAG, "开始播放");
    }

    @Override
    public void onTTSPlayWait() {
        Log.d(TAG, "播放完成，等待音频数据");
    }

    @Override
    public void onTTSPlayResume() {
        Log.d(TAG, "恢复播放");
    }

    @Override
    public void onTTSPlayPause() {
        Log.d(TAG, "暂停播放");
    }

    @Override
    public void onTTSPlayNext(String text, String utteranceId) {
        Log.d(TAG, "开始播放: " + utteranceId + "|" + text);
    }

    @Override
    public void onTTSPlayStop() {
        Log.d(TAG, "播放停止，内部队列已清空");
    }

    @Override
    public void onTTSPlayError(QPlayerError error) {
        Log.d(TAG, "播放器发生异常:"+error.getmCode() + ":" + error.getmMessage());
    }

    /**
     * @param currentWord 当前播放的字符（此为预估值）
     * @param currentIndex 当前播放的字符在所在的句子中的下标（此为预估值）
     */
    @Override
    public void onTTSPlayProgress(String currentWord, int currentIndex) {
        Log.d(TAG, "onTTSPlayProgress: " + currentWord + "|" + currentIndex);
    }
});
```

#### 播放器入参
**enqueue()方法签名说明**

| 参数               | 说明                             |
| ------------------ | -------------------------------- |
| byte[] bytes       | 返回音频流，通过传入字节数组播放 |
| File audio         | 返回音频文件，通过传入文件播放   |
| String text        | 音频对应的文本                   |
| String utteranceId | 文本 ID                           |

**示例**
```java
//通过音频数据入参
QPlayerError err = mediaPlayer.enqueue(byte[] bytes,String text,String utteranceId);

//通过音频文件入参
QPlayerError err = mediaPlayer.enqueue(File audio,String text,String utteranceId);
```

#### 暂停、恢复或停止播放 
```
mediaPlayer.PausePlay();
mediaPlayer.ResumePlay();
mediaPlayer.StopPlay();
```

### 客户端错误码

| ID   | 错误码                                | 说明                                             |
| ---- | ------------------------------------- | ------------------------------------------------ |
| -100 | TTS_ERROR_CODE_UNINITIALIZED          | SDK 未初始化                                      |
| -101 | TTS_ERROR_CODE_GENERATE_SIGN_FAIL     | 签名失败                                         |
| -102 | TTS_ERROR_CODE_NETWORK_CONNECT_FAILED | 网络异常                                         |
| -103 | TTS_ERROR_CODE_DECODE_FAIL            | Response 解析失败                                 |
| -104 | TTS_ERROR_CODE_SERVER_RESPONSE_ERROR  | 后端返回失败错误码，详细错误信息请查看后端错误码 |
| -105 | TTS_ERROR_CODE_QUEUE_IS_FULL          | 合成队列已满                                     |
| -106 | TTS_ERROR_CODE_CANCEL_FAILURE         | 取消失败，请稍后重试                             |
| -900 | TTS_ERROR_CODE_OFFLINE_NOSUPPORT      | 当前 SDK 不支持离线合成能力，请使用 TtsMode.ONLINE  |



### 服务端错误码
请参考 [语音合成 API 文档](https://cloud.tencent.com/document/product/1073/37995)。
