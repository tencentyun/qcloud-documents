本课程讲解跨房音视频交流相关问题

## 效果图

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 点击[下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/Demo_LinkRoom.zip)
## 相关概念

** 跨房音视频交流**
两个不同房间的用户互相拉到对方的流，实现跨房间的音视频互通

## 流程图
直接发起跨房音视频交流，不需要双方互相同意，只要参数传入正确，则建立跨房音视频交流(也是本Demo的实现方式，以下简称直连跨房)
![](https://main.qcloudimg.com/raw/9ee9be2e66e64e93d867c46f22cca0e5.png)

A发起跨房音视频交流请求后，需要B同意，B同意之后A再发起跨房音视频交流，流程图如下(以下简称交互跨房)
![](https://main.qcloudimg.com/raw/f7a94d60d637051e031502ad2ad3e9d1.png)

## 直连跨房具体实现

### 准备工作
准备两台设备，分别登录两个账号，每台设备均创建不同的房间(**注意：两台设备都是创建房间，并不是一台创建一台加入**)

### 生成跨房音视频交流鉴权串
生成跨房音视频交流的鉴权字符串(强烈建议在用户后台生成)，生成规则参考[这里](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo/blob/master/doc/ILiveSDK/cross_sign.md)

### 发起跨房音视频交流

```
//toRoomId:要音视频交流的房间号
//toId:要音视频交流的房间的主播id
//authBuff:鉴权串
[[ILiveRoomManager getInstance] linkRoom:toRoomId userId:toId authBuff:sig succ:^{
    NSLog(@"跨房音视频交流成功")
} failed:^(NSString *module, int errId, NSString *errMsg) {
    if (errId == 10001) {
        NSLog(@"对方房间不存在，检查房间号是否输入错误")
    } else {
        NSLog(@"其它错误，详见错误码和错误信息")
    }
}];
```

### 取消跨房音视频交流

```
[[ILiveRoomManager getInstance] unLinkRoom:^{
    NSLog(@"取消跨房音视频交流成功");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"取消跨房音视频交流失败，错误详情参考具体错误码和错误消息");
}];
```

## 交互跨房具体实现
### 发起跨房连音视频交流请求
```
//发起跨房音视频交流请求，toId：要音视频交流的对方的id
[[TILLiveManager getInstance] linkRoomRequest:toId succ:^{
    NSLog(@"跨房音视频交流请求成功");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"跨房音视频交流请求失败");
}];
```

### 接受跨房音视频交流请求
```
//需监听onCustomMessage回调事件
//收到跨房音视频交流请求，选择接受音视频交流请求
- (void)onCustomMessage:(ILVLiveCustomMessage *)msg
{
    int cmd = msg.cmd;
    if (msg.type == ILVLIVE_IMTYPE_C2C)
    {
        switch (cmd)
        {
              case ILVLIVE_IMCMD_LINKROOM_REQ:
              {
                  [[TILLiveManager getInstance] acceptLinkRoom:msg.sendId succ:^{
                      NSLog(@"accpet succ");
                  } failed:^(NSString *module, int errId, NSString *errMsg) {
                      NSLog(@"accpet fail");
                  }];
             }
                  break;

             default:
                  break;
      }
   }
}
```

### 拒绝跨房音视频交流请求

```
//收到跨房音视频交流请求，选择拒绝音视频交流请求
- (void)onCustomMessage:(ILVLiveCustomMessage *)msg
{
    int cmd = msg.cmd;
    if (msg.type == ILVLIVE_IMTYPE_C2C)
    {
        switch (cmd)
        {
            case ILVLIVE_IMCMD_LINKROOM_REQ:
            {
                [[TILLiveManager getInstance] refuseLinkRoom:msg.sendId succ:^{
                    NSLog(@"refuse succ");
                } failed:^(NSString *module, int errId, NSString *errMsg) {
                    NSLog(@"refuse fail");
                }];
            }
                break;

            default:
                break;
       }
    }
}
```

### 发起跨房音视频交流
```
//收到对方接收请求的消息之后，开始真正的跨房音视频交流
- (void)onCustomMessage:(ILVLiveCustomMessage *)msg
{
    int cmd = msg.cmd;
    if (msg.type == ILVLIVE_IMTYPE_C2C)
    {
        switch (cmd)
        {
            case ILVLIVE_IMCMD_LINKROOM_ACCEPT:
            {
                NSString *toRoomId = [[NSString alloc] initWithData:msg.data encoding:NSUTF8StringEncoding];
                NSString *linkSig = @"";
                [[TILLiveManager getInstance] linkRoom:[toRoomId intValue] userId:msg.sendId authBuff:linkSig succ:^{
                    NSLog(@"连接成功");
                } failed:^(NSString *module, int errId, NSString *errMsg) {
                    NSLog(@"连接失败");
                }];
            }
                break;

            default:
                break;
       }
    }
}
```

## 超出音视频交流房间数限制

```
//目前跨房音视频交流上限为3，也就是说同一个房间最多和另外3个房间建立跨房连接，如果已经有3路跨房音视频交流，再次收到跨房音视频交流邀请时，ILiveSDK内部会自动发送一个超出限制的消息，告知对方，已经达到跨房音视频交流上限，不能再开启跨房连麦了。
- (void)onCustomMessage:(ILVLiveCustomMessage *)msg
{
    int cmd = msg.cmd;
    if (msg.type == ILVLIVE_IMTYPE_C2C)
    {
        switch (cmd)
        {
            case ILVLIVE_IMCMD_LINKROOM_LIMIT:
            {
                NSLog(@"对方跨房音视频交流画面已经到达上限，无法建立跨房音视频交流");
            }
                break;

            default:
               break;
       }
    }
}
```


## 常见问题
* 1 跨房音视频交流鉴权Sig的生成方式，参考[这里](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo/blob/master/doc/ILiveSDK/cross_sign.md)

## 联系邮箱
如果对上述文档有不明白的地方，请反馈到trtcfb@qq.com
