本文将指导您的客户端定制自己的视频布局。


## 效果图

二分布局|四分布局
:--:|:--:
![](https://main.qcloudimg.com/raw/6ba80388ea6ae759b513e0f1295e894d.png)|![](https://main.qcloudimg.com/raw/faaa32291f79a818193c2fee452400a0.png)

上面分别为二分、四分布局，用户可以根据自己的需求定制自己的布局

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 
[点击下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/Demo_RenderLayout.rar)

## 相关概念
- **AVRootView**
AVRootView继承自Android原生的SurfaceView，可以理解为一个容器，用于放置所有的视频画面
- **AVVideoView**
逻辑上在的渲染控件，用于渲染一路视频画面，一个**AVRootView**可以包含多个**AVVideoView**

![](https://main.qcloudimg.com/raw/26cb9aa302bcab6f3da3c0e28f62e3a1.png)

## 流程图

![](https://main.qcloudimg.com/raw/3d17190cbd718f43406b65e47a8137b4.png)


## 具体实现
可以通过**AVRootView**的宽高，动态设置**AVVideoView**的宽高。

### 二分布局
```Java
public void trViewDouble(){
    avRootView.getViewByIndex(0).setPosLeft(0);
    avRootView.getViewByIndex(0).setPosTop(0);
    avRootView.getViewByIndex(0).setPosWidth(avRootView.getWidth());
    avRootView.getViewByIndex(0).setPosHeight(avRootView.getHeight()/2);
    avRootView.getViewByIndex(0).autoLayout();

    avRootView.getViewByIndex(1).setPosLeft(0);
    avRootView.getViewByIndex(1).setPosTop(avRootView.getHeight()/2);
    avRootView.getViewByIndex(1).setPosWidth(avRootView.getWidth());
    avRootView.getViewByIndex(1).setPosHeight(avRootView.getHeight()/2);
    avRootView.getViewByIndex(1).autoLayout(); 
}
```

### 四分布局
```Java
public void trViewQuarter(){
    // 计算视频画面的宽高
    int subWidth = avRootView.getWidth()/2;
    int subHeight = avRootView.getHeight()/2;

    // 设置视频画面左上角位置
    avRootView.getViewByIndex(0).setPosLeft(0);
    avRootView.getViewByIndex(0).setPosTop(0);
    
    avRootView.getViewByIndex(1).setPosLeft(subWidth);
    avRootView.getViewByIndex(1).setPosTop(0);
    
    avRootView.getViewByIndex(2).setPosLeft(0);
    avRootView.getViewByIndex(2).setPosTop(subHeight);
    
    avRootView.getViewByIndex(3).setPosLeft(subWidth);
    avRootView.getViewByIndex(3).setPosTop(subHeight);

    for (int i=0; i<4; i++){
        avRootView.getViewByIndex(i).setPosWidth(subWidth);
        avRootView.getViewByIndex(i).setPosHeight(subHeight);
        avRootView.getViewByIndex(i).autoLayout();
    }
}
```

## API说明

### setPosLeft
属于**AVVideoView**的方法，设置**AVVideoView**左上角x轴坐标，参数如下:

|名称|类型|描述|
|--|--|--|
|posLeft|int|左上角x轴坐标，单位为像素|

### setPosTop
属于**AVVideoView**的方法，设置**AVVideoView**左上角y轴坐标，参数如下:

|名称|类型|描述|
|--|--|--|
|posTop|int|左上角y轴坐标，单位为像素|

### setPosWidth
属于**AVVideoView**的方法，设置**AVVideoView**宽度，参数如下:

|名称|类型|描述|
|--|--|--|
|posWidth|int|宽度，单位为像素|

### setPosHeight
属于**AVVideoView**的方法，设置**AVVideoView**高度，参数如下:

|名称|类型|描述|
|--|--|--|
|posHeight|int|高度，单位为像素|

### autoLayout
属于**AVVideoView**的方法，刷新**AVVideoView**显示(使用设置的位置生效)

## 常见问题

- 使用独立渲染如何定制布局?
> 独立渲染时，一个渲染控件ILiveRootView只显示一路视频画面，所以可以直接在布局文件布局ILiveRootView来实现视频布局