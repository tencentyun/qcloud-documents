## 1 使用简述
本文档介绍了GVoice游戏语音Objective-C接口SDK的接入方法，适用于iOS平台直接开发的游戏或者APP。

GVoice游戏语音目前提供了实时语音(Real-Time)、语音消息 (Message)两大功能。实时语音能够让多名玩家进行实时语音聊天。语音消息为用户提供快速录制并向其他玩家发送一段语音消息的能力。

实时语音分为小队语音、国战语音两种模式。如果一个房间内同时聊天的玩家小于20人，则使用小队语音模式，这时玩家可以自由发言（该模式常用于队友间沟通）。当一个房间内语音聊天的玩家大于20人时，则使用国战语音模式，在国战语音中，允许开发者控制发言权限，同时说话人数不得超过5人（该模式常用于团战指挥、主播）。

GVoice 客户端SDK接口主要分成三个部分：基本API、实时语音API以及语音消息API。

### 1.1 系统配置和基本使用
[IOS SDK 下载](https://cloud.tencent.com/document/product/556/10041)  
[IOS Demo 下载](https://cloud.tencent.com/document/product/556/10042)


下载iOS SDK包后，解压得到.a文件、.h文件以及bundle文件。按如下流程即可接入。 1、导入库文件和Bundle文件到Xcode工程中：
![](https://mc.qcloudimg.com/static/img/b980d0e2ba93fd8ce0884170c6cab596/1.png)

并导入以下库文件：
![](https://mc.qcloudimg.com/static/img/00705b94a989e2d452846136c971095f/2.png)


在iOS10以后还需要在Info中配置麦克风权限

![](https://mc.qcloudimg.com/static/img/4f821f50b9c45118cba2cd17c34f5a94/3.png)


2、在合适的地方进行包含头文件“GVoice.h”并进行初始化

GVoice通过单例方法[GVGCloudVoice sharedInstance]来获得示例对象并进行相关的操作。首先 要设置应用的信息，然后初始化引擎

    [[GVGCloudVoice sharedInstance] setAppInfo:"your_appid" withKey:"your_appkey" andOpenID:"your_open_id"];
	[[GVGCloudVoice sharedInstance] initEngine];  

3、在使用语音前先进行语音模式以及回调delegate的实现等操作

    [[GVGCloudVoice sharedInstance] setMode:RealTime];

    @interface TeamRoomViewController : UIViewController <GVGCloudVoiceDelegate>
    @end

    #pragma mark delegate

        - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {
        }

        - (void) onStatusUpdate:(enum GCloudVoiceCompleteCode) status withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {

        }

        - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName {
        }

        - (void) onMemberVoice:    (const unsigned int * _Nullable)members withCount: (int) count {
        }

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID  {

        }

        - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID {

        }

        - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath {

        }

        - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code {

        }

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result {

        }

        - (void) onRecording:(const unsigned char* _Nullable) pAudioData withLength: (unsigned int) nDataLength {

        }
  
4、要驱动回调，需要您定时调用Poll函数，这样才会触发回调

比如在UI线程里面通过定时器来调用：

    _pollTimer = [NSTimer scheduledTimerWithTimeInterval:1.000/15 repeats:YES block:^(NSTimer * _Nonnull timer) {
    [[GVGCloudVoice sharedInstance] poll];
    }];
  
5、加入房间：（记得在进房回调中才能确定是否进房成功）

   `[[GVGCloudVoice sharedInstance] joinTeamRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000];`
  
6、如果回调中成功进房了，就可以打开麦克风和扬声器，进行通话了

      [[GVGCloudVoice sharedInstance] openSpeaker];

### 1.2  接口调用流程
![](https://mc.qcloudimg.com/static/img/db4301975a4007a65e2b71152e103fd4/4.png)



- 实现GVGCloudVoiceDelegate回调类。  


- 调用GVGCloudVoice的[GVGCloudVoice sharedInstance]方法获取GVGCloudVoice对象。  


- 对该对象进行初始化操作并设置回调。  


- 根据需要调用实时语音接口或语音消息接口。  


- 在系统可以Tick的地方（如Unity3D的Update）调用poll()函数驱动程序运行。  
### 1.3  实时语音接口调用流程
![](https://mc.qcloudimg.com/static/img/d7eb0df95ebdff5e8f9d44a8a01bd74f/5.png)



- 调用setMode()方法设置使用实时语音模式。


- 根据业务需求使用小队语音或国战语音，分别调用joinTeamRoom()或joinNationalRoom()。


- 需要Tick的调用poll来检查回调，当加入房间成功或者失败时，会回调onJoinRoomComplete()方法。


- 加入房间成功后，就可以调用openMic()打开麦克风进行采集并发送到网络。


- 调用openSpeaker()打开扬声器，开始接受网络上的音频流并自动进行播放。


- 当需要退出房间时，调用quitRoom()即可，成功后会回调onQuitRoomComplete()方法。  

注意：  
对于国战语音，系统要求说话人数不能超过5个人，每个用户多了一个角色信息，在加入房间的时候需要指定是以听众的身份加入还是以主播的身份加入。

### 1.4  离线语音接口调用流程
![](https://mc.qcloudimg.com/static/img/28ec9bf0eab80c06c7883219fbd7604a/6.png)



- 调用setMode方法设置使用语音消息模式。


- 调用applyMessageKey()获取语音消息安全密钥key信息，当申请成功后会通过onApplyMessageKeyComplete进行回调。


- 当需要录音时，调用startRecording()录制音频到文件中（文件的路径格式是/your path）。


- 如果想取消录制可以调用stopRecording接口进行取消。


- 当录制完成后，调用uploadRecordedFile将文件上传到GcloudVoice的服务器上，该过程会通过onUploadReccordFileComplete回调在上传成功的时候返还一个ShareFileID.该ID是这个文件的唯一标识符，用于其他用户收听时候的下载。服务器需要对其进行管理和转发


- 当游戏客户端需要收听其他人的录音时，首先从服务器获取转发的ShareFileID，然后调用downloadRecordedFile下载该语言文件，下载结果通过onDownloadRecordFileComplete回调来通知。当下载成功时，就可以调用playRecordedFile播放下载完成的语音数据了。同样的，如果想取消播放，可以调用stopPlayFile进行取消。
### 1.5  语音转文字调用流程
![](https://mc.qcloudimg.com/static/img/c0789172ff0ffb679cc9beeb3ba4d18b/7.png)



- 调用setMode方法设置使用翻译（Translation）模式。


- 调用applyMessageKey()获取语音消息安全密钥key信息，当申请成功后会通过onApplyMessageKeyComplete进行回调。


- 当需要录音时，调用startRecording()录制音频到文件中（文件的路径格式是/your path）。


- 如果想取消录制可以调用stopRecording接口进行取消。


- 当录制完成后，调用uploadRecordedFile将文件上传到GcloudVoice的服务器上，该过程会通过onUploadReccordFileComplete回调在上传成功的时候返还一个ShareFileID.该ID是这个文件的唯一标识符，用于其他用户收听时候的下载。服务器需要对其进行管理和转发
翻译时，调用speechToText，其中一个重要参数是上一步骤中的fileid，调用该函数后，会在onSpeechToText回调中通知翻译结果。

注意：翻译的fileid，需要是在translation模式下录制得来的，不是message模式录制得来的

## 2 接口说明
### 2.1 基本API
#### 2.1.1 创建IGcloudVoiceEngine对象
1、接口说明

在使用语音功能时，需要首先获取IGcloudVoiceEngine对象 。

2、函数原型

    + (GVGCloudVoice* _Nullable) sharedInstance;
    该函数返回一个GVGCloudVoice对象，通过调用该对象的接口，可以执行相关动作。

3、出错处理

出错时，返回NULL对象

4、示例代码  
    
    [[GVGCloudVoice sharedInstance] closeMic]; 

#### 2.1.2 设置业务信息
1、接口说明

在初始化之前，需要设置之前申请的游戏ID和游戏Key以及用户的唯一标示OpenID。

2、函数原型

    - (enum GCloudVoiceErrno) setAppInfo:(const char *_Nullable) appID withKey: (const char *_Nullable)appKey andOpenID:(const char *_Nullable)openID;
    参数	类型	意义
    appID	const char *	开通业务页面中的游戏ID
    appKey	const char *	开通业务页面中的游戏Key
    openID	const char *	玩家唯一标示，比如从手Q或者微信获得到的OpenID
    
3、返回值

	GCloudVoiceErr	成功时返回GCLOUD_VOICE_SUCC
  
4、示例代码  

    [[GVGCloudVoice sharedInstance] setAppInfo:"93223849489" withKey:"d94749efe9dddfce61333121de84123ef9b" andOpenID:[_openID cStringUsingEncoding:NSUTF8StringEncoding]];

#### 2.1.3 初始化引擎
1、接口说明

在设置好业务信息后就可以开始初始化引擎了。

2、函数原型

    - (enum GCloudVoiceErrno) initEngine;

3、示例代码

    [[GVGCloudVoice sharedInstance] initEngine];

4、出错处理

GCLOUD_VOICE_NEED_SETAPPINFO ：  需要先调用SetAppInfo    


#### 2.1.4 设置引擎模式
1、接口说明

在使用语音功能时，需要根据需要设置成离线、实时还是转文字的模式；如果是小队语音或者国战语音，设置成实时模式；如果是语音消息，设置成离线模式；如果是语音转文字，设置成翻译模式。

2、函数原型

    enum GCloudVoiceMode
    {
    RealTime = 0, // realtime mode for TeamRoom or NationalRoom
    Messages, // voice message mode
    Translation,  // speach to text mode
    };
    (enum GCloudVoiceErrno) setMode:(enum GCloudVoiceMode) mode;
    
    参数	类型	意义
    mode	GCloudVoiceMode	如果是小队语音或者国战语音，设置成实时模式；如果是语音消息，设置成离线模式；如果是语音转文字，设置成翻译模式
  
3、示例代码

    [[GVGCloudVoice sharedInstance] setMode:RealTime];
                                
4、出错处理

GCLOUD_VOICE_NEED_SETAPPINFO ：需要先调用SetAppInfo  
  
#### 2.1.5 查询触发事件回调
1、接口说明

通过在update里面周期的调用Poll可以触发事件回调

2、函数原型

   ` - (enum GCloudVoiceErrno) poll;`
  
3、示例代码

_pollTimer = [NSTimer scheduledTimerWithTimeInterval:1.000/15 repeats:YES block:^(NSTimer * _Nonnull timer) {
    [[GVGCloudVoice sharedInstance] poll];
}];
  
4、出错处理

    GCLOUD_VOICE_NEED_INIT ：需要先调用Init进行初始化 

#### 2.1.6 系统发生Pause
1、接口说明

当系统发生Pause事件时，需要同时通知引擎进行Pause

2、函数原型

    - (enum GCloudVoiceErrno) pause;

3、出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化 


#### 2.1.7 系统发生Resume
1、接口说明

当系统发生Resume事件时，需要同时通知引擎进行Resume

2、函数原型

    - (enum GCloudVoiceErrno) resume;

3、出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化

### 2.2实时语音API
#### 2.2.1 加入小队语音
1、接口说明

使用实时语音的小队语音功能时，需要先加入小队语音房间

2、函数原型

       - (enum GCloudVoiceErrno) joinTeamRoom:(const char * _Nullable)roomName timeout: (int) msTimeout;
    参数	类型	意义
    roomName	const char *	要加入的房间名
    msTimeout	int	加入房间的超时时间，单位是毫秒
    加入房间的结果，需要通过void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID) ;进行回调
  
3、示例代码

     [[GVGCloudVoice sharedInstance] joinTeamRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000]; 
 
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR ：  需要先调用SetMode设置成实时模式    
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
GCLOUD_VOICE_REALTIME_STATE_ERR ：** 实时语音状态不对，比如已经加入房间了，需要先调用QuitRoom才能再次加入

#### 2.2.2 加入国战语音
1、接口说明

使用国战语音功能时，需要先加入国战语音房间

2、函数原型

        enum GCloudVoiceMemberRole
    {
    Anchor = 1, // member who can open microphone and say
    Audience,   // member who can only hear anchor's voice
    };
    - (enum GCloudVoiceErrno) joinNationalRoom:(const char *_Nullable)roomName role: (enum GCloudVoiceMemberRole) role timeout: (int) msTimeout;   
    参数	类型	意义
    roomName	const char *	要加入的房间名
    role	GCloudVoiceMemberRole	成员加入的角色，听众只能收听语音不能发送语音，而主播既可以发送语音也可以收听语音
    msTimeout	int	加入房间的超时时间，单位是毫秒
    加入房间的结果，需要通过void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID) ;进行回调

3、示例代码

    [[GVGCloudVoice sharedInstance] joinNationalRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] role:role timeout:18000];   

4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  需要先调用SetMode设置成实时模式    
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如已经加入房间了，需要先调用QuitRoom才能再次加入

#### 2.2.3 退出实时语音
1、接口说明

当不需要使用实时语音，可以从实时语音（包括小队语音和国战语音）房间中退出。

2、函数原型

        - (enum GCloudVoiceErrno) quitRoom:(const char * _Nullable)roomName timeout:(int) msTimeout ;  
    参数	类型	意义
    roomName	const char *	要退出的房间名
    msTimeout	int	退出房间的超时时间，单位是毫秒
    退出房间的结果，需要通过void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName)进行回调

3、示例代码

    [[GVGCloudVoice sharedInstance] quitRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000]; 

4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是实时语音模式   
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如还没有加入房间

#### 2.2.4 打开麦克风

1、接口说明

在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），需要打开麦克风才能采集音频并发送到网络

2、函数原型

    - (enum GCloudVoiceErrno) openMic; 
 
3、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是实时语音模式   
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如还没有加入房间
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR ： 当前以听众身份加入的大房间，不能开麦

#### 2.2.5 关闭麦克风
1、接口说明

在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），当不需要采集音频并发送到网络，可以调用关闭麦克风接口

2、函数原型
    
  ` - (enum GCloudVoiceErrno) closeMic;`
   
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是实时语音模式   
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如还没有加入房间
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR ： 当前以听众身份加入的大房间，不能开麦关麦


#### 2.2.6 打开扬声器

1、接口说明 在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），需要打开扬声器才能从网络接收数据并播放

2、函数原型

   `- (enum GCloudVoiceErrno) openSpeaker;`
   
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是实时语音模式   
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如还没有加入房间

#### 2.2.7 关闭扬声器

1、接口说明
在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），当不需要从网络接收数据并播放时，可以调用关闭麦克风接口

2、函数原型

 `   - (enum GCloudVoiceErrno) closeSpeaker;  `
    
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是实时语音模式   
GCLOUD_VOICE_REALTIME_STATE_ERR ：  实时语音状态不对，比如还没有加入房间

#### 2.2.8 加入房间回调

1、接口说明

当加入房间成功或者失败时会通过回调进行通知

2、函数原型

        - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID;
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    roomName	const char *	加入的房间名
    memberID	int	如果加入成功的话，表示加入后的成员ID


3、示例代码

    #pragma mark delegate

    - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {
        NSString *msg;
        if (GV_ON_JOINROOM_SUCC == code) {
            msg = [NSString stringWithFormat:@"Join Room Success"];
        } else {
            msg = [NSString stringWithFormat:@"Join Room Failed with code: %d", code];
        }
        [self warnning:msg];
    }

#### 2.2.9 退出房间回调

1、接口说明

当退出房间时，结果通过回调进行通知

2、函数原型

        - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    roomName	const char *	退出的房间名
    memberID	int	如果加入成功的话，表示加入后的成员ID

3、示例代码

             - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName {
    [_pollTimer invalidate];
    }

#### 2.2.10 成员状态改变回调

1、接口说明

当房间中的其他成员开始说话或者停止说话的时候，通过该回调进行通知

2、函数原型

    - (void) onMemberVoice:(const unsigned int * _Nullable)members withCount: (int) count
    参数	类型	意义
    members	int[]	改变状态的member成员，其值为[memberID	status]这样的对，总共有count对，status有“0”：停止说话 “1”：开始说话 “2”:继续说话
    count	int	改变状态的成员的数目

3、示例代码

    - (void) onMemberVoice:    (const unsigned int * _Nullable)members withCount: (int) count {
        for (int i=0; i<count; i++) {
            NSLog(@"Member %d status %d", *((int*)members+2*i), *((int *)members+2*i+1));
        }
    }
### 2.3 离线语音API
#### 2.3.1 申请语音消息key
1、接口说明

在语音消息的模式下，需要先申请许可才可以正常使用

2、函数原型

        - (enum GCloudVoiceErrno) applyMessageKey:(int) msTimeout;
    参数	类型	意义
    msTimeout	itn	超时时间，单位毫秒
    申请的结果通过void OnApplyMessageKey(GCloudVoiceCompleteCode code) ;进行回调

4、出错处理

GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，比如超时范围5000ms-60000ms。
GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_AUTHKEY_ERR ： 请求Key的内部错误，此时需要联系GCloud团队，并提供日志进行定位
#### 2.3.2 限制最大语音消息的长度

1、接口说明

在语音消息的模式下，可以限制最大语音消息的长度，目前默认是2min，最大不超过2min。

2、函数原型

    - (enum GCloudVoiceErrno) setMaxMessageLength:(int) msTime;
    参数	类型	意义
    msTimeout	itn	最大语音消息长度，单位毫秒

3、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，时间范围1000ms-1000*2*60ms。

#### 2.3.3 开始录音
1、接口说明

在语音消息的模式下，开始录音时，需要提供一个录音文件存储的地址路径

2、函数原型

    - (enum GCloudVoiceErrno) startRecording:(const char *_Nullable) filePath;
参数	类型	意义
filePath	const char *	录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是离线语音模式
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，路径为空。
GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写


#### 2.3.4 停止录音
1、接口说明

在语音消息的模式下，调用停止录音接口会

2、函数原型

    - (enum GCloudVoiceErrno) stopRecording;
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是离线语音模式
GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可  

#### 2.3.5 上传录音的文件

1、接口说明

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2、函数原型
    
       - (enum GCloudVoiceErrno) uploadRecordedFile:(const char *_Nullable) filePath timeout: (int) msTimeout ;
    参数	类型	意义
    filePath	const char *	录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"
    msTimeout	int	上传文件超时时间
    上传的结果通过void OnUploadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID)进行回调
    
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是离线语音模式
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，路径为空。
GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可读
GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试

#### 2.3.6 下载录音的文件

1、接口说明

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2、函数原型

        - (enum GCloudVoiceErrno) downloadRecordedFile:(const char *_Nullable)fileID filePath:(const char *_Nullable) downloadFilePath timeout: (int) msTimeout ;
    参数	类型	意义
    fileID	const char *	要下载文件的文件ID
    downloadFilePath	const char *	下载录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"
    msTimeout	int	下载文件超时时间
    下载的结果通过void OnDownloadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID) ;进行回调

4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是离线语音模式
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，路径为空。
GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写或者不可读
GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试

#### 2.3.7 开始播放下载的音频

1、接口说明

下载下来的音频文件，需要调用相关接口进行播放

2、函数原型

       - (enum GCloudVoiceErrno) playRecordedFile:(const char *_Nullable) downloadFilePath;
    参数	类型	意义
    filePath	const char*	下载文件存储的地址路径，路径中需要"/"作分隔，不能用"\"
    如果正常播放完，会回调void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath)

4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ： 当前模式不是离线语音模式
GCLOUD_VOICE_PARAM_INVALID ：  传入的参数不对，路径为空。
GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写
GCLOUD_VOICE_SPEAKER_ERR : 打开麦克风失败

#### 2.3.8 停止播放下载的音频

1、接口说明

中断播放动作

2、函数原型

  ` - (enum GCloudVoiceErrno) stopPlayFile;`
   
4、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_MODE_STATE_ERR  ：  当前模式不是离线语音模式

#### 2.3.9 请求语音消息Key回调

1、接口说明

请求语音消息许可的时候会回调

2、函数原型

    - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code
参数	类型	意义
code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义

3、示例代码

   - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code {
NSString *msg;
msg = @"Apply AuthKey Success";
[self warnning:msg];
}
#### 2.3.10 上传完成回调
1、接口说明

上传语音文件后的结果通过这个进行回调

2、函数原型

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    filepath	const char *	上传的文件路径
    fileid	const char *	文件的id

3、示例代码

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID  {
    _fileID = [NSString stringWithFormat:@"%s", fileID];
    [self warnning:@"Upload Success"];
    }

#### 2.3.11 下载完成回调

1、接口说明

下载语音文件后的结果通过这个进行回调

2、函数原型

      - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID 
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    filepath	const char *	下载的路径
    fileid	const char *	文件的id

3、示例代码

     - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID {
    NSString *msg;
    msg = @"Download File Success";
    [self warnning:msg];
    }

#### 2.3.12 正常播放完成后回调

1、接口说明

如果用户没有暂停播放，而语音文件已经播放完了，通过这个进行回调

2、函数原型

       - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    filepath	const char *	播放的文件路径

3、示例代码

       - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath {
    
    NSString *msg;
    msg = @"Finish Play File";
    [self warnning:msg];
    } 

### 2.4 语音转文字
#### 2.4.1 进行语音转文字
1、接口说明

使用该函数，进行语音转文字。

2、函数原型

     - (enum GCloudVoiceErrno) speechToText:(const char *_Nullable)fileID timeout:(int) msTimeout language:(enum GCloudLanguage) language ;
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    fileID	string	需要翻译的文件id
    result	string	翻译的文字结果

3、出错处理

GCLOUD_VOICE_NEED_INIT ：  需要先调用Init进行初始化
GCLOUD_VOICE_STTING  ：  正在进行上一次的语音转文字

4、示例代码

[[GVGCloudVoice sharedInstance] speechToText:[_fileID cStringUsingEncoding:NSUTF8StringEncoding]  timeout:18000 language:China];

#### 2.4.2 语音转文字完成后回调
1、接口说明

语音转文字的结果通过这个回调进行通知

2、函数原型

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result
    参数	类型	意义
    code	GCloudVoiceCompleteCode	参见GCloudVoiceCompleteCode定义
    fileID	const char *	翻译文件的fileid
    result	const char *	翻译的文字结果
  
3、示例代码

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result {
    _resultTV.text = [NSString stringWithUTF8String: result];
    }
    