TUIkit 是腾讯云音视频团队在5000+客户的服务积累中，结合业内主流的音视频场景，提炼出的开源解决方案，包含视频通话组件、直播组件、视频房间组件等多个客户端音视频组件，可以帮助开发者快速搭建诸如通话、客服、直播、语聊、教育等场景解决方案。

## TUIKit 全家桶
![](https://qcloudimg.tencent-cloud.cn/raw/22b2ed779af3b76550ae5eefc8704e4c.png)

如上图所示，TUIKit 分为 TUICompenont 和 TUIWidget 两种，同时支持可选的基础后台服务。
```java
├── TUIComponent
│   ├── TUICalling     // 通话组件（类微信通话），针对视频通话、客服、金融审核等音视频场景；
│   ├── TUIRoom        // 多人视频房间组件，针对教育、会议、面试等音视频场景，具备禁言禁画等功能；
│   ├── TUILiveVoice   // 语聊直播组件，针对交友语聊、排队语聊，音乐房等音频场景； 
│   ├── TUILiveVideo   // 视频互动直播组件，具备连麦、PK、音效等功能；
│   ├── TUIChatSolon   // 语音沙龙组件，针对商务圆桌，兴趣论坛等音视频场景；
│   ├── TUIPusher      // 含完整UI的推流组件，支持多种协议推流，PK等功能，支持挂载音效、弹幕等挂件；
│   ├── TUIPusher      // 含完整UI的播放组件，支持多种协议播放，连麦主播等功能，支持挂载礼物、弹幕等挂件；
│   ├── TUIPlayer      // 创新组件，针对在线KTV等新玩法的音视频的组件，可以搭配腾讯云正版曲库解锁更多玩法；
│   ├── TUIChorus       // 创新组件，针对合唱的音视频新玩法的音视频组件，可以搭配腾讯云正版曲库解锁更多玩法；
│   ├── TUIKaraoke      // 创新组件，针对在线KTV等新玩法的音视频的组件，可以搭配腾讯云正版曲库解锁更多玩法；
├── TUWidget
│   ├── TUIBeauty      // 美颜挂件
│   ├── TUIAudioEffect // 音效挂件
│   ├── TUIBarrage     // 弹幕挂件
│   ├── TUIGift        // 礼物挂件
├── aPass （可选）
│   ├── Room Service   // 提供房间列表、房间热度、主播列表等功能；
```

## 交流&反馈
当然，一样的环境，一样的步骤，可能也会有不一样的报错，这是工程师的逃不开的魔咒，您可以通过如下方式来尝试解决：
- [TUIKit 常见问题](https://cloud.tencent.com/developer/article/1952880)
- **TUIKit 技术交流 QQ 群：592465424**
 ![](https://qcloudimg.tencent-cloud.cn/raw/fa8a9ca2a400319a1e7362706e6ed69d.png)
- [更多联系](https://cloud.tencent.com/document/product/647/19906)
