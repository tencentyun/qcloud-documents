
## Log Location

Logs are written to the storage of terminal at the same time when they are output to the development console. Developers can find the logs at the following locations:

### Android

SDK | Directory
:--:|:--:
iLiveSDK|tencent/imsdklogs/SDK name/ilivesdk_YYYYMMDD.log
IMSDK|tencent/imsdklogs/SDK name/imsdk_YYYYMMDD.log
AVSDK|tencent/imsdklogs/SDK name/QAVSDK_YYYYMMDD.log



### iOS

SDK | Directory
:--:|:--:
iLiveSDK|Library/Caches/imsdk_YYYMMDD.log
IMSDK|Library/Caches/imsdk_YYYMMDD.log
AVSDK|Library/Caches/QAVSDK_YYYMMDD.log



## API for Acquiring Logs

### Application scenarios 

* Any scenario where ILVB logs need to be acquired from phone


<img src="https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/log_report.png" width = "360" height = "480" alt="Picture name" align=center />

### Tips on Usage

1. Integrate iLive SDK
      
	**Above 1.4.0**
	 	
2. When the user needs to report the log, call the API for reporting log. iLive SDK will directly transmit the log to Tencent Cloud backend.     

	
**Android API**	

```java
/**
 * Report the log
 *
 * @param desc Description
 * @param data - 0: today; 1: yesterday; 2: the day before yesterday, and so on
 * @param callBack Callback
 * 
 */
ILiveSDK.getInstance().uploadLog(String desc, int data ILiveCallBack callback);
```
**iOS API**         

```java
/**
 Report the log
 
 @param logDesc       Log description
 @param dayOffset    Date, 0: today; 1: yesterday; 2: the day before yesterday, and so on
 @param uploadResult Report callback
 */
(void)uploadLog:(NSString *)logDesc logDayOffset:(int)dayOffset uploadResult:(ILiveLogUploadResultBlock)uploadResult;
```

