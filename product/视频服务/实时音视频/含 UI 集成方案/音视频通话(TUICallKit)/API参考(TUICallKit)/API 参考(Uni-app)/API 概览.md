## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API | 描述 |
|-----|-----|
| [login](https://cloud.tencent.com/document/product/647/78763#login) | 登录                     |
| [logout](https://cloud.tencent.com/document/product/647/78763#logout) | 登出                     |
| [setSelfInfo](https://cloud.tencent.com/document/product/647/78763#setselfinfo) | 设置用户的头像、昵称     |
| [call](https://cloud.tencent.com/document/product/647/78763#call) | 发起 1v1 通话            |
| [groupCall](https://cloud.tencent.com/document/product/647/78763#groupcall) | 发起群组通话             |
| [joinInGroupCall](https://cloud.tencent.com/document/product/647/78763#joiningroupcall) | 主动加入当前的群组通话中 |
| [setCallingBell](https://cloud.tencent.com/document/product/647/78763#setcallingbell) | 设置自定义来电铃音       |
| [enableMuteMode](https://cloud.tencent.com/document/product/647/78763#enablemutemode) | 开启/关闭静音模式        |
| [enableFloatWindow](https://cloud.tencent.com/document/product/647/78763#enablefloatwindow) | 开启/关闭悬浮窗功能      |

## TUICallObserver 
TUICallObserver 是回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](https://cloud.tencent.com/document/product/647/78764#onerror) | 通话过程中错误回调           |
| [onCallReceived](https://cloud.tencent.com/document/product/647/78764#oncallreceived) | 通话请求的回调               |
| [onCallCancelled](https://cloud.tencent.com/document/product/647/78764#oncallcancelled) | 通话取消的回调               |
| [onCallBegin](https://cloud.tencent.com/document/product/647/78764#oncallbegin) | 通话接通的回调               |
| [onCallEnd](https://cloud.tencent.com/document/product/647/78764#oncallend) | 通话结束的回调               |
