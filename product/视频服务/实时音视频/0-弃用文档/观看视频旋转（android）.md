本课程讲解房间内画面旋转和拉伸相关问题

### 效果图
全屏模式|黑边模式
:--:|:--:
![](https://main.qcloudimg.com/raw/b9e44f80ac8826c8d65c9f29ccba6d94.png)|![](https://main.qcloudimg.com/raw/56bf48220b2efc67db1932bd0cda59dc.png)

### 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/Demo_Rotation.rar)
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

**渲染模式**
sdk提供全屏(放大)和黑边(缩小)两种渲染模式
> |模式名称|常量|描述|
> |--|--|--|
> |全屏模式|BaseVideoView.BaseRenderMode.SCALE_TO_FIT|通过放大视频画面并裁剪来解决尺寸不一致问题|
> |黑边模式|BaseVideoView.BaseRenderMode.BLACK_TO_FILL|通过缩小视频画面并补充黑边来解决尺寸不一致问题|

### 流程图

![](https://main.qcloudimg.com/raw/27b7c9b712ba66641760eafde919d10b.png)

### 具体实现

#### 尺寸不一致的渲染方式
我们知道
> 画面不一致时，视频画面与渲染视频的宽高比肯定是不一致的；
> 画面一致时，视频画面与渲染视频的宽高比仍有可能是不一致的；

所以在画面不拉伸变形的前提下，如果渲染画面就有了两种方案:

- 放大视频画面，然后做裁剪
实现这里要有区分，画面一致时:
```
AVVideoView.setSameDirectionRenderMode(BaseVideoView.BaseRenderMode.SCALE_TO_FIT);
```
画面不一致时:
```
AVVideoView.setDiffDirectionRenderMode(BaseVideoView.BaseRenderMode.SCALE_TO_FIT);
```

- 缩小画面，然后补黑边
实现同样要区分，画面一致时：
```
AVVideoView.setSameDirectionRenderMode(BaseVideoView.BaseRenderMode.BLACK_TO_FILL);
```
画面不一致时:
```
AVVideoView.setDiffDirectionRenderMode(BaseVideoView.BaseRenderMode.BLACK_TO_FILL);
```

#### 画面不一致的渲染方式
在方向正常时仍有可能出现画面不一致(如移动端竖屏观看 PC 端的屏幕分享或外接摄像头)；
为最大程度展示画面，如果画面不一致时，我们可以配置是否自动旋转视频画面(默认是关闭)，来保证画面一致:
```
// 自动旋转视频画面，保证画面一致
AVVideoView.setRotate(true);
```

### API 说明
#### setSameDirectionRenderMode
属于 AVVideoView 的方法，用于设置画面一致时的渲染方式。
参数：

|名称|类型|描述|
|--|--|--|
|mode|BaseVideoView.BaseRenderMode|[渲染模式](#相关概念)|

#### setDiffDirectionRenderMode
属于 AVVideoView 的方法，用于设置画面一致时的渲染方式。
参数：

|名称|类型|描述|
|--|--|--|
|mode|BaseVideoView.BaseRenderMode|[渲染模式](#相关概念)|

#### setRotate
属于 AVVideoView 的方法，用于设置是否通过旋转视频画面来保证画面一致。
参数：

|名称|类型|描述|
|--|--|--|
|enable|Boolean|开关(默认关闭)|


## 常见问题
* 设置旋转无效，检查是否禁用了自动旋转(禁用后才生效)。
* 设置填充模式无效, 检查角度是否一致(角度一致时需使用sameDirectionRenderMode属性，否则使用diffDirectionRenderMode属性)。
