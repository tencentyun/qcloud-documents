本文主要介绍使用 TIM 作为同步通道。

### 平台支持

|iOS|Android|Windows|Mac OS|Web|小程序|
|:-:|:-:|:-:|:-:|:-:|:-:|
|&#10003; |&#10003; |&#10003; |&#10003; |&#10003; |&#10003;|

### 注意事项

因为实时录制会以 TIMSDK 作为信令通道，同时是以自定义消息的 extension:'TXWhiteBoardExt' 为标识，所以在同步的信令的时候需要注意以下四点：

1. 使用 TIMSDK 作为信令通道。
2. 关闭互动白板内置的信令通道。
3. 同步信令的时候发送的消息类型为自定义消息类型。
4. 自定义消息的 extension 字段必须为 TXWhiteBoardExt。

### 同步原理

![](https://main.qcloudimg.com/raw/e42ce8554f85222602e3f63b0d3478d5.jpg)

- 监听 onTEBSyncData 事件（事件名以各端实际为准），将事件中回调的数据通过信令通道进行广播。
- 收到白板信令后，调用互动白板 addSyncData 接口（接口名以各端实际为准）进行同步。

### 代码集成

**Mac/iOS**

创建自定义消息接口文档请参考 [TIM 提供的文档](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#ab0aa735c735cf82a593707b296d2a060)。

```objc
// 1. 将 TEduBoardInitParam 的 timSync 参数初始为 NO (关闭互动白板内置的信令通道)
TEduBoardInitParam *initParam = [[TEduBoardInitParam alloc] init];
initParam.timSync = NO;  // 关闭互动白板内置的信令通道
_boardController = [[TEduBoardController alloc] initWithAuthParam:authParam roomId:_classId initParam:initParam];

// 2. 监听白板信令数据回调 onTEBSyncData，将数据发送给其他白板用户
- (void)onTEBSyncData:(NSString *)data {
  NSString *groupId = @"课堂id";
  NSString *message = @"白板数据";
  NSString *ext = @"TXWhiteBoardExt";  //扩展字段信息
  TIMMessage *msg = [[TIMMessage alloc] init];
  [msg setPriority:1];
  TIMCustomElem *customElem = [[TIMCustomElem alloc] init];
  customElem.data = message;
  customElem.ext = ext;
  [msg addElem:customElem];
  TIMOfflinePushInfo *info = [[TIMOfflinePushInfo alloc] init];
  info.ext = ext;
  [msg setOfflinePushInfo:info];
          
  TIMConversation *conv = [[TIMManager shareInstance] getConversation:TEDUIM_GROUP receiver:groupId];
  if (conv) {
      [conv sendMessage:msg callback:^(int code, NSString *desc) {
          if(code == 0){
              //发送 IM 消息成功
              //信令发送成功后调用互动白板 addAckData(data)，确认数据发送状态
          }
          else {
              //发送 IM 消息失败，建议进行重试
          }
      }];
  }
}

// 3. 在收到其他用户的白板信令时，将消息传递给白板。
[_boardController addSyncData:data];
```

**Android**

创建自定义消息接口文档请参考 [TIM 提供的文档](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a313b1ea616f082f535946c83edd2cc7f)。

```java
// 1. 将 TEduBoardInitParam 的 timSync 参数初始为 NO (关闭互动白板内置的信令通道)
TEduBoardController.TEduBoardInitParam initParam = new TEduBoardController.TEduBoardInitParam(); 
initParam.timSync = false; // 关闭互动白板内置的信令通道

// 2. 监听白板信令回调 onTEBSyncData，将信令发送给其他白板用户
 @Override
  public void onTEBSyncData(String data) {
    // 创建同步白板信令自定义消息
    String groupId = "课堂id";
    String message = data;
    String ext = "TXWhiteBoardExt"; //扩展字段信息

    byte[] data = message.getBytes();
    int length = data.length;

    TIMMessageOfflinePushSettings timMessageOfflinePushSettings = new TIMMessageOfflinePushSettings();
    timMessageOfflinePushSettings.setExt(ext.getBytes());

    TIMMessage timMessage = new TIMMessage();
    timMessage.setOfflinePushSettings(timMessageOfflinePushSettings);
    timMessage.setPriority(TIMMessagePriority.High);

    TIMCustomElem timCustomElem = new TIMCustomElem();
    timCustomElem.setData(data);
    timCustomElem.setExt(ext.getBytes());
    timMessage.addElement(timCustomElem);

    TIMManager timManager = TIMManager.getInstance();
    TIMConversation timConversation = timManager.getConversation(TIMConversationType.Group, groupId);
    timConversation.sendMessage(timMessage, new TIMValueCallBack<TIMMessage>() {
        @Override
        public void onError(int i, String s) {
          // 信令发送失败，建议进行重试
        }

        @Override
        public void onSuccess(TIMMessage timMessage) {
          //信令发送成功后调用 addAckData(data)，确认数据发送状态
        }
    });
  }

// 3. 在收到其他用户的白板信令时，将信令透传给白板
mBoard.addSyncData(data);
```

**Windows**

创建自定义消息接口文档请参考 [TIM 提供的文档](https://cloud.tencent.com/document/product/269/33553#customelem)。

```cpp
// 引入IM SDK头文件
#include "TIMCloud.h"

// 这里为了演示方便，使用ostringstream来构造JSON串，生产环境建议使用第三方JSON库来生成JSON串
#include <iostream>
#include <sstream>
#include <string>


// 1. 将 TEduBoardInitParam 的 timSync 参数初始为 NO (关闭互动白板内置的信令通道)
TEduBoardInitParam initParam;
initParam.timSync = false; // 关闭互动白板内置的信令通道
boardCtrl->Init(authParam, ROOM_ID, initParam); // 使用上面构造的初始化参数

// 2. 监听白板信令回调 onTEBSyncData，将信令发送给其他白板用户
virtual void onTEBSyncData(const char * data) override {
    //使用自定义信令通道，发送 data 给其他白板用户
  std::string message = data;
  std::ostringstream json;
  json << "{";
  json << "\"" << kTIMMsgElemArray << "\":";
  json << "[{";
  json << "\"" << kTIMMsgPriority << "\": " << kTIMMsgPriority_High << ",";  // 设置消息优先级为高
  json << "\"" << kTIMElemType << "\": " << kTIMElem_Custom << ",";  // 消息类型为自定义消息 
  json << "\"" << kTIMCustomElemExt << "\": \"TXWhiteBoardExt\",";  // 扩展字段信息
  json << "\"" << kTIMCustomElemData << "\": \"" << message << "\",";  // 消息内容为白板数据
  json << "}]";
  json << "}";
  int ret = TIMMsgSendNewMsg("课堂id", kTIMConv_Group, json.str().c_str(), [](int32_t code, const char *desc, const char *json_param, const void *user_data) {
      if (ERR_SUCC == code) {  // 消息发送成功
        //信令发送成功后调用 addAckData(data)，确认数据发送状态
      } else {  // 消息发送失败，建议进行重试
      }
  }, nullptr);
  if (ERR_SUCC != ret) {  // 消息发送失败，建议进行重试
    
  }
}

// 3. 在收到其他用户的白板信令时，将信令透传给白板
boardCtrl->AddSyncData(data);
```

**Web**

创建自定义消息接口文档请参考 [TIM 提供的文档](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#createCustomMessage)。


```js
// Web没有内置TIM通道，不需要额外关闭内置TIM通道。
// 1. 在 onTEBSyncData 回调里，将数据发送给其他白板用户
teduBoard.on(TEduBoard.EVENT.TEB_SYNCDATA, data => {
  const message = tim.createCustomMessage({
    to: '课堂ID',
    conversationType: TIM.TYPES.CONV_GROUP,
    priority: TIM.TYPES.MSG_PRIORITY_HIGH,  // 因为im消息有限频，白板消息的优先级调整为最高
    payload: {
        data: '白板数据',
        description: '',
        extension: 'TXWhiteBoardExt',
    },
  });
  // 发送消息
  tim.sendMessage(message).then(() => {
    // 发送成功
    //信令发送成功后调用 addAckData(data)，确认数据发送状态
  }, (error) => {
    // 发送失败，建议进行重试
  });
});
// 3. 在收到其他用户的白板信令时，将信令透传给白板
teduBoard.addSyncData(data);
```
