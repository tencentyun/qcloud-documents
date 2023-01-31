
## 功能描述
TUIKit 从 [v0.1.3](https://cloud.tencent.com/document/product/269/52049#im-flutter-tuikit.EF.BC.88.E5.90.AB-ui.EF.BC.89-0.1.3-.402022.08.03) 版本开始 ，支持表情回应功能。

“表情回应”功能采用消息编辑能力实现。

## 效果展示

### 发送表情回应

开启表情回应能力后，长按消息菜单中，靠近消息本身的方向，会多一条表情选择区。该区域支持点击“加号”扩大，展示更多表情。

| 长按消息菜单 | 更多表情 |
|---------|---------|
| <img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/d9b075b14d89d5394d22c01e43cd7e05.jpg"  /> | <img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/b6019220ec7643a8dd11fcf19f7cba56.jpg" /> |

### 展示表情回应

一条消息收到的所有回应表情，都会展示在这条消息的下方，会话中所有成员均可看到。

在消息下方，回应表情后面会显示该表情的发送人姓名，点击姓名可以触发 `onTapAvatar` 回调，以查看其Profile。

点击展示中表情，可以方便快捷回应同样的表情，或取消该表情。

当发送同一个回应表情人数过多被省略时，点击最后的“...共xx人”，可查看完整的回应成员名单。

| 表情回应消息展示 | 完整回应成员名单 |
|---------|---------|
| <img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/8ce9ece5031655cd38f5a20e25b0ed8c.jpg"  /> | <img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/678ae70ae8f810b50b0e57946306a329.jpg" /> |


## 控制表情回应

在 TIMUIKitChat 的配置参数 `config` 中，提供了“表情回应”功能开关 **isUseMessageReaction** , 其类型为 boolean，默认为 `true` 。

```dart
TIMUIKitChat(
  config: TIMUIKitChatConfig(
    isUseMessageReaction: true 或 false,
    // ... 其他 config 配置
  ),
  // ... 其他 TIMUIKitChat 参数
)
```

## 联系我们[](id:contact)

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
