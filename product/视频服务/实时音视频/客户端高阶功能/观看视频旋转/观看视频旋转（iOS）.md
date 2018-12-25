本课程讲解房间内画面旋转和拉伸相关问题

### 效果图
全屏模式|黑边模式
:--:|:--:
![](https://main.qcloudimg.com/raw/b9e44f80ac8826c8d65c9f29ccba6d94.png)|![](https://main.qcloudimg.com/raw/56bf48220b2efc67db1932bd0cda59dc.png)


### 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 [Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/Demo_Rotate.zip)
### 相关概念

**画面一致**
画面一致的场景:
> 视频画面的宽 < 视频画面的高
> 渲染视图的宽 < 渲染视图的高

以及:
> 视频画面的宽 > 视频画面的高
> 渲染视图的宽 > 渲染视图的高

**画面不一致**
画面不一致的场景:
> 视频画面的宽 < 视频画面的高
> 渲染视图的宽 > 渲染视图的高

以及:
> 视频画面的宽 > 视频画面的高
> 渲染视图的宽 < 渲染视图的高


### 流程图
![](https://main.qcloudimg.com/raw/27b7c9b712ba66641760eafde919d10b.png)

### 具体实现

#### 创建房间

[创建房间参考基础教程](https://cloud.tencent.com/document/product/647/16811)

#### 禁用自动旋转
```
ILiveRenderView *view =  [[TILLiveManager getInstance] addAVRenderView:[UIScreen mainScreen].bounds foruserId:user srcType:type];
view.autoRotate = NO;
```
#### 旋转
```
NSArray *views = [[TILLiveManager getInstance] getAllAVRenderViews];
for (ILiveRenderView *view in views) {
    view.rotateAngle = ILIVEROTATION_90;//枚举值，根据自己的需要旋转指定角度
}
```
#### 角度一致时的填充
```
NSArray *views = [[TILLiveManager getInstance] getAllAVRenderViews];
for (ILiveRenderView *view in views) {
    view.sameDirectionRenderMode = ILIVERENDERMODE_SCALEASPECTFILL;//枚举值，根据自己的需要设置填充模式
}
```
#### 角度不一致时的填充
```
NSArray *views = [[TILLiveManager getInstance] getAllAVRenderViews];
for (ILiveRenderView *view in views) {
    view.diffDirectionRenderMode = ILIVERENDERMODE_SCALEASPECTFILL;//枚举值，根据自己的需要设置填充模式
}
```

## 常见问题
* 设置旋转无效，检查是否禁用了自动旋转(禁用后才生效)
* 设置填充模式无效, 检查角度是否一致(角度一致时需使用sameDirectionRenderMode属性，否则使用diffDirectionRenderMode属性)
