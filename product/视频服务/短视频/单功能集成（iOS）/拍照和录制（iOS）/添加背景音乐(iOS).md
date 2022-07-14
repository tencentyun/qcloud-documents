## 录制添加 BGM 

<dx-codeblock>
::: ios 
//获取 recorder 对象
TXUGCRecord *recorder =  [TXUGCRecord shareInstance]；

// 设置 BGM 文件路径
[recorder setBGMAsset:path];

// 设置 BGM，从系统媒体库 loading 出来的音乐，可以直接传入对应的 AVAsset
[recorder setBGMAsset:asset];

// 播放 BGM
[recorder playBGMFromTime:beginTime
                   toTime:endTime
          withBeginNotify:^(NSInteger errCode) {
      // 播放开始回调, errCode 0为成功其它为失败
     } withProgressNotify:^(NSInteger progressMS, NSInteger durationMS) {
      // progressMS: 已经播放的时长， durationMS: 总时长
      } andCompleteNotify:^(NSInteger errCode) {
      // 播放结束回调, errCode 0为成功其它为失败
      }];

// 停止播放 BGM
[recorder stopBGM];

// 暂停播放 BGM
[recorder pauseBGM];

// 继续播放 BGM
[recorder resumeBGM];

// 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小
// volume: 音量大小，1为正常音量，建议值为0-2，如果需要调大音量可以设置更大的值
[recorder setMicVolume:1.0];

// setBGMVolume 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小
// volume: 音量大小，1为正常音量，建议值为0-2，如果需要调大背景音量可以设置更大的值
[recorder setBGMVolume:1.0];
:::
</dx-codeblock>

## 编辑添加 BGM
<dx-codeblock>
::: ios 
//初始化编辑器
TXPreviewParam *param = [[TXPreviewParam alloc] init];
param.videoView = videoView;
param.renderMode = PREVIEW_RENDER_MODE_FILL_EDGE;
ugcEdit = [[TXVideoEditer alloc] initWithPreview:param];

//设置 BGM 路径
 [ugcEdit setBGMAsset:fileAsset result:^(int result) {
 }];

//设置 BGM 开始和结束时间
[ugcEdit setBGMStartTime:0 endTime:5];

//设置 BGM 是否循环
[ugcEdit setBGMLoop:YES];

//设置 BGM 在视频添加的起始位置
[ugcEdit setBGMAtVideoTime:0];

//设置视频声音大小
[ugcEdit setVideoVolume:1.0];

//设置 BGM 声音大小
[ugcEdit setBGMVolume:1.0];
:::
</dx-codeblock>

BGM 设置完之后，当启动编辑器预览，BGM 就会根据设置的参数播放，当启动编辑器生成，BGM 也会按照设置的参数合成到生成的视频中。
