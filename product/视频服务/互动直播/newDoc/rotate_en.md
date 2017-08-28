## iLiveSDK Video Rotation and Scaling Solutions

### Problem

As the screen orientation and size may be different between VJ and viewers, VJ's view needs to be selected, scaled or cut to adapt to the screen orientation and size at viewer side.

### Scheme Selection

As of Ver.1.2.0, iLiveSDK comes with common display schemes for selection by developers based on business needs.

Parameter List

Android SDK

Parameter/Function Name | Description | Default Value  
:-----: | :-----: | :-----: 
setRotate | Whether to rotate the VJ's view | true (rotate) 
setSameDirectionRenderMode | Rendering mode for the same orientation | ILiveRenderMode.SCALE_TO_FIT (full screen adaptation)  
setDiffDirectionRenderMode | Rendering mode for different orientations | ILiveRenderMode.BLACK_TO_FILL (black edge)  

iOS SDK

Parameter/Function Name | Description | Default Value  
:-----: | :-----: | :-----: 
isRotate | Whether to rotate VJ's view | YES (rotate)   
sameDirectionRenderMode | Rendering mode for the same orientation | ILIVERENDERMODE_SCALEASPECTFILL (full screen adaptation)   
diffDirectionRenderMode | Rendering mode for different orientations | ILIVERENDERMODE_SCALEASPECTFIT (black edge) 

#### Scheme 1 Rotate VJ's view

The effect is as follows:

VJ's View | Viewer's Screen | The screen is fully occupied without black edges | The same view size | Make the view fit in the screen with black edges
:-----: | :-----: | :-----: | :-----: | :-----: 
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e9c1483107c3031dded8cbfc42821ef2/2.png)|![](https://mc.qcloudimg.com/static/img/152585d9f400feb2c35a899fd939737e/model1.png)|![](https://mc.qcloudimg.com/static/img/452c30d775789b72ecea8164ae084014/model2.png)|![](https://mc.qcloudimg.com/static/img/9193fc0d84c115de1bde449ffadc9635/model3.png)
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/5b5427bb528185e6fdb8e60784099f92/1.png)|![](https://mc.qcloudimg.com/static/img/31ebc8a5fa580e5678c8c6db38bdd858/model7.png)|![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e78daedf38d466b2ea66ad262580714f/model9.png)

The configuration is as follows:

Android SDK APIs:

```java
//Rotate the view
AVVideoView.setRotate(true);
//Whether to make the screen fully occupied or allow black edges
AVVideoView.setSameDirectionRenderMode(ILiveRenderMode sameDirectionRenderMode);
```

iOS SDK APIs:

```Object-C
//Rotate the view
iLiveRenderView.isRotate = YES;
//Whether to make the screen fully occupied or allow black edges
iLiveRenderView.sameDirectionRenderMode = ILiveRenderMode;
```

#### Scheme 2 Do not rotate the VJ's view

The effect is as follows:

VI's View | Viewer's Screen | The screen is fully occupied without black edges | The same view size | Make the view fit in the screen with black edges
:-----: | :-----: | :-----: | :-----: | :-----: 
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e9c1483107c3031dded8cbfc42821ef2/2.png)|![](https://mc.qcloudimg.com/static/img/b442c7dffc76612d08bc0fcf8b220f61/model4.png)|![](https://mc.qcloudimg.com/static/img/e5f28f0210cfa878e8e4bbf41bb3ab72/model5.png)|![](https://mc.qcloudimg.com/static/img/7e75b7a6a227297207e4f955bec44ef8/model6.png)
![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/5b5427bb528185e6fdb8e60784099f92/1.png)|![](https://mc.qcloudimg.com/static/img/31ebc8a5fa580e5678c8c6db38bdd858/model7.png)|![](https://mc.qcloudimg.com/static/img/538ff9d974532d3cc13787f137dd0ea4/model8.png)|![](https://mc.qcloudimg.com/static/img/e78daedf38d466b2ea66ad262580714f/model9.png)

The configuration is as follows:

Android SDK APIs:

```java
//Rotating the screen is not required
AVVideoView.setRotate(false);
//Whether to make the screen fully occupied or allow black edges when the orientation at viewer side is different
AVVideoView.setDiffDirectionRenderMode(ILiveRenderMode diffDirectionRenderMode);
//Whether to make the screen fully occupied or allow black edges when the orientation at viewer side is the same
AVVideoView.setSameDirectionRenderMode(ILiveRenderMode sameDirectionRenderMode);
```

iOS SDK APIs:

```Object-C
//Rotating the screen is not required
iLiveRenderView.isRotate = NO;
//Whether to make the screen fully occupied or allow black edges when the orientation at viewer side is different
iLiveRenderView.diffDirectionRenderMode = ILiveRenderMode;
//Whether to make the screen fully occupied or allow black edges when the orientation at viewer side is the same
iLiveRenderView.sameDirectionRenderMode = ILiveRenderMode;
```






