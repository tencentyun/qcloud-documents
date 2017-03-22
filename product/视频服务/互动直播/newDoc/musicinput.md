

# 使用第三方App播放背景音乐

需求背景：主播使用第三方音乐App播放背景音乐，自己收听的同时也希望观众一起畅听。
## IOS

只需要**主播端**开启高音质即可，观众和上麦者的配置无需改变

```
//进入房间时开启高音质配置
ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
option.avOption.autoHdAudio = YES;
```

## Android
android无需配置即可支持

**注意**
> * 必须先进入房间然后才打开音乐App开启背景音乐，否则直播间会中断背景音乐
> * 主播和上麦观众的后台spear配置需要开启aec（回声消除）


