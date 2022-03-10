## 接入步骤[](id:step)

Podfile 中添加：
```
  # 主SDK
  pod 'TCGSDK', :git => "https://github.com/tencentyun/cloudgame-ios-sdk.git"
  # 可选虚拟按键SDK
  pod 'TCGVKey', :git => "https://github.com/tencentyun/cloudgame-ios-sdk.git"
```
## 调用示例 [](id:example)
```objectivec
- (void)createGamePlayer {
    if (self.gamePlayer) {
        return;
    }
    // 初始化SDK
    self.gamePlayer = [[TCGGamePlayer alloc] initWithParams:nil andDelegate:self];
    self.gameController = self.gamePlayer.gameController;
    self.gameController.controlDelegate = self;
    // 添加video视图
    [self.gamePlayer.videoView setFrame:self.view.bounds];
    // 初始化鼠标视图
    self.mouseCursor = [[TCGVirtualMouseCursor alloc] initWithFrame:self.gamePlayer.videoView.bounds
                                                         controller:self.gameController];
    // 设置默认的鼠标指针图片，防止后台未及时下放时显示空白
    [self.mouseCursor setCursorImage:[UIImage imageNamed:@"default_cursor"] andRemoteFrame:CGRectMake(0, 0, 32, 32)];

    [self.gamePlayer.videoView addSubview:self.mouseCursor];
    [self.view insertSubview:self.gamePlayer.videoView atIndex:0];
}

- (void)startGameWithRemoteSession:(NSString *)remoteSession {
    NSLog(@"从业务后台成功申请到云端机器");
    NSError *error;
    // 开始游戏
    [self.gamePlayer startGameWithRemoteSession:remoteSession error:&error];
    NSLog(@"start game %@", error);
}

- (void)stopGame {
    dispatch_async(dispatch_get_main_queue(), ^{
        if (self.gamePlayer == nil) {
            return;
        }
        [self.mouseCursor removeFromSuperview];
        self.mouseCursor = nil;
        [self.gamePlayer.videoView removeFromSuperview];
        [self.gamePlayer stopGame];
        self.gamePlayer = nil;
    }
}

#pragma mark --- TCGGamePlayerDelegate ---
- (void)onInitSuccess:(NSString *)localSession {
    NSLog(@"SimplePCDemo onInitSuccess， 本地初始化成功");
    // 开始向后台申请云端资源
    [self getRemoteSessionWithLocalSession:localSession];
}

- (void)onVideoSizeChanged:(CGSize)videoSize {
    NSLog(@"更新画面尺寸:%@", NSStringFromCGSize(videoSize));
    CGFloat newWidth = self.view.frame.size.width - [self.view safeAreaInsets].left - [self.view safeAreaInsets].right;
    CGFloat newHeight = self.view.frame.size.height;
    // 游戏画面强制横屏、设置游戏画面居中显示类似 UIViewContentModeScaleAspectFit
    if (newWidth/newHeight < videoSize.width/videoSize.height) {
        newHeight = floor(newWidth * videoSize.height / videoSize.width);
    } else {
        newWidth = floor(newHeight * videoSize.width / videoSize.height);
    }
    self.gamePlayer.videoView.frame = CGRectMake((self.view.frame.size.width - newWidth) / 2,
                                                 (self.view.frame.size.height - newHeight) / 2,
                                                 newWidth, newHeight);
    self.mouseCursor.frame = self.gamePlayer.videoView.bounds;
}

- (void)onVideoShow {
    NSLog(@"SimplePCDemo onVideoShow, 游戏开始有画面");
    // 设置正确的鼠标显示与控制模式
    [self.gameController setCursorShowMode:TCGMouseCursorShowMode_Local];
    [self.mouseCursor setCursorTouchMode:TCGMouseCursorTouchMode_RelativeTouch];
}

- (void)onConnectionFailure:(TCGErrorType)errorCode msg:(NSError *)errorMsg {
    NSLog(@"SimplePCDemo onConnectionFailure");
    [self stopGame];
}

- (void)onInitFailure:(TCGErrorType)errorCode msg:(NSError *)errorMsg {
    NSLog(@"SimplePCDemo onInitFailure");
    [self stopGame];
}

- (void)onStartReConnectWithReason:(TCGErrorType)reason {
    NSLog(@"onStartReConnectWithReason 与云端链接断开，SDK内部重连中");
}

#pragma mark --- TCGGameControllerDelegate ---
- (void)onCursorImageUpdated:(UIImage *)image frame:(CGRect)imageFrame {
    [self.mouseCursor setCursorImage:image andRemoteFrame:imageFrame];
}

- (void)onCursorVisibleChanged:(BOOL)isVisble {
    NSLog(@"onCursorVisibleChanged 鼠标状态:%@", isVisble?@"显示":@"隐藏");
    [self.mouseCursor setCursorIsShow:isVisble];
}

- (void)onClickedTextField:(TCGTextFieldType)type {
    NSLog(@"onClickedTextField:%zu", type);
}

```
- 客户端获取的 localSession 作为参数传递给 App 后台（传递方式业务方可以自行实现），业务后台请求云 API 锁定机器并创建会话，拿到 remoteSession。
- 客户端通过 remoteSession 启动游戏。
- SDK 启动游戏之后会通过 TCGGamePlayerDelegate 把启动过程中的回调告知给客户端。
- videoView 的尺寸业务方根据自身场景调整尺寸，如果使用 SDK 内置虚拟鼠标，鼠标的视图最好设置成 video 视图的子视图且大小与之相同。

