## 1. Project Structure

[Download](https://cloud.tencent.com/document/product/454/6991) Mini LVB's source code and find the TCLVBIMDemo.xcworkspace file. This is Mini LVB's XCode project workspace to manage Mini LVB's project code and 3rd-party open-source class library dependencies (under the directory Pods). Use this workspace to compile or browse code related to Mini LVB, instead of directly open Mini LVB's project file TCLVBIMDemo.xcodeproj. After opening TCLVBIMDemo.xcworkspace, you will see the following project directory structure:
![](//mc.qcloudimg.com/static/img/8673bf53392e34a9f38d8a5a8625e8eb/image.jpg)

| Project Directory | Description | 
|---------|---------|
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/Base | The common library used by Mini LVB's modules |
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/Logic| The code of Mini LVB's logic layer |
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/UI| The code of Mini LVB's UI layer |
| TCLVBIMDemo/Framework | The frameworks Mini LVB depends on, mainly TLSSDK, IMSDK TRMPSDK and QALSDK (COS upload components) |
| TCLVBIMDemo/TCLVBIMDemoUpload | The code of the logic layer of the extension for screen capture with Replaykit |
| TCLVBIMDemo/TCLVBIMDemoUploadUI | The code of the UI layer of the extension for screen capture with Replaykit |
| Pods | CocoaPods is used to manage the 3rd-party open-source class libraries used by Mini LVB |

## 2. Compile and Run

Download the code and open **TCLVBIMDemo.xcworkspace** project file (do NOT directly open Mini LVB's project file TCLVBIMDemo.xcodeproj). Currently Mini LVB only support real device debugging, not simulator debugging. Therefore, a project certificate needs to be setup by following steps:
**Step 1: Configure bundle id and signature certificate**
![](//mc.qcloudimg.com/static/img/e2c29a0daa9dbba958c970fadc0a3f09/image.jpg)
**Step 2: Configure App Groups after the signature is configured**
![](//mc.qcloudimg.com/static/img/cd7f2559857e8248efa08551e80e8c05/image.jpg)
**Step 3: Configure other TARGETS**
Follow step 1 and 2 to configure the other two targets: TCLVBIMDemoUpload and TCLVBIMDemoUploadUI. These two targets are used to push videos captured by Replaykit. They can be removed if this feature is not required.

After configuration, the project should be able to run on real devices. However, to actually enable Mini LVB's features, TCConstants.h needs to be configured. For more information, please see [Mobile End Integration](https://cloud.tencent.com/document/product/454/7999#4.-.E7.BB.88.E7.AB.AF.E9.9B.86.E6.88.90.E5.8F.8A.E5.9B.9E.E8.B0.83.E8.AE.BE.E7.BD.AE).

## 3. Module Introduction

Mini LVB is divided into 7 modules by their functions. They are: account, LVB/Replay list management, push, playback, messaging, profile and joint broadcasting. The code is also classified in this way. Below we will introduce these modules and their implementations respectively:

### Account Module
#### Module Introduction
- Account module handles the logics of user login/registration and login cache.
- Login and registration are implemented by login via [TLS SDK Delegate](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F).
- If you already have your own account system, you can simply replace this module and call guestLogin function in TCIMPlatform to use IM channel as a guest. For more information, please see [Replace Account](https://cloud.tencent.com/doc/api/258/6441).
- After the TLS SDK login authentication is successful, you can login to the IM module by passing UserId and UserSig returned by the authentication to the login interface of the ImSDK.
- Users can register and login by either username and password or mobile verification code.
- Account module caches locally the basic information (UserId and UserSig) of the last logged-in user. It will get the information of recently logged-in users from the interface and determine if re-login is required.
- Login is mutually exclusive. The client that logged in first would be forcibly logged out.

#### Related Code
- Logic:
	- TCLoginParam: Used to manage users login information, such as cache and expiration.
	- TCTLSPlatform: Wrappers for interfaces of TLS registration and login
	- TCIMPlatform: Wrappers for interfaces of ImSDK login

- UI:
	- TCLoginViewController: Transition interface, which reads login data from cache, and calls imlogin's interface to login to IM, otherwise jump to the login page.
	- TCTLSLoginViewController: TLS login interface that provides login with username, SMS or as a guest.
	- TCTLSRegisterViewController: TLS registration interface that provides registration with username or SMS.

### Main Interface & List Management
#### Module Introduction
- The main interface is mainly responsible for switching between the three top-level functions: list, push and personal information.
- After a successful login, the list interface is shown by default. Tapping the push button would switch to the push settings; tapping the personal information button would switch to the personal information.
- List management includes pulling and displaying lists. Currently, our list pulling protocols support pulling LVB lists, VOD lists and hybrid lists. Mini LVB uses hybrid lists, which sort LVBs in front of VODs.

#### Related Code
- Logic:
	- TCLiveListModel: Defines the data access layer of LVB/VOD lists and implements serialization / deserialization.
	- TCLiveListMgr: Implements list management's logic layer, which is mainly responsible for fetching, caching and updaing list data. Currently, only full pull is supported. Incremental pull is not supported. List pulling protocol works by paging. When the list pulling interface is called, the logic layer would pull the list from the back-end with a loop until the pulling finishes. To improve users' experience in pulling, refresh the interface and display the data immediately after the first page is fetched.
	
- UI:
	- TCNavigationController: Customize navigation bar, mainly to set the background color of the navigation bar.
	- TCMainTabViewController: The tab bar control for main interface, used to switch between lists, push and personal information.
	- TCPushSettingViewController: Page for push settings, used to set push cover, title and location.
	- TCLiveListCell: The Cell class of LVB/VOD lists, mainly used to display cover, title, nickname, online count, like count and location.
	- TCLiveListViewController: The TableViewController of LVB/VOD lists, responsible for displaying LVB and VOD lists, and jumping to the playback interface when an LVB/VOD is tapped.

### Push Module
#### Module Introduction
- The main features of push module are VJ video data acquisition, rendering, pushing, interacting between VJs and viewers, etc.
- VJs can capture their video and audio data and push them to the video cloud servers, so that the viewers can view them on other clients. VJs can customize features such as capture resolution, beauty filter, whitening and hardware encoding.
- VJs can create their own rooms. Viewers can join these rooms and interact with the VJs by ordinary comments, on-screen comments, and "Like" comments. These comments are shown to the VJs in corresponding comment lists and on-screen comments' locations. For more information about comments, please see "Message" module.
- The viewer lists can be displayed on VJ ends. When viewers join or leave a room, the list is refreshed, and the VJ is notified.

### Push Timing Diagram
![](//mc.qcloudimg.com/static/img/6fb00666a6a1cdea732fbddccc5fc786/image.png)

#### UI Hierarchy
![](//mc.qcloudimg.com/static/img/df03a372dfdb1fe5ca8a8675dc9e7dcb/image.png)

#### Related Code
- Logic:
	- TCPusherMgr: The logic layer code of push module, performing protocol communication with the service server.
- UI:
	- TCPushController: The main controller of push module, which accommodates the rendering view, logic view and push related logic; meanwhile, it also receives the event notification of SDK layer.
	- TCPushDecorateView: The logic view of push module, which presents the message list, bullet screen animation, viewer list, beauty, whitening and other UIs, wherein the logic interaction with the SDK needs to be processed by the main controller.

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
	- TCPlayerMgr: The logic layer code of play module, performing protocol communication with the service server.
- UI:
	- TCPlayController: The main controller of play module, which accommodates the rendering view, logic view and play related logic; meanwhile, it also receives the event notification of SDK layer.
	- TCPlayDecorateView: The logic view of play module, which presents the message list, bullet screen animation, viewer list, and other UIs, wherein the logic interaction with the SDK needs to be processed by the main controller.

### Message
#### Module Introduction
- Mini LVB's interactive message feature is mainly based on the group chat feature of [ImSDK](https://cloud.tencent.com/doc/product/269/1569). It's available when IMSDK is logged-in.
- Every live room is a large LVB group, which needs to be created before actually pushing occurs on the push end and disbanded after the pushing ends. Player ends join the group when they join the live room, and exit the group when they exit the room.
- To listen for desired messages, implement a messaging listener class. Currently supported message types include text message, "Like" message, user joining/leaving message and group disband message.
- All messages are sent as text messages in a uniform JSON format. The JSON carries information about message type, sender ID, nickname, profile photo and message text. The receivers receive and parse the JSON, and accordingly use the callbacks to pass all kinds of messages to the upper levels.
- To listen for a message, implement the corresponding delegate. Please note that to listen for group system messages, setup the delegates before login.

#### Related Code
- Class description:
	- Logic:
		- TCMsgHandler: Wrappers and callbacks of message related interfaces. It mainly implements wrappers for ImSDK related interfaces to send and receive ordinary text, on-screen and "Like" messages.
	
	- UI:
		- TCMsgBulletView: On-screen emoji. It displays users' on-screen comments and supports customization of animation effects. 
		- TCMsgListTableView: Message list. It displays users' ordinary messages and messages for users' entering/leaving the room.
		- TCMsgListCell: The Cell of TCMsgListTableView message list. It displays a message.
		- TCAudienceListTableView Shows the animation of viewer lists.
		- TCMsgModel: Message data model.
	
- Description on animation:
   - TCMsgBulletView: On-screen emoji. An instance of TCMsgBulletView is the container of one line of on-screen emoji. You can create n instances to show n lines of animations. During initialization, every container instance creates a view to hold on-screen comments. When an on-screen comment message is received, the view automatically resizes based on the message, then starts the animation. When the animation ends, the view is placed into the unUsedAnimateViewArray container. In the event that a new on-screen comment message is received, if there are unused views in unUsedAnimateViewArray, a view is selected to show the new animation; otherwise, a new view is initialized for the animation. Similarly, the new view is placed into the unUsedAnimateViewArray container when the animation is over. Moreover, TCMsgBulletView has a public property lastAnimateView that records the position for the last view created by each container of one line of on-screen emoji. When a new on-screen comment message is received, the lastAnimateView thus can be used to determine which container should be used to display it.
   
   - TCMsgListTableView: Message lists' animation. When a new message is received, the class would check if the list needs to be scrolled. In the computation two heights are recorded: the total height of all cells (totalCellHeight), and the height of TCMsgListTableView (listTableViewHeight). If totalCellHeight >= listTableViewHeight, it scrolls the list. In addition, when the user is dragging a message list, the scroll is paused. When the user stop dragging and listTableViewOffset >= totalCellHeight, the list starts scrolling again. Of course, there are a few tweaks. Please see the code of Mini LVB.

   - TCAudienceListTableView: The animation of viewer lists. The number of viewers varies and viewers enter and leave the room frequently. Therefore to avoid frequent memory allocation and deallocation, the class uses the tableView control instead of scrollView + imageView to reuse memory. By rotating tableView by 90 degrees, the class implements the desired horizontal list. Please note that the frame of tableView needs to be specially configured. Please see the code of Mini LVB.
   - Because the project was written in a limited time, the animations above may not have optimal performance and effects. They are provided only as a reference. Users can customize these animations basing on their needs.

### Personal Information
#### Module Introduction
- Personal information module is mainly responsible for displaying, storing, modifying and synchronizing user information to the server.
- User information includes profile photo, nickname, gender, LVB cover and location, etc. Personal information module is provided by IMSDK. For developers to customize users' information, IMSDK supports custom field extension.
- The module synchronizes users' latest personal information to the App. Users can browse their information through this module, including profile photo, nickname and gender.
- With this module, users can also modify their information, which would be synchronized to the servers.
- Other modules can also get and modify users' information through this module.
	
#### Related Code
- Logic:
	   - TCUserInfoMgr: User information management class. It's responsible for storing, modifying, and synchronizing user information.	   
- UI:
	   - TCEditUserInfoController: Implements the page to modify user information such as profile photo, nickname and gender.
	   - TCUserInfoController: Implements the interface to display user information such as profile photo, nickname and user ID.
	   - TCUserInfoTableViewCell: Used to draw the TableView that displays users' personal information.
	   - TCEditUserInfoTableViewCell: Used to draw the TableView for editing users' personal information directly.
	   - TCUserInfoTableViewCell: Used to draw the cell in the corresponding TableView to display a combination of controls such as image and text.

### Joint Broadcasting
#### Module Introduction
- Combining the joint broadcasting feature of the SDK and IM's C2C message interface, Mini LVB implements joint broadcasting.
- C2C messages are mainly used in notifications of VJs and replies to joint broadcasting viewer. VJs are notified about joint broadcasting requests, make replies and are notified about connection success.
- After VJs start LVB, viewers could request joint broadcasting. If the VJs agree, the viewers and the VJs would start pulling video data from each other's addresses. The push data from the VJs and the viewers are mixed at backend, and other viewers see the mixed video.

#### Timing Diagram
![](//mc.qcloudimg.com/static/img/1b80501829fd5528bf41d4c9a84aed2b/image.png)

#### Related Code
- Logic:
	- TCLinkMicMgr: Wrappers of C2C messages. It provides notification and reply interfaces for the upper levels.
- UI:
	- TCLinkMicPushController: Implements the interface of joint broadcasting's VJ ends. It inherits from TCPushController, and implements response to request for joint broadcasting and pulling viewers' video data.
	- TCLinkMicPlayController: Implements the interface of joint broadcasting's viewer ends. It inherits from TCPushController, and implements request for joint broadcasting, pushing and pulling VJs' video data.

  