4. Developers can query and download the logs uploaded by users at [Log Query Platform](http://vip.avc.qcloud.com/SdkLog/home).


![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/iLiveSDK_Log.png)


5. When further analysis of problem is needed, log ID can be provided for Tencent Cloud technical support staff.

### FAQs

* What logs will be reported?  
     
    ** iLiveSDK process log, IMSDK message system log, AVSDK log, as well as Crash information log which will be available later**
    
* How to specify the date for which the logs need to be reported?     

	**0: today; 1: yesterday; 2: the day before yesterday, and so on**
	
* What happens if the network is disconnected during the reporting process?      

	**Retransmission is needed**
	
*Do the reported logs have a deletion policy?     

    **The logs are retained for a maximum of 15 days. When this limit is reached, or the number of logs exceeds 1000, deletion will be performed automatically** 
    
# Error Codes 
		        
	0: Log reported successfully

	8101: Incorrect parameter

	8102: File does not exist

	8103: Compression failed

	8104: Failed to obtain the signature

	8105: Protocol resolution failed

	8106: Upload failed

	8107: Reporting failed






## Log of iLive SDK key path

When encountering some problem, developer can, based on the logs, identify the process with which an error occurs and thus solve the problem.<br/><br/>
*Filtering keyword Key_Procedure in iLiveSDK 1.0.3 or above allows you to search for the key path for creating or joining a room*

### Android

#### The correct log on creating a room is as follows

![Create a room]https://mc.qcloudimg.com/static/img/587519130c2cb55ea0788def61b2e70d/rightProcess.png)

* The following steps are involved


```C
1. Initialization
ILiveSDK: Key_Procedure|initSdk->init appid:1400001692, accountType:884    

2. Configure rendering layer       
ILVBRoom: Key_Procedure|ILVB-Room|init root view    
AVVideoGroup: Key_Procedure|ILVB-AVVideoGroup|init sub views
    
3. iLive login   
ILVBLogin: Key_Procedure|ILVB-iLiveLogin strart |id:will     
ILVBLogin: Key_Procedure|ILVB-iLiveLogin|login success    

4. Create room   
ILVBRoom: Key_Procedure|ILVB-Room|start create room:6357 enter with im:true|video:true   

5. Live room is created
ILVBRoom: Key_Procedure|createRoom->im room ok:6357     

6. AV room is created
ILVBRoom: Key_Procedure|ILVB-Room|enter av room complete result: 0      

7. Enable camera
ILVBRoom: Key_Procedure|ILVB-Room|strart enableCamera     

8. Server callback "User has become online"
ILVBRoom: Key_Procedure|ILVB-Room|onEndpointsUpdateInfo myself id has camera will     

9. Rendering
AVRootView: Key_Procedure|ILVB-AVRootView|renderVideoView->enter index:0|0,0,1080,1845       

10. The camera reports a success callback    
ILVBRoom: Key_Procedure|ILVB-Room|enable camera id:0/true     

```

#### The correct log on joining a room is as follows

![Join a room](https://mc.qcloudimg.com/static/img/7932e829882bbd68e9c0a05af24a2e68/joinRoomProcess.png)

* The following steps are involved


```C
1. Initialization 

ILiveSDK: Key_Procedure|initSdk->init appid:1400001692, accountType:884   
  
2. Configure rendering layer
ILVBRoom: Key_Procedure|ILVB-Room|init root view      
AVVideoGroup: Key_Procedure|ILVB-AVVideoGroup|init sub views   

3. iLive login
ILVBLogin: Key_Procedure|ILVB-iLiveLogin strart |id:will      
ILVBLogin: Key_Procedure|ILVB-iLiveLogin|login success       

4. Join the room  
ILVBRoom: Key_Procedure|joinRoom->id: 6352 isIMsupport: true       

5. Live room is created    
ILVBRoom: Key_Procedure|joinLiveRoom joinIMChatRoom callback succ    

6. Joined AV room successfully       
ILVBRoom: Key_Procedure|ILVB-Room|enter av room complete result: 0        

7. Get the server callback "Member has become on line" 
ILVBRoom: Key_Procedure|ILVB-Endpoint | requestRemoteVideo id [willguo]     

8. Render the interface
AVRootView: Key_Procedure|ILVB-AVRootView|renderVideoView->enter index:0| 0,0,1080,1845      

```


### iOS

#### The correct log on creating a room is as follows

![Create a room](http://mc.qcloudimg.com/static/img/f1ee4994ede1dd89199361973a1cfbee/image.jpg)

* The following steps are involved

```C
1. Initialize the SDK
ILiveSDK:Key_Procedure|initSdk|succ

2. Log in to the SDK (in hosted mode. If it is in a standalone mode, no log for tlsLogin exists)
ILiveLogin:Key_Procedure|tlsLogin|start:id:ken1
ILiveLogin:Key_Procedure|tlsLogin|succ
ILiveLogin:Key_Procedure|iLiveLogin|start:id:ken1
ILiveLogin:Key_Procedure|iLiveLogin|succ

3. Create the root view and VJ view for rendering
ILiveOpenGL:Key_Procedure|createOpenGLView|succ
ILiveOpenGL:Key_Procedure|addRenderView|succ:frame:{{0, 0}, {375, 667}},key:ken1

4. Create a chat group
ILiveRoom:Key_Procedure|createIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|createIMGroup|succ

5. Create a live room
ILiveRoom:Key_Procedure|enterAVRoom|start:roomId:9878
ILiveRoom:Key_Procedure|enterAVRoom|succ

6. Enable the camera and receive the server event (in this case, the camera enabling event) callback
ILiveRoom:Key_Procedure|enableCamera|start:enable:YES
ILiveRoom:Key_Procedure|OnEndpointsUpdateInfo|evenId:3,id:ken1
ILiveRoom:Key_Procedure|enableCamera|succ:enable:YES

7. Receive the video frame (printing at intervals)
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:1
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:11
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:21

8. Exit the live room
ILiveRoom:Key_Procedure|exitAVRoom|start
ILiveRoom:Key_Procedure|exitAVRoom|succ

9 Quit the chat group (group owner disbands the group)
ILiveRoom:Key_Procedure|quitIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|quitIMGroup|succ:code:10009
ILiveRoom:Key_Procedure|deleteIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|deleteIMGroup|succ
```

#### The correct log on joining a room is as follows

![Join a room](http://mc.qcloudimg.com/static/img/54b586d5fa373c5f1c359d624bf4557a/image.png)

* The following steps are involved

```C
1. Initialize the SDK
ILiveSDK:Key_Procedure|initSdk|succ

2. Log in to the SDK (in hosted mode. If it is in a standalone mode, no log for tlsLogin exists)
ILiveLogin:Key_Procedure|tlsLogin|start:id:ken2
ILiveLogin:Key_Procedure|tlsLogin|succ
ILiveLogin:Key_Procedure|iLiveLogin|start:id:ken2
ILiveLogin:Key_Procedure|iLiveLogin|succ

3. Create the root view and VJ view for rendering
ILiveOpenGL:Key_Procedure|createOpenGLView|succ
ILiveOpenGL:Key_Procedure|addRenderView|succ:frame:{{0, 0}, {414, 736}},key:ken1

4. Join the chat group
ILiveRoom:Key_Procedure|joinIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|joinIMGroup|succ

5. Join the live room
ILiveRoom:Key_Procedure|enterAVRoom|start:roomId:9878
ILiveRoom:Key_Procedure|enterAVRoom|succ

6. server event (in this case, the camera enabling event) callback
ILiveRoom:Key_Procedure|OnEndpointsUpdateInfo|evenId:3,id:ken1

7. Receive the video frame (printing at intervals)
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:1
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:11
ILiveGLBase:Key_Procedure|videoFrame|id:ken1,index:21

8. Exit the live room
ILiveRoom:Key_Procedure|exitAVRoom|start
ILiveRoom:Key_Procedure|exitAVRoom|succ

9. Quit the chat group
ILiveRoom:Key_Procedure|quitIMGroup|start:groupId:9878
ILiveRoom:Key_Procedure|quitIMGroup|succ
```



