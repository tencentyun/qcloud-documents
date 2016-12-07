# 画面对焦

## 自动对焦
------
### iOS自动对焦
iLiveSDK在iOS中已提供自动对焦功能，用户无需任何配置
### Android自动对焦
iLiveSDK在Android中也提供了自动对焦功能，需要用户手动开启，在进入房间(发起呼叫)时的option配置
```java
ILiveRoomOption option = new ILiveRoomOption(strHostId)
                .autoFocus(true);       // 开启自动对焦
```
Android的对焦原理是，基于运动传感器事件，在手机发生移动时，对手机中心进行对焦操作。

## 手动对焦
**注：当前只支持后置摄像头手动对焦**
如果需要对自带对焦效果不满意，或有高级应用场景需求，用户可以自己完成对焦功能，这里以实现手动对焦为例:

### iOS手动对焦
> 流程如下：
![](http://img.blog.csdn.net/20160921185424943)

1、单击事件<br/>
因为交互界面在最顶层，渲染界面在最底层，所以单击事件添加到交互界面上<br/>
2、获取单击点坐标<br/>
获取单击手势在视图上的坐标，此坐标是相对于交互视图的坐标<br/>
3、将单击手势坐标转换为layer坐标<br/>
步骤2获取的是相对于交互视图的坐标，要转换为画面渲染视图的坐标，将交互视图和渲染视图想对的屏幕的坐标同时计算出来，即可将交互视图坐标映射到渲染视图。<br/>
转换函数
```
//功能：将交互视图上的点映射成渲染视图的点
//本demo只实现了全屏下的聚焦和缩放功能，所以在转换时使用的liveViewController.livePreview.imageView，如果用户要将交互视图上的点映射为小画面的，这里需要替换成小画面上方的透明视图，在随心播中，小画面上的透明视图对应为TCShowMultiSubView对象


- (CGPoint)layerPointOfInterestForPoint:(CGPoint)point
{
    FocusDemoViewController *liveViewController = (FocusDemoViewController *)_liveController;

    CGRect rect = [liveViewController.livePreview.imageView relativePositionTo:[UIApplication sharedApplication].keyWindow];

    BOOL isContain = CGRectContainsPoint(rect, point);

    if (isContain)
    {
        CGFloat x = (point.x - rect.origin.x)/rect.size.width;
        CGFloat y = (point.y - rect.origin.y)/rect.size.height;

        CGPoint layerPoint = CGPointMake(x, y);


        return layerPoint;
    }
    return CGPointMake(0, 0);
}
```

4、获取AVCaptureSession并设置焦点<br/>
通过AVSDK接口获取相机session，通过此session设置相机焦点，见demo 中onSingleTap函数<br/>

## 缩放 ##

```
//响应双击事件
- (void)onDoubleTap:(UITapGestureRecognizer *)tapGesture
{
    CGPoint point = [tapGesture locationInView:self.view];

    [_focusView.layer removeAllAnimations];

    __weak FocusDemoUIViewController *ws = self;
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(0.05 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
          [ws layoutFoucsView:point];
    });

    static BOOL isscale = YES;
    CGFloat rate = isscale ? 1.0 : -2.0;
    [ self zoomPreview:rate];
    isscale = !isscale;
}
```

```
//缩放
-(void)zoomPreview:(float)rate
{
    // 以下是获取AVCaptureSession演示摄像头缩放的。iphone4s暂时不支持。
    if ([FocusDemoUIViewController isIphone4S:self])
    {
       return;
    }
    //to do
    QAVVideoCtrl *videoCtrl = [_roomEngine getVideoCtrl];
    AVCaptureSession *session = [videoCtrl getCaptureSession];
    if (session)
    {
        for( AVCaptureDeviceInput *input in session.inputs)
        {
            NSError* error = nil;
            AVCaptureDevice*device = input.device;

            if ( ![device hasMediaType:AVMediaTypeVideo] )
            continue;

            BOOL ret = [device lockForConfiguration:&error];
            if (error)
            {
                DebugLog(@"ret = %d",ret);
            }

            if (device.videoZoomFactor == 1.0)
            {
               CGFloat current = 2.0;
               if (current < device.activeFormat.videoMaxZoomFactor)
               {
                 [device rampToVideoZoomFactor:current withRate:10];
               }
            }
            else

{
                [device rampToVideoZoomFactor:1.0 withRate:10];
            }
            [device unlockForConfiguration];
            break;
        }
    }
}
```

### Android手动对焦
>流程如下:

![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/focus_flow.png)


1、添加点击事件回调，如setOnTouchListener

2、获取点击坐标，如MotionEvent

3、获取Camera对象:

```java
Camera camera = ILiveSDK.getInstance().getAvVideoCtrl().getCamera();
```

4、根据焦点来对焦
以下代码可供参考:
```java
protected boolean onFocus(Point point, Camera.AutoFocusCallback callback) {
    if (camera == null) {
        return false;
    }

    Camera.Parameters parameters = null;
    try {
        parameters = camera.getParameters();
    } catch (Exception e) {
        e.printStackTrace();
        return false;
    }
    //不支持设置自定义聚焦，则使用自动聚焦，返回
    if(Build.VERSION.SDK_INT >= 14) {
        if (parameters.getMaxNumFocusAreas() <= 0) {
            return focus(camera, callback);
        }

        Log.i(TAG, "onCameraFocus:" + point.x + "," + point.y);

        List<Camera.Area> areas = new ArrayList<Camera.Area>();
        int left = point.x - 300;
        int top = point.y - 300;
        int right = point.x + 300;
        int bottom = point.y + 300;
        left = left < -1000 ? -1000 : left;
        top = top < -1000 ? -1000 : top;
        right = right > 1000 ? 1000 : right;
        bottom = bottom > 1000 ? 1000 : bottom;
        areas.add(new Camera.Area(new Rect(left, top, right, bottom), 100));
        parameters.setFocusAreas(areas);
        try {
            //兼容部分定制机型，在此捕捉异常，对实际聚焦效果没影响
            camera.setParameters(parameters);
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            return false;
        }
    }

    return focus(camera, callback);
}

private boolean focus(Camera camera, Camera.AutoFocusCallback callback) {
    try {
        camera.autoFocus(callback);
    } catch (Exception e) {
        e.printStackTrace();
        return false;
    }
    return true;
}
```
