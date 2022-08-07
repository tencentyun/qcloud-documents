## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallKit 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallKit 实例（单例模式）|
| [setSelfInfo](#setSelfInfo) | 设置用户的头像、昵称|
| [call](#call) | 发起 1v1 通话|
| [groupCall](#groupCall) | 发起群组通话|
| [joinInGroupCall](#joinInGroupCall) | 主动加入当前的群组通话中 |
| [setCallingBell](#setCallingBell) | 设置自定义来电铃音 |
| [enableMuteMode](#enableMuteMode) | 开启/关闭静音模式 |
| [enableFloatWindow](#enableFloatWindow) | 开启/关闭悬浮窗功能 |
