## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API | 描述 |
|-----|-----|
| [login](https://tcloud-doc.isd.com/document/product/647/78763?!preview#login) | 登录                     |
| [logout](https://tcloud-doc.isd.com/document/product/647/78763?!preview#logout) | 登出                     |
| [setSelfInfo](https://tcloud-doc.isd.com/document/product/647/78763?!preview#setselfinfo) | 设置用户的头像、昵称     |
| [call](https://tcloud-doc.isd.com/document/product/647/78763?!preview#call) | 发起 1v1 通话            |
| [groupCall](https://tcloud-doc.isd.com/document/product/647/78763?!preview#groupcall) | 发起群组通话             |
| [joinInGroupCall](https://tcloud-doc.isd.com/document/product/647/78763?!preview#joiningroupcall) | 主动加入当前的群组通话中 |
| [setCallingBell](https://tcloud-doc.isd.com/document/product/647/78763?!preview#setcallingbell) | 设置自定义来电铃音       |
| [enableMuteMode](https://tcloud-doc.isd.com/document/product/647/78763?!preview#enablemutemode) | 开启/关闭静音模式        |
| [enableFloatWindow](https://tcloud-doc.isd.com/document/product/647/78763?!preview#enablefloatwindow) | 开启/关闭悬浮窗功能      |

## TUICallObserver 
TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](https://tcloud-doc.isd.com/document/product/647/78764?!preview#onerror) | 通话过程中错误回调           |
| [onCallReceived](https://tcloud-doc.isd.com/document/product/647/78764?!preview#oncallreceived) | 通话请求的回调               |
| [onCallCancelled](https://tcloud-doc.isd.com/document/product/647/78764?!preview#oncallcancelled) | 通话取消的回调               |
| [onCallBegin](https://tcloud-doc.isd.com/document/product/647/78764?!preview#oncallbegin) | 通话接通的回调               |
| [onCallEnd](https://tcloud-doc.isd.com/document/product/647/78764?!preview#oncallend) | 通话结束的回调               |
