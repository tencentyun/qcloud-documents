## 消息发送

### 通用消息发送

#### 会话获取

会话是指面向一个人或者一个群组的对话，通过与单个人或群组之间会话收发消息，发消息时首先需要先获取会话，获取会话需要指定会话类型（群组或者单聊），以及会话对方标志（对方帐号或者群号）。获取会话由`getConversation`实现。
>!如果本地没有这个会话，调用会话 TIMConversation 的 API 会失败。建议在收到 TIMUserConfig > TIMRefreshListener 回调后再去操作 TIMConversation 对象。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  获取会话
 *
 *  @param type 会话类型，TIM_C2C 表示单聊 TIM_GROUP 表示群聊
 *  @param conversationId C2C 为对方帐号identifier， GROUP 为群组 ID
 *
 *  @return 会话对象
 */
- (TIMConversation*)getConversation:(TIMConversationType)type receiver:(NSString*)conversationId;
@end
```

**参数说明：**

参数 | 说明
---|---
type | 会话类型，如果是单聊，填写 TIM_C2C，如果是群聊，填写 TIM_GROUP
conversationId | 会话标识，单聊情况下，receiver 为对方帐号 identifier，群聊情况下，receiver 为群组 ID

**获取对方 `identifie`r 为『iOS-001』的单聊会话：**

```
TIMConversation * c2c_conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS-001"];
```

**获取群组 ID 为『TGID1JYSZEAEQ』的群聊会话示例：** 

```
TIMConversation * grp_conversation = [[TIMManager sharedInstance] getConversation:TIM_GROUP receiver:@"TGID1JYSZEAEQ"];
```

#### 消息发送

通过 `TIMManager` 获取会话 `TIMConversation` 后，可发送消息和获取会话缓存消息。IM SDK 中消息的解释可参阅 [IM SDK 基本概念](https://cloud.tencent.com/document/product/269/9147)。IM SDK 中的消息由 `TIMMessage` 表达， 一个 `TIMMessage` 由多个 `TIMElem` 组成，每个 `TIMElem` 可以是文本和图片，也就是说每一条消息可包含多个文本和多张图片。发消息通过 `TIMConversation` 的成员 `sendMessage` 实现，有两种方式实现，一种使用闭包，另一种调用方实现 `protocol` 回调。

![](https://main.qcloudimg.com/raw/6bf979993ac8490ce53f68256e05ef01.png)


**原型：**

```
@interface TIMConversation : NSObject
-(int) sendMessage: (TIMMessage*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数 | 说明
--- | ---
msg | 消息
succ | 成功回调
fail | 失败回调

### 文本消息发送

文本消息由 `TIMTextElem` 定义。

```
@interface TIMTextElem : TIMElem {
    NSString * text;
}
```

**示例：**


>?
>- text 传递需要发送的文本消息。
>- 失败回调中，code 表示错误码，具体可参阅 [错误码](https://cloud.tencent.com/doc/product/269/1671)，err 表示错误描述。

```
TIMTextElem * text_elem = [[TIMTextElem alloc] init];

[text_elem setText:@"this is a text message"];

TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:text_elem];

[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 图片消息发送

图片消息由 `TIMImageElem` 定义。它是 `TIMElem` 的一个子类，也就是说图片也是消息的一种内容。 发送图片的过程，就是将 `TIMImageElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。发送图片时，只需要设置图片路径 `path`。发送成功后可通过 `imageList` 获取所有图片类型。另外通过 `TIMUserConfig -> TIMUploadProgressListener` 监听当前上传进度。

**`TIMImageElem` 原型：**

```
/**
 *  存储要发送的图片路径，必须是本地路径，可参考下面示例
 */
@interface TIMImageElem : TIMElem
/**
 *  要发送的图片路径
 */
@property(nonatomic,retain) NSString * path;
/**
 *  发送时不用关注，接收时保存生成的图片所有规格
 */
@property(nonatomic,retain) NSArray * imageList;
/**
 * 上传时任务Id，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
 */
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;

/**
 *  图片压缩等级，详见 TIM_IMAGE_COMPRESS_TYPE（仅对 jpg 格式有效）
 */
@property(nonatomic,assign) TIM_IMAGE_COMPRESS_TYPE level;

/**
 *  图片格式，详见 TIM_IMAGE_FORMAT
 */
@property(nonatomic,assign) TIM_IMAGE_FORMAT format;
@end
```

**参数说明：**

|参数 | 说明|
|---|---|
|path | 存储要发送的图片路径，必须是本地路径，可参考图片发送示例 |
|imageList | 发送时不用关注，接收时保存生成的图片所有规格，可以参阅图片消息接收部分|
|taskId | 发送图片时用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）|
|level | 发送图片前对图片进行压缩，level 表示压缩等级，详见 TIM_IMAGE_COMPRESS_TYPE 定义|
|format | 图片格式，详见 TIM_IMAGE_FORMAT|

以下示例中发送了一张绝对路径是 `/xxx/imgPath.jpg` 的图片。**示例：**

```
/**
*  获取聊天会话, 以同用户 iOS-001 的单聊为例
*/
TIMConversation * c2c_conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS-001"];
/**
*  构造一条消息
*/
TIMMessage * msg = [[TIMMessage alloc] init];
/**
*  构造图片内容
*/
TIMImageElem * image_elem = [[TIMImageElem alloc] init];
image_elem.path = @"/xxx/imgPath.jpg";
/**
*  将图片内容添加到消息容器中
*/
[msg addElem:image_elem];
/**
*  发送消息
*/
[conversation sendMessage:msg succ:^(){  //成功
       NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {  //失败
       NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 表情消息发送

表情消息由 `TIMFaceElem` 定义，IM SDK 并不提供表情包，如果开发者有表情包，可使用 `index` 存储表情在表情包中的索引，由用户自定义，或者直接使用 `data` 存储表情二进制信息以及字符串 `key`，都由用户自定义，SDK 内部只做透传。

```
@interface TIMFaceElem : TIMElem
/**
 *  表情索引，用户自定义
 */
@property(nonatomic, assign) int index;
/**
 *  额外数据，用户自定义
 */
@property(nonatomic,retain) NSData * data;
@end
```

**参数说明：**

>?index 和 data 只需要传入一个即可，IM SDK 只是透传这两个数据。

参数 | 说明
---|---
index|表情索引标号，由开发者定义
data|表情二进制数据，由开发者定义

以下示例中发送了索引为10的表情，具体10标识哪种表情，需要开发者在两端都持有一份表情包，索引到编号为10的表情，也可以通过 data 通过二进制数据来标识。**示例：**

```
TIMFaceElem * face_elem = [[TIMFaceElem alloc] init];

[face_elem setIndex:10];

TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:face_elem];

[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 语音消息发送

语音消息由 `TIMSoundElem` 定义，其中 `data` 存储语音数据，语音数据需要提供时长信息，以秒为单位。

>!
>- 一条消息只能有一个语音 `Elem`，添加多条语音 `Elem` 时，`AddElem` 函数返回错误1，添加不生效。
>- 语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示，而且语音和文件 `Elem` 也不保证按照发送的 `Elem` 顺序排序。 

```
/**
 *  语音消息 Elem
 */
@interface TIMSoundElem : TIMElem
/**
 *  上传时任务 ID，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
 */
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;
/**
 *  上传时，语音文件的路径，接收时使用 getSound 获得数据
 */
@property(nonatomic,strong) NSString * path;
/**
 *  存储语音数据
 */
@property(nonatomic,retain) NSData * data;
/**
 *  语音消息内部 ID
 */
@property(nonatomic,strong) NSString * uuid;
/**
 *  语音数据大小
 */
@property(nonatomic,assign) int dataSize;
/**
 *  语音长度（秒），发送消息时设置
 */
@property(nonatomic,assign) int second;

/**
 *  获取语音的 URL 下载地址
 *
 *  @param urlCallBack 获取 URL 地址回调
 */
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
 *  获取语音数据到指定路径的文件中
 *
 *  getSound 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 语音保存路径
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getSound:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  获取语音数据到指定路径的文件中（有进度回调）
 *
 *  getSound 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 语音保存路径
 *  @param progress 语音下载进度
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getSound:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

|参数|说明|
|---|---|
|path|上传语音的文件路径|
|uuid|上传成功以后会生成唯一的标识，用户可以根据此标识保存文件，IM SDK 内部不会保存资源数据|
|dataSize|语音数据大小|
|second|语音长度|

**示例：**

```
TIMSoundElem * sound_elem = [[TIMSoundElem alloc] init];
[sound_elem setPath:@"./xxx.mp3"];
[sound_elem setSecond:10];
TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:sound_elem];
[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 地理位置消息发送

地理位置消息由 `TIMLocationElem` 定义，其中 `desc` 存储位置的描述信息，`longitude`、`latitude`分别表示位置的经度和纬度。

```
@interface TIMLocationElem : TIMElem
/**
 *  地理位置描述信息，发送消息时设置
 */
@property(nonatomic,retain) NSString * desc;
/**
 *  纬度，发送消息时设置
 */
@property(nonatomic,assign) double latitude;
/**
 *  经度，发送消息时设置
 */
@property(nonatomic,assign) double longitude;
@end
```

**示例：**

```
NSString *desc= @"腾讯大厦";
TIMLocationElem * location_elem = [[TIMLocationElem alloc] init];
[location_elem setDesc:desc];
[location_elem setLatitude:113.93];
[location_elem setLongitude:22.54];
TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:location_elem];
[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 小文件消息发送

文件消息由 `TIMFileElem` 定义，另外还可以提供额外的显示文件名信息。

>! 语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示。

```
/**
 *  文件消息 Elem
 */
@interface TIMFileElem : TIMElem
/**
 *  上传时任务 ID，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
 */
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;
/**
 *  上传时，文件的路径（设置 path 时，优先上传文件）
 */
@property(nonatomic,strong) NSString * path;
/**
 *  文件内部 ID
 */
@property(nonatomic,strong) NSString * uuid;
/**
 *  文件大小
 */
@property(nonatomic,assign) int fileSize;
/**
 *  文件显示名，发消息时设置
 */
@property(nonatomic,strong) NSString * filename;

/**
 *  获取文件的 URL 下载地址
 *
 *  @param urlCallBack 获取 URL 地址回调 
 */
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
 *  获取文件数据到指定路径的文件中
 *
 *  getFile 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 文件保存路径
 *  @param succ 成功回调，返回数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getFile:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  获取文件数据到指定路径的文件中（有进度回调）
 *
 *  getFile 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 文件保存路径
 *  @param progress 文件下载进度
 *  @param succ 成功回调，返回数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getFile:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
path | 文件路径
data | 要发送的文件二进制数据。如设置 path，可不用设置 data，二者只需要设置一个字段即可，推荐使用 path
filename | 文件名，IM SDK 不校验是否正确，只透传

**示例：**

```
TIMFileElem * file_elem = [[TIMFileElem alloc] init];
[file_elem setPath:./xxx/a.txt];
[file_elem setFilename:@"a.txt"];
TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:file_elem];
[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 自定义消息发送

自定义消息是指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，内容全部由开发者定义，IM SDK 只负责透传。另外如果需要 iOS APNs 推送，还需要提供一段推送文本描述，方便展示。自定义消息由 `TIMCustomElem` 定义，其中 `data`存储消息的二进制数据，其数据格式由开发者定义。一条消息内可以有多个自定义 `Elem`，并且可以跟其他 `Elem` 混合排列，离线 `Push` 时叠加每个 `Elem` 的 `desc` 描述信息进行下发。

```
/**
 *  自定义消息类型
 */
@interface TIMCustomElem : TIMElem
/**
 *  自定义消息二进制数据
 */
@property(nonatomic,strong) NSData * data;
/**
 *  自定义消息描述信息，做离线Push时文本展示（已废弃，请使用 TIMMessage 中 offlinePushInfo 进行配置）
 */
@property(nonatomic,strong) NSString * desc DEPRECATED_ATTRIBUTE;
/**
 *  离线Push时扩展字段信息（已废弃，请使用 TIMMessage 中 offlinePushInfo 进行配置）
 */
@property(nonatomic,strong) NSString * ext DEPRECATED_ATTRIBUTE;
/**
 *  离线Push时声音字段信息（已废弃，请使用 TIMMessage 中 offlinePushInfo 进行配置）
 */
@property(nonatomic,strong) NSString * sound DEPRECATED_ATTRIBUTE;
@end
```

**参数说明：**

参数|说明
---|---
data | 自定义消息二进制数据

以下示例中拼接一段 XML 消息，具体展示由开发者决定。

**示例：**

```
// XML 协议的自定义消息
NSString * xml = @"testTitlethis is custom msgtest msg body";
// 转换为 NSData
NSData *data = [xml dataUsingEncoding:NSUTF8StringEncoding];
TIMCustomElem * custom_elem = [[TIMCustomElem alloc] init];
[custom_elem setData:data];
TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:custom_elem];
TIMConversation *conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"yahaha"];
[conversation sendMessage:msg succ:^(){
	NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### 短视频消息发送

短视频消息由 `TIMVideoElem` 定义。它是 `TIMElem` 的一个子类，也就是说视频截图和视频内容也是消息的一种内容。发送短视频的过程，就是将 `TIMVideoElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。

**`TIMVideoElem` 原型：**

```
/**
 *  微视频消息
 */
@interface TIMVideoElem : TIMElem
/**
 *  上传时任务Id，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
 */
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;

/**
 *  视频文件路径，发送消息时设置
 */
@property(nonatomic,strong) NSString * videoPath;

/**
 *  视频信息，发送消息时设置
 */
@property(nonatomic,strong) TIMVideo * video;

/**
 *  截图文件路径，发送消息时设置
 */
@property(nonatomic,strong) NSString * snapshotPath;

/**
 *  视频截图，发送消息时设置
 */
@property(nonatomic,strong) TIMSnapshot * snapshot;
@end
```

**参数说明：**

参数 | 说明
---|---
taskId | 上传时任务 ID，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
videoPath | 发送短视频时，本地视频文件的路径
video | 视频信息，发送消息时设置 type、duration 参数
snapshotPath | 发送短视频时，本地截图文件的路径
snapshot | 截图信息，发送消息时设置 type、width、height 参数

以下示例中发送了一个短视频消息。**示例：**

```
/**
*  获取聊天会话, 以同用户 iOS-001 的单聊为例
*/
TIMConversation * c2c_conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS-001"];
/**
*  构造一条消息
*/
TIMMessage * msg = [[TIMMessage alloc] init];
/**
*  构短视频内容
*/
TIMVideoElem * videoElem = [[TIMVideoElem alloc] init];
videoElem.videoPath = @"/xxx/videoPath.mp4";
videoElem.video = [[TIMVideo alloc] init];
videoElem.video.type = @"mp4";
videoElem.video.duration = 10;
videoElem.snapshotPath = @"/xxx/snapshotPath.jpg";
videoElem.snapshot = [[TIMSnapshot alloc] init];
videoElem.snapshot.type = @"jpg";
videoElem.snapshot.width = 100;
videoElem.snapshot.height = 200;
/**
*  将短视频内容添加到消息容器中
*/
[msg addElem:videoElem];
/**
*  发送消息
*/
[conversation sendMessage:msg succ:^(){  //成功
       NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {  //失败
       NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

### Elem 顺序

目前文件和语音 Elem 不一定会按照添加顺序传输，其他 Elem 按照顺序，不过建议不要过于依赖 Elem 顺序进行处理，应该逐个按照 Elem 类型处理，防止异常情况下进程 Crash。

### 在线消息

对于某些场景，需要发送在线消息，即用户在线时收到消息，如果用户不在线，下次登录也不会看到消息，可用于通知类消息，这种消息不会进行存储，也不会计入未读计数。发送接口与 `sendMessage` 类似。如果您不希望收到离线推送，可以在消息中设置 `TIMOfflinePushInfo`，设置 `TIMOfflinePushFlag` 关闭推送 `TIM_OFFLINE_PUSH_NO_PUSH`。

>!
>- 2.5.3版本以前只针对单聊消息有效。
>- 2.5.3版本以后对群组消息有效（暂不支持 AVChatRoom 和 BChatRoom 类型）

```
@interface TIMConversation : NSObject
/**
 *  发送在线消息（服务器不保存消息）
 *
 *  @param msg  消息体
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
-(int) sendOnlineMessage: (TIMMessage*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

### 消息转发

在2.4.0及以上版本，在 `TIMMessage` 中提供了 `copyFrom` 接口，可以方便地拷贝其他消息的内容到当前消息，然后将消息重新发送给其他人。

**原型：**

```
/**
 *  消息
 */
@interface TIMMessage : NSObject
/**
 *  拷贝消息中的属性（ELem、priority、online、offlinePushInfo）
 *
 *  @param srcMsg 源消息
 *
 *  @return 0 成功
 */
- (int)copyFrom:(TIMMessage*)srcMsg;
@end
```

## 接收消息

用户需要感知新消息的通知时，只需注册新消息通知回调 `TIMMessageListener`，如果用户是登录状态，IM SDK 收到新消息会通过回调中的  `onNewMessage` 抛出。回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息（例如消息文本，语音数据，图片等等），详情请参见 [消息解析](#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90)。

>!通过 `onNewMessage` 抛出的消息不一定是未读的消息，只是本地曾经没有过的消息（例如在另外一个终端已读，拉取最近联系人消息时可以获取会话最后一条消息，如果本地没有，会通过此方法抛出）。在用户登录之后，IM SDK 会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。
群系统消息、关系链变化、好友资料变更也会通过该回调 `onNewMessage` 抛出。


**原型：**

```
@protocol TIMMessageListener
@optional
/**
 *  新消息通知
 *
 *  @param msgs 新消息列表，TIMMessage 类型数组
 */
- (void)onNewMessage:(NSArray*) msgs;
@end

@interface TIMManager : NSObject
- (int)addMessageListener:(id<TIMMessageListener>)listener;
@end
```

**参数说明：**

参数 | 说明
---|---
msgs | 新消息列表，注意这里可能同时会有多条消息抛出，相同会话的消息由老到新排序

以下示例中设置消息回调通知，并且在有新消息时直接打印消息。**示例：**

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(NSArray*) msgs;
@end
@implementation TIMMessageListenerImpl
- (void)onNewMessage:(NSArray*) msgs {
    NSLog(@"NewMessages: %@", msgs);
}
@end
TIMMessageListenerImpl * impl = [[TIMMessageListenerImpl alloc] init];
[[TIMManager sharedInstance] addMessageListener:impl];
```

### 消息解析

收到消息后，可通过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点。

**遍历 `Elem` 原型：**

```
@interface TIMMessage : NSObject
-(int) elemCount;
-(TIMElem*) getElem:(int)index;
@end
```

**示例：**

```
TIMMessage * message = /* 消息 */
int cnt = [message elemCount];
for (int i = 0; i < cnt; i++) {
 TIMElem * elem = [message getElem:i];
 if ([elem isKindOfClass:[TIMTextElem class]]) {
     TIMTextElem * text_elem = (TIMTextElem * )elem;
 }
 else if ([elem isKindOfClass:[TIMImageElem class]]) {
     TIMImageElem * image_elem = (TIMImageElem * )elem;
 }
}
```

### 接收图片消息

接收方收到消息后，可通过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中类型为 `TIMImageElem` 的是图片消息节点。然后通过 `imageList` 获取该图片的所有规格用来展示。

** `TIMImageElem` 类原型：**

```
**
 *  图片消息 Elem
 */
@interface TIMImageElem : TIMElem
/**
 *  要发送的图片路径
 */
@property(nonatomic,retain) NSString * path;
/**
 *  保存本图片的所有规格，目前最多包含三种规格: 缩略图、大图、原图， 每种规格保存在一个 TIMImage 对象中
 */
@property(nonatomic,retain) NSArray * imageList;
@end
```

**参数说明：**

参数|说明
---|---
path | 收消息时不用关注，为 nil
imageList | 保存本图片的所有规格，目前最多包含三种规格：缩略图、大图、原图， 每种规格保存在一个 TIMImage 对象中

**`TIMImage` 说明：**

获取到消息时通过 `imageList` 得到所有的图片规格，为 `TIMImage` 数据，得到 `TIMImage` 后可通过图片大小进行占位，通过接口 `getImage` 下载不同规格的图片进行展示。**下载的数据需要由开发者缓存，IM SDK 每次调用 `getImage` 都会从服务端重新下载数据。建议通过图片的 `uuid` 作为 `key` 进行图片文件的存储。**

**原型：**

```
@interface TIMImage : NSObject
/**
 *  图片 ID，内部标识，可用于外部缓存 key
 */
@property(nonatomic,strong) NSString * uuid;
/**
 *  图片类型
 */
@property(nonatomic,assign) TIM_IMAGE_TYPE type;
/**
 *  图片大小
 */
@property(nonatomic,assign) int size;
/**
 *  图片宽度
 */
@property(nonatomic,assign) int width;
/**
 *  图片高度
 */
@property(nonatomic,assign) int height;
/**
 *  下载 URL
 */
@property(nonatomic, strong) NSString * url;

/**
 *  获取图片
 *
 *  下载的数据需要由开发者缓存，IM SDK 每次调用 getImage 都会从服务端重新下载数据。建议通过图片的 uuid 作为 key 进行图片文件的存储。
 *
 *  @param path 图片保存路径
 *  @param succ 成功回调，返回图片数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getImage:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  获取图片（有进度回调）
 *
 *  下载的数据需要由开发者缓存，IM SDK 每次调用 getImage 都会从服务端重新下载数据。建议通过图片的 uuid 作为 key 进行图片文件的存储。
 *
 *  @param path 图片保存路径
 *  @param progress 图片下载进度
 *  @param succ 成功回调，返回图片数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getImage:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**图片规格说明：**每幅图片有三种规格，分别是 Original（原图）、Large（大图）、Thumb（缩略图）。

- **原图：**指用户发送的原始图片，尺寸和大小都保持不变。
- **大图：**是将原图等比压缩，压缩后宽、高中较小的一个等于720像素。
- **缩略图：**是将原图等比压缩，压缩后宽、高中较小的一个等于198像素。

>?
>- 如果原图尺寸就小于198像素，则三种规格都保持原始尺寸，不需压缩。
>- 如果原图尺寸在198 - 720之间，则大图和原图一样，不需压缩。
>- 在手机上展示图片时，建议优先展示缩略图，用户单击缩略图时再下载大图，单击大图时再下载原图。当然开发者也可以选择跳过大图，单击缩略图时直接下载原图。
>- 在 Pad 或 PC 上展示图片时，由于分辨率较大，且基本都是 Wi-Fi 或有线网络，建议直接显示大图，用户单击大图时再下载原图。

以下示例从会话中取出 10 条消息，获取图片消息并下载相应数据。**示例：**

```
//以收到新消息回调为例，介绍下图片消息的解析过程
//接收到的图片保存的路径
NSString * pic_path = @"/xxx/imgPath.jpg";
[conversation getMessage:10 last:nil succ:^(NSArray * msgList) {  //获取消息成功
	//遍历所有的消息
	for (TIMMessage * msg in msgList) {
		//遍历一条消息的所有元素
		for (int i = 0; i < msg.elemCount; ++i) {
           TIMElem *elem = [msg getElem:i];
           //图片元素
			if ([elem isKindOfClass:[TIMImageElem class]]) {
				TIMImageElem * image_elem = (TIMImageElem * )elem;

				//遍历所有图片规格(缩略图、大图、原图)
				NSArray * imgList = [image_elem imageList];
				for (TIMImage * image in imgList) {
					[image getImage:pic_path succ:^(){  //接收成功
						NSLog(@"SUCC: pic store to %@", pic_path);
					}fail:^(int code, NSString * err) {  //接收失败
						NSLog(@"ERR: code=%d, err=%@", code, err);
					}];
				}
			}
		}
	}
} fail:^(int code, NSString * err) {  //获取消息失败
	NSLog(@"Get Message Failed:%d->%@", code, err);
}];
```

### 接收语音消息

收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中 `TIMSoundElem` 为语音消息节点。其中`path`为创建消息时填写的语音信息，接收消息时为空。获取到消息时可通过时长占位，通过接口 `getSound` 下载语音资源，`getSound` 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 `uuid` 作为 `key` 进行外部存储，IM SDK 并不会存储资源文件。

**原型：**

```
@interface TIMSoundElem : TIMElem
/**
 *  上传时任务 ID，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
 */
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;
/**
 *  发送时设置为语音数据，接收时使用 getSound 获得数据
 */
@property(nonatomic,strong) NSString * path;
/**
 *  语音消息内部 ID
 */
@property(nonatomic,strong) NSString * uuid;
/**
 *  语音数据大小
 */
@property(nonatomic,assign) int dataSize;
/**
 *  语音长度（秒），发送消息时设置
 */
@property(nonatomic,assign) int second;

/**
 *  获取语音的 URL 下载地址
 *
 *  @param urlCallBack 获取 URL 地址回调
 */
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
 *  获取语音数据到指定路径的文件中 
 *
 *  getSound 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 语音保存路径
 *  @param succ 成功回调，返回语音数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getSound:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  获取语音数据到指定路径的文件中（有进度回调）
 *
 *  getSound 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 * 
 *  @param path 语音保存路径
 *  @param progress 语音下载进度
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getSound:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**其他参数说明：**

参数|说明
---|---
path | 发送时设置为语音数据，接收时使用 getSound 获得数据
uuid | 唯一标识，方便用户缓存
dataSize | 语音文件大小
second | 语音时长，以秒为单位

**语音消息已读状态：**语音是否已经播放，可使用 [消息自定义字段](https://cloud.tencent.com/doc/product/269/消息收发（iOS%20SDK）#.E6.B6.88.E6.81.AF.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) 实现，如 `customInt` 的值0表示未播放，1表示播放，当用户单击播放后可设置 `customInt` 的值为1。

```
@interface TIMMessage : NSObject
/**
 *  设置自定义整数，默认为0
 *
 *  @param param 设置参数
 *
 *  @return TRUE 设置成功
 */
- (BOOL) setCustomInt:(int32_t) param;

/**
 *  获取 CustomInt
 *
 *  @return CustomInt
 */
- (int32_t)customInt;

@end
```

### 接收小文件消息

收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中 `TIMFileElem` 为文件消息节点。其中 `path` 为创建消息时填写的文件路径，GET 消息时为空。获取到消息时可只展示文件大小和显示名，通过接口 `getFile` 下载文件资源。`getFile` 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 `uuid` 作为 `key` 进行外部存储，IM SDK 并不会存储资源文件。

**原型：**

```
@interface TIMFileElem : TIMElem
/**
*  上传时任务Id，可用来查询上传进度（已废弃，请在 TIMUploadProgressListener 监听上传进度）
*/
@property(nonatomic,assign) uint32_t taskId DEPRECATED_ATTRIBUTE;
/**
*  上传时，文件的路径（设置 path 时，优先上传文件）
*/
@property(nonatomic,strong) NSString * path;
/**
*  文件内部ID
*/
@property(nonatomic,strong) NSString * uuid;
/**
*  文件大小
*/
@property(nonatomic,assign) int fileSize;
/**
*  文件显示名，发消息时设置
*/
@property(nonatomic,strong) NSString * filename;

/**
*  获取文件的 URL 下载地址
*
*  @param urlCallBack 获取 URL 地址回调
*/
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
*  获取文件数据到指定路径的文件中
*
*  getFile 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
*
*  @param path 文件保存路径
*  @param succ 成功回调，返回数据
*  @param fail 失败回调，返回错误码和错误描述
*/
- (void)getFile:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
*  获取文件数据到指定路径的文件中（有进度回调）
*
*  getFile 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
*
*  @param path 文件保存路径
*  @param progress 文件下载进度
*  @param succ 成功回调，返回数据
*  @param fail 失败回调，返回错误码和错误描述
*/
- (void)getFile:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
path | 上传时，文件的路径
uuid | 唯一 ID，方便用户进行缓存
fileSize | 文件大小
filename |文件显示名

### 接收短视频消息
收到消息后，可通过 getElem 从 TIMMessage 中获取所有的 Elem 节点，其中 TIMVideoElem 为文件消息节点，通过 TIMVideo 和 TIMSnapshot 对象获取视频和截图内容。接收到 TIMVideoElem 后，通过 video 属性和 snapshot 属性中定义的接口下载视频文件和截图文件。如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
原型：

```
@interface TIMVideo : NSObject
/**
 *  视频消息内部 ID，不用设置
 */
@property(nonatomic,strong) NSString * uuid;
/**
 *  视频文件类型，发送消息时设置
 */
@property(nonatomic,strong) NSString * type;
/**
 *  视频大小，不用设置
 */
@property(nonatomic,assign) int size;
/**
 *  视频时长，发送消息时设置
 */
@property(nonatomic,assign) int duration;

/**
 *  获取视频的 URL 下载地址
 *
 *  @param urlCallBack 获取 URL 地址回调
 */
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
 *  获取视频
 *
 *  getVideo 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 视频保存路径
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getVideo:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  获取视频（有进度回调）
 *
 *  getVideo 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
 *
 *  @param path 视频保存路径
 *  @param progress 视频下载进度
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getVideo:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;

@end

@interface TIMSnapshot : NSObject
/**
*  图片ID，不用设置
*/
@property(nonatomic,strong) NSString * uuid;
/**
*  截图文件类型，发送消息时设置
*/
@property(nonatomic,strong) NSString * type;
/**
*  图片大小，不用设置
*/
@property(nonatomic,assign) int size;
/**
*  图片宽度，发送消息时设置
*/
@property(nonatomic,assign) int width;
/**
*  图片高度，发送消息时设置
*/
@property(nonatomic,assign) int height;

/**
*  获取截图的 URL 下载地址
*
*  @param urlCallBack 获取 URL 地址回调
*/
-(void)getUrl:(void (^)(NSString * url))urlCallBack;

/**
*  获取图片
*
*  getImage 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
*
*  @param path 图片保存路径
*  @param succ 成功回调，返回图片数据
*  @param fail 失败回调，返回错误码和错误描述
*/
- (void)getImage:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
*  获取图片（有进度回调）
*
*  getImage 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 uuid 作为 key 进行外部存储，IM SDK 并不会存储资源文件。
*
*  @param path 图片保存路径
*  @param progress 图片下载进度
*  @param succ 成功回调，返回图片数据
*  @param fail 失败回调，返回错误码和错误描述
*/
- (void)getImage:(NSString*)path progress:(TIMProgress)progress succ:(TIMSucc)succ fail:(TIMFail)fail;
@end

//以收到新消息回调为例，介绍下短视频消息的解析过程
//接收到的视频和截图保存的路径
NSString * video_path = @"/xxx/video.mp4";
NSString * snapshot_path = @"/xxx/snapshot.jpg";
[conversation getMessage:10 last:nil succ:^(NSArray * msgList) {  //获取消息成功
   //遍历所有的消息
   for (TIMMessage * msg in msgList) {
     //遍历一条消息的所有元素
     for (int i = 0; i < msg.elemCount; ++i) {
         TIMElem *elem = [msg getElem:i];
         if ([elem isKindOfClass:[TIMVideoElem class]]) {
              TIMVideoElem * video_elem = (TIMVideoElem * )elem;
              [video_elem.video getVideo:video_path succ:^()｛
                  NSLog(@"下载视频文件成功");
              ｝ fail:^(int code, NSString * err) {
                  NSLog(@"下载视频文件失败:%@ %d", err, code);
              }];
              [video_elem.snapshot getImage:snapshot_path succ:^() {
                  NSLog(@"下载截图成功");
              } fail:^(int code, NSString * err) {
                  NSLog(@"下载截图失败:%@ %d", err, code);
              }];
         }
     }
} fail:^(int code, NSString * err) {  //获取消息失败
    NSLog(@"Get Message Failed:%d->%@", code, err);
}];

```

## 消息属性 

### 消息是否已读

通过消息属性 `isReaded` 是否消息已读。这里已读与否取决于 App 侧进行的 [已读上报](https://cloud.tencent.com/doc/product/269/未读消息计数（iOS%20SDK）#.E5.B7.B2.E8.AF.BB.E4.B8.8A.E6.8A.A5)。

```
@interface TIMMessage : NSObject
/**
 *  是否已读
 *
 *  @return TRUE 已读  FALSE 未读
 */
-(BOOL) isReaded;
@end
```

### 消息状态

通过消息属性 `status` 可以获取消息的当前状态(如，发送中、发送成功、发送失败和删除)，对于删除的消息，需要 UI 判断状态并隐藏。

```
/**
 *  消息状态
 */
 typedef NS_ENUM(NSInteger, TIMMessageStatus){
 /**
  *  消息发送中
  */
 TIM_MSG_STATUS_SENDING              = 1,
 /**
  *  消息发送成功
  */
 TIM_MSG_STATUS_SEND_SUCC            = 2,
 /**
  *  消息发送失败
  */
 TIM_MSG_STATUS_SEND_FAIL            = 3,
 /**
  *  消息被删除
  */
 TIM_MSG_STATUS_HAS_DELETED          = 4,
 /**
  *  导入到本地的消息 
  */
 TIM_MSG_STATUS_LOCAL_STORED         = 5,
 /**
  *  被撤销的消息
  */
 TIM_MSG_STATUS_LOCAL_REVOKED        = 6,
 };

@interface TIMMessage : NSObject
/**
 *  消息状态
 *
 *  @return TIMMessageStatus 消息状态
 */
-(TIMMessageStatus) status;
@end
```

### 是否是自己发出的消息

通过消息属性 `isSelf` 可以判断消息是否是自己发出的消息，界面显示时可用。

```
@interface TIMMessage : NSObject
/**
 *  是否发送方
 *
 *  @return TRUE 表示是发送消息    FALSE 表示是接收消息
 */
-(BOOL) isSelf;
@end
```

### 消息发送者以及相关资料

对于群消息，可以通过 `TIMMessage` 的方法 `sender` 得到发送用户，另外也可以通过方法 `GetSenderProfile` 和 `GetSenderGroupMemberProfile` 获取用户自己的资料和所在群的资料。1.9版本之前，只有在线消息 `onNewMessage` 抛出的消息可以获取到用户资料，1.9版本以后，通过 `getMessage` 得到的消息也可以拿到资料（更新版本之前已经收到本地的消息无法获取到）。对于单聊消息，通过通过 `TIMMessage` 的 `getConversation` 获取到对应会话，会话的 `getReceiver` 可以得到正在聊天的用户。

>!此字段是消息发送时获取用户资料写入消息体，如后续用户资料更新，此字段不会相应变更，只有产生的新消息中才会带最新的昵称。

```
@interface TIMMessage : NSObject
/**
 *  获取发送方
 *
 *  @return 发送方标识
 */
-(NSString *) sender;
/**
 *  获取发送者资料
 *
 *  如果本地有发送者资料，会在 profileCallBack 回调里面立即同步返回发送者资料，如果本地没有发送者资料，SDK 内部会先向服务器拉取发送者资料，并在 profileCallBack 回调里面异步返回发送者资料。
 *
 *  @param  profileCallBack 发送者资料回调
 *
 */
- (void)getSenderProfile:(ProfileCallBack)profileCallBack;
/**
 *  获取发送者群内资料（发送者为本人时可能为空）
 *
 *  @return 发送者群内资料，nil 表示没有获取资料或者不是群消息，目前仅能获取字段：member ，其他的字段获取建议通过 TIMGroupManager+Ext.h -> getGroupMembers 获取 
 */
-(TIMGroupMemberInfo *) GetSenderGroupMemberProfile;
@end
```

### 消息时间

通过消息属性 `timestamp` 可以得到消息时间，该时间是 Server 时间，而非本地时间。在创建消息时，此时间为根据 Server 时间校准过的时间，发送成功后会改为准确的 Server 时间。

```
@interface TIMMessage : NSObject
/**
 *  当前消息的时间戳
 *
 *  @return 时间戳
 */
-(NSDate*) timestamp;
@end
```

### 消息 ID

消息 ID 分为两种，一种是当消息生成时，就已经固定（`msgId`），这种方式可能跟其他用户产生的消息冲突，需要再加一个时间维度，可以认为10分钟以内的消息可以使用 `msgId` 区分。另外一种，当消息发送成功以后才能固定下来（`uniqueId`），这种方式能保证全局唯一。这两种方式都需要在同一个会话内判断。

```
@interface TIMMessage : NSObject
/**
 *  消息 ID
 */
-(NSString *) msgId;
/**
 *  获取消息uniqueId
 *
 *  @return uniqueId
 */
- (uint64_t) uniqueId;
@end
```

### 消息自定义字段

开发者可以对消息增加自定义字段，如自定义整数、自定义二进制数据，可以根据这两个字段做出各种不通效果，例如语音消息是否已经播放等等。另外需要注意，此自定义字段仅存储于本地，不会同步到 Server，更换终端获取不到。

```
@interface TIMMessage : NSObject
/**
 *  设置自定义整数，默认为 0
 *
 *  @param param 设置参数
 *
 *  @return TRUE 设置成功
 */
- (BOOL) setCustomInt:(int32_t) param;
/**
 *  设置自定义数据，默认为""
 *
 *  @param data 设置参数
 *
 *  @return TRUE 设置成功
 */
- (BOOL) setCustomData:(NSData*) data;
/**
 *  获取CustomInt
 *
 *  @return CustomInt
 */
- (int32_t) customInt;
/**
 *  获取CustomData
 *
 *  @return CustomData
 */
- (NSData*) customData;
@end
```

### 消息优先级

对于直播场景，会有点赞和发红包功能，点赞相对优先级较低，红包消息优先级较高，具体消息内容可以使用 `TIMCustomElem` 进行定义，发送消息时，可设置消息优先级。

>!只针对群聊消息有效。

```
@interface TIMMessage : NSObject
/**
 *  设置消息的优先级
 *
 *  @param priority 优先级
 *
 *  @return TRUE 设置成功
 */
- (BOOL) setPriority:(TIMMessagePriority)priority;
/**
 *  获取消息的优先级
 *
 *  @return 优先级
 */
- (TIMMessagePriority) getPriority;
@end
```

### 已读回执

对于单聊消息，用户开启已读回执功能后，对方调用 `setReadMessage` 时会同步已读信息到本客户端。

**开启已读回执功能：**

```
@interface TIMUserConfig : NSObject
/**
 *  启用已读回执，启用后在已读上报时会给对方发送回执，只对单聊回话有效
 */
-(void) enableReadReceipt;
/**
 *  消息已读回执监听器
 */
@property(nonatomic,weak) id<TIMMessageReceiptListener> messageReceiptListener;
@end
```

**原型：**

```
@interface TIMMessage : NSObject

/**
 *  对方是否已读（仅 C2C 消息有效）
 *
 *  @return TRUE 已读  FALSE 未读
 */
-(BOOL) isPeerReaded;
@end
```

## 会话操作

### 获取所有会话

```
@interface TIMManager : NSObject

/**
 *  获取会话（TIMConversation*）列表
 *
 *  @return 会话列表
 */
-(NSArray*) getConversationList;
@end
```

>!SDK 会在内部不断更新会话列表，每次更新后都会通过 `TIMRefreshListener.onRefresh` 回调，请**在 `onRefresh` 之后再调用 `getConversationList`** 更新会话列表。

**示例：**

```
NSArray * conversations = [[TIMManager sharedInstance] getConversationList];
NSLog(@"current session list : %@", [conversations description])
```

### 获取会话本地消息

IM SDK 会在本地进行消息存储，可通过 `TIMConversation` 方法的 `getLocalMessage` 获取，此方法为异步方法，需要通过设置回调得到消息数据，对于单聊，登录后可以获取离线消息，对于群聊，开启最近联系人漫游的情况下，登录后只能获取最近一条消息，可通过 `getMessage` 获取漫游消息。对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参阅 [消息解析](#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90)，下载后的真实数据不会缓存，需要调用方进行缓存。

**原型：**

```
@interface TIMConversation : NSObject
/**
 *  获取本地会话消息
 *
 *  @param count 获取数量
 *  @param last  上次最后一条消息
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0 本次操作成功
 */
-(int) getLocalMessage: (int)count last:(TIMMessage*)last succ:(TIMGetMsgSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
count | 指定获取消息的数量
last | 指定上次获取的最后一条消息，如果 last 传 nil，从最新的消息开始读取
succ | 成功回调
fail | 失败回调

**示例：**

```
[conversation getLocalMessage:10 last:nil succ:^(NSArray * msgList) {
	for (TIMMessage * msg in msgList) {
		if ([msg isKindOfClass:[TIMMessage class]]) {
			NSLog(@"GetOneMessage:%@", msg);
		}
	}
}fail:^(int code, NSString * err) {
	NSLog(@"Get Message Failed:%d->%@", code, err);
}];
```

### 获取会话漫游消息

对于群组，登录后可以获取漫游消息，对于 C2C，开通漫游服务后可以获取漫游消息，通过 IM SDK 的 `getMessage` 接口可以获取漫游消息，如果本地消息全部都是连续的，则不会通过网络获取，如果本地消息不连续，会通过网络获取断层消息。对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参与消息解析部分，下载后的真实数据不会缓存，需要调用方进行缓存。

**原型：**

```
@interface TIMConversation : NSObject
/**
 *  获取会话消息
 *
 *  @param count 获取数量
 *  @param last  上次最后一条消息
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0 本次操作成功
 */
-(int) getMessage: (int)count last:(TIMMessage*)last succ:(TIMGetMsgSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
count | 指定获取消息的数量
last | 指定上次获取的最后一条消息，如果 last 传 nil，从最新的消息开始读取
succ | 成功回调
fail | 失败回调

**示例：**

```
[conversation getMessage:10 last:nil succ:^(NSArray * msgList) {
	for (TIMMessage * msg in msgList) {
		if ([msg isKindOfClass:[TIMMessage class]]) {
			NSLog(@"GetOneMessage:%@", msg);
		}
	}
}fail:^(int code, NSString * err) {
	NSLog(@"Get Message Failed:%d->%@", code, err);
}];
```

### 删除会话

删除会话的同时 IM SDK 会删除该会话的本地和漫游消息，会话和消息删除后，无法再恢复。

**原型：**

```
@protocol TIMManager : NSObject
/**
 *
 *  删除会话的同时会把会话的漫游消息从本地和后台都删除。
 *
 *  @param type 会话类型，详情请参考 TIMComm.h 里面的 TIMConversationType 定义
 *  @param conversationId 会话 Id
 *                        单聊类型（C2C）   ：为对方 userID；
 *                        群组类型（GROUP） ：为群组 groupId；
 *                        系统类型（SYSTEM）：为 @""
 *
 *  @return YES:删除成功；NO:删除失败
 */
- (BOOL)deleteConversation:(TIMConversationType)type receiver:(NSString*)conversationId;
@end
```

**参数说明：**

参数|说明
---|---
type|会话类型，如果是单聊，填写 TIM_C2C，如果是群聊，填写 TIM_GROUP
conversationId|会话标识，单聊情况下，receiver 为对方用户 identifier，群聊情况下，receiver 为群组 ID

示例中删除好友『iOS_002』的 C2C 会话。**示例：**

```
[[TIMManager sharedInstance] deleteConversation:TIM_C2C receiver:@"iOS_002"];
```

### 同步获取会话最后的消息

UI 展示最近联系人列表时，时常会展示用户的最后一条消息，在1.9以后版本增加了同步获取接口 `getLastMsg`，用户可以通过此接口方便获取最后一条消息进行展示。**目前没有网络无法获取**。此接口获取并不会过滤删除状态消息，需要 App 层进行屏蔽。获取最近的多条消息，可以通过 `getMessage` 来获取。

**原型：**

```
@interface TIMConversation : NSObject
/**
 *  从  Cache 中获取最后一条消息
 *  @return 最后一条消息（TIMMessage*）
 */
- (TIMMessage*)getLastMsg;

/**
 *  获取会话漫游消息
 *  @param count 获取数量
 *  @param last  上次最后一条消息，如果 last 为 nil，从最新的消息开始读取
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *  @return 0：本次操作成功；1：本次操作失败
 */
- (int)getMessage:(int)count last:(TIMMessage*)last succ:(TIMGetMsgSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
count | 需要获取的消息数，注意这里最多为 20 


### 设置会话草稿

UI 展示最近联系人列表时，时常会展示用户的草稿内容，在2.2以后版本增加了设置和获取草稿的接口，用户可以通过此接口设置会话的草稿信息。**草稿信息会存本地数据库，重新登录后依然可以获取**。

**原型：**

```
@interface TIMMessageDraft : NSObject
/**
 *  设置自定义数据
 *
 *  @param userData 自定义数据
 *
 *  @return 0 成功
 */
-(int) setUserData:(NSData*)userData;
/**
 *  获取自定义数据
 *
 *  @return 自定义数据
 */
-(NSData*) getUserData;
/**
 *  增加 Elem
 *
 *  @param elem elem 结构
 *
 *  @return 0       表示成功
 *          1       禁止添加 Elem（文件或语音多于两个 Elem）
 *          2       未知 Elem
 */
-(int) addElem:(TIMElem*)elem;
/**
 *  获取对应索引的 Elem
 *
 *  @param index 对应索引
 *
 *  @return 返回对应 Elem
 */
-(TIMElem*) getElem:(int)index;
/**
 *  获取 Elem 数量
 *
 *  @return elem 数量
 */
-(int) elemCount;
/**
 *  草稿生成对应的消息
 *
 *  @return 消息
 */
-(TIMMessage*) transformToMessage;
/**
 *  当前消息的时间戳
 *
 *  @return 时间戳
 */
-(NSDate*) timestamp;
@end

@interface TIMConversation : NSObject
/**
 *  设置会话草稿
 *
 *  @param draft 草稿内容
 *
 *  @return 0 成功
 */
-(int) setDraft:(TIMMessageDraft*)draft;
/**
 *  获取会话草稿
 *
 *  @return 草稿内容，没有草稿返回nil
 */
-(TIMMessageDraft*) getDraft;
@end
```

**参数说明：**

参数|说明
---|---
draft | 需要设置的草稿 ，需要清空会话草稿时传入 nil

### 删除会话消息

IM SDK 支持删除会话的本地及漫游消息，消息删除后，无法再恢复。

**原型：**

```
@interface TIMConversation : NSObject
/**
 *  删除当前会话的本地及漫游消息
 *
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0 本次操作成功
 */
- (int)deleteMessages:(NSArray<TIMMessage *>*)msgList succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
msgList | 需要删除的消息列表
succ | 成功回调
fail | 失败回调

### 获取本地指定 ID 的消息

IM SDK 2.5.3 版本提供获取本地指定 ID 消息的接口。

**原型：**

```
/**
 *  消息
 */
@interface TIMMessage : NSObject
/**
 *  获取消息定位符
 *
 *  @return locator
 */
- (TIMMessageLocator*) locator;
@end
@interface TIMConversation : NSObject
/**
 *  获取会话消息
 *
 *  @param locators 消息定位符（TIMMessageLocator）数组
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0 本次操作成功
 */
-(int) findMessages:(NSArray*)locators succ:(TIMGetMsgSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
locators | 消息定位符 TIMMessageLocator 列表
succ | 成功回调，返回消息列表
fail | 失败回调

### 撤回消息

IM SDK 在 3.1.0 版本开始提供撤回消息的接口。可以通过调用 `TIMConversation` 的 `revokeMessage` 接口来撤回自己发送的消息。

>!
> - 仅 C2C 和 GROUP 会话有效、onlineMessage 无效、AVChatRoom 和 BChatRoom 无效。
> - 默认只能撤回 2 分钟内的消息。

**原型：**

```
/**
 * 消息撤回（仅 C2C 和 GROUP 会话有效，其中 onlineMessage、AVChatRoom 和 BChatRoom 无效）
 *  @param msg   被撤回的消息
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0：本次操作成功；1：本次操作失败
 */
- (int)revokeMessage:(TIMMessage*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
```

成功撤回消息后，群组内其他用户和 C2C 会话对端用户会收到一条消息撤回通知，并通过消息撤回通知监听器 `TIMMessageRevokeListener` 通知到上层应用。消息撤回通知监听器可以在登录前，通过 `TIMUserConfig` 的 `messageRevokeListener` 来进行配置。具体可以参考 [用户配置](https://cloud.tencent.com/document/product/269/9148)。

**原型：**

```
@protocol TIMMessageRevokeListener <NSObject>
@optional
/**
 *  消息撤回通知
 *
 *  @param locator 被撤回消息的标识
 */
- (void)onRevokeMessage:(TIMMessageLocator*)locator;

@end

```

收到一条消息撤回通知后，通过 `TIMMessage` 中的 `respondsToLocator` 方法判断当前消息是否是被对方撤回了，然后根据需要对 UI 进行刷新。

**原型：**

```
/**
 *  是否为 locator 对应的消息
 *
 *  @param locator 消息定位符
 *
 *  @return YES：是对应的消息；NO：不是对应的消息
 */
- (BOOL)respondsToLocator:(TIMMessageLocator*)locator;

```

## 系统消息

会话类型（TIMConversationType）除了 C2C 单聊和 Group 群聊以外，还有一种系统消息，系统消息不能由用户主动发送，是系统后台在相应的事件发生时产生的通知消息。系统消息目前分为两种，一种是关系链系统消息，一种是群系统消息。

- **关系链变更系统消息：**当有用户加自己为好友，或者有用户删除自己好友的情况下，系统会发出变更通知，开发者可更新好友列表。相关细节可参阅 [关系链变更系统通知](https://cloud.tencent.com/doc/product/269/用户资料与关系链（iOS%20SDK）#.E5.85.B3.E7.B3.BB.E9.93.BE.E5.8F.98.E6.9B.B4.E7.B3.BB.E7.BB.9F.E9.80.9A.E7.9F.A5) 部分。

- **群事件消息：**当群资料变更，如群名变更或者群内成员变更，在群里会有系统发出一条群事件消息，开发者可在收到消息时可选择是否展示给用户，同时可刷新群资料或者群成员。详细内容可参阅：[群组管理-群事件消息](https://cloud.tencent.com/doc/product/269/群组管理（iOS%20SDK）#.E7.BE.A4.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF)。

- **群系统消息：**当被管理员踢出群组，被邀请加入群组等事件发生时，系统会给用户发出群系统消息，相关细节可参阅 [群组管理-群系统消息](https://cloud.tencent.com/doc/product/269/群组管理（iOS%20SDK）#.E7.BE.A4.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF)。

