


## 步骤1：账号注册及认证

• 注册 [腾讯云账号](https://cloud.tencent.com/document/product/378/17985)。
• 完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 步骤2：服务开通

- [创建并编译](https://cloud.tencent.com/document/product/647/32396) 实时音视频应用服务。
- 开通正版曲库直通车服务：登录 [正版曲库直通车控制台](https://console.cloud.tencent.com/ame)，单击左侧菜单栏【推荐歌曲】，勾选“我已阅读并同意 《[腾讯云服务协议](https://cloud.tencent.com/document/product/301/1967)》和 《[正版曲库直通车服务协议](https://cloud.tencent.com/document/product/1155/40757)》”并单击【立即开通】，即可开通服务。
![](https://main.qcloudimg.com/raw/b08d2e31443ca74f506d057d11c9d638.png)



## 步骤3：应用创建

单击左侧导航栏【应用管理】>【创建应用】进入“创建应用”页面，填写相应的信息。
![](https://main.qcloudimg.com/raw/cf01f5d03eb7c0708ec085216b0cad97.jpg)
- 应用名称：接入 App 的应用名称。应用名称涉及版权授权，请准确填写，创建后无法再次修改。
- Android PackageName：接入应用在安卓应用市场的 PackageName。请准确填写，创建后无法再次修改。
- IOS BundleID： 接入应用在 IOS 应用市场的 BundleID。请准确填写，创建后无法再次修改。
- 应用场景：请根据接入应用的具体使用场景进行选择。
- DAU：请基于接入应用实际情况准确填写。

## 步骤4：白名单添加

因产品尚在内测，在正式接入之前，请联系对应商务经理为您添加白名单。

## 步骤5：API 联调

| API 名称                | 描述             | 
| ---------------------- | ---------------- | 
| SearchKTVMusics        | [搜索 KTV 曲库](https://cloud.tencent.com/document/product/1155/56401)      | 
| DescribeKTVMusicDetail | [查询曲库歌曲详情](https://cloud.tencent.com/document/product/1155/56402) |

1. 首先调用 SearchKTVMusics 搜索目标歌曲，返回的列表包含歌曲的信息及 Id。
<dx-codeblock>
:::  Java
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SearchKTVMusics
<公共请求参数>

{
    "Limit": 10,
    "KeyWord": "周周",
    "Offset": 0
}

// 响应
{
  "Response": {
    "TotalCount": 1,
    "KTVMusicInfoSet": [
      {
        "ComposerSet": [
          "方方"
        ],
        "MusicId": "ame-78d***",
        "SingerSet": [
          "周周"
        ],
        "Name": "七里香",
        "LyricistSet": [
          "周周"
        ],
        "TagSet": [
          "华语",
          "流行"
        ]
      }
    ],
    "RequestId": "**"
  }
}
:::
</dx-codeblock>
2. 根据接口返回的 Id 查询歌曲详情，包含 SDK 中所需要的 PlayToken。
<dx-codeblock>
:::  Java
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeKTVMusicDetail
<公共请求参数>

{
    "MusicId": "ame-78d2***"
}

// 响应
{
  "Response": {
    "PlayToken": "DUE3344******",
    "KTVMusicBaseInfo": {
      "ComposerSet": [
        "周周"
      ],
      "MusicId": "ame-78d2***",
      "SingerSet": [
        "周周"
      ],
      "Name": "七里香",
      "LyricistSet": [
        "方方"
      ],
      "TagSet": [
        "华语",
        "流行"
      ]
    },
    "RequestId": "**"
  }
}
:::
</dx-codeblock>


## 步骤6：SDK 接入

### 6.1 集成 SDK

a. 拷贝 TXCopyrightedMedia-release-1.0.0.aar 到 libs目录，添加依赖项 `implementation(name:'TXCopyrightedMedia-release-1.0.0', ext:'aar')`。
b. 集成 TRTC SDK（implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'）


注意混淆

```
-keep class com.tencent.** { *; }
```



### 6.2 使用 SDK

#### 获取 TXCopyrightedMedia 单例

- **接口说明**
获取 TXCopyrightedMedia 单例。
- **示例代码**
<dx-codeblock>
:::  Java
TXCopyrightedMedia copyrightedMedia = TXCopyrightedMedia.instance();
:::
</dx-codeblock>


#### 设置 License

- **接口说明**
设置 License。
- **示例代码**
<dx-codeblock>
:::  Java
copyrightedMedia.setLicense(Context context, String licenseUrl, String key);
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



### 6.3 代码示例

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

