## Project Structure
Download the Mini LVB source code from Github and open the project with Android Studio. The project structure is as follows:
![](//mc.qcloudimg.com/static/img/af1b516a6c254da0224486bd35e3d2b6/image.png)

| File/Directory | Description | 
|---------|---------|
| base | The common library used by Mini LVB's modules |
| logic | The code of Mini LVB's logic layer |
| ui | The code of Mini LVB's UI layer |
| ui/customviews | Custom widgets used by Mini LVB's UI |
| jniLibs | Tencent SDKs relied by Mini LVB, mainly Bugly SDK, TLS SDK, IM SDK and RTMP SDK |

## Library Instructions

### [LVB SDK (Required)](https://cloud.tencent.com/document/product/454/7873)  

The main SDK used by MLVB, providing features such as push, LVB, VOD, joint broadcasting and screencap.
- JAR package
txrtmpsdk.jar
- so library
    Because MLVB uses joint broadcasting, choose the integrated full version. Currently, the full version supports only armeabi and armeabi-v7 architectures.
		
| Library Name | Description |
|  --------- | ---------- |
| libtxrtmpsdk.so | LVB core components |
| libtraeimp-rtmp-armeabi.so | Joint broadcasting library |
| libstlport_shared.so | Joint broadcasting library |

### IM SDK (Required)

Provides messaging feature.
- JAR package

| Package Name | Description |
| :--------: | :--------:| 
| imsdk.jar | ImSDK base package. It only provides basic features such as messaging, data relation chain management and group management. | 
| qalsdk.jar | SDK network layer JAR package |  
| soload.jar | Improve the success rate of loading IM SDK so libraries | 
| mobilepd.jar | JAR package related to protobuffer handling |  
| tls_sdk.jar | JAR package related to the account system |   
| wup-1.0.0-SNAPSHOT.jar | JAR pacakge related to Wireless Uniform Protocol | 

- so library
MLVB currently integrates only the armeabi architecture.
	- lib_imcore_jni_gyp.so
	- libqalcodecwrapper.so
	- libqalmsfboot.so
  - libwtcrypto.so

### [UGC Short Videos (Optional)](https://cloud.tencent.com/document/product/584/9369)
Recording, editing and publishing UGC videos.
- JAR package


| Package Name | Description |
| :--------: | :--------:| 
| ugcupload.jar | JAR package that implements UGC files' upload to the VOD system |
| sha1utils.jar | JAR package that implements SHA calculation of UGC files to be uploaded |
| okio-1.6.0.jar | I/O library to handle network operations |
| okhttp-3.2.0.jar | Network request library |
| cos-sdk-android.1.4.3.6.jar | JAR package related to COS object-based storage |

- so library


| Library Name | Description |
| :--------: | :--------:| 
| libTcHevcDec.so | Used for H265 playback |
| libTXSHA1.so | Implements SHA calculation of UGC files to be uploaded |


### Value-added Commercial Version (not included in Mini LVB's source code)

With patented AI technologies developed by YouTu Lab, this version supports special effects such as eye enlarging, face slimming, motion effect sticker and green screen. Related so libraries could be deleted if these features are not required.
- libblasV8.so   
- librsjni.so  
- libRSSupport.so  

### volley (optional)
3rd-party network request library

### Gson (optional)
3rd-party Java class library to convert Java objects into JSON and back

### Glide (optional)
3rd-party image loading library

### dfm (optional)
3rd-party on-screen commenting library. It's recommended to keep this library if on-screen commenting is desired.



## Module Introduction
Mini LVB is divided into 6 modules by their functions. They are: account, LVB/Replay list management, push, playback, messaging and profile. The code is also classified in this way. Below we will introduce these modules and their implementations respectively:

### Account Module
#### Module Introduction
- Account module handles the logics of user login/registration and login cache.
- Login and registration are implemented by login via [TLS SDK Delegate](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F).
- If you already have your own account system, you can simply replace this module and call guestLogin function in TCLoginMgr to use IM channel as a guest. For more information, please see [Replace Account](https://cloud.tencent.com/doc/api/258/6441).
- After the TLS SDK login authentication is successful, you can login to the IM module by passing UserId and UserSig returned by the authentication to the login interface of the ImSDK.
- Users can register and login by either username and password or mobile verification code.
- Account module caches locally the basic information (UserId and UserSig) of the last logged-in user. It will get the information of recently logged-in users from the interface and determine if re-login is required.
- Login is mutually exclusive. The client that logged in first would be forcibly logged out.

#### Related Code 
- Logic:
	- TCLoginMgr.java: login management class that implements user login/registration related interface and the last login user cache interface.
	- TCApplication.java: During TIMManager's initialization, registers UserStatusListener to listen for user signature invalidation and forced logout.
	
- UI:
	- TCLoginActivity.java: user login page
	- TCRegisterActivity.java: user registration page

### Message
#### Module Introduction
- Mini LVB's interactive message feature is mainly based on the group chat feature of [ImSDK](https://cloud.tencent.com/doc/product/269/1561). It's available when IMSDK is logged-in.
- Every live room is a large LVB group, which needs to be created before actually pushing occurs on the push end and disbanded after the pushing ends. Player ends join the group when they join the live room, and exit the group when they exit the room.
- To listen for desired messages, implement a messaging listener class. Currently supported message types include text message, "Like" message, user joining/leaving message and group disband message.
- All messages are sent as text messages in a uniform JSON format. The JSON carries information about message type, sender ID, nickname, profile photo and message text. The receivers receive and parse the JSON, and accordingly use the callbacks to pass all kinds of messages to the upper levels.

#### Related Code
- Logic:
	- TCCharRoomMgr.java: Messaging management class. It's responsible for initializing message loop, message parsing and packaging. It also provide interfaces for VJs to create/disband message groups, and for viewers to join/exit message groups.
- UI:	
	- TCLivePublisherActivity.java: Implements VJ ends' message displaying activity.
	- TCLivePlayerActivity.java: Implements viewer ends' message displaying activity.
	- TCInputTextMsgDialog.java: Custom widget that implements a text input.
	- TCHeartLayout.java/TCHeartView.java: Custom widget that implements floating heart animation when "Like" is given.
	- TCDanmuMgr.java: Widget that implements on-screen comments. Based on open-sourced Bilibili Danmaku library.

### Main Interface & List Management
#### Module Introduction
- The main interface is mainly responsible for switching between the three top-level functions: list, push and personal information.
- After a successful login, the list interface is shown by default. Tapping the push button would switch to the push settings; tapping the personal information button would switch to the personal information.
- List management includes pulling and displaying lists. Currently, our list pulling protocols support pulling LVB lists, VOD lists and hybrid lists. Mini LVB uses hybrid lists, which sort LVBs in front of VODs.

#### Related Code 
- Logic:
	- TCLiveListMgr.java: LVB list management class that implements fetching list from local memory and updating list on the servers.
	- TCLiveInfo.java: LVB video data.
- UI:
	- TCLiveListFragment.java: LVB list display page that displays the whole LVB list.
	- TCLiveListAdapter.java: LVB list's adapter that adapts LVB data into list views.

### Push Module
#### Module Introduction
- The main features of push module are VJ video data acquisition, rendering, pushing, interacting between VJs and viewers, etc.
- VJs can capture their video and audio data and push them to the video cloud servers, so that the viewers can view them on other clients. VJs can customize features such as capture resolution, beauty filter, whitening and hardware encoding.
- VJs can create their own rooms. Viewers can join these rooms and interact with the VJs by ordinary comments, on-screen comments, and "Like" comments. These comments are shown to the VJs in corresponding comment lists and on-screen comments' locations. For more information about comments, please see "Message" module.
- The viewer lists can be displayed on VJ ends. When viewers join or leave a room, the list is refreshed, and the VJ is notified.

#### Push Timing Diagram
![](//mc.qcloudimg.com/static/img/6fb00666a6a1cdea732fbddccc5fc786/image.png)

#### UI Hierarchy
The SDK would render the video on parameter View (i.e. videoParentView) of startCameraPreview. The SDK would create a sub-view for OpenGL to render on. To add UI widgets such as on-screen comments and flower gifting on top of the video, create a sibling view as shown in the follow figure.
![](//mc.qcloudimg.com/static/img/3da33f8c62b9339a365faddd2635faa2/image.png)

#### Related Code 
- Logic:
	- TCPusherMgr.java: LVB management class. It communicates with the backend, pulls the LVB URL, and notifies the backend to exit LVB.
- UI:
	- TCLivePublisherActivity.java: Push module activity. All the push management, message management and animation effects are implemented in this class.

### Playback Module
#### Module Introduction
- The main features of playback module are VJ video data playback, message interaction between viewers and VJs, etc.
- Viewers can join VJs' rooms and send ordinary comments, on-screen comments, and "Like" comments. For more information about comments, please see "Message" module.
- Viewers can see VJs' information. When viewers join or leave a room, the viewer list is refreshed, and notifications about their joining or leaving are shown in the notification list.

#### Playback Timing Diagram
![](//mc.qcloudimg.com/static/img/fb9f9002c2d973d069bb9c1568037e26/image.png)

#### UI Hierarchy
Please see the UI hierarchy of the push module.

#### Related Code
- Logic:
	- TCPlayerMgr.java: Playback management class. It communicates with the backend, and notifies the backend to enter the room, exit from the room, and use the "giving a like" feature
- UI:
	- TCLivePublisherActivity.java: Playback module activity, including VOD and LVB. All the playback management, message management and animation effects are implemented in this class.


	
### Personal Information
#### Module Introduction
- Personal information module is mainly responsible for displaying, storing, modifying and synchronizing user information to the server.
- User information includes profile photo, nickname, gender, LVB cover and location, etc. Personal information module is provided by IMSDK. For developers to customize users' information, IMSDK supports custom field extension.
- The module synchronizes users' latest personal information to the App. Users can browse their information through this module, including profile photo, nickname and gender.
- With this module, users can also modify their information, which would be synchronized to the servers.
- Other modules can also get and modify users' information through this module.
	
#### Related Code
- Logic:
	- TCUserInfoMgr.java: User information management class. It's responsible for storing, modifying, and synchronizing user information.
	- ITCUserInfoMgrListener.java: The callbacks of the communication between user information management class and the servers. It's responsible for receiving the results of user information queries and modifications, etc.
- UI:	
	- TCUserInfoFragment.java: Implements the activity that displays user information.
	- TCEditUseInfoActivity.java: Implements the activity to modify user information.
	- TCLineEditTextView.java: A text editing widget. It's a simple wrapper of EditText to edit text and display related information.
	- TCTextEditActivity.java: Implements the text editing activity. It's a wrapper of EditText to edit text in an independent activity and display related information.

