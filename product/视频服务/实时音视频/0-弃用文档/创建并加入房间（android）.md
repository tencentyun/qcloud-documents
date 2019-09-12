本文将指导您在客户端中创建一个房间，开始发布自己的个人直播秀。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_create.zip)

## 相关概念
 - [房间](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [角色配置](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - 渲染控件
 在拿到视频数据时，需要一个展示数据的平台，这个就是渲染控件，可以实际对应到一个 Android 控件。

## 添加渲染控件
首先，需要在前面的 demo 布局中添加一个控件来渲染视频：
```
<com.tencent.ilivesdk.view.AVRootView
        android:id="@+id/av_root_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```

## 创建房间模块
定义一个房间模块与 Activity 通讯的接口：
```Java
public interface IRoomView {
    // 进入房间成功
    void onEnterRoom();
    // 进房间失败
    void onEnterRoomFailed(String module, int errCode, String errMsg);

    // 退出房间成功
    void onQuitRoomSuccess();
    // 退出房间失败
    void onQuitRoomFailed(String module, int errCode, String errMsg);

    // 房间断开
    void onRoomDisconnect(String module, int errCode, String errMsg);
}
```

然后创建房间模块：
```Java
public class RoomHelper implements ILiveRoomOption.onExceptionListener, ILiveRoomOption.onRoomDisconnectListener {
    private IRoomView roomView;

    public RoomHelper(IRoomView view){
        roomView = view;
    }
    // 设置渲染控件
    public void setRootView(AVRootView avRootView){
        ILiveRoomManager.getInstance().initAvRootView(avRootView);
    }
    // 创建房间
    public int createRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .imsupport(false)       // 不需要IM功能              
                .exceptionListener(this)  // 监听异常事件处理
                .roomDisconnectListener(this)   // 监听房间中断事件
                .controlRole("user")    // 使用user角色
                .autoCamera(true)       // 进房间后自动打开摄像头并上行
                .autoMic(true);         // 进房间后自动要开Mic并上行

        return ILiveRoomManager.getInstance().createRoom(roomId, option, new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                roomView.onEnterRoom();
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                roomView.onEnterRoomFailed(module, errCode, errMsg);
            }
        });
    }
    // 退出房间
    public int quitRoom(){
        return ILiveRoomManager.getInstance().quitRoom(new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                roomView.onQuitRoomSuccess();
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                roomView.onQuitRoomFailed(module, errCode, errMsg);
            }
        });
    }

    // 处理Activity事件
    public void onPause(){
        ILiveRoomManager.getInstance().onPause();
    }
    public void onResume(){
        ILiveRoomManager.getInstance().onResume();
    }

    @Override
    public void onException(int exceptionId, int errCode, String errMsg) {
        //处理异常事件
    }

    @Override
    public void onRoomDisconnect(int errCode, String errMsg) {
        // 处理房间中断(一般为断网或长时间无长行后台回收房间)
    }
}
```

## UI 开发
同样在房间的 Activity 的 onCreate 事件中，可以上面创建的房间模块，并设置渲染控件。
```Java
roomHelper = new RoomHelper(this);
// 获取渲染控件
AVRootView avRootView = findViewById(R.id.av_root_view);
// 设置没有渲染时的背景色为蓝色(注意不支持在布局中直接设置)
avRootView.getVideoGroup().setBackgroundColor(Color.BLUE);
// 设置渲染控件
roomHelper.setRootView(avRootView);
```
界面中可以允许用户输入房间号的，并根据用户输入的房间后创建房间，也可以先直接写死（测试）。
```Java
roomHelper.createRoom(1234);
```
如果能够上抛 onEnterRoom 事件，并且能够看到自己的视频画面，那么恭喜您的房间已经成功创建了。

## 常见问题

#### 进房失败10004，提示request room server address failed
确认正确配置了进房票据privateMapKey，若控制台在【帐号信息】开启【启用权限密钥】,则privateMapKey为必填字段

#### 进房失败71，提示decodeSsoCmd_pbvideoapp_pbvideoinfoErr:user id error longConnHead.account=0
这种情况多帐号登录引起，请确认之前登录新帐号时，已注销老的帐号

#### onException 中收到 EXCEPTION_ENABLE_CAMERA_FAILED 并且 errCode 为 1，找开摄像头失败。
1. 确认 Android 设备有摄像头并且可以正常使用；
2. 确认后台没有其它应用占用摄像头；
3. 如果是 Android 6.0 以上设备需要确认已申请打开摄像头的动态权限`Manifest.permission.CAMERA`。

#### 失败回调，错误码 1003 或 8011
1. 进房/退房为线性互斥操作，若请求太频繁，sdk便会上抛 8011，这种情况需要上次操作完成(回调上抛)再继续操作(进出房间)；
2. 用户一次只能加入一个房间，所以若上次房间未退出，再次调用创建(或加入)便会上抛 1003，这种情况需要先退出上次房间；
