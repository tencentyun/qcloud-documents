## 产品原理
![](https://qcloudimg.tencent-cloud.cn/raw/eecef5ff484321607f1139f4fb477d8f.png)

## 接入前准备工作
### 步骤1：账号注册及认证
- 注册 [腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
- 完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。


### 步骤2：服务开通
- **正版曲库直通车 AME 服务开通**：登录 [正版曲库直通车 AME 控制台](https://console.cloud.tencent.com/ame) 后，您可在勾选同意 [腾讯云服务协议](https://cloud.tencent.com/document/product/301/1967) 以及 [正版曲库直通车服务协议](https://cloud.tencent.com/document/product/1155/40757) 后单击**立即开通**，即可开通服务。
- **实时音视频 TRTC 服务开通**：登录 [实时音视频 TRTC 控制台](https://console.cloud.tencent.com/trtc) 开通并使用产品。

### 步骤3：应用创建
您可在左导航栏进入**正版曲库直通车控制台** > [**应用管理**](https://console.cloud.tencent.com/ame/app) 页面，单击**创建应用**，根据弹窗填空提示，填写相应的信息：

| 配置项 | 配置说明 | 
|---------|---------| 
| 应用名称 | 指接入 App 应用名称。应用名称涉及版权授权，请准确填写，创建后无法再次修改。 | 
| Android PackageName | 指接入应用在 Android 应用市场的 PackageName。请准确填写，创建后无法再次修改。 | 
|  IOS BundleID | 指接入应用在 iOS 应用市场的 BundleID，请准确填写，创建后无法再次修改。 | 
| 应用场景 | 请根据接入应用的具体使用场景如实选择（语聊房/直播/FM）。 | 
| DAU | 请基于接入应用实际情况准确填写。 | 

![](https://qcloudimg.tencent-cloud.cn/raw/d9aa702f15daedbc090a0d7b8343003a.png)

### 步骤4：白名单添加
因产品尚在内测，在正式接入之前，请联系对应商务经理为您添加白名单。

### 步骤5：API 联调

| API名称     | 描述   | 使用说明                   |
| ---------- | ------ | ---------------------- |
| SearchKTVMusics | 搜索 KTV 曲库 |  [文档地址](https://cloud.tencent.com/document/product/1155/56401) |
| DescribeKTVMusicDetail | 查询曲库歌曲详情 | [文档地址](https://cloud.tencent.com/document/product/1155/56402) |

1. 首先调用 SearchKTVMusics 搜索目标歌曲，返回的列表包含歌曲的信息及 ID：
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
2. 根据上面接口返回的 ID 查询歌曲详情，包含 SDK 中所需要的 PlayToken：
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


## SDK 接入
### SDK 集成
1. 集成版权曲库 SDK（拷贝 `TXCopyrightedMedia.framework`）到项目工程中并集成。
2. 如果使用 pod 导入，则在 podfile 里面添加：
```
pod 'TXCopyrightedMedia'
```
>?如果搜索不到，原因是没有更新到源。建议使用 `https://cdn.cocoapods.org/` 做源。在 `Podfile` 最上面添加即可：
```bash
source 'https://cdn.cocoapods.org/'
```
更新源：
```
pod repo update trunk
```
清理 Caches：
```
rm -rf ~/Library/Caches/Cocoapods
```
3. [集成 TRTC SDK](https://cloud.tencent.com/document/product/647/32173)。


### SDK 使用说明
- **获取 TXCopyrightedMedia 单例**
```java
TXCopyrightedMedia *copyrightedMedia = [TXCopyrightedMedia instance];
```
- **设置 License**
```java
[copyrightedMedia setLicense:licenseUrl key:key];
```
参数说明：：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>licenseUrl</td>
<td>NSString</td>
<td>控制台生成的 License URI</td>
</tr><tr>
<td>key</td>
<td>NSString</td>
<td>控制台生成的 key</td>
</tr>
</tbody></table>
- **初始化 TXCopyrightedMedia**
初始化TXCopyrightedMedia。
```java
[copyrightedMedia initialization];
```
- **销毁 TXCopyrightedMedia**
当程序退出后调用销毁。
```java
[TXCopyrightedMedia destroy];
```
- **预加载 Music 数据**
每次播放/重播前都需要调用该接口。
```java
[copyrightedMedia preloadMusic:musicId bitrateDefinition:bitrateDefinition playToken:playToken callback:self]
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>NSString</td>
<td>歌曲 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>NSString</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr><tr>
<td>playToken</td>
<td>NSString</td>
<td>播放 Token</td>
</tr><tr>
<td>callback</td>
<td>ITXMusicPreloadCallback</td>
<td>回调代理</td>
</tr>
</tbody></table>
```java
@protocol ITXMusicPreloadCallback <NSObject>

@optional

- (void)onPreloadStart:(NSString *)musicId bitrateDefinition:(NSString *)bitrateDefinition;

- (void)onPreloadProgress:(NSString *)musicId
        bitrateDefinition:(NSString *)bitrateDefinition
                 progress:(float)progress;

- (void)onPreloadComplete:(NSString *)musicId
        bitrateDefinition:(NSString *)bitrateDefinition
                errorCode:(int)errorCode
                      msg:(NSString *)msg;

@end
```
errorCode返回错误码定义如下：
<table>
<thead>
<tr>
<th>定义</th>
<th>数值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>TXCopyrightedErrorNoError</td>
<td>0</td>
<td>无错误</td>
</tr><tr>
<td>TXCopyrightedErrorInitFail</td>
<td>-1</td>
<td>初始化失败</td>
</tr><tr>
<td>TXCopyrightedErrorCancel</td>
<td>-2</td>
<td>用户取消数据获取</td>
</tr><tr>
<td>TXCopyrightedErrorTokenFail</td>
<td>-3</td>
<td>Token 过期</td>
</tr><tr>
<td>TXCopyrightedErrorNetFail</td>
<td>-4</td>
<td>网络错误</td>
</tr><tr>
<td>TXCopyrightedErrorInner</td>
<td>-5</td>
<td>内部错误</td>
</tr><tr>
<td>TXCopyrightedErrorParseFail</td>
<td>-6</td>
<td>解析错误</td>
</tr><tr>
<td>TXCopyrightedErrorDecryptFail</td>
<td>-7</td>
<td>解密错误</td>
</tr><tr>
<td>TXCopyrightedErrorLicenseFail</td>
<td>-8</td>
<td>License 校验不通过</td>
</tr>
</tbody></table>
- **取消预加载 Music 数据**
```java
[copyrightedMedia cancelPreloadMusic:musicId bitrateDefinition:bitrateDefinition];
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>NSString</td>
<td>歌曲 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>NSString</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr>
</tbody></table>
- **检测是否已预加载 Music 数据**
```java
BOOL isPreloaded = [copyrightedMedia isMusicPreloaded:musicId bitrateDefinition:bitrateDefinition];
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>NSString</td>
<td>音乐 ID</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>NSString</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr>
</tbody></table>
- **生成 Music URI**
App 客户端在 preloadMusic 成功之后调用，原唱&伴奏传给 TRTC 进行播放。
```java
NSString *musicUri = [copyrightedMedia genMusicURI:musicId bgmType:musicType bitrateDefinition:bitrateDefinition];
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicId</td>
<td>NSString</td>
<td>歌曲 ID</td>
</tr><tr>
<td>musicType</td>
<td>Int</td>
<td>0：原唱，1：伴奏，2：歌词</td>
</tr><tr>
<td>bitrateDefinition</td>
<td>NSString</td>
<td>码率描述（audio/mi：64，audio/lo：128，audio/hi：320）</td>
</tr>
</tbody></table>
返回说明：
<table>
<thead><tr><th>返回值</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>musicUri</td>
<td>NSString</td>
<td><ul style="margin:0"><li>原唱&amp;伴奏：传给 TRTC  播放的 URI，格式：<code>CopyRightMusic://audiotype=xxxx&amp;musicid=xxxx&amp;bitrate=xxxx；</code></li><li>歌词：返回歌词的本地路径</li></ul</td>
</tr>
</tbody></table>
- **清理本地所有缓存歌曲数据**
```java
[copyrightedMedia clearMusicCache];
```
- **设置缓存歌曲最大数量**
```java
[copyrightedMedia setMusicCacheMaxCount:maxCount];
```
参数说明：
<table>
<thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead>
<tbody><tr>
<td>maxCount</td>
<td>Int</td>
<td>歌曲最大缓存数量，默认50</td>
</tr>
</tbody></table>

### 代码示例
- application 创建时候调用：
```java
[[TXCopyrightedMedia instance] setLicense:licence key:key];
```
- 进入主界面时候调用：
```java
[[TXCopyrightedMedia instance] initialization];
```
- 退出主界面时候调用：
```java
[TXCopyrightedMedia destroy];
```
- 进入 K 歌房间，单击 **K 歌**，下载 Music：
```java
TXCopyrightedMedia *copyRightedMedia = [TXCopyrightedMedia instance];
if([copyRightedMedia isMusicPreloaded:musicId bitrateDefinition:@"audio/lo"]) {
		 [self startPlayMusic];
}else {
		[copyRightedMedia preloadMusic:musicId bitrateDefinition:@"audio/lo" playToken:playToken callback:self];
}

- (void)startPlayMusic
{
    NSString *origintUri = [[TXCopyrightedMedia instance] genMusicURI:musicId bgmType:0 bitrateDefinition:@"audio/lo"];//获取原唱 uri
    NSString *accompUri = [[TXCopyrightedMedia instance] genMusicURI:musicId bgmType:1 bitrateDefinition:@"audio/lo"];//获取伴奏 uri
    // 注意，上面的 musicId 是曲库后台接口返回的字符串，用来区分存储在后台的音乐资源
    //      下面的 originMusicId 和 accompMusicId 是 int 型格式，您可以自己设置，
    //      用于 TRTC 的 BGM 播放接口区分不同的音乐使用，保证原唱和伴奏的 id 不同即可
    int originMusicId = 0;//原唱的 music id
    int accompMusicId = 1;//伴唱的 music id
    TXAudioMusicParam *originMusicParam = [[TXAudioMusicParam alloc] init];
    originMusicParam.ID = originMusicId;
    originMusicParam.path = origintUri;
    TXAudioMusicParam *accompMusicParam = [[TXAudioMusicParam alloc] init];
    accompMusicParam.ID = accompMusicId;
    accompMusicParam.path = accompUri;
    
    // 播放原唱和伴奏
    [[[TRTCCloud sharedInstance] getAudioEffectManager] startPlayMusic:originMusicParam onStart:^(NSInteger errCode) {

    } onProgress:^(NSInteger progressMS, NSInteger durationMS) {
        
    } onComplete:^(NSInteger errCode) {
        
    }];
    
    [[[TRTCCloud sharedInstance] getAudioEffectManager] startPlayMusic:accompMusicParam onStart:^(NSInteger errCode) {

    } onProgress:^(NSInteger progressMS, NSInteger durationMS) {
        
    } onComplete:^(NSInteger errCode) {
        
    }];
    
    //调用以下代码会播放并上行伴奏：
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPlayoutVolume:originMusicId volume:0];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPlayoutVolume:accompMusicId volume:100];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPublishVolume:originMusicId volume:0];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPublishVolume:accompMusicId volume:100];
    
    //调用以下代码会播放并上行原唱：
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPlayoutVolume:originMusicId volume:100];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPlayoutVolume:accompMusicId volume:0];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPublishVolume:originMusicId volume:100];
    [[[TRTCCloud sharedInstance] getAudioEffectManager] setMusicPublishVolume:accompMusicId volume:0];
}
```
