#互动直播视频旋转方案
##前言
本文用于介绍开发腾讯互动直播时可选用的三种视频旋转模式。开发前请参考
[ios文档](https://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/iOS_ILiveSDK_BeforeHand.md)或者
[Android文档](https://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/Android_ILiveSDK_BeforeHand.md)完成基础SDK的导入。
##方案详细介绍
###方案一：智能旋转模式
####简述
智能旋转方案保证显示的视频（包括观众端和主播端等任意角色）始终是正向画面（以主播眼睛看到的上下顺序为准）。视频会自适应到界面View中。
####效果
主播（镜像）  | 观众横屏  | 观众竖屏
------------- | ------------- | -------------
<center>![](https://mc.qcloudimg.com/static/img/9c92bc6451a93a712bc690546f50f599/A1.jpg)</center>| ![](https://mc.qcloudimg.com/static/img/bcd3f3c3de5f9bde1c4118d2f6b3184e/A2.jpg) | ![](https://mc.qcloudimg.com/static/img/3046bacdce4346d3648463f1ff9e9528/A3.jpg)|
<center>![](https://mc.qcloudimg.com/static/img/0b060536074d4694135053e50f85ac44/A4.jpg)</center>| ![](https://mc.qcloudimg.com/static/img/b3b5844c8b8ca160a22d997cc5da9e88/A5.jpg) | ![](https://mc.qcloudimg.com/static/img/cdd8766bc972215373b1ae8126a73b7a/A6.jpg)|

####Android实现方式
1.在工程中导入iLiveSDK    
2.获取布局中的AVRootView

	avRootView = (AVRootView) findViewById(R.id.av_root_view);
3.把AVRootView中指定的AVVideoView的旋转方案设置为ILiveConstants.ROTATION_AUTO，该设置可以随时修改，立即生效

	avRootView.getViewByIndex(i).setRotationMode(ILiveConstants.ROTATION_AUTO);
####iOS实现方式：

    glView.iLiveRotationType = ILiveRotation_Auto;
默认是ILiveRotation_Auto，可在任何时候设置，设置即生效，glView是AVGLCustomRenderView对象，即渲染视图
###方案二：全屏模式
####简述
全屏模式保证观众端始终看到全屏画面，并尽量保证观众看到更多的图像。
####效果
主播（镜像）  | 观众横屏  | 观众竖屏
------------- | ------------- | -------------
![](https://mc.qcloudimg.com/static/img/9c92bc6451a93a712bc690546f50f599/B1.jpg)| ![](https://mc.qcloudimg.com/static/img/9c92bc6451a93a712bc690546f50f599/B2.jpg) | ![](https://mc.qcloudimg.com/static/img/ef07e8078875acf21469c322ce5b0f9a/B3.jpg)|
<center>![](https://mc.qcloudimg.com/static/img/0b060536074d4694135053e50f85ac44/B4.jpg)<center> | ![](https://mc.qcloudimg.com/static/img/11cd19c76da96c5407feeaf986c603cd/B5.jpg) | ![](https://mc.qcloudimg.com/static/img/cdd8766bc972215373b1ae8126a73b7a/B6.jpg)|
####Android实现方式
1.在工程中导入iLiveSDK    
2.获取布局中的AVRootView

	avRootView = (AVRootView) findViewById(R.id.av_root_view);
3.把AVRootView中指定的AVVideoView的旋转方案设置为ILiveConstants.ROTATION_FULL_SCREEN，该设置可以随时修改，立即生效

	avRootView.getViewByIndex(i).setRotationMode(ILiveConstants.ROTATION_FULL_SCREEN);
####iOS实现方式    
    
    glView.iLiveRotationType = ILiveRotation_FullScreen;    
可在任何时候设置，设置即生效，glView是AVGLCustomRenderView对象，即渲染视图

###方案三：裁剪模式
裁剪模式1：（Android和iOS都有）    
画面源端的设备**关闭**系统的“竖排方向锁定”开关，即**支持横竖屏自由旋转**时，保证观众端始终看到全屏画面，并保证始终是正向画面（以主播眼睛看到的上下顺序为准），超出显示范围的图像会被裁剪。：
####效果
主播（镜像）  | 观众横屏  | 观众竖屏
:-------------: | :-------------: | :-------------:
![](https://mc.qcloudimg.com/static/img/9c92bc6451a93a712bc690546f50f599/C1.jpg)| ![](https://mc.qcloudimg.com/static/img/bcd3f3c3de5f9bde1c4118d2f6b3184e/C2.jpg) | ![](https://mc.qcloudimg.com/static/img/a1fa421bdd054eb0f4421f09cc595514/C3.png)|
![](https://mc.qcloudimg.com/static/img/0b060536074d4694135053e50f85ac44/C4.jpg)| ![](https://mc.qcloudimg.com/static/img/591b988158d3b3b48c3fdc8f82b6a91e/C5.png) | ![](https://mc.qcloudimg.com/static/img/cdd8766bc972215373b1ae8126a73b7a/C6.jpg)|

裁剪模式2：(iOS独有)    
画面源端的设备**打开**系统的：“竖排方向锁定”开关，即**不支持横竖屏的自由旋转**时，保证观众端始终看到全屏画面，但**不保证**看到的始终是正向画面，超出显示范围的图像会被裁剪：
####效果
主播（镜像）  | 观众横屏  | 观众竖屏
:-------------: | :-------------: | :-------------:
![](https://mc.qcloudimg.com/static/img/9c92bc6451a93a712bc690546f50f599/D1.jpg)| ![](https://mc.qcloudimg.com/static/img/bcd3f3c3de5f9bde1c4118d2f6b3184e/D2.jpg) |![](https://mc.qcloudimg.com/static/img/4f95ffe1aa8e9a30c51f187231c5ec69/D3.jpg) |
![](https://mc.qcloudimg.com/static/img/0b060536074d4694135053e50f85ac44/D4.jpg)| ![](https://mc.qcloudimg.com/static/img/02689f4cf0bb045daff0d20333d36575/D5.jpg) |![](https://mc.qcloudimg.com/static/img/cdd8766bc972215373b1ae8126a73b7a/D6.jpg)|
####Android实现方式
1.在工程中导入iLiveSDK    
2.获取布局中的AVRootView

	avRootView = (AVRootView) findViewById(R.id.av_root_view);
3.把AVRootView中指定的AVVideoView的旋转方案设置为ILiveConstants.ROTATION_CROP，该设置可以随时修改，立即生效

	avRootView.getViewByIndex(i).setRotationMode(ILiveConstants.ROTATION_CROP);
	
####iOS实现方式

    glView.iLiveRotationType = ILiveRotation_Crop;
可在任何时候设置，设置即生效，glView是AVGLCustomRenderView对象，即渲染视图