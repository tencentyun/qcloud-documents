本文将指导您的客户端有选择的看到房间内用户画面。

## 效果图
![](https://main.qcloudimg.com/raw/ecb8992538a7cb7ba60dc30f021f992d.png)

上图中当前除老师外，共有四名学生开启了视频，老师可以选择只看到其中的两名学生的视频画面
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 
[点击下载]( http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/Demo_ProactiveRender.rar)

## 相关概念
 - **视频数据类型**
 腾讯云支持一个帐号同时上行一路主流和一路辅流，这里用于区分视频流的来源称为视频类型，目前支持的视频类型有： 摄像头，屏幕分享，播片（PC端产生）。

|常量|视频类型|流类型|描述|
|--|--|--|--|
|CommonConstants.Const_VideoType_Camera|摄像头|主流|通过摄像头采集数据产生|
|CommonConstants.Const_VideoType_Screen|屏幕分享|辅流|通过分享屏幕产生|
|CommonConstants.Const_VideoType_File|播片|辅流|通过播放视频文件产生|


## 流程图

![](https://main.qcloudimg.com/raw/3008d9a4940b7dab4af5c0176d3735b2.png)

## 具体实现

### 修改进房配置
要实现手动选择用户视频画面，需要在进房间中配置关闭自动渲染，并监听音视频回调(可参考[音视频事件与成员状态](音视频事件与成员状态.md)),以及视频请求回调:

```Java
ILiveRoomOption option = new ILiveRoomOption()
                .autoRender(false)
                .exceptionListener(this)
                .roomDisconnectListener(this)
                .setRoomMemberStatusLisenter(this) // 监听房间内音视频事件
                .setRequestViewLisenter(this)   // 监听视频请求回调
                .autoCamera(true)
                .autoMic(true);
```

### 请求视频画面
在收到用户的has camera或has screen事件(如果有播片，还有处理has file事件)时，调用接口去请求用户视频画面:
```Java
public boolean onEndpointsUpdateInfo(int eventid, String[] updateList) {
        switch (eventid){
            case ILiveConstants.TYPE_MEMBER_CHANGE_HAS_CAMERA_VIDEO:
                for (String identifier : updateList){
                    // 请求视频画面
                    ILiveSDK.getInstance().getContextEngine().requestUserVideoData(identifier, 
                        CommonConstants.Const_VideoType_Camera);
                }
                break;
            case ILiveConstants.TYPE_MEMBER_CHANGE_HAS_SCREEN_VIDEO:
                for (String identifier : updateList){
                    // 请求视频画面
                    ILiveSDK.getInstance().getContextEngine().requestUserVideoData(identifier, 
                        CommonConstants.Const_VideoType_Screen);
                }
                break;
        }

        // 这里需要返回false
        return false;
    }
```

### 渲染视频画面
在视频请求成功后，调用渲染控件的接口来进行渲染
```Java
public void onComplete(String[] identifierList, AVView[] viewList, int count, int result, String errMsg) {
    if (ILiveConstants.NO_ERR == result){
        for (int i=0; i<identifierList.length; i++){
            avRootView.renderVideoView(true, identifierList[i], viewList[i].videoSrcType, true);
        }
    }else {
        // Todo 失败处理
    }
}
```

## API说明

### requestUserVideoData
属于ContextEngine的方法，用于请求视频画面，参数说明如下:

|名称|类型|描述|
|--|--|--|
|identifier|String|需要请求的用户identifier|
|srcType|int|视频类型|

### removeUserVideoData
属于ContextEngine的方法，用于取消请求视频画面，参数说明如下:

|名称|类型|描述|
|--|--|--|
|identifier|String|需要请求的用户identifier|
|srcType|int|视频类型|

### renderVideoView
属于渲染控件AVRootView的方法，用于渲染一路视频画面，参数说明如下:

|名称|类型|描述|
|--|--|--|
|bHasVideo|boolean|当前是否已有画面，建议填true|
|identifier|String|需要请求的用户identifier|
|srcType|int|视频类型|
|bAutoRender|boolean|是否自动渲染(自动空闲AVVideoView渲染)，建议填true|

## 常见问题

- 请求视频画面是否需要取消?
> sdk内部是在音视频事件的has camera和no camera中成对使用，即has camera时请求，no camera时取消请求，推荐用户也这样实现，避免该用户断开后重新上行，画面会自动渲染出来。