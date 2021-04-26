## 1.Project Structure
![](https://main.qcloudimg.com/raw/f5f676f1fbbd87cc86fab4682e63de39.png)

| Project Directory | Description | 
|---------|---------|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/Login | Mini Video login module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/List| Mini Video VOD list module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/Play | Mini Video VOD playback module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCRecord | Mini Video recording module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCEditor | Mini Video editing module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCPublish | Mini Video publishing module |
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UserInfo | Mini Video user information module |

## 2. Overview of Modules
Mini Video consists of 7 modules: account, list management, playback, recording, editing, publishing, and user information. Each module comes with its own code. The following describes these modules and how to implement them.

### Account module
#### Module description
- Account module handles the logics of user login/registration and login caching.
- Login and registration are implemented by login via [TLS SDK Hosting](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F).
- You can directly replace this module with your own account system (if any), and use IM channel as a guest by calling API guestLogin of TCIMPlatform. For more information, please see [Replace Account](https://cloud.tencent.com/doc/api/258/6441).
- If the TLS SDK login authentication is successful, you can log in to the IM module by calling API login of ImSDK using UserId and UserSig returned in the authentication.
- Registration and login can be performed using either account and password or mobile verification code.
- Account module caches the basic information (UserId and UserSig) of the last logged-in user locally, and obtains the information by calling API to determine if re-login is required.
- Login is mutually exclusive. The user that logged in first will be forcibly logged out by receiving a notification.

#### Code
- Logic:
	- TCLoginParam: Used to manage user's login information, for example, caching login information and determining its expiration.
	- TCTLSPlatform: Wrappers of APIs for TLS registration and login
	- TCIMPlatform: Wrappers of APIs for ImSDK login

- UI:
	- TCLoginViewController: Transition page that reads login data from the cache. If auto login is allowed, imlogin API is called for login to IM. Otherwise, login page is pulled.
	- TCTLSLoginViewController: TLS login page, including login by user name, login by SMS message and login as guest.
	- TCTLSRegisterViewController: TLS registration page, including registration by user name and by SMS message.

### Main page & list management
#### Module description
- Main page is used to switch between three primary features: VOD list, video recording and user information.
- When user enters the App, list page is displayed by default. After clicking **Record** button, users who have not logged in are redirected to login page, and logged-in users are redirected to push page. Click **User Information** button to go to user information page.
- List management includes pulling and displaying lists.

#### Code
- Logic:
	- TCLiveListModel: Used to define VOD list at data layer and implement serialization/deserialization.
	- TCLiveListMgr: Logic layer code for list management, used to pull, cache and update list data. Only full pull is supported. Incremental pull is not supported. Pulling protocol is designed to pull list data in pages. After the API for pulling list is called, the list data is pulled continuously from backend at logic layer until all the data is pulled. To enhance user experience, the display is refreshed immediately after data in the first page is pulled.
	
- UI:
	- TCNavigationController: Controller for the navigation bar, used to customize background color of the navigation bar.
	- TCMainTabViewController: Controller for the tab bar of main page, used to switch between list, recording and user information pages.
	- TCLiveListCell: Cell class of VOD list, used to display cover, title and alias.
	- TCLiveListViewController: TableViewController for VOD list, used to display VOD list. Users will be redirected to playback page after clicking a video in the VOD list.


### Playback module
#### Module description
- Playback module contains features such as pre-loading, playback, caching and sharing of short videos.

#### Code
- Logic:
	+ TCPlayerMgr: Logic layer code of playback module, used for communication with business server using protocol.
- UI:
	- TCPlayController: Main controller of playback module, which contains rendering view, logic view and playback logic, and receives event notifications from SDK layer.
	- TCPlayDecorateView: Logic view of playback module, which displays VJ information and logic control for playback, with the logic interaction with SDK handled by the main controller.
	- TCPlayViewCell: Cell used to switch between VOD videos by swiping up/down. Users can swipe up/down to switch between VJs during playback.


### Recording module
#### Module description
- Recording module contains features such as multi-part short video recording/deletion, multi-resolution recording and recording speed control.

#### Code
- Logic:
	- PituMotionAddress: Stores the download path of dynamic effects.
- UI:
	- TCVideoRecordViewController: Main controller of recording module, which contains rendering view, logic view and recording logic, and receives event notifications from SDK layer.
	- TCVideoRecordProcessView: Recording progress view, used to display and delete videos during recording.
	- BeautySettingPanel: view for setting dynamic effects in recording. It allows you to configure beauty filter, whitening and other effects for recording, which are then called back to the main recording controller.

### Editing module
#### Module description
- Editing module contains features such as short video clipping, BGM, filter style, special effects and dynamic/static stickers.

#### Code
- Logic:
	- VideoInfo: Stores information about dynamic/static stickers, ordinary subtitles and bubble subtitles.
- UI:
	- TCVideoCutViewController : Main controller for video clipping, which contains rendering view, logic view and clipping logic.
	- TCVideoEditViewController: Main controller for video editing, which contains rendering view, logic view and editing logic.
	- TCVideoLoadingController: Main controller for loading videos locally, which contains logic of loading videos locally. The loaded videos are sent to the main clipping controller.
	- VideoPreview: Rendering view for video editing, used to preview videos during editing.
	- BottomTabBar: Switching view for video editing, used to switch between features such as BGM, filter styles, special effects, dynamic/static stickers.
	- VideoCutView: Video thumbnail view, used for playback progress selection, video clipping, etc.
	- EffectSelectView: view for selecting special effects.
	- PasterAddView: view for adding dynamic/static stickers.
	- TextAddView: view for adding ordinary/bubble subtitles.

### Publishing module
#### Module description
- Publishing module mainly involves publishing short videos.

#### Code
- UI:
	- TCVideoPublishController: Main controller for video publishing, which contains publishing logic.

### User information module
#### Module description
- User information module is used to display, store, modify and synchronize user information to server.
- User information includes profile photo, alias, gender, LVB cover, and location, etc. User information module is provided by IMSDK, which supports expanding custom fields to allow developers to customize more user information.
- This module synchronizes users' latest information to App, and users can browse their information through this module, including profile photo, alias and gender.
- Users can modify and synchronize their information to the server through this module.
- Other modules can also obtain and modify the user information through this module.
	
#### Code
- Logic:
	   - TCUserInfoMgr: User information management class, used to store, modify, and synchronize user information to server or query user information from server.	   
- UI:
	   - TCEditUserInfoController: Page for modifying user information such as profile photo, alias and gender.
	   - TCUserInfoController: Page for displaying user information such as profile photo, alias and user ID.
	   - TCUserInfoTableViewCell: tableview for drawing the page for displaying user information.
	   - TCEditUserInfoTableViewCell: tableview for drawing the page for editing user information. User information can be edited directly in this tableview.
	   - TCUserInfoTableViewCell      用于绘制负责的tableview中的cell如图片，文字等组合控件


  

