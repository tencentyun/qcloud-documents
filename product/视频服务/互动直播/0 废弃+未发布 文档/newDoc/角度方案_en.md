In mobile video scenarios, mobile phone's screen can be rotated horizontally or vertically with 4 orientations. To ensure the normal video streaming on interconnected devices, we provide a set of angle schemes.

# 1. Capturing Angles

## Angle definition
The capturing orientations are defined variably with different platforms, systems and devices, and are collectively called "capturing angles".  The rear cameras of iOS and Android have the same angle, so the mobile phone's rear camera can be taken as the reference. The images captured by PC's camera are all horizontal, so the horizontal capturing angle in PC camera is defined as 0.  The definition is as follows:

Captured by Mobile Phone | Video Data | Angle Value
:--------------------: | :---------------------: | :-------------:
![h](https://mc.qcloudimg.com/static/img/df42bc04e5362a94d43b1cd57c08a9a2/phone_0.png) | ![f](https://mc.qcloudimg.com/static/img/b9ef73b8bf2dfc8e0b489a6e4f955ea3/frame_0.png) | 0
![v](https://mc.qcloudimg.com/static/img/a3c5ef84b6cf98930087dcbc172d4289/phone_1.png) | ![f](https://mc.qcloudimg.com/static/img/454e6d4d0c0ed7b11d766d5fa050f4c6/frame_1.png) | 1
![h](https://mc.qcloudimg.com/static/img/888e0b6d55e5198cd1328eb76307433b/phone_2.png) | ![f](https://mc.qcloudimg.com/static/img/ad426d61381ccafc3b4aa4972adee5ad/frame_2.png) | 2
![v](https://mc.qcloudimg.com/static/img/263a82b3c74d785159ef5aac0d493396/phone_3.png) | ![f](https://mc.qcloudimg.com/static/img/d5c770e75b9f47cd8440e0a10df396d4/frame_3.png) | 3

The image captured by mobile phone is the one shown in Preview on the phone, and the video data is the data sent to SDK. No matter how the phone rotates, the data acquired from the camera is always horizontal, except that the content changes with the rotation. Thus, the images from video data are always horizontal.

## Front Camera
The capturing angle of front camera is defined differently between iOS and Android, as shown below:

Captured by iOS Front Camera | Captured by Android Front Camera | Video Data | Angle Value
:--------------------: | :--------------------: | :---------------------: | :-------------:
![h](https://mc.qcloudimg.com/static/img/888e0b6d55e5198cd1328eb76307433b/phone_2.png) | ![h](https://mc.qcloudimg.com/static/img/df42bc04e5362a94d43b1cd57c08a9a2/phone_0.png) | ![f](https://mc.qcloudimg.com/static/img/b9ef73b8bf2dfc8e0b489a6e4f955ea3/frame_0.png) | 0
![v](https://mc.qcloudimg.com/static/img/a3c5ef84b6cf98930087dcbc172d4289/phone_1.png) | ![v](https://mc.qcloudimg.com/static/img/263a82b3c74d785159ef5aac0d493396/phone_3.png) | ![f](https://mc.qcloudimg.com/static/img/454e6d4d0c0ed7b11d766d5fa050f4c6/frame_1.png) | 1
![h](https://mc.qcloudimg.com/static/img/df42bc04e5362a94d43b1cd57c08a9a2/phone_0.png) | ![h](https://mc.qcloudimg.com/static/img/888e0b6d55e5198cd1328eb76307433b/phone_2.png) | ![f](https://mc.qcloudimg.com/static/img/ad426d61381ccafc3b4aa4972adee5ad/frame_2.png) | 2
![v](https://mc.qcloudimg.com/static/img/263a82b3c74d785159ef5aac0d493396/phone_3.png) | ![v](https://mc.qcloudimg.com/static/img/a3c5ef84b6cf98930087dcbc172d4289/phone_1.png) | ![f](https://mc.qcloudimg.com/static/img/d5c770e75b9f47cd8440e0a10df396d4/frame_3.png) | 3


## Rotation Lock
Both iOS and Android phones have automatic rotation lock.

Currently, when rotation is locked on Android, the angle remains unchanged and rotating effect persists; and on iOS, whether rotation is locked in portrait mode or landscape mode, the angle remains at 1 (landscape mode).

> The implementation of locking will be optimized later to achieve a consistency between on iOS and Android and to allow rotation lock in horizontal mode.


## API Settings

### iOS Capture
iOS capturing angle can be implemented within the SDK and does not need configuration.

### Android Capture
For Android, the current rotation angle of phone needs to be sent to SDK through gravity sensor event.

```java
AVVideoCtrl avVideoCtrl = AVContextModel.getInstance().getAVContext().getVideoCtrl();
avVideoCtrl.setRotation(rotation);
```


# 2. Video Drawing
Video data is not rotated and remains horizontal throughout the process from encoding and transmission, to receipt and decoding. The angle information is transparently transmitted from capturing end to the rendering module of receiving end. Before drawing the remote video, rendering module rotates the video view based on the capturing angle and the rotation angle of current device so that the video view is displayed normally at viewer end.

 Video Data | Normal| Rotated Left |Rotated Right | Inverted |
 :------------------------------------------: | :--------------------: | :---------------------: | :---------------------: | :--------------------: |
 ![sf](https://mc.qcloudimg.com/static/img/b9ef73b8bf2dfc8e0b489a6e4f955ea3/frame_0.png) ![sf](https://mc.qcloudimg.com/static/img/ad426d61381ccafc3b4aa4972adee5ad/frame_2.png)| ![v](https://mc.qcloudimg.com/static/img/cdb2f8ec5e6708ea2fd3d950048bbacc/watch_up.png)| ![h](https://mc.qcloudimg.com/static/img/df42bc04e5362a94d43b1cd57c08a9a2/phone_0.png)  | ![h](https://mc.qcloudimg.com/static/img/888e0b6d55e5198cd1328eb76307433b/phone_2.png)  | ![v](https://mc.qcloudimg.com/static/img/44e9bfbc3f196916de78fb256127ea65/watch_down.png)|
 ![sf](https://mc.qcloudimg.com/static/img/454e6d4d0c0ed7b11d766d5fa050f4c6/frame_1.png) ![sf](https://mc.qcloudimg.com/static/img/d5c770e75b9f47cd8440e0a10df396d4/frame_3.png)| ![v](https://mc.qcloudimg.com/static/img/a3c5ef84b6cf98930087dcbc172d4289/phone_1.png) |![h](https://mc.qcloudimg.com/static/img/3bb4183b2412532910d08f97b3771c36/watch_left.png)|![h](https://mc.qcloudimg.com/static/img/96aae9236078f9b0ef043cf201a68508/watch_right.png)|![v](https://mc.qcloudimg.com/static/img/263a82b3c74d785159ef5aac0d493396/phone_3.png) |
 
## Rotation Lock
Both iOS and Android phones have automatic rotation lock. Locking rotation can affect the video drawing angle.

Currently, when rotation is locked on Android, the video drawing remains unchanged and rotating effect persists; and on iOS, whether the rotation is locked in portrait mode or landscape mode, the video drawing behavior remains at landscape mode for a normal view. 

> The implementation of locking will be optimized later to achieve a consistency between on iOS and Android and to allow horizontal view with rotation locked.

## API Settings

### iOS Render
For iOS rendering, angle needs to be handled at business layer. The sample code is as follows:

```Obj-C
#pragma mark remoteVideoDelegate
-(void)OnVideoPreview:(QAVVideoFrame*)frameData{
	int peerRotate = frameData.frameDesc.rotate;
	int selfRotate = 0;
	UIInterfaceOrientation currentOri=(UIInterfaceOrientation)[[UIDevice currentDevice] orientation];
	switch (currentOri) {
	    case UIDeviceOrientationPortrait:
	        selfRotate = 0;
	        break;
	    case UIDeviceOrientationLandscapeLeft:
	        selfRotate = 1;
	        break;
	    case UIDeviceOrientationLandscapeRight:
	        selfRotate = 3;
	        break;
	    case UIDeviceOrientationPortraitUpsideDown:
	        selfRotate = 2;
	        break;
	    default:
	        
	        break;
	}
	frameData.frameDesc.rotate = (selfRotate + peerRotate ) % 4;
	... ...
}
```
### Android Render
For Android, the current rotation angle of phone needs to be sent to SDK, which then internally handles the adjustment logic for capturing angle.

```java
AVVideoCtrl avVideoCtrl = AVContextModel.getInstance().getAVContext().getVideoCtrl();
avVideoCtrl.setRotation(rotation);
```





