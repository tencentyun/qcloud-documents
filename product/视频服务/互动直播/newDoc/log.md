## 日志说明

在程序运行的时候，会把关键信息写入日志中。<br/>
这些信息是调试和查问题的重要帮助，不建议开发者关闭这些日志。

## 日志位置

日志在开发控制台输出的同时，也会写入终端的存储中。开发者可以在这些地方找到日志：

### Android

SDK|目录
:--:|:--:
iLiveSDK|tencent/imsdklogs/包名/ilivesdk_YYYYMMDD.log
IMSDK|tencent/imsdklogs/包名/imsdk_YYYYMMDD.log
AVSDK|tencent/imsdklogs/包名/QAVSDK_YYYYMMDD.log



### ios

SDK|目录
:--:|:--:
iLiveSDK|Library/Caches/imsdk_YYYMMDD.log
IMSDK|Library/Caches/imsdk_YYYMMDD.log
AVSDK|Library/Caches/QAVSDK_YYYMMDD.log


## iLive SDK 关键路径的LOG

开发者在遇到问题时，可以根据这些日志，判断哪个流程执行出错，有助于定位问题。<br/><br/>
*在iLiveSDK 1.0.3以后版本过滤关键字Key_Procedure 会搜索到创建房间或加入房间的关键路径*

### Android

#### 创建房间流程正确LOG如下

