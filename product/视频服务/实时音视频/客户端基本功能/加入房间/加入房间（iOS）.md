本文将指导您的观众端如何加入一个直播房间，并打开摄像头麦克风与其他用户视频互动。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_join.zip)
## 加入房间
加入房间的方法在 ILiveRoomManager.h 中，跟创建房间的方法一样，该方法也需要传入两个参数，房间 ID  roomId 和房间配置对象  option （加入房间的 roomId 要和创建的 roomId 一致），创建配置对象时，我们要关闭自动打开摄像头和麦克风。

```objc
- (IBAction)onJoinRoom:(id)sender {
    // 1. 创建live房间页面
    LiveRoomViewController *liveRoomVC = [[LiveRoomViewController alloc] init];

    // 2. 创建房间配置对象
    ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
    option.imOption.imSupport = NO;
    // 不自动打开摄像头
    option.avOption.autoCamera = NO;
    // 不自动打开mic
    option.avOption.autoMic = NO;
    // 设置房间内音视频监听
    option.memberStatusListener = liveRoomVC;
    // 设置房间中断事件监听
    option.roomDisconnectListener = liveRoomVC;

    // 该参数代表进房之后使用什么规格音视频参数，参数具体值为客户在腾讯云实时音视频控制台画面设定中配置的角色名（例如：默认角色名为user, 可设置controlRole = @"user"）
    option.controlRole = #腾讯云控制台配置的角色名#;

    // 3. 调用创建房间接口，传入房间ID和房间配置对象
    [[ILiveRoomManager getInstance] joinRoom:[self.roomIDTF.text intValue] option:option succ:^{
        // 加入房间成功，跳转到房间页
        [self.navigationController pushViewController:liveRoomVC animated:YES];animated:YES];
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        // 加入房间失败
        NSLog(@"加入房间失败 errId:%d errMsg:%@",errId, errMsg);
    }];
}
```
加入房间成功后直接跳转到房间页面。

## 视频互动
要与房间内其他用户进行视频互动，只需要打开摄像头和麦克风即可：

```objc
/**
 打开/关闭 相机

 @param cameraPos 相机位置 cameraPos
 @param bEnable   YES:打开 NO:关闭
 @param succ      成功回调
 @param fail      失败回调
 */
- (void)enableCamera:(cameraPos)cameraPos enable:(BOOL)bEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;

/**
 打开/关闭 麦克风

 @param bEnable YES:打开 NO:关闭
 @param succ      成功回调
 @param fail      失败回调
 */
- (void)enableMic:(BOOL)bEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;
```
在触发相应的动作之后，调用对应的接口即可。

## 音视频事件监听
音视频事件回调方法中需要处理多人的事件，主要是对摄像头开关事件的处理。

>检测到有人开启了摄像头 QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO，就添加该用户的渲染视图；
检测到有人关闭了摄像头 QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO，则移除该用户的渲染视图。

渲染视图的 frame 不是固定的，需要根据当前渲染视图的个数和产品需求进行计算。在本文提供的 Demo 中，简单的对渲染视图做了一个从上到下等分的布局，您也可根据需要自己定义布局逻辑。

```objc
// 音视频事件回调
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints {
    if (endpoints.count <= 0) {
        return NO;
    }
    for (QAVEndpoint *endpoint in endpoints) {
        switch (event) {
            case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO:
            {
                /*
                 创建并添加渲染视图，传入userID和渲染画面类型，这里传入 QAVVIDEO_SRC_TYPE_CAMERA（摄像头画面）
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher addRenderAt:CGRectZero foruserId:endpoint.userId srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [self.view addSubview:renderView];
                [self.view sendSubviewToBack:renderView];
                // 房间内打开摄像头用户数量变化，重新布局渲染视图
                [self onCameraNumChange];
            }
                break;
            case QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO:
            {
                // 移除渲染视图
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher removeRenderViewFor:endpoint.userId srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [renderView removeFromSuperview];
                 // 房间内打开摄像头用户数量变化，重新布局渲染视图
                 [self onCameraNumChange];
            }
                break;
            default:
                break;
        }
    }
    return YES;
}
```

```objc
// 房间内打开摄像头用户数量变化时调用，重新布局所有渲染视图，这里简单处理，从上到下等分布局
- (void)onCameraNumChange {
    // 获取当前所有渲染视图
    NSArray *allRenderViews = [[TILLiveManager getInstance] getAllAVRenderViews];

    // 检测异常情况
    if (allRenderViews.count == 0) {
        return;
    }

    // 计算并设置每一个渲染视图的frame
    CGFloat renderViewHeight = [UIScreen mainScreen].bounds.size.height / allRenderViews.count;
    CGFloat renderViewWidth = [UIScreen mainScreen].bounds.size.width;
    __block CGFloat renderViewY = 0.f;
    CGFloat renderViewX = 0.f;

    [allRenderViews enumerateObjectsUsingBlock:^(ILiveRenderView *renderView, NSUInteger idx, BOOL * _Nonnull stop) {
        renderViewY = renderViewY + renderViewHeight * idx;
        CGRect frame = CGRectMake(renderViewX, renderViewY, renderViewWidth, renderViewHeight);
        renderView.frame = frame;
    }];
}
```
> 注意：
> 1. 添加渲染视图时，客户不用担心重复添加，SDK 内部对同一用户的同一种类型视频源的渲染视图只会添加一次。
> 2. 目前 SDK 内部限制了同时最多可以存在 10 个渲染视图。

## 常见问题
#### 进房失败，提示没有权限
确认正确配置了进房票据privateMapKey，若控制台在【帐号信息】开启【启用权限密钥】,则privateMapKey为必填字段

切换角色失败，错误码 - 1 。
> 这表示配置后台找不到要切换角色，这里需要确认角色名是否填写正常（区分大小写）。
