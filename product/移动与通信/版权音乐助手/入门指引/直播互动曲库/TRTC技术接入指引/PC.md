## 产品原理
流程图：
![](https://qcloudimg.tencent-cloud.cn/raw/cec74bd81f718b03ce5d9ab32794f97b.png)

## 接入前准备工作

### 步骤1：账号注册及认证
- 注册 [腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
- 完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

### 步骤2：服务开通
- **正版曲库直通车 AME 服务开通**：登录 [正版曲库直通车 AME 控制台](https://console.cloud.tencent.com/ame) 后，您可在勾选同意 [腾讯云服务协议](https://cloud.tencent.com/document/product/301/1967) 以及 [正版曲库直通车服务协议](https://cloud.tencent.com/document/product/1155/40757) 后单击**立即开通**，即可开通服务。<br>
- **实时音视频 TRTC 服务开通**：登录 [实时音视频 TRTC 控制台](https://console.cloud.tencent.com/trtc) 开通并使用产品。

### 步骤3：应用创建
您可在左导航栏进入**应用管理**页面，单击**创建应用**按钮，根据弹窗填空提示，填写相应的信息。

| 配置项              | 配置说明                                                     |
| ---------------- | ---------------------------------------------------------- |
| 应用名称            | 指接入 App 应用名称。应用名称涉及版权授权，请准确填写，创建后无法再次修改。 |
| Android PackageName | 指接入应用在 Android 应用市场的 PackageName。请准确填写，创建后无法再次修改。 |
| IOS BundleID        | 指接入应用在 iOS 应用市场的 BundleID，请准确填写，创建后无法再次修改。 |
| 应用场景            | 请根据接入应用的具体使用场景如实选择（语聊房/直播/FM）。     |
| DAU                 | 请基于接入应用实际情况准确填写。                             |

![img](https://qcloudimg.tencent-cloud.cn/raw/d9aa702f15daedbc090a0d7b8343003a.png)

### 步骤4：白名单添加
因产品尚在内测，在正式接入之前，请联系对应商务经理为您添加白名单。

### 步骤5：API 联调

| API 名称     | 描述   | 使用说明                   |
| ---------- | ------ | ---------------------- |
| SearchKTVMusics | 搜索 KTV 曲库 |  [文档地址](https://cloud.tencent.com/document/product/1155/56401) |
| DescribeKTVMusicDetail | 查询曲库歌曲详情 | [文档地址](https://cloud.tencent.com/document/product/1155/56402) |

1. 首先调用 SearchKTVMusics 搜索目标歌曲，返回的列表包含歌曲的信息及 ID。
```java
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SearchKTVMusics
<公共请求参数>

{
    "Limit": 10,
    "KeyWord": "歌手",
    "Offset": 0
}

// 响应
{
  "Response": {
    "TotalCount": 1,
    "KTVMusicInfoSet": [
      {
        "ComposerSet": [
          "作词人"
        ],
        "MusicId": "ame-78dxxx",
        "SingerSet": [
          "歌手"
        ],
        "Name": "歌名",
        "LyricistSet": [
          "歌手"
        ],
        "TagSet": [
          "华语",
          "流行"
        ]
      }
    ],
    "RequestId": "xx"
  }
}
```
2. 根据上面接口返回的 ID 查询歌曲详情，包含 SDK 中所需要的 PlayToken。
```java
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeKTVMusicDetail
<公共请求参数>

{
    "MusicId": "ame-78d2xxx"
}

// 响应
{
  "Response": {
    "PlayToken": "DUE3344xxxxxx",
    "KTVMusicBaseInfo": {
      "ComposerSet": [
        "歌手"
      ],
      "MusicId": "ame-78d2xxx",
      "SingerSet": [
        "歌手"
      ],
      "Name": "歌名",
      "LyricistSet": [
        "作词人"
      ],
      "TagSet": [
        "华语",
        "流行"
      ]
    },
    "RequestId": "xx"
  }
}
```


## 接入 SDK
### 集成 SDK
集成版权曲库 SDK 的头文件 `ITXCopyrightedMedia.h` 和 `TXCopyrightedMedia.dll` 动态库。

### 使用 SDK
- **获取 TXCopyrightedMedia**
```java
TXCopyrightedMedia* copyrightedMedia = CreateCopyRightMedia();
```

- **设置 License**
```c++
m_pCopyrightMedia->setCopyrightedLicense(const char* key, const char* licenseUrl);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>licenseUrl</td>
<td>char*</td>
<td>控制台生成的 licenseUrl</td>
</tr><tr>
<td>key</td>
<td>char*</td>
<td>控制台生成的 key</td>
</tr></tbody></table>

- **销毁 TXCopyrightedMedia**
当程序退出后调用销毁。
```c++
DestroyCopyRightMedia(&m_pCopyrightMedia)
```

- **预加载 Music 获取接口**
```c++
m_pCopyrightMedia->QueryInterface(int type, void** ppv)
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>type</td>
<td>int</td>
<td>传入 TXIID_MediaPreload</td>
</tr><tr>
<td>ppv</td>
<td>void**</td>
<td>获取 <code>ITXMediaPreload* m_pMediaPreload</code> 指针</td>
</tr></tbody></table>
```c++
m_pCopyrightMedia->QueryInterface(TXIID_MediaPreload, (void**)&m_pMediaPreload);
```

- **预加载 Music 数据**
每次播放/重播前都需要调用该接口。
```c++
m_pMediaPreload->preloadMusic(const char* musicId, const char* bitrateDefine,
                                   const char* playToken, ITXMediaPreloadCallback* callback);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>char*</td>
<td>歌曲 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>char*</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr><tr>
<td>playToken</td>
<td>char*</td>
<td>播放 Token</td>
</tr><tr>
<td>callback</td>
<td>ITXMusicPreloadCallback*</td>
<td>回调函数</td>
</tr></tbody></table>
```c++
class ITXMediaPreloadCallback {
   public:
    ITXMediaPreloadCallback() = default;
    virtual ~ITXMediaPreloadCallback() = default;
    /// 版权音乐开始下载
    virtual void onPreloadStart(const char* musicId, const char* bitrateDefinition) = 0;
    /// 版权音乐下载进度回调
    virtual void onPreloadProgress(const char* musicId, const char* bitrateDefinition,
                                   float progress) = 0;
    /// 版权音乐下载完成回调
    virtual void onPreloadComplete(const char* musicId, const char* bitrateDefinition,
                                   int errorCode, const char* msg) = 0;
};
```
errCode 返回错误码定义如下
<table>
<thead>
<tr>
<th>定义</th>
<th>数值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>ERR_NONE</td>
<td>0</td>
<td>无错误</td>
</tr><tr>
<td>ERR_INIT_FAIL</td>
<td>-1</td>
<td>初始化失败</td>
</tr><tr>
<td>ERR_CANCEL</td>
<td>-2</td>
<td>用户取消数据获取</td>
</tr><tr>
<td>ERR_TOKEN_FAIL</td>
<td>-3</td>
<td>Token 过期</td>
</tr><tr>
<td>ERR_NET_FAIL</td>
<td>-4</td>
<td>网络错误</td>
</tr><tr>
<td>ERR_INNER</td>
<td>-5</td>
<td>内部错误</td>
</tr><tr>
<td>ERR_PARSE_FAIL</td>
<td>-6</td>
<td>解析错误</td>
</tr><tr>
<td>ERR_DECRYPT_FAIL</td>
<td>-7</td>
<td>解密错误</td>
</tr><tr>
<td>ERR_LICENCE_FAIL</td>
<td>-8</td>
<td>License 校验不通过</td>
</tr></tbody></table>

- **取消预加载 Music 数据**
```java
m_pMediaPreload->cancelPreloadMusic(const char* musicId, const char* bitrateDefinition);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>char*</td>
<td>歌曲 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>char*</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr></tbody></table>
- **检测是否已预加载 Music 数据**
```c++
bool isPreloaded = m_pMediaPreload->isMusicPreload(const char* musicId, const char* bitrateDefinition);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>char*</td>
<td>音乐 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>char*</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr></tbody></table>

- **生成 Music URI**
App 客户端在 preloadMusic 成功之后调用，原唱&伴奏传给 TRTC 进行播放。
```java
m_pCopyrightMedia->genMusicURI(const char* musicId, int bgmType,
                                             const char* bitrateDefinition, char* out,
                                             int out_size) ;
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>char*</td>
<td>歌曲 ID</td>
</tr><tr>
<td>musicType</td>
<td>Int</td>
<td>0：原唱，1：伴奏，2：歌词</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>char*</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr><tr>
<td>out</td>
<td>char*</td>
<td>用户传入的 buffer，用来存放 genMusicURI 返回的字符串</td>
</tr><tr>
<td>out_size</td>
<td>int</td>
<td>out_size 用户 buffer 的大小</td>
</tr></tbody></table>

- **清理本地所有缓存歌曲数据**
```java
m_pMediaPreload->clearMusicCache();
```

- **设置缓存歌曲最大数量**
```java
m_pMediaPreload->setMusicCacheMaxCount(int maxCount);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>maxCount</td>
<td>Int</td>
<td>歌曲最大缓存数量，默认50</td>
</tr></tbody></table>

- **创建音乐轨道类**
用于获取音乐的数据帧数据，客户端在 preloadMusic 成功之后调用。
```java
ITXCMMusicTrack* m_pMusicTrack = copyrightedMedia->createMusicTrack(TXCMMusicInfo& musicInfo);
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicInfo</td>
<td>TXCMMusicInfo</td>
<td>歌曲信息</td>
</tr></tbody></table>
```c++
class TXCMusicInfo {
   public:
    std::string musicId_;            ///**字段含义**歌曲Id
    int musicType_;            ///**字段含义**0：原唱，1：伴奏
    std::string bitrateDefinition_;  ///**字段含义**码率描述（audio/mi：64，audio/lo：128，audio/hi：320）

    TXCMusicInfo(const std::string& musicId, const std::string& bitrateDefinition, int musicType)
        : musicId_(musicId), bitrateDefinition_(bitrateDefinition), musicType_(musicType_) {
    }

    virtual ~TXCMusicInfo() {
    }
};

class ITXCMMusicTrack {
   public:
    ITXCMMusicTrack() = default;
    virtual ~ITXCMMusicTrack() = default;
    /**
     * onPrepared后调用，返回采样率，16000、24000、32000、44100、48000等
     */
    virtual int getSampleRate() = 0;

    /**
     * onPrepared后调用，返回声道数
     */
    virtual int getChannelCount() = 0;

    /**
     * onPrepared后调用，返回音轨时长
     */
    virtual int getDuration() = 0;

    /**
     * 获取最近一次{@link #read)}解码得到的帧时间戳。单位:millisecond
     */
    virtual long getPresentTimeMs() = 0;

    /**
     * 设置prepare处理回调
     */
    virtual void setOnPreparedListener(ITXOnPreparedCallback* listener) = 0;

    /**
     * 设置错误事件回调
     */
    virtual void setOnErrorListener(ITXOnErrorCallback* listener) = 0;

    /**
     * 准备音频数据，对musicId进行解密&拼接成m4a，然后准备把音乐参数解出来，异步回调onPrepared
     */
    virtual void prepare() = 0;

    /**
     * onPrepared后调用，开始音频解码
     */
    virtual void start() = 0;

    /**
     * 跳转音乐的解码进度，注意：请尽量避免过度频繁地调用该接口，因为该接口可能会再次读写音乐文件，耗时稍高。
     *
     * @param timeMs seek时间，单位：ms
     */
    virtual void seek(int timeMs) = 0;

    /**
     * @param audioData 同步读取，读取解码后的一帧音频数据，audioData大小必须>=getMinBufferSize
     * @return readSize 读取到的大小， -1 表示读到流末尾
     */
    virtual int read(uint8_t* audioData) = 0;

    /**
     * 返回最小buffer大小
     */
    virtual int getMinBufferSize() = 0;

    /**
     * 停止音频轨道
     */
    virtual void stop() = 0;

    /**
     * 释放资源
     */
    virtual void destroy() = 0;
};


```

### 代码示例

- 创建时候调用：
```c++
 m_pCopyrightMedia = CreateCopyRightMedia();
 m_pCopyrightMedia->QueryInterface(TXIID_MediaPreload, (void**)&m_pMediaPreload);
 if (m_pCopyrightMedia) {
        m_pCopyrightMedia->setCopyrightedLicense(
            "key",
            "licenseURL");
}
```
- 退出主界面时候调用：
```java
 DestroyCopyRightMedia(&m_pCopyrightMedia);
```
- 进入 K 歌房间，单击 K 歌，下载 Music：
```c++
MusicTrackController::MusicTrackController() {
    m_pCopyrightMedia = CreateCopyRightMedia();
    m_pCopyrightMedia->QueryInterface(TXIID_MediaPreload, (void**)&m_pMediaPreload);
    if (m_pCopyrightMedia) {
        m_pCopyrightMedia->setCopyrightedLicense(
            "cbcd617******08f043a32b337763abf",
            "http://license.vod2.myqcloud.com/license/v1/dc8451c40******69e20f2b33c986438/"
            "TXAmeSDK.licence");
    }
}

void MusicTrackController::onPreloadStart(const char* musicId, const char* bitrateDefinition) {
}

void MusicTrackController::onPreloadProgress(const char* musicId, const char* bitrateDefinition,
                                             float progress) {
}

void MusicTrackController::onPreloadComplete(const char* musicId, const char* bitrateDefinition,
                                             int errorCode, const char* msg) {
    if (errorCode == 0) {
        startPlayMusic();
    }
}

void MusicTrackController::startPlayMusic() {
    std::string music_id = "61b7104c-1fee-***-****-54bf41efef8f";
    std::string birate_define = "audio/mi: 64";
    TXCMusicInfo musicInfo(music_id, birate_define, 0);
    m_pMusicTrack = m_pCopyrightMedia->createMusicTrack(musicInfo);
    m_pMusicTrack->setOnPreparedListener(this);
    m_pMusicTrack->prepare();//回调onPrepared进行解析pcm
}

void MusicTrackController::onPrepared() {
    if (m_pMusicTrack) {
        m_pMusicTrack->start();
        auto task = [=]() {
            int buf = m_pMusicTrack->getMinBufferSize();
            uint8_t* audioData = (uint8_t*)calloc(buf, sizeof(uint8_t));
            while (true) {
                int size = m_pMusicTrack->read(audioData);
                if (size < 0) {
                    break;
                }
               
            }
            free(audioData);
        };
        new std::thread(task);
    }
}

void MusicTrackController::startDownloadMusic() {
    if (m_pMediaPreload) {
        if (m_pMediaPreload->isMusicPreload("musicId",
                                            "bitrateDefine")) {
            startPlayMusic();

        } else {
            m_pMediaPreload->preloadMusic("musicId", "bitrateDefine","musicToken",this);
        }
    }
}

MusicTrackController::~MusicTrackController() {

    if (m_pMusicTrack) {
        m_pMusicTrack->destroy();
    }

    if (m_pCopyrightMedia) {
        DestroyCopyRightMedia(&m_pCopyrightMedia);
    }
}
```



