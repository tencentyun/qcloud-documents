
## 功能描述
TUIKit 分别从 [6.2.2363](https://cloud.tencent.com/document/product/269/1606#6.2.2363-.402022.04.29---.E5.A2.9E.E5.BC.BA.E7.89.88) 和 [6.3.2609](https://cloud.tencent.com/document/product/269/1606#6.3.2619-.402022.06.29---.E5.A2.9E.E5.BC.BA.E7.89.88) 版本开始支持“群聊消息已读回执”与“单聊消息已读回执”功能。

> ! “消息已读回执”功能仅旗舰版套餐支持，使用前请确认已开通旗舰版套餐。


## 效果展示

### 单聊消息已读回执

通过消息左侧 “已读” / “未读” 标签展示。

<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/7c41cb7cb5ec8b11a5dcf0f3808e52ca/%E5%8D%95%E8%81%8A%E5%B7%B2%E8%AF%BB2.png"  />

### 群聊消息已读回执

消息左侧显示消息阅读情况：无人阅读时，显示"未读"；部分人阅读时，显示“x人已读”，x 为已经阅读消息的人数；所有人已读时，显示“全部已读”。

### 消息列表

<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/59ca752a93309eb93259bd61b83047d2/%E7%BE%A4%E5%B7%B2%E8%AF%BB%E5%9B%9E%E6%89%A72.png"  />


### 已读回执详情
点击“x人已读”即可进入已读回执详情页面，“未读”、“全部已读”不可点击。

<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">已读 群成员 <br></th>
    <th style="text-align:center;" width="300px">未读 群成员<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/e539ce90fa5fd48800edf16b4fb5dc46/%E7%BE%A4%E5%9B%9E%E6%89%A7%E5%B7%B2%E8%AF%BB2.png"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/5bec8ae768860e8a1dc4be31d7d8fab5/%E7%BE%A4%E5%9B%9E%E6%89%A7%E6%9C%AA%E8%AF%BB2.png" />     </td>
	 </tr>
</table>


## 开启消息已读回执

在 `TUIChat`组件的 [TUIChatConfig](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/TUIKit/TUIChat/CommonModel/TUIChatConfig.h) 配置参数中，提供了“消息已读回执”功能开关 **msgNeedReadReceipt** , 其类型为 BOOL，默认为 `NO` 。

```Java
- (id)init
{
    self = [super init];
    if(self){
        //...其他配置
        self.msgNeedReadReceipt = NO;
    }
    return self;
}
```
如果想开启消息已读回执功能，首先请开通旗舰套餐包，然后把 **msgNeedReadReceipt** 的默认值改为 `YES` ，或者在聊天页面初始化之前调用以下方法来开启。
```java
TUIChatConfig.defaultConfig.msgNeedReadReceipt = YES;
```

## 常见问题

### Error: 套餐包不支持该接口的使用，请升级到旗舰版套餐

“消息已读回执” 功能仅旗舰版套餐支持，该报错信息表示您当前的套餐包不支持此能力，请登录 [即时通信 IM 购买页](https://buy.cloud.tencent.com/avc) 开通旗舰版套餐包进行体验。

### 6.3.2609 之前版本的单聊已读回执功能不需要开通旗舰版套餐也可以使用，为什么 6.3.2609 之后需要开通旗舰版套餐包了？

6.3.2609 版本之前的单聊已读回执无法针对单条消息上报已读，只能批量上报整条会话所有的消息已读。6.3.2609 及之后的版本使用了旗舰版套餐包专属的 [消息已读回执](https://cloud.tencent.com/document/product/269/75343) 功能，可以针对单条消息上报已读，使用体验更好。如果想回退到旧版本方案，可以参考 [TUIKit 恢复旧版 C2C 已读上报指引](https://docs.qq.com/doc/DWWRPaHpSQ0hpZlVI)。


## 交流与反馈[](id:feedback)
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/>