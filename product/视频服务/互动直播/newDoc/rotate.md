## iLiveSDK视频旋转缩放解决方案

### 问题

由于观众和主播的屏幕方向和大小都可能不一致，所以需要在观众端，按照观众的屏幕大小和方向对主播的画面进行选择，缩放或裁剪。

### 方案选择

从1.2.0版本起，iLiveSDK已经封装了常见显示方案，开发者只需按自己的业务需要选择即可。

参数列表

Android SDK

参数名/函数名  |说明  |默认值  
:-----: | :-----: | :-----: 
setRotate  |主播画面是否旋转  |true（旋转） 
setSameDirectionRenderMode  |方向一致渲染模式  |ILiveRenderMode.SCALE_TO_FIT（全屏适应）  
setDiffDirectionRenderMode  |方向不一致渲染模式  |ILiveRenderMode.BLACK_TO_FILL（黑边）  

IOS SDK

参数名/函数名  |说明  |默认值  
:-----: | :-----: | :-----: 
isRotate  |主播画面是否旋转  |YES（旋转）   
sameDirectionRenderMode  |方向一致渲染模式  |ILIVERENDERMODE_SCALEASPECTFILL（全屏适应）   
diffDirectionRenderMode  |方向不一致渲染模式  |ILIVERENDERMODE_SCALEASPECTFIT（黑边） 

#### 方案一 旋转主播画面

效果如下：

主播画面  |观众屏幕  |铺满屏幕，不留黑边  | 画面大小一致  | 尽量显示，可以留黑边
:-----: | :-----: | :-----: | :-----: | :-----: 
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e9c1483107c3031dded8cbfc42821ef2/2.png)|![](https://mc.qcloudimg.com/static/img/152585d9f400feb2c35a899fd939737e/model1.png)|![](https://mc.qcloudimg.com/static/img/452c30d775789b72ecea8164ae084014/model2.png)|![](https://mc.qcloudimg.com/static/img/9193fc0d84c115de1bde449ffadc9635/model3.png)
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/5b5427bb528185e6fdb8e60784099f92/1.png)|![](https://mc.qcloudimg.com/static/img/31ebc8a5fa580e5678c8c6db38bdd858/model7.png)|![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e78daedf38d466b2ea66ad262580714f/model9.png)

配置如下：

Android SDK 接口:

```java
//设定需要旋转画面
AVVideoView.setRotate(true);
//设定是铺满屏幕还是留黑边
AVVideoView.setSameDirectionRenderMode(ILiveRenderMode sameDirectionRenderMode);
```

IOS SDK接口：

```Object-C
//设定需要旋转画面
iLiveRenderView.isRotate = YES;
//设定是铺满屏幕还是留黑边
iLiveRenderView.sameDirectionRenderMode = ILiveRenderMode;
```

#### 方案二 不旋转主播画面

效果如下：

主播画面  |观众屏幕  |铺满屏幕，不留黑边  | 画面大小一致  | 尽量显示，可以留黑边
:-----: | :-----: | :-----: | :-----: | :-----: 
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e9c1483107c3031dded8cbfc42821ef2/2.png)|![](https://mc.qcloudimg.com/static/img/b442c7dffc76612d08bc0fcf8b220f61/model4.png)|![](https://mc.qcloudimg.com/static/img/e5f28f0210cfa878e8e4bbf41bb3ab72/model5.png)|![](https://mc.qcloudimg.com/static/img/7e75b7a6a227297207e4f955bec44ef8/model6.png)
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/5b5427bb528185e6fdb8e60784099f92/1.png)|![](https://mc.qcloudimg.com/static/img/31ebc8a5fa580e5678c8c6db38bdd858/model7.png)|![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e78daedf38d466b2ea66ad262580714f/model9.png)

配置如下：

Android SDK 接口:

```java
//设定不需要旋转画面
AVVideoView.setRotate(false);
//设定在方向不一致情况下，是铺满屏幕还是留黑边
AVVideoView.setDiffDirectionRenderMode(ILiveRenderMode diffDirectionRenderMode);
//设定在方向一致情况下，是铺满屏幕还是留黑边
AVVideoView.setSameDirectionRenderMode(ILiveRenderMode sameDirectionRenderMode);
```

IOS SDK接口：

```Object-C
//设定不需要旋转画面
iLiveRenderView.isRotate = NO;
//设定在方向不一致情况下，是铺满屏幕还是留黑边
iLiveRenderView.diffDirectionRenderMode = ILiveRenderMode;
//设定在方向一致情况下，是铺满屏幕还是留黑边
iLiveRenderView.sameDirectionRenderMode = ILiveRenderMode;
```





