本文将指导您的客户端加入之前所创建的房间，并与其他用户音视频互动。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[单击下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_join.zip)

## 加入房间
与创建房间类似，需要先初始化、登录之后才能加入房间；加入房间也需要先填写 iLiveRoomOption 结构体，用于描述所加入房间的相关信息，然后调用 joinRoom() 接口进行加入房间。
```c++
//房间内成员状态变化通知(如打开\关闭摄像头等)
void  OnMemStatusChange(E_EndpointEventId eventId, const Vector<String> &ids, void* data)
{
}

iLiveRoomOption roomOption;
roomOption.roomId = RoomId;                 //要加入的房间id
roomOption.authBits = AUTH_BITS_DEFAULT;    //拥有所有权限
roomOption.controlRole = "user";      //使用Spear上配置的"user"角色
roomOption.memberStatusListener = OnMemStatusChange;//房间内成员状态变化回调
roomOption.data = NULL;//在回调中原封不动传回的void*数据指针;

GetILive()->joinRoom(roomOption, [](void* data) {
	//加入房间成功
}, [](const int code, const char *desc, void* data) {
	//加入房间失败
}, NULL);
```

## 打开摄像头和麦克风

进入房间后，就可以打开摄像头和麦克风与其他用户互动了,打开摄像头和麦克风的方式与之前完全一样。
详细请参考[ 创建房间-打开摄像头和麦克风](/document/product/647/16819#.E6.89.93.E5.BC.80.E6.91.84.E5.83.8F.E5.A4.B4.E5.92.8C.E9.BA.A6.E5.85.8B.E9.A3.8E)。

## 远端视频渲染
加入房间后，SDK 会自动请求房间内其他成员的视频画面,即此时在此回调中就能拿到远端视频数据了；您需要按照之前视频渲染的方式，把远端画面渲染出来。详细请参考[ 创建房间-视频渲染](/document/product/647/16819#.E8.A7.86.E9.A2.91.E6.B8.B2.E6.9F.93)。

至此，房间内成员便可以进行音视频互动。

## 源码说明
- 测试说明
本文 Demo 和[ 创建房间 ](/document/product/647/16819)的完整 Demo 进行互通测试时，需要分别在两台电脑上进行测试，因为代码中都写死打开第一个摄像头和第一个麦克风；如果要在一台电脑上测试，需要电脑至少有两个摄像头及麦克风，且两个用户不能使用同一个设备。

## 运行结果

![](https://main.qcloudimg.com/raw/7f16017270f4be5d36d8954b85dd57d6.png)

## 常见问题

#### 进房失败，提示没有权限
确认正确配置了进房票据privateMapKey，若控制台在【帐号信息】开启【启用权限密钥】,则privateMapKey为必填字段
