## 一. 视频设备管理
音视频SDK中的所有与视频相关的功能和操作统一由视频控制器的封装类QAVVideoCtrl来管理，通过调用QAVContext类的方法getVideoCtrl可获得QAVVideoCtrl的实例。

```
QAVVideoCtrl *videoCtrl = [AVUtil sharedContext].videoCtrl;
```

## 二. 获取本地视频流（视频输入设备）
获取本地视频流分为三个步骤：

### 1. 使用本地视频委托协议
##### (1)首先在相应的ViewController.h里使用QAVLocalVideoDelegate

##### (2)然后在相应的ViewController.m设置delegate为self

```
[[AVUtil sharedContext].videoCtrl setLocalVideoDelegate:self];
```

### 2. 摄像头操作
#### (1)打开/关闭摄像头
 iOS端的主要视频输入设备为摄像头，打开/关闭摄像头的接口声明如下：

`-(QAVResult)enableCamera:(cameraPos)pos isEnable:(BOOL)bEnable complete:(cameraOptionComplete)block;`

通过设置 pos 来改变摄像头的前后方向，通过设置 bEnable 来设置是打开或者关闭摄像头。

注意：
    打开摄像头这个操作还包含了另外两个潜在的操作：

1.申请一个视频态。        

2.若申请成功，将会把本地摄像头捕捉的画面上传到服务器。

申请视频态可以理解为获取视频的权限，而现在SDK同一时间只支持四路视频上行，也就是最多四个人能开启视频，假如已经有四个人开启视频则不能开启并异步返回false。


示例代码：
```
[[AVUtil sharedContext].videoCtrl enableCamera:CameraPosFront isEnable:YES complete:^(int result) {
        // to do 
}];
```
#### (2). 切换摄像头方向
  改变摄像头的前置和后置方向的接口如下：
`-(QAVResult)switchCamera:(cameraPos)pos complete:(cameraOptionComplete)block;`
 切换为后置摄像头示例代码：
```
[[AVUtil sharedContext].videoCtrl switchCamera:CameraPosBack complete:^(int result) {
        // to do
}];
```
### 3. 获取并处理本地视频流数据
假如打开摄像头成功了，就可以通过以下方法返回本地画面预览回调：

`- (void)OnLocalVideoPreview:(QAVVideoFrame *)frameData`

## 三. 获取远端视频流 （视频输出设备）
获取远端视频流分为以下三个步骤：

### 1. 使用远端视频委托协议
(1)首先在相应的ViewController.h里使用QAVRemoteVideoDelegate

(2)然后在相应的ViewController.m设置delegate为self
```
[[AVUtil sharedContext].videoCtrl setRemoteVideoDelegate:self];
```

### 2. 请求和取消请求远端视频
#### （1）请求多个远端视频流

请求远端视频流要通过QAVEndpoint中的类方法进行远端的视频画面请求，接口声明如下：

```
+(int)requestViewList:(QAVContext*)context identifierList:(NSArray*)identifierList srcTypeList:(NSArray*)srcTypeList ret:(RequestViewListBlock)block;
```
 其中，参数中context为当前的context实例，identifierList为请求成员的id列表，传递成员的identifier(NSString*)，srcTypeList为视频源类型列表，传递成员为avVideoSrcType，必须转为(NSNumber*)再添加到数组里。

示例代码如下：
```
    QAVMultiRoom *multiRoom = (QAVMultiRoom *)[AVUtil sharedContext].room;
    NSArray *memberList = [multiRoom GetEndpointList];
    if ([memberList count]) {
        QAVEndpoint *endpoint = [memberList objectAtIndex:0]; //请求列表中第1个人的视频
        NSMutableArray *identifierListArray = [NSMutableArray arrayWithObject:endpoint.identifier];
        
        NSMutableArray *scrTypeListArray = [NSMutableArray new];
        int requestingSrcType = QAVVIDEO_SRC_TYPE_NONE;
        if(endpoint.isCameraVideo)
        {
            requestingSrcType = QAVVIDEO_SRC_TYPE_CAMERA;
            [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
        }
        else if (endpoint.isScreenVideo)
        {
            requestingSrcType = QAVVIDEO_SRC_TYPE_SCREEN;
            [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
        }
        else
        {
            return;
        }
        
        [QAVEndpoint requsetViewList:[AVUtil sharedContext] identifierList:identifierListArray srcTypeList:scrTypeListArray ret:^(QAVResult result) {
            NSLog(@"requestView Result = %ld",(long)result);
        }];
    }
```
#### （2）取消所有请求的视频画面

