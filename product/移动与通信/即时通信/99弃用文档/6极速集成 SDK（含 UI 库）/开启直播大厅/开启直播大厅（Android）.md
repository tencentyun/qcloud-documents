`TUIKit`组件在`5.0.10`以上版本开始支持直播大厅功能，并且支持 iOS 和 Android 平台的互通 ，直播大厅的实现需要额外集成`TUIKitLive`组件，请参考 [步骤2：配置工程文件](#step2) ，直播大厅界面请参考下图所示：


|              直播广场页               |              主播准备页               |              主播开播页               |
| :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| <img src="https://main.qcloudimg.com/raw/cad568b62a39ee5608e080363364db72.jpg" width="300" height="600"> | <img src="https://main.qcloudimg.com/raw/7981702bce71b8a8bb95ba4525a9b1e0.jpg" width="300" height="600"> | <img src="https://main.qcloudimg.com/raw/9ea7d501a30138378acd0b4dcb804f72.jpg" width="300" height="600"> |


## 步骤1：开通音视频服务[](id:step1)

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【开通腾讯实时音视频服务】区域的【立即开通】。
3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击【确认】。
4. 您还可以 [单击购买](https://cloud.tencent.com/act/pro/IMTRTC?from=13947) IM 专业版/旗舰版套餐包和 TRTC 时长包。
>?系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。
   	

## 步骤2：配置工程文件[](id:step2)

建议使用源码集成 `tuikit` 和 `tuikit-live`，以便于您修改源码满足自身的业务需求。
将 `tuikit` 和 `tuikit-live` 代码拷贝到自己项目中，在 `settings.gradle` 引入 `tuikit` 和 `tuikit-live module`，最后在自己项目中导入依赖。

```groovy
implementation project(':tuikit')
implementation project(':tuikit-live')
```

## 步骤3：初始化并登录 TUIKit[](id:step3)

初始化`TUIKit`需要传入 [步骤1](#Step1) 生成的 SDKAppID，并调用 `login` 登录，其中 UserSig 生成的具体操作请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。

```java
TUIKitConfigs config = new ConfigHelper().getConfigs();
TUIKit.init(this, SDKAPPID, config);
TUIKit.login(userID, userSig, new IUIKitCallBack() {
    @Override
    public void onError(String module, final int code, final String desc) {
        // 登录失败
    }

    @Override
    public void onSuccess(Object data) {
        // 登录成功
    }
});
```

## 步骤4：主播端开播[](id:step4)

创建主播端，您需要创建 `TUILiveRoomAnchorLayout` 并设置一个唯一的 roomid，即可开播。

```java
TUILiveRoomAnchorLayout layoutTuiLiverRomAnchor = findViewById(R.id.tui_liveroom_anchor_layout);
// 接收主播创建成功/退出 回调
layoutTuiLiverRomAnchor.setLiveRoomAnchorLayoutDelegate(this);
// roomId：123456，观众端也需要设置和主播端一样的roomid才可以看到该主播。这里的roomid仅用于测试，实际应该生成一个唯一的值。
layoutTuiLiverRomAnchor.initWithRoomId(getSupportFragmentManager(), 12345);
```

## 步骤5：观众端观看直播[](id:step5)

创建观众端，您需要创建 `TUILiveRoomAudienceLayout` 并设置和主播端一致的 roomId 即可观看该主播的直播。

```java
TUILiveRoomAudienceLayout roomAudienceLayout = findViewById(R.id.layout_room_audience);
// 初始化观众页，设置与主播端一致的 roomId，即可观看该主播的直播，anchorId为主播id
// useCDN 可以先设置成 false，如果您有CDN播放的需求，可以参照后面章节
roomAudienceLayout.initWithRoomId(getSupportFragmentManager(), 12345, “1280”, false, “”);
```

## 步骤6：实现直播大厅[](id:step6)

现在，您已经拥有了主播端和观众端，还需要一个直播房间列表将两者关联起来。

- 主播端创建房间成功后，将房间 ID 记录到服务端。
- 主播端销毁房间后，服务端同步销毁房间 ID。
- 观众端通过服务端拉取到房间 ID 列表，单击后进入对应房间。

由于房间列表千差万别，我们暂时未提供服务端房间列表搭建示例，您可以参考 Demo 中的 [`RoomManager`](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/scenes/net/RoomManager.java) 来实现客户端上报的逻辑。

1. 主播端创建成功后，在主播端回调函数中，上报开播、停播信息。
```java
// TUILiveRoomAnchorLayoutDelegate
// 创建房间成功回调
public void onRoomCreate(final TRTCLiveRoomDef.TRTCLiveRoomInfo roomInfo) {
    // 上报新的直播间创建成功
    RoomManager.getInstance().createRoom(roomInfo.roomId, RoomManager.TYPE_LIVE_ROOM, null);
} 

 // 退出/停止直播回调
public void onRoomDestroy(TRTCLiveRoomDef.TRTCLiveRoomInfo roomInfo) {
    // 销毁房间
    RoomManager.getInstance().destroyRoom(roomInfo.roomId, RoomManager.TYPE_LIVE_ROOM, null);
}
```
2. 创建直播大厅页 UI：
直播大厅页用于展示直播列表，具体实现请参考 Demo 中 `LiveRoomFragment.java` 的实现。
3. 单击观看：
在直播大厅页单击任意直播间，参照 [步骤5：观众端观看直播](#step5) 生成观看端即可观看。

## 步骤7：使用直播 CDN 观看[](id:step7)

创建观众端 TUILiveRoomAudienceLayout 时，如果设置 useCdn 为 false，则默认使用 TRTC 进行观看；如果设置 useCdn 为 true，且设置了 cdnDomain，则会采用 CDN 进行观看。

TRTC 采用 UDP 协议进行传输音视频数据，标准直播 CDN 则采用的 RTMP/HLS/FLV 等协议进行数据传输。TRTC 的特点是延迟低，上下麦体验更加流畅，但价格会比标准直播的 CDN 高。

若您对观看延迟要求不高，可以使用 CDN 观看，以降低成本。

#### 前提条件

已开通腾讯 [云直播](https://console.cloud.tencent.com/live) 服务。应国家相关部门的要求，直播播放必须配置播放域名，具体操作请参考 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。

#### 开启旁路推流功能

1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2. 在左侧导航栏选择【应用管理】，单击目标应用所在行的【功能配置】。
3. 在【旁路推流配置】中，单击【启用旁路推流】右侧的![](https://main.qcloudimg.com/raw/5f58afe211aa033037e5c0b793023b49.png)，在弹出的【开启旁路推流功能】对话框中，单击【开启旁路推流功能】即可开通。

#### 配置播放域名

1. 登录 [云直播控制台](https://console.cloud.tencent.com/live/)。
2. 单击【添加域名】，输入您已经备案过的播放域名，选择域名类型为【播放域名】，选择加速区域（默认为【中国大陆】），单击【确定】即可。
3. 观众端进入观看时传入播放 URL。
   当您开通好旁路推流后，主播端已经为您自动推流到云端。当观众端在观看的时候，需要您传入 CDN 直播的 URL。

```
// eg: 假设您的 配置播放域名并完成 CNAME 中设置的域名为 my.com，那么默认播放 URL 为 http://[播放域名]/live/[sdkappid]_[roomId]_[userID]_main.flv
TUILiveRoomAudienceLayout roomAudienceLayout = findViewById(R.id.layout_room_audience);
roomAudienceLayout.initWithRoomId(getSupportFragmentManager(), 12345, "12565", true, "http://[播放域名]/live/[sdkappid]_[roomId]_[userID]_main.flv");
```

>!  更多关于 TRTC 旁路直播的介绍，可以查看 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826) 和  [云端混流服务](https://cloud.tencent.com/document/product/647/16827)。


## 常见问题

### 如何自定义礼物？

TUIKit_live SDK 支持用户自定义礼物，如果修改礼物内容或来源时，请在 TUIKit_live 的 `DefaultGiftAdapterImp.java` 文件中修改服务器请求地址，或者请求逻辑；仅需保证最后返回的数据与现在的数据格式一致即可。

```java
//eg 数据格式，完整参考链接：https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gift_data.json，json字符串内容如下：
{
  "giftList": [
    {
      "giftId": "1", // 礼物id，每个礼物对应一个唯一的礼物id
      "giftImageUrl": "https://8.url.cn/huayang/resource/now/new_gift/1590482989_25.png", // 礼物面板上显示图片
      "lottieUrl": "https://assets5.lottiefiles.com/packages/lf20_t9v3tO.json", // 对应大礼物动画文件
      "price": 2989, // 礼物虚拟物品价格
      "title": "火箭", // 礼物标题
      "type": 1 // 礼物类型：1 大礼物，全屏展示  2 小礼物，消息列表顶部动效展示
    },
    {
      "giftId": "2",
      "giftImageUrl": "https://8.url.cn/huayang/resource/now/new_gift/1507876726_3",
      "lottieUrl": "",
      "price": 298,
      "title": "鸡蛋",
      "type": 0
    }
}
```

### 如何实现 PK？

如果您希望实现 PK 功能，仅需完成以下两个步骤：

1. 在主播端创建 TUILiveRoomAnchorLayout 时开启 PK。
```java 
TUILiveRoomAnchorLayout layoutTuiLiverRomAnchor = findViewById(R.id.tui_liveroom_anchor_layout);
mLayoutTuiLiverRomAnchor.initWithRoomId(getSupportFragmentManager(), 12345);
//  开启PK
layoutTuiLiverRomAnchor.enablePK(true);
layoutTuiLiverRomAnchor.setLiveRoomAnchorLayoutDelegate(this);
```
2. 在主播端 TUILiveRoomAnchorLayout 的回调函数中 getRoomPKList 设置 PK 列表数据。
```java
public void getRoomPKList(final TUILiveRoomAnchorLayout.OnRoomListCallback callback) {
    /// 如果您创建的房间需要PK功能，在这个回调通过 callback 返回可以PK的主播房间id数组。
    RoomManager.getInstance().getRoomList(RoomManager.TYPE_LIVE_ROOM, new RoomManager.GetRoomListCallback() {
        @Override
        public void onSuccess(List<String> roomIdList) {
            if (callback != null) {
                callback.onSuccess(roomIdList);
            }
        }

        @Override
        public void onFailed(int code, String msg) {
        }
    });}
```
