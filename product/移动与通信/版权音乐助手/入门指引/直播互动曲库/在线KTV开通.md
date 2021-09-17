本文为您介绍正版曲库直通车 AME & 实时音视频 TRTC 在线 KTV 解决方案服务开通指引。

## 步骤1：开通直播互动曲库
完成 [直播曲库服务开通](https://cloud.tencent.com/document/product/1155/61649)。

## 步骤2：创建实时音视频应用

创建 [实时音视频 TRTC 应用](https://console.cloud.tencent.com/trtc/quickstart)。

### 步骤3：API 联调


|API 名称 | 描述 | 使用说明 |
|---------|---------|---------|
| SearchKTVMusics | 搜索曲目 | [搜索直播互动曲库歌曲](https://cloud.tencent.com/document/product/1155/56401) |
| DescribeKTVMusicDetail | 查询歌曲详情 | [查询直播互动曲目详情](https://cloud.tencent.com/document/product/1155/56402) |

1. 调用 SearchKTVMusics 搜索目标歌曲，返回的列表包含歌曲的信息及 Id。
<dx-codeblock>
:::  HTTP
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SearchKTVMusics
<公共请求参数>

{
    "Limit": 10,
    "KeyWord": "周*伦",
    "Offset": 0
}

// 响应
{
  "Response": {
    "TotalCount": 1,
    "KTVMusicInfoSet": [
      {
        "ComposerSet": [
          "方*山"
        ],
        "MusicId": "ame-78dxxx",
        "SingerSet": [
          "周*伦"
        ],
        "Name": "七里香",
        "LyricistSet": [
          "周*伦"
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

:::
</dx-codeblock>
2. 根据上面接口返回的 Id 查询歌曲详情，包含 SDK 中所需要的 PlayToken。
<dx-codeblock>
:::  HTTP
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
        "周*伦"
      ],
      "MusicId": "ame-78d2xxx",
      "SingerSet": [
        "周*伦"
      ],
      "Name": "七里香",
      "LyricistSet": [
        "方*山"
      ],
      "TagSet": [
        "华语",
        "流行"
      ]
    },
    "RequestId": "xx"
  }
}

:::
</dx-codeblock>


## 步骤4：SDK 接入

### 集成 SDK
 
- **Android**
a. 拷贝 TXCopyrightedMedia-release-1.0.1.aar 到 libs目录，添加依赖项 `implementation(name:'TXCopyrightedMedia-release-1.0.1', ext:'aar')`。
b. 参考此处集成 TRTC SDKimplementation `com.tencent.liteav:LiteAVSDK_TRTC:latest.release` 并 [设置混淆规则](https://cloud.tencent.com/document/product/647/32175#.E8.AE.BE.E7.BD.AE.E6.B7.B7.E6.B7.86.E8.A7.84.E5.88.99)。
- **iOS**
a. 集成版权曲库 SDK（拷贝TXCopyrightedMedia.framework）到项目工程中并集成。
b. 若使用 pod 导入，则需要在 podfile 里添加以下代码。
```
pod 'TXCopyrightedMedia', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/Podspec/TXCopyrightedMedia/1.0.1/TXCopyrightedMedia.podspec'
```
c. [集成 TRTC SDK ]( https://cloud.tencent.com/document/product/647/32173)。
<dx-alert infotype="explain" title="">
请搭配 professional 或 enterprise 版本的 TRTC SDK 使用。
</dx-alert>

- **Windows** 
目前 Windows 平台曲库和 TRTC SDK 已经集成到一起，因此直接下载 Windows 版本的 TRTC SDK 即可使用曲库相关的功能，详情请参见 [精简版（TRTC Windows C++）](https://cloud.tencent.com/document/product/647/32689)。

### SDK 使用说明（Android 和 iOS）

#### 获取 TXCopyrightedMedia 单例

- **接口说明**
获取 TXCopyrightedMedia 单例。
- **示例代码**
```
TXCopyrightedMedia copyrightedMedia = TXCopyrightedMedia.instance();
```

#### 设置 License

- **接口说明**
设置 License。
- **示例代码**
```
copyrightedMedia.setLicense(Context context, String licenseUrl, String key);
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>context</td>
<td>Context</td>
<td>Context 上下文</td>
</tr>
<tr>
<td>licenseUrl</td>
<td>String</td>
<td>控制台生成的 licenseUrl</td>
</tr>
<tr>
<td>key</td>
<td>String</td>
<td>控制台生成的 key</td>
</tr>
</tbody></table>

#### 初始化 TXCopyrightedMedia

- **接口说明**
初始化 TXCopyrightedMedia。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.init();
:::
</dx-codeblock>


#### 销毁 TXCopyrightedMedia

- **接口说明**
当程序退出后调用销毁。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.destroy();
:::
</dx-codeblock>

#### 预加载 Music 数据

- **接口说明**
预加载 Music 数据，每次播放/重播前都需要调用该接口。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.preloadMusic(String musicId, String playToken, ITXMusicPreloadCallback callback);
:::
</dx-codeblock>
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>musicId</td>
<td>String</td>
<td>歌曲 Id</td>
</tr>
<tr>
<td>playToken</td>
<td>String</td>
<td>播放 Token</td>
</tr>
<tr>
<td>callback</td>
<td>ITXMusicPreloadCallback</td>
<td>回调函数</td>
</tr>
</tbody></table>
- **接口示例**
<dx-codeblock>
:::  Java
interface ITXMusicPreloadCallback {
    void onPreloadStart(String musicId);
    void onPreloadProgress(String musicId, float progress);
    void onPreloadComplete(String musicId, int errCode, String errMsg);
}
:::
</dx-codeblock>

#### 取消预加载 Music 数据

- **接口说明**
取消预加载 Music 数据。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.cancelPreloadMusic(String musicId);
:::
</dx-codeblock>
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>musicId</td>
<td>String</td>
<td>歌曲 Id</td>
</tr>
</tbody></table>

#### 检测是否已预加载 Music 数据

- **接口说明**
检测是否已预加载 Music 数据。
- **示例代码**
<dx-codeblock>
:::  Java
boolean isPreloaded = copyrightedMedia.isMusicPreloaded(String musicId);
:::
</dx-codeblock>
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>musicId</td>
<td>String</td>
<td>音乐 Id</td>
</tr>
</tbody></table>


#### 生成 Music URI

- **接口说明**
生成 MusicUri，App 客户端在 preloadMusic 成功之后调用，`原唱、amp;伴奏`组合传给 TRTC 进行播放。
- **示例代码**
<dx-codeblock>
:::  Java
String MusicUri = TXCopyrightedMedia.genMusicURI(String musicId，int musicType);
:::
</dx-codeblock>
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>musicId</td>
<td>String</td>
<td>歌曲 Id</td>
</tr>
<tr>
<td>musicType</td>
<td>Int</td>
<td><ul><li>0：原唱</li><li>1：伴奏</li><li>  2：歌词 </li></ul></td>
</tr>
</tbody></table>
- **返回说明**
<table>
<thead>
<tr>
<th>返回值</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>musicUri</td>
<td>String</td>
<td><ul><li>原唱、amp;伴奏：传给 TRTC 播放的 uri，格式 CopyRightMusic://audiotype=****&amp;musicid=****<li>歌词：返回歌词的本地路径</ul></td>
</tr>
</tbody></table>

#### 清理歌曲缓存

- **接口说明**
清理本地所有缓存歌曲数据。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.clearMusicCache();
:::
</dx-codeblock>

#### 设置缓存歌曲最大数量

- **接口说明**
设置缓存歌曲最大数量。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.setMusicCacheMaxCount(int maxCount);
:::
</dx-codeblock>
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>maxCount</td>
<td>Int</td>
<td>歌曲最大缓存数量，默认50</td>
</tr>
</tbody></table>

#### 示例代码

application 创建时调用：
<dx-codeblock>
:::  Java
TXCopyrightedMedia.instance().setLicense(context, licenseUrl, key);
:::
</dx-codeblock>
进入主界面时调用：
<dx-codeblock>
:::  Java
TXCopyrightedMedia.instance().init();
:::
</dx-codeblock>
退出主界面时调用：
<dx-codeblock>
:::  Java
TXCopyrightedMedia.instance().destroy();
:::
</dx-codeblock>
进入 K 歌房间，点击 K 歌，下载 Music：
<dx-codeblock>
:::  Java
TXCopyrightedMedia copyRightedMedia = TXCopyrightedMedia.instance();
if(copyRightedMedia.isMusicPreloaded(musicId)){
     startPlayMusic();
}else{
  ITXMusicPreloadCallback callback = new ITXMusicPreloadCallback() {
      @override
      public void onPreloadStart(String musicId) {
        // 界面提示 Music 开始加载
      }
      @override
      public void onPreloadProgress(String musicId, float progress){
        // 界面显示进度
      }
      @override
      void onPreloadComplete(String musicId, int errorCode, String errMsg){
        // 缓存完毕
        if(errorCode == ErrorCode.Success) {
          startPlayMusic();
        } else {
          // 提示失败，详情见ErrorCode
        } 
      }
  }
  copyRightedMedia.preloadMusic(musicId, playToken, callback);
}

void startPlayMusic(){
    String origintUri = TXCopyrightedMedia.genMusicURI(musicId, 0);//获取原唱 uri
    String accompUri = TXCopyrightedMedia.genMusicURI(musicId, 1);//获取伴奏 uri
    // 注意，上面的 musicId 是曲库后台接口返回的字符串，用来区分存储在后台的音乐资源
    //      下面的 originMusicId 和 accompMusicId 是 int 型格式，您可以自己设置，
    //      用于 TRTC 的 BGM 播放接口区分不同的音乐使用，保证原唱和伴奏的 id 不同即可
    int originMusicId = 0;//原唱的 music id
    int accompMusicId = 1;//伴唱的 music id
    TXAudioEffectManager.AudioMusicParam originMusicParam = 
      new TXAudioEffectManager.AudioMusicParam(originMusicId, origintUri);
    TXAudioEffectManager.AudioMusicParam accompMusicParam = 
      new TXAudioEffectManager.AudioMusicParam(accompMusicId, accompUri);
    // 播放原唱和伴奏
    TRTCCloud.sharedInstance(this).startPlayMusic(originMusicParam);
    TRTCCloud.sharedInstance(this).startPlayMusic(accompMusicParam);
  
    //调用以下代码会播放并上行伴奏：
    TXAudioEffectManager.setMusicPlayoutVolume(originMusicId,0);
    TXAudioEffectManager.setMusicPlayoutVolume(accompMusicId,100);
    TXAudioEffectManager.setMusicPublishVolume(originMusicId,0);
    TXAudioEffectManager.setMusicPublishVolume(accompMusicId,100);

    //调用以下代码会播放并上行原唱：
    TXAudioEffectManager.setMusicPlayoutVolume(originMusicId,100);
    TXAudioEffectManager.setMusicPlayoutVolume(accompMusicId,0);
    TXAudioEffectManager.setMusicPublishVolume(originMusicId,100);
    TXAudioEffectManager.setMusicPublishVolume(accompMusicId,0);
}
:::
</dx-codeblock>

### SDK 使用说明（Windows）

#### 获取 TXCopyrightedMedia 单例

- **接口说明**
获取 TXCopyrightedMedia 单例。
- **示例代码**
```
ITXCopyrightedMedia *media = CreateCopyRightMedia();
```

#### 设置 License

- **接口说明**
设置 License。
- **示例代码**
```
void setCopyrightedLicense(const char* key,const char* license_url)
```

#### 获取音乐文件下载接口


- **接口说明**
获取音乐文件下载接口。
- **示例代码**
<dx-codeblock>
:::  Java
int QueryInterface(int type, void** ppv);
ITXMediaPreload *preload;
media->QueryInterface(TXIID_MediaPreload, (void**)&preload);

:::
</dx-codeblock>

#### 预加载 Music 数据

- **接口说明**
预加载 Music 数据。
- **示例代码**
```
preloadMedia(const char* music_id, const char* path)
```

#### 取消预加载 Music 数据

- **接口说明**
取消预加载 Music 数据。
- **示例代码**
<dx-codeblock>
:::  Java
cancelPreloadMedia(const char* music_id, const char* path)
:::
</dx-codeblock>


#### 销毁 ITXCopyrightedMedia 实例
- **接口说明**
销毁 ITXCopyrightedMedia 实例。
- **接口代码**
<dx-codeblock>
:::  Java
DestroyCopyRightMedia(ITXCopyrightedMedia** media)
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
ITXMediaPreload 不需要手动销毁，销毁 ITXCopyrightedMedia 实例时 ITXMediaPreload 会被自动销毁。
</dx-alert>
- **示例代码**
<dx-codeblock>
:::  Java
ITXCopyrightedMedia *media = CreateCopyRightMedia();

// license 设置
// key 和 url 的获取请参考应用创建中的内容
char key[] = "7915c47e****134bed50e1e80f0c303b";
char url[] = "http://license.vod2.myqcloud.com/license/v1/dc7c4eff3eeaf3b****31f7941288830/TXAmeSDK.licence";
media->setCopyrightedLicense(key, url);

//  版权音乐的下载和播放
// 获取 ITXMediaPreload 接口
ITXMediaPreload *preload;
media->QueryInterface(TXIID_MediaPreload, (void**)&preload);

// 设置回调
CTXMediaPreloadCallback* callback = new CTXMediaPreloadCallback();
preload->setCallback(callback);

// 下载原唱 music_id 和 ptoken 的获取参考接入说明
// url 的格式为 CopyRightMusic://audiotype=0&ptoken=xxxxx
char music_id[] = "c9fea17d-0040-4f81-af54-9f71d0bf1a91";
char url[] = "audiotype=0&ptoken=eyJNdXNpY0lkIjoiYzlmZWExN2QtMDA0MC00ZjgxLWFmNTQtOWY3MWQwYmYxYTkxIiwiRmlsZUlkIjoiMzcwMTkyNTkyMTI4NTE0NTMxOSIsIlBsYXlTaWduIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhjSEJKWkNJNk1UVXdNREF3TlRBM01pd2lZM1Z5Y21WdWRGUnBiV1ZUZEdGdGNDSTZNVFl6TVRBeE9ESTJOU3dpWlhod2FYSmxWR2x0WlZOMFlXMXdJam94TmpNeE1ESXhPRFkxTENKbWFXeGxTV1FpT2lJek56QXhPVEkxT1RJeE1qZzFNVFExTXpFNUlpd2ljR05tWnlJNkltRnRaVVJ5YlZCeVpYTmxkRGt3TURFaUxDSjFjbXhCWTJObGMzTkpibVp2SWpwN0luUWlPaUkyTVRNM05tSXlPU0o5ZlEuUXFkNzlwU0N5WmNsZmpyY0RTTGlmbzlXdXY4LVFISS1yNVpwXzBvcVJqTSIsIlJlcG9ydEtleSI6ImV5SmhiR2NpT2lKSVV6VXhNaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpCY0hCSlpDSTZNVEkxTVRJeU9ESTROU3dpVFhWemFXTkpaQ0k2SW1NNVptVmhNVGRrTFRBd05EQXROR1k0TVMxaFpqVTBMVGxtTnpGa01HSm1NV0U1TVNJc0lrbFFJam9pTVRBdU1URXpMakV6Tmk0ME9DSXNJbEpsY0c5eWRGUnBiV1VpT2lJeU1ESXhMVEE1TFRBM0lESXdPak0zT2pRMUlpd2laWGh3SWpveE5qTXhNREkxTkRZMUxqYzFOalV5Tml3aWFYTnpJam9pVTJWeWRtbGpaU0o5LlI1Qm1IRXFudkFIT2dnTkFBM3ZCN3ZrYnptcHVwQzRVODZBYUJNNFZCb3labXZLZjZXWERQQk05anlyX2ZNNWR5QUxOSEYzMU1rU1lXVGxqT094YTBBIiwiVm9kQXBwSWQiOjE1MDAwMDUwNzJ9";

if(!preload->isPreloaded(music_id,url)){
    preload->preloadMedia(music_id,url);
}
else{
    StartPlay();
}

int onPreloadComplete(const char*music_id, int error){
    if(error == TXMeidaErrorCode::kSuccessed){
          StartPlay();		
		}
}

// 版权音乐的播放 
AudioMusicParam param;
param.id = 6;///< 用户自定义值，用于对音乐进行标记 控制音乐的开始 停止 音量等
/// 进行版权音乐播放时，注意格式为CopyRightMusic://ptoken=xxxx&audiotype=xxxxx
/// ptoken 为DescribeKTVMusicDetail请求下来的PlayToken字段的值。
/// audiotype 版权音乐的类型 0：原唱 1：伴奏
param.path = CopyRightMusic://ptoken=xxxx&audiotype=xxxx; 
/// 音乐循环播放的次数
/// 取值范围为0 - 任意正整数，默认值：0。0表示播放音乐一次；1表示播放音乐两次；以此类推
param.loopCount = 0;

/// 是否将音乐传到远端
/// YES：音乐在本地播放的同时，会上行至云端，因此远端用户也能听到该音乐；NO：音乐不会上行至云端，因此只能在本地听到该音乐。默认值：NO
param.publish = true;

/// 【字段含义】播放的是否为短音乐文件
/// 【推荐取值】YES：需要重复播放的短音乐文件；NO：正常的音乐文件。默认值：NO
param.isShortFile=false;

/// 【字段含义】音乐开始播放时间点，单位毫秒 版权音乐此值要设置为0
param.startTimeMS = 0;
param.lendTimeMS = 0;

ITRTCCloud* pCloud = getTRTCShareInstance();
ITXAudioEffectManager* pEffect = pCloud->getAudioEffectManager();

void StartPlay(){
      pEffect->startPlayMusic(param);
}

// 伴奏的播放与下载
同原唱，只需把 audiotype 的值设置为 1 即可。

:::
</dx-codeblock>

- **歌曲同步**
<dx-codeblock>
:::  Java
利用 ITXAudioEffectManager 中的 setMusicObserver 接口。

void onPlayProcess(int id,long curPtsMS,long durationMs){
    // 当前音乐的播放进度
		long cur_pos = pEffect->getMusicCurrentPosInMS(id);
		// 设置当前需要展示的歌词即可
}

:::
</dx-codeblock>

## 步骤5：SDK 下载

### Android &iOS AME SDK
- [Android 1.0.3版本 zip包](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TXCopyrightedMedia/Release/1.0.3/TXCopyRightedMedia-Android-1.0.3.zip)。
- [iOS 1.0.3版本 zip包](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TXCopyrightedMedia/Release/1.0.3/TXCopyrightedMedia-iOS-1.0.3.zip
)。
- [iOS podspec接入方式](https://mediacloud-76607.gzc.vod.tencent-cloud.com/Podspec/TXCopyrightedMedia/1.0.3/TXCopyrightedMedia.podspec)。

### Windows AME SDK

- [AME SDK & TRTC SDK](https://cloud.tencent.com/document/product/647/32689)。

## 步骤6：场景实践

您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验 KTV 的能力，包括低延时 K 歌、麦位管理、收发礼物、文字聊天等 TRTC 在 KTV 场景下的相关能力，详情请参见 [在线 K 歌_KTV](https://cloud.tencent.com/document/product/647/59402)。

