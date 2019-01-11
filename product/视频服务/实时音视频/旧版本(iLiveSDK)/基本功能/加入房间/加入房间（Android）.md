本文将指导您的客户端加入一个房间，并自己打开摄像头麦克风与其他用户互动。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[ Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_join.zip)

## 相关概念
* [实时音视频应用](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
* [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
* [角色配置](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
* 摄像头 id （cameraId）
  Andorid 手机中一般有两个摄像头: 前置摄像头和后置摄像头，SDK 通过 cameraId 来区分。

|常量|描述|
|--|--|
|ILiveConstants.NONE_CAMERA|无效摄像头 id(一般表示摄像头未开启)|
|ILiveConstants.FRONT_CAMERA|前置摄像头 id|
|ILiveConstants.BACK_CAMERA|后置摄像头 id|

## 加入房间
加入房间与[ 创建房间 ](/document/product/647/16806)中的房间模块基本一致，不同的是这里需要的方式是  joinRoom。
```Java
    // 加入房间
    public int joinRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .imsupport(false)       // 不需要IM功能
                .exceptionListener(this)  // 监听异常事件处理
                .roomDisconnectListener(this)   // 监听房间中断事件
                .controlRole("user")  // 使用user角色
                .autoCamera(false)       // 进房间后不需要打开摄像头
                .autoMic(false);         // 进房间后不需打开Mic

        return ILiveRoomManager.getInstance().joinRoom(roomId, option, new ILiveCallBack() {
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
```

## 打开采集设备（摄像头和麦克风）
如果需要上行音视频与其他用户互动，您就需要在房间模块中添加两个接口分别用于控制摄像头和麦克风。
```
    // 摄像头
    public int enableCamera(int cameraId, boolean enable){
        return ILiveRoomManager.getInstance().enableCamera(cameraId, enable);
    }
    // 麦克风
    public int enableMic(boolean enable){
        return ILiveRoomManager.getInstance().enableMic(enable);
    }
```

## UI开发
界面中我们可以丰富一些，在渲染控件上层布局一组按钮，用于切换角色，开关摄像头和麦克风。
这里就不具体赘述。

## 常见问题
#### 进房失败，提示没有权限
确认正确配置了进房票据privateMapKey，若控制台在【帐号信息】开启【启用权限密钥】,则privateMapKey为必填字段
