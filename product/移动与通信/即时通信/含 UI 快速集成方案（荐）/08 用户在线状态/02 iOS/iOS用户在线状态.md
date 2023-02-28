
## 功能描述

TUIKit 从 [6.5.2803](https://cloud.tencent.com/document/product/269/1606#6.5.2803-.402022.07.15---.E5.A2.9E.E5.BC.BA.E7.89.88) 版本开始支持用户在线状态展示。

开启“显示用户在线状态” 后，会在会话列表和联系人列表的用户头像上显示用户的在线状态。当绿圈出现时表示对方在线，灰色圆圈则表示对方当前离线。
关闭“显示用户在线状态” 时，不再显示好友的用户在线状态。
> ! 
>
> - “用户在线状态”功能仅旗舰版套餐支持，使用前请确认已开通旗舰版套餐。
> - “用户在线状态”功能需要在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 打开用户状态开关，使用前请确认开关已经打开。

## 开启用户在线状态

在 `TUICore` 组件的 [TUIConfig](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/TUIKit/TUICore/TUIConfig.h) 类中提供了“用户在线状态”功能开关 **displayOnlineStatusIcon** , 其类型为 BOOL，默认为 NO 。

```Java
- (id)init
{
    self = [super init];
    if(self){
        //...其他配置
        self.displayOnlineStatusIcon = NO;
    }
    return self;
}
```
如果想开启会话列表展示用户在线状态功能，首先请开通旗舰套餐包，然后在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)  打开用户状态配置的功能开关，再将 **displayOnlineStatusIcon** 的默认值改为 `YES` ，或者在会话页面初始化之前调用以下方法来开启。

```JAVA
[TUIConfig defaultConfig].displayOnlineStatusIcon = YES;
```

## 效果展示

### 会话列表
<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">开启“显示用户在线状态” <br></th>
    <th style="text-align:center;" width="300px">关闭“显示用户在线状态”<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/1d308f09d978076887587b42dcd7682b.png"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/5c33edc849b2dc4492bd5db4ae53cd85.png" />     </td>
	 </tr>
</table>

### 联系人列表

<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">开启“显示用户在线状态” <br></th>
    <th style="text-align:center;" width="300px">关闭“显示用户在线状态”<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/72447d6591fe84a090879aad90b68fcb.png"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/0246a3976239be54d034aa20ea43b28b.png" />     </td>
	 </tr>
</table>

## 常见问题

### 调用订阅/取消订阅接口时，接口提示 “72001” 的错误码

72001 错误码表示在控制台上并没有开启对应的能力，请登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)  打开对应的功能开关。

![](https://qcloudimg.tencent-cloud.cn/raw/bae708cef66717ef0e1298a26cafff81.png)

### Error: 套餐包不支持该接口的使用，请升级到旗舰版套餐

“用户在线状态”功能仅旗舰版套餐支持，该报错信息表示您当前的套餐包不支持此能力，请登录 [即时通信 IM 购买页](https://buy.cloud.tencent.com/avc) 开通旗舰版套餐包进行体验。


## 交流与反馈[](id:feedback)
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/>