![创建房间](https://mc.qcloudimg.com/static/img/587519130c2cb55ea0788def61b2e70d/rightProcess.png)

* 具体包括以下几个步骤


```C
1. 初始化步骤
ILiveSDK: Key_Procedure｜initSdk->init appid:1400001692, accountType:884    

2. 设置渲染层       
ILVBRoom: Key_Procedure|ILVB-Room|init root view    
AVVideoGroup: Key_Procedure|ILVB-AVVideoGroup|init sub views
    
3. iLive登录   
ILVBLogin: Key_Procedure｜ILVB-iLiveLogin strart |id:will     
ILVBLogin: Key_Procedure｜ILVB-iLiveLogin|login success    

4. 创建房间   
ILVBRoom: Key_Procedure|ILVB-Room|start create room:6357 enter with im:true|video:true   

5. 直播聊天室创建完毕
ILVBRoom: Key_Procedure|createRoom->im room ok:6357     

6. AV房间创建完毕
ILVBRoom: Key_Procedure|ILVB-Room|enter av room complete result: 0      

7. 打开摄像头
ILVBRoom: Key_Procedure|ILVB-Room|strart enableCamera     

8. server回调用户上线
ILVBRoom: Key_Procedure|ILVB-Room|onEndpointsUpdateInfo myself id has camera will     

9. 渲染
AVRootView: Key_Procedure|ILVB-AVRootView|renderVideoView->enter index:0|0,0,1080,1845       

10. 摄像头上报成功回调    
ILVBRoom: Key_Procedure|ILVB-Room|enable camera id:0/true     

```

#### 加入房间流程正确LOG如下

![加入房间](https://mc.qcloudimg.com/static/img/7932e829882bbd68e9c0a05af24a2e68/joinRoomProcess.png)

* 具体包括以下几个步骤


```C
1. 初始化 

ILiveSDK: Key_Procedure｜initSdk->init appid:1400001692, accountType:884   
  
2. 设置渲染层
ILVBRoom: Key_Procedure|ILVB-Room|init root view      
AVVideoGroup: Key_Procedure|ILVB-AVVideoGroup|init sub views   

3. iLive登录
ILVBLogin: Key_Procedure｜ILVB-iLiveLogin strart |id:will      
ILVBLogin: Key_Procedure｜ILVB-iLiveLogin|login success       

4. 加入房间  
ILVBRoom: Key_Procedure|joinRoom->id: 6352 isIMsupport: true       

5. 直播聊天室加入成功    
ILVBRoom: Key_Procedure|joinLiveRoom joinIMChatRoom callback succ    

6. AV房间加入成功       
ILVBRoom: Key_Procedure|ILVB-Room|enter av room complete result: 0        

7. 获取server 成员上线回调 
ILVBRoom: Key_Procedure|ILVB-Endpoint | requestRemoteVideo id [willguo]     

8. 渲染界面
AVRootView: Key_Procedure|ILVB-AVRootView|renderVideoView->enter index:0| 0,0,1080,1845      

```


### ios

#### 创建房间流程正确LOG如下

![创建房间](http://mc.qcloudimg.com/static/img/f1ee4994ede1dd89199361973a1cfbee/image.jpg)

* 具体包括以下几个步骤

```C
1. 初始化SDK
ILiveSDK:Key_Procedure|initSdk|succ

2. 登录SDK（托管模式，如果是独立模式，无tlsLogin的log）
ILiveLogin:Key_Procedure|tlsLogin|start:id:ken1
ILiveLogin:Key_Procedure|tlsLogin|succ
ILiveLogin:Key_Procedure|iLiveLogin|start:id:ken1
ILiveLogin:Key_Procedure|iLiveLogin|succ

3. 创建渲染根视图和主播渲染视图
ILiveOpenGL:Key_Procedure|createOpenGLView|succ
ILiveOpenGL:Key_Procedure|addRenderView|succ:frame:{{0, 0}, {375, 667}},key:ken1

4. 创建聊天群组
ILiveRoom:Key_Procedure|createIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|createIMGroup|succ

5. 创建直播房间
ILiveRoom:Key_Procedure|enterAVRoom|start:roomId:9878
ILiveRoom:Key_Procedure|enterAVRoom|succ

6. 打开摄像头并收到server事件（此处是摄像头开启事件）回调
ILiveRoom:Key_Procedure|enableCamera|start:enable:YES
ILiveRoom:Key_Procedure|OnEndpointsUpdateInfo|evenId:3,id:ken1
ILiveRoom:Key_Procedure|enableCamera|succ:enable:YES

7. 收到视频帧（间隔打印）
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:1
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:11
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:21

8. 退出直播房间
ILiveRoom:Key_Procedure|exitAVRoom|start
ILiveRoom:Key_Procedure|exitAVRoom|succ

9 退出聊天群组（群主解散群组）
ILiveRoom:Key_Procedure|quitIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|quitIMGroup|succ:code:10009
ILiveRoom:Key_Procedure|deleteIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|deleteIMGroup|succ
```

#### 加入房间流程正确LOG如下

![加入房间](http://mc.qcloudimg.com/static/img/54b586d5fa373c5f1c359d624bf4557a/image.png)

* 具体包括以下几个步骤

```C
1. 初始化SDK
ILiveSDK:Key_Procedure|initSdk|succ

2. 登录SDK（托管模式，如果是独立模式，无tlsLogin的log）
ILiveLogin:Key_Procedure|tlsLogin|start:id:ken2
ILiveLogin:Key_Procedure|tlsLogin|succ
ILiveLogin:Key_Procedure|iLiveLogin|start:id:ken2
ILiveLogin:Key_Procedure|iLiveLogin|succ

3. 创建渲染根视图和主播渲染视图
ILiveOpenGL:Key_Procedure|createOpenGLView|succ
ILiveOpenGL:Key_Procedure|addRenderView|succ:frame:{{0, 0}, {414, 736}},key:ken1

4. 加入聊天群组
ILiveRoom:Key_Procedure|joinIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|joinIMGroup|succ

5. 进入直播房间
ILiveRoom:Key_Procedure|enterAVRoom|start:roomId:9878
ILiveRoom:Key_Procedure|enterAVRoom|succ

6. server事件（此处是摄像头开启事件）回调
ILiveRoom:Key_Procedure|OnEndpointsUpdateInfo|evenId:3,id:ken1

7. 收到主播视频帧（间隔打印）
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:1
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:11
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:21

8. 退出直播房间
ILiveRoom:Key_Procedure|exitAVRoom|start
ILiveRoom:Key_Procedure|exitAVRoom|succ

9 退出聊天群组
ILiveRoom:Key_Procedure|quitIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|quitIMGroup|succ
```