```
+(int)cancelAllview:(QAVContext*)context ret:(CancelViewListBlock)block;
```
 示例代码：
```
[QAVEndpoint cancelAllview:[AVUtil sharedContext] ret:^(QAVResult result) {
    // to do                
}];
```

#### （3）请求单个远端视频流

在获取到某个QAVEndpoint的实例的情况下，可以请求该用户的视频流，接口声明如下：

```
-(QAVResult)requestView:(requestViewBlock)block;
```
示例代码：
```
[endpoint requestView:^(QAVResult result) 
{
    // to do
}];
```

#### （4） 取消请求某个成员的视频画面

接口声明如下：

```
-(QAVResult)cancelView:(requestViewBlock)block;
```
示例代码：

```
[endpoint cancelView:^(QAVResult result) 
{
    // to do        
}];
```

### 3. 获取并处理远端视频流数据
 
 假如请求画面成功了，就可以通过以下方法返回远端画面回调：

```
- (void)OnVideoPreview:(QAVVideoFrame *)frameData
```

## 四. 获取屏幕分享画面 
与获取远端视频流的流程相似，获取屏幕分享画面分为以下三个步骤：

### 1. 使用屏幕分享协议

(1)首先在相应的ViewController.h里使用QAVScreenVideoDelegate

(2)然后在相应的ViewController.m设置delegate为self

`[[AVUtil sharedContext].videoCtrl setScreenVideoDelegate:self];`
### 2. 请求屏幕分享视频
该步骤与请求远端视频流的代码一致，请参考。在获取了endpoint的情况下，判断该endpoint是否有发来自屏幕分享的视频，假如有，则改变requestingScrType的枚举值，在请求时，服务器将会根据scrTypeList的不同的枚举值来决定返回屏幕分享的数据还是远端视频流的数据。
```
if (endpoint.isScreenVideo)
   {
      requestingSrcType = QAVVIDEO_SRC_TYPE_SCREEN;
      [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
   }
[QAVEndpoint requestViewList:[AVUtil sharedContext] identifierList:identifierListArray srcTypeList:scrTypeListArray ret:^(QAVResult result) {
}];
```
### 3. 获取并处理屏幕分享视频流数据
 假如请求画面成功了，就可以通过以下方法返回屏幕分享视频流回调：

`- (void)OnVideoPreview:(QAVVideoFrame *)frameData`
## 五. 视频美颜
现在美颜功能已深受广大女生的宠爱，音视频SDK提供了简单的接口来为用户达到一键美颜的效果

注意事项：
- 1.美颜功能受机型限制，iphone4s及以上，ipad，ipodtouch5及以上才支持美颜

- 2.美颜功能需要进入房间打开摄像头才能开启，即enableBeauty()和inputBeautyParam接口需要打开摄像头再调用才能生效。isEnableBeauty()接口不受此限制。

- 3.美颜程度参数的范围在0-9之间，0级最弱，9级最强。


接口声明如下：
```
-(bool)isEnableBeauty;                        //查询机型是否支持美颜
-(bool)enableBeauty:(bool)isEnable;           //打开美颜
-(void)inputBeautyParam:(float)beautyParam;   //传递美颜程度参数
```
示例代码如下，isCameraOn为摄像头开关标志位：
```
float beautyParam = 9.0;    //最大化美颜效果

if( [[AVUtil sharedContext].videoCtrl isEnableBeauty] && isCameraOn)
{
    [[AVUtil sharedContext].videoCtrl enableBeauty:YES];
    [[AVUtil sharedContext].videoCtrl inputBeautyParam:beautyParam];
}
```