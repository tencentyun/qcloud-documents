## Project Structure

Download Mini Video source code and open the project with Android Studio. The directory structure is displayed as follows:

![](https://main.qcloudimg.com/raw/a9fe91e85884f06627ababcfca796f5c.png)

| File/Directory | Description |
| ------------ | ------------------------------------------------------------ |
| common | Common components, including various tools and custom pages (beauty filter and player control) |
| login | Account module, including login and registration |
| mainui | Mini Video main page, including main Activity and video list |
| play | VOD playback module |
| userinfo | User information module |
| videochoose | Short video file selection module |
| videoeditor | Short video editing module |
| videojoiner | Short video stitching module |
| videopublish | Short video publishing module |
| videorecord | Short video recording module |
| jniLibs | Tencent SDK that Mini Video is dependent on, including BuglySDK, the library for file upload, and LiteAVSDK |

## Dynamic Stickers

In the Mini Video source code, the basic version, instead of the commercial version, of UGSV SDK is used by default. Therefore, features such as dynamic stickers are not included. To use this feature, go to [DOWNLOAD](https://cloud.tencent.com/document/product/584/9366) to obtain the commercial version.

## Overview of Modules

Mini Video consists of account, main page, playback, and short video (editing, stitching, recording, and publishing) modules, and each module comes with its own code. The following describes these modules and how to implement them.

### Account module

#### Module description

- Account module handles the logics of user login/registration and login caching.
- You can directly replace this module with your own account system (if any).
- Account module registers user name and password to Mini Video backend by calling TCUserMgr's register method, calls TCUserMgr's login method for login, caches the login information in the local Sharepreference, and then logs out and clears up the local cache.

#### Code

| Class Name | Description |
| ----------------------- | ------------------------------------------------------------ |
| TCApplication.java | SDK initialization class |
| TCLoginActivity.java | User login page |
| TCRegisterActivity.java | User registration page |
| TCUserMgr | User login/registration management class |
| OnProcessFragment | Fragment showing progress bar |
| TCUserInfoFragment.java | User information page |
| TCAboutActivity | "About this video" page |

### Main page & list management

#### Module description

- Main page is used to switch between three primary features: short video list, video recording/editing and personal information.
- After you log in, video list page displays by default. When you click **+**, a dialog box pops up for you to select short video recording or editing. After clicking **Personal Information**, you will be redirected to personal information page.
- List management includes pulling and displaying lists.

#### Code

| Class Name | Description |
| -------------------------- | -------------------------------------------------------- |
| TCSplashActivity.java | Splash screen |
| TCMainActivity.java | Main page where short video list, video recording/editing and user information page are provided |
| TCLiveListMgr.java | List management class that provides API to obtain local memory list and update list from server |
| TCLiveListFragment.java | List page used to display short video data |
| TCLiveListAdapter.java | Short video list adapter |
| TCUGCVideoListAdapter.java | Short video list adapter |
| TCVideoInfo | Video data |

### Short video recording module

#### Module description

- Mini Video supports recording [short videos](https://cloud.tencent.com/document/product/584/9453) not longer than 1 minute. But SDK itself does not show the recording length.

#### Code

| Class Name | Description |
| -------------------------- | -------------------- |
| TCVideoRecordActivity.java | Short video recording page |
| RecordProgressView | View for recording short videos by pressing and holding the key |
| ComposeRecordBtn | Progress bar for multi-part video recording |


### File selection module

#### Module description

- This module is used to select files locally and lists all mp4 files in mobile phone.

#### Code

| Class Name | Description |
| ----------------------------- | ---------------------------------------------------- |
| TCVideoChooseActivity.java | Page for selecting local mp4 files |
| TCVideoEditerListAdapter.java | Adapter for local mp4 file list |
| TCVideoEditerMgr.java | mp4 file management class that provides API to obtain mp4 files stored in phone |
| TCVideoFileInfo.java | Local video data |

### Editing module

#### Module description

- [Video editing](https://cloud.tencent.com/document/product/584/9502) involves video clipping, slow motion, filter, music mixing, stickers and subtitling.

#### Code

- videoeditor/directory

| Class Name | Description |
| ------------------------------ | ------------------------------------------------------------ |
| TCVideoPreprocessActivity.java | Page for preprocessing the videos to be edited |
| TCVideoCutterActivity.java | Page for clipping short videos |
| TCVideoEditerActivity.java | Page for editing clipped short videos, where music, filter, speed control, tone selection, stickers, subtitles and other features are provided at the bottom |
| TCVideoEffectActivity.java | Page for adding special effects. Clicking the button at the bottom can lead you to this page. |
| BaseEditFragment.java | The parent class of the effect Fragment to control the playback status of effects on multiple pages |
| TCVideoJoinerActivity.java | Used to merge multiple video files to be edited into one page |

- videoeditor/cutter/directory
  Related to video clipping

- videoeditor/time/directory
  Related to time effects, including slow motion, replay and playback in reverse.

- videoeditor/bgm/directory
  Related to background music

- videoeditor/paster/directory
  Related to stickers, including dynamic and static stickers.

- videoeditor/motion/directory
  Related to dynamic filter: including four types of dynamic filters [custom expansion is not supported. If you need more filter effects, please contact us.]

- videoditor/bubble/directory
  Related to bubble subtitles

- videoeditor/utils/directory
  Related to short video editing tools

- videoeditor/common/directory
  Common component for short video editing

- videojoiner/directory
  Related to short video stitching

### Short video publishing module

#### Module description

- You can publish recorded files to Tencent Cloud Video Distribution Platform (VOD system) via this module.

#### Code

| Class Name | Description |
| ----------------------------- | -------------- |
| TCVideoPublisherActivity.java | Page for publishing short videos |

### Short video playback module

#### Module description

- This module is used to play videos that have been published to VOD system. You can switch to the previous/next video by swiping up/down on the short video list page.

#### Code

| Class Name | Description |
| ------------------------- | -------------- |
| TCVodPlayerActivity.java | Short video playback page |
