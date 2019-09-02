# Camera Focus

## Auto Focus
------
### iOS Auto Focus
iLiveSDK on iOS has included auto focus feature. No configuration is needed
### Android Auto Focus
iLiveSDK on Android has also included auto focus feature that needs to be manually enabled by configuring option when joining a room (initiating a call)
```java
ILiveRoomOption option = new ILiveRoomOption(strHostId)
                .autoFocus(true);       // ## Enable Auto Focus
```
Auto focus on Android is based on motion sensor events, and focuses on the center point when the phone moves.

## Manual Focus
**Note: Currently, manual focus is only supported on rear cameras**
If the users are unsatisfied with the effect of auto focus or if they need to satisfy the requirement for advanced application scenarios, they can adjust the focus themselves. Take manual focus as an example:

### iOS Manual Focus
> The process is as follows:
![](http://img.blog.csdn.net/20160921185424943)

1. Tap event<br/>
The interactive interface is at the top level and the rendering interface is at the bottom level, so the tap events are added to the interactive interface.<br/>
2. Obtain tap point coordinates<br/>
Obtain the relative coordinates of tap gestures on the interactive view.<br/>
3. Transform tap gesture coordinates to layer coordinates<br/>
The coordinates obtained in step 2 are relative to the interactive view. To convert them to the coordinates of rendering view, map the coordinates of interactive view to rendering view by computing the screen coordinates of both.<br/>
Conversion function
```
//Function: To map points from the interactive view to the rendering view.
//This demo implements only focusing and zooming under full screen mode, so it uses liveViewController.livePreview.imageView during the conversion. To map points on interactive views to secondary screen, use the transparent view on top of the secondary screen instead. In FreeShow, the transparent view corresponds to TCShowMultiSubView object.


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

4. Obtain AVCaptureSession and set focus<br/>
Obtain camera session by AVSDK API, and set camera's focus by the session. Please see the onSingleTap function in the demo.<br/>

## Zooming ##

```
//Response to double-tap event
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
//Zooming
-(void)zoomPreview:(float)rate
{
    // Following code illustrates how to obtain AVCaptureSession and control camera zooming. Currently not supported on iPhone 4s.
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

### Android manual focus
>The process is as follows:

![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/focus_flow.png)


1. Add tap event callback, such as setOnTouchListener.

2. Obtain tap coordinates, such as MotionEvent.

3. Obtain Camera object:

```java
Camera camera = ILiveSDK.getInstance().getAvVideoCtrl().getCamera();
```

4. Focus on a focal point
Following code is an example:
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
    //If custom focus is not supported, use auto focus and return.
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
            //Compatible with some custom models. Catching exception here has no influence on actual focus performance
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

