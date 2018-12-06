本文将指导您的客户端使用IM功能，在房间内收发消息。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_msg.zip)
## 相关概念
本课程涉及到的概念有：
 * [群组系统](/document/product/647/16792#.E7.BE.A4.E7.BB.84.E7.B3.BB.E7.BB.9F)

|类型|名称|类|描述|
 |--|--|--|--|
 |ILiveMessage.ILIVE_MSG_TYPE_TEXT|文本消息|ILiveTextMessage|消息内容为一个字符串( String 类型 )|
|ILiveMessage.ILIVE_MSG_TYPE_CUSTOM|自定义消息|ILiveCustomMessage|消息内容为一个 byte 数组|
 |ILiveMessage.ILIVE_MSG_TYPE_OTHER|其它消息|ILiveOtherMessage|[ IMSDK消息类型 ](https://cloud.tencent.com/document/product/269/9232#1.2-.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)其它消息|

## 开启IM功能
修改房间模块中的创建和加入房间，配置 imsupport 为true 。

> 在配置imsupport为true时，createRoom会自动创建IM群组，quitRoom时创建者会自动解散群组

```
    // 创建房间
    public int createRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .imsupport(true)       // 开启IM功能
                .groupType("Public")    // 使用实时音视频聊天室(默认)
                .exceptionListener(this)
                .roomDisconnectListener(this)
                .controlRole("LiveMaster")
                .autoCamera(true)
                .autoMic(true);

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
    // 加入房间
    public int joinRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .imsupport(true)       // 开启IM功能
                .groupType("AVChatRoom")    // 使用实时音视频聊天室(默认),与创建一致
                .exceptionListener(this)
                .roomDisconnectListener(this)
                .controlRole("Guest")
                .autoCamera(false)
                .autoMic(false);

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
```

## 设置消息监听
为了全局监听，可以在每个应用中都可以监听到消息，可以创建一个消息观察者：
```Java
/**
 * 消息观察者
 */
public class MessageObservable implements ILiveMessageListener {
    // 消息监听链表
    private LinkedList<ILiveMessageListener> listObservers = new LinkedList<>();
    // 句柄
    private static MessageObservable instance;


    public static MessageObservable getInstance(){
        if (null == instance){
            synchronized (MessageObservable.class){
                if (null == instance){
                    instance = new MessageObservable();
                }
            }
        }
        return instance;
    }

    // 添加观察者
    public void addObserver(ILiveMessageListener listener){
        if (!listObservers.contains(listener)){
            listObservers.add(listener);
        }
    }

    // 移除观察者
    public void deleteObserver(ILiveMessageListener listener){
        listObservers.remove(listener);
    }

    @Override
    public void onNewMessage(ILiveMessage message) {
        // 拷贝链表
        LinkedList<ILiveMessageListener> tmpList = new LinkedList<>(listObservers);
        for (ILiveMessageListener listener : tmpList){
            listener.onNewMessage(message);
        }
    }
}
```

并在 Application 初始化的地方设置监听：
```Java
        if (MsfSdkUtils.isMainProcess(this)) {
            ILiveSDK.getInstance().initSdk(this, Constants.SDKAPPID, Constants.ACCOUNTTYPE);
            // 初始化iLiveSDK房间管理模块并设置消息监听
            ILiveRoomManager.getInstance().init(new ILiveRoomConfig()
                    .setRoomMsgListener(MessageObservable.getInstance()));
        }
```
然后只需要在关心消息的Acitivty的onCreate中设置消息监听：
```Java
MessageObservable.getInstance().addObserver(this);
```
并在onDestory中移除消息：
```Java
MessageObservable.getInstance().deleteObserver(this);
```
这样在收到消息时，就可以在Acitivty中收到 onNewMessage 事件。

## 发送消息
这里以发送文本消息为例，您可以直接在房间模块中添加一个发送群文本消息的接口：
```Java
    public void sendGroupMsg(String test){
        ILiveMessage message = new ILiveTextMessage(test);
        ILiveRoomManager.getInstance().sendGroupMessage(message, new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                // 处理发消息成功
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                // 处理发消息失败
            }
        });
    }
```

## UI开发
本文 Demo 中需要一个展示消息列表的地方，推荐使用 ListView 控件，可以盖在渲染控件上，具体实现可以自己定义。

## 常见问题

- 加入房间失败，错误模块 IMSDK，错误码 10010。
> 这表示要加入的IM群组不存在，需要检测是否先创建了群组（创建房间 imsupport 为 true 时会自动创建群组），并确认群组类型一致。
