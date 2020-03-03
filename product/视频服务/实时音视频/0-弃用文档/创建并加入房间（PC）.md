本文将指导您在客户端中创建一个房间，打开摄像头和麦克风，并看到自己的视频画面。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_create.zip)

## 相关概念
 - [房间](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [角色配置](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - 视频渲染
 在拿到视频数据时，需要将视频数据绘制显示出来，此过程即为视频渲染。

## 设置视频数据回调
为了拿到视频数据，在创建/加入房间之前，还需要先设置本地和远端视频数据的回调函数。
```c++
//本地视频数据回调
void OnLocalVideo(const LiveVideoFrame* video_frame, void* data)
{
}

//远端视频数据回调
void OnRemoteVideo(const LiveVideoFrame* video_frame, void* data)
{
}

GetILive()->setLocalVideoCallBack(OnLocalVideo, NULL);
GetILive()->setRemoteVideoCallBack(OnRemoteVideo, NULL);
```

## 创建房间
创建房间需要先填写一个结构体 iLiveRoomOption ,它描述了所创建房间的相关信息,示例代码如下：
```c++
//房间内成员状态变化通知(如打开\关闭摄像头等)
void  OnMemStatusChange(E_EndpointEventId eventId, const Vector<String> &ids, void* data)
{
}

iLiveRoomOption roomOption;
roomOption.roomId = RoomId;                 //要创建的房间id
roomOption.authBits = AUTH_BITS_DEFAULT;    //拥有所有权限
roomOption.controlRole = "LiveMaster";      //使用Spear上配置的"LiveMaster"角色
roomOption.memberStatusListener = OnMemStatusChange;//房间内成员状态变化回调
roomOption.data = NULL;//在回调中原封不动传回的void*数据指针;

GetILive()->createRoom(roomOption, [](void* data) {
	//创建房间成功
}, [](const int code, const char *desc, void* data) {
	//创建房间失败
}, NULL);
```

## 打开摄像头和麦克风
在创建房间后，此时已经在房间中了，不需要再调用加入房间；此时，就可以打开摄像头、麦克风，进行音视频数据的上行了。
```c++
//打开摄像头
Vector< Pair<String/*id*/, String/*name*/> > cameraList;
GetILive()->getCameraList(cameraList);//获取可用摄像头列表
if (cameraList.size() > 0 )
{
	GetILive()->openCamera(cameraList[0].first); //打开第一个摄像头(默认摄像头)
}

//打开麦克风
Vector< Pair<String/*id*/, String/*name*/> > micList;
GetILive()->getMicList(micList);//获取可用麦克风列表
if (micList.size() > 0)
{
	GetILive()->openMic(micList[0].first); //打开第一个麦克风(默认麦克风);
}
```

此时，前面设置的回调函数OnLocalVideo会收到每一帧视频数据了；可以在回调中打印输出每一帧视频的数据大小，验证确实收到视频数据了。

```c++
void OnLocalVideo(const LiveVideoFrame* video_frame, void* data)
{
	printf("frame size: %d\n", video_frame->dataSize);
}
```

## 视频渲染
前面已经收到本地摄像头的视频数据了，要看到视频画面，还需要对收到的视频画面进行渲染。iLiveSDK 提供了渲染模块( iLiveRootView )，为渲染模块指定一个窗口句柄，并往渲染模块中添加 view( 要渲染画面的用户信息 )，最后，将每一帧视频画面传给渲染模块，即可进行渲染。请您仔细阅读[ 渲染模块使用文档 ](/document/product/647/16919),并结合本例 Demo 源码进行理解。

## 界面设计
本例 Demo，为了兼容后面课程，创建了一个窗口，上半部分显示本地视频画面，下半部分显示远端视频画面，示意图如下：

![](https://main.qcloudimg.com/raw/a1fee03da78f0a145bb2fd06a62a5b27.png)

为降低 demo 的复杂度，此 demo 只演示两人音视频互通的情况，实际开发中，用户可以根据需要添加多个渲染视图。

## 运行结果

![](https://main.qcloudimg.com/raw/1f1677b779f36f761bfef6a0d5282c15.png)

## 常见问题

#### 进房失败，提示没有权限
确认正确配置了进房票据privateMapKey，若控制台在【帐号信息】开启【启用权限密钥】,则privateMapKey为必填字段


#### 控制台输出一些无用信息:

在调用 SDK 某些接口时，控制台可能输出一些无用信息，例如，创建房间的输出如下图：

![](https://main.qcloudimg.com/raw/b849f6239ca311d2d72a381db455d623.png)

这是因为 iLiveSDK 内部使用了其他 SDK，这是其他 SDK 的打印输出信息，不会影响实际使用,忽略不管即可。
