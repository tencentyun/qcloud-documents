## iLiveSDK Version Update
#### iLiveSDK Android V1.8.5 (4/04/2018)
 - Updated AVSDK to 1.9.8.2
 - Optimized event reporting and log reporting

[More versions](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo/blob/master/doc/ILiveSDK/release%20note.md)

#### iLiveSDK iOS 1.8.4.13473 (4/04/2018)
* Fixed the crash caused by log reporting
* Updated AVSDK to 1.9.8
* Separated log reporting modules to create the independent ILiveLogReport.Framework
* Adjusted internal log reporting mechanism in ILiveSDK
* Fixed the crash issue with logging

[More versions](https://github.com/zhaoyang21cn/iLiveSDK_iOS_Suixinbo/blob/master/doc/ILiveSDK_ChangeList.md)

#### iLiveSDK PC V1.8.2.0 (4/08/2018)
* Updated AVSDK to 1.9.8.2
* Supported 720p video playback
* Supported specifying the type of IM group used to create a room
* Added the default spear configuration parameter to the login API
* Removed SkinBeauty.dll which was often killed by 360

[More versions](https://github.com/zhaoyang21cn/iLiveSDK_PC_Suixinbo/blob/master/doc/iLiveSDK_ChangeList.md)

#### iLiveSDK IE V1.5.0.1 (2/09/2018)
* Return the error code ERR_NOT_FOUND (8022) if an empty device list is obtained
* SDK internal optimization

[More versions](https://github.com/zhaoyang21cn/iLiveSDK_Web_Suixinbo/blob/master/doc/iLiveSDK_ChangeList.md)

#### iLiveSDK mac V1.8.4.13473 (4/12/2018)
* 1. Updated AVSDK to 1.9.8
* 2. Separated log reporting modules to create the independent ILiveLogReport.Framework
* 3. Adjusted internal log reporting mechanism in ILiveSDK

[More versions](https://github.com/zhaoyang21cn/iLiveSDK_Mac_Suixinbo/blob/master/doc/iLiveSDK_ChangeList.md)

## AVSDK Version Update
#### AVSDK 1.9.8 (3/25/2018)

* Supported transcoding at backend in ILVB for VJs and viewers to freely choose H264, H265 and other resolutions
* Supported video H265 soft/hard encoding/decoding
* Increased video resolution to support panoramic LVB
* Supported the resolution of 720p or above for video playback
* Optimized speedy mode to allow more people to join a room
* Local music can be collected when high-quality playback is enabled at the VJ side on PC
* Optimized audio pre-processing for PC
* Supported controlling parameters for speedy​mode on​the cloud in a more flexible manner
* Supported setting the shader matrix of OpenGL externally for Android
* Supported low resolution 192*144

#### AVSDK 1.9.5 (9/15/2017)
* Added speedy mode, supporting one-to-one and one-to-many audio/video chat to cover real-time audio/video chat scenario.
* Supported howling suppressing on iOS/Android
* Supported test on capturing data from microphone before a chat on iOS/Android
* Supported high-performance video rendering, to effectively reduce system consumption, improve rendering, and minimize access cost.
* Privatized xplatform to avoid conflict with other xplatform versions used in Apps or other SDKs
* Enabled high-quality sound capture and playback on MAC when a wired headphone is detected to improve the audio experience

#### AVSDK 1.9.2 (7/24/2017)
* Supported video encoding/decoding hardware acceleration (PC)
* Supported screen sharing (MAC)
* Optimized audio and video quality for real-time chat scenarios and game scenarios (PC/Android/iOS)
* Reduced the loading time of first frame after joining a room (PC/Android/iOS)
* Added quick room switch during chat (PC/Android/iOS)
* Optimized the memory consumed in LVB video viewing and repeated joint broadcasting (PC/Android/iOS)
* Further improved quality monitoring and reporting capability (PC/Android/iOS)
* Systematically solved the security issue with native multithreading (PC/Android/iOS)

#### AVSDK 1.9.1 (5/27/2017)
* Supported local recording of MP4 videos (PC)
* Supported preview mode before joining a room (Android/iOS)
* Optimized the performance of filter and pendant (Android/iOS)
* Simplified voice changing API (Android/iOS)
* Optimized high-quality AEC (Android)


#### AVSDK 1.9.0 (3/21/2017)
* Enabled cross-room joint broadcasting to realize interaction between VJs
* Added an interesting chat mode with filter + pendant built in SDK to facilitate integration
* Supported on MAC platform
* Supported 3D sound effect on PC

#### AVSDK 1.8.5 (1/18/2017)
* Optimized loading time when joining a room in LVB scenarios
* Added VJ voice changing (Android/iOS)
* In addition to IMSDK channel, a new set of channels have been implemented in AVSDK. Users can use HTTP channel and HTTPS channel implemented within AVSDK in Andriod and iOS, respectively (Android/iOS).
* Supported automatic request for screen sharing
* Supported dynamic change of areas on the screen to which content is shared (Windows)

## FAQs Update (1/18/2017)

* [Adapt to more rotating and cropping scenarios](https://cloud.tencent.com/document/product/268/7647)
* [Support background music in LVB](https://cloud.tencent.com/document/product/268/8297)

## FreeShow Backend 2.0.0 (1/18/2017)

* FreeShow backend in standalone account mode has been released, which should be used along with iLive SDK 1.2.0.
* [QuickStart Document](https://cloud.tencent.com/document/product/268/7603)
* Adopted standalone mode for account integration
* Supported querying recording files
* Support non-interactive push and recording callback
* Refined the interaction protocol with FreeShow, which can be used as a reference for business process design

## Release of Screenshot and Porn Detection (1/05/2017)

As we know, screenshot and porn detection are a must in LVB industry.
Tencent Video Cloud provides powerful screenshot and porn detection features. For more information, please see [Screenshot and Porn Detection](https://cloud.tencent.com/document/product/268/8109).

## AV_iOS_SDK Version Update
#### AV_iOS_SDK 1.8.4 (12/28/2016)
* Optimized loading time when joining a room in LVB scenarios
* Added high-quality joint broadcasting feature (Android)
* Switched from HTTP channel to HTTPS (iOS)
* Optimized traffic control policy to speed up the display of frames for screen sharing, thus improving user experience
* Added the API for controlling playback of specified user audio streams
* Supported capturing external audio data (Android/iOS)
* Added the option of local rendering to external video input stream capture API (Android/iOS)
* Added client IP to the API for obtaining quality parameters

#### AV_iOS_SDK 1.8.2 (8/12/2016)
* Added video watermark feature
* Supported reporting via SDK node
* Refactored audio/video packet receiving/sending module
* Supported switching audio scenarios in a room
* Added timeout callback for joining a room
* Supported notification for changes in camera capturing settings in a room
* Application for video bits can be automatically submitted to prevent invalid videos caused by missing video bits
* Added notification for setting camera capturing parameters
* Adjusted some APIs

#### AV_iOS_SDK 1.8.1.1 (6/21/2016)
* Fixed some crash issues
* Fixed black screen caused by switching back from background to room

#### AV_iOS_SDK 1.8.1 (6/6/2016)
** 1. New SDK Features**

* Video hardware encoding
* Supported the aspect ratio of 16:9 when capturing videos
* Added support for beauty filter API
* Optimized loading time when joining a room
* Video quality was optimized, resolution/frame rate was synched with Web configurations, and video (soft) encoding output was improved to 720P
* Optimized audio quality and supported 64 Kbps bitrate
* Added high-quality chat API for "Broadcast" mode in VJ scenarios
* Optimized listening API and lowered latency
* Added the API for directly receiving existing screen videos instead of making additional requests when joining a room
* Added the API for switching roles without joining room again
* Added the API for customizing sound effects in real time and supported custom sampling rates
* Added sound engine terminal and recovery feature
* Added the API for externally querying whether beauty filter is supported
* Added the API for local video image pre-processing callback
* Added the API for notification of an exception caused by a room member who uses a chatting capacity without relevant permission
* Added the API for obtaining version number
* Added the API for obtaining timestamp

**2. SDK Bug Fixes**

* Optimized the effect of encoding video software under VJ mode
* Fixed issues of blurred screen, green screen, reversed playback in videos
* Fixed occasional inconsistency between display and sound
* Fixed the issue regarding video images being compressed/stretched on certain models
* Fixed the issue that audio is stopped briefly when video is closed
* Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios
* Fixed the issue that some viewers cannot hear any sound in VJ scenarios
* Fixed the issue regarding audio accompaniment memory not being released
* Fixed several Crash issues
* Supported switching from hardware encoding to software encoding when VJ answers a call
* Fixed the crash that occasionally occurs when exiting a room
* Added protection for calling stopcontext in a room
* Fixed the crash caused by continuing sending packets after exiting a room
* Fixed the possible memory leak when receiving packets
* Fixed the issue that screen sharing and camera video primary screen can be sent simultaneously
* Fixed the issue that a user cannot request video image with downstream permission only
* Fixed the issue that the remote end of the camera cannot see the video status after a user is given upstream permission
* Fixed the possible crash caused by the network interruption when beauty filter is enabled
* Fixed the issue that room members cannot hear any sound from microphones on iOS 7.1.2
* Fixed the issue that beauty filter cannot be enabled on iPod Touch 6
* Fixed the issue that SDK process has to be manually terminated when requesting another viewer's video on iOS
* Fixed the issue regarding reboot after a BSOD

#### AV_iOS_SDK1.7 (3/17/2016)

** 1. New SDK Features**

* Added beauty filter API
* Split IMSDK to reduce installation package size
* Added the API for obtaining room status parameters
* Added the API for modifying permissions in plaintext

**2. SDK Bug Fixes**

* Fixed blue screen caused by hardware encoding at backend
* Fixed potential crashes caused by network status change
* Fixed the issue that it sometimes takes long to load videos in case of a request for screen sharing

#### AV_iOS_SDK 1.6 (1/11/2016)

** 1. New SDK Features**

* Added screen sharing feature to allow receiving videos on screen shared by PC
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
* Added terminal network type reporting
* Improved the content, display format and style of tips about call quality

**2. SDK Bug Fixes**

* Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
* Fixed the crash occurs when enabling camera after executing the logic for external capturing


## AV_Android_SDK Version Update
#### AV_Android_SDK 1.8.2 (8/12/2016)
* Added video watermark feature
* Supported reporting via SDK node
* Refactored audio/video packet receiving/sending module
* Supported switching audio scenarios in a room
* Added timeout callback for joining a room
* Supported notification for changes in camera capturing settings in a room
* Application for video bits can be automatically submitted to prevent invalid videos caused by missing video bits
* Added notification for setting camera capturing parameters
* Adjusted some APIs

#### AV_Android_SDK 1.8.1.1 (6/21/2016)
* Added main thread protection for "create context"
* Fixed black screen caused by the asynchronization between traffic control parameter and encoder status 
* Fixed the crash caused by modifying "change role"
* Fixed the issue that user cannot join a room after switching the account due to mismatch between "create" and "destroy"
* Fixed the possible memory leak when receiving packets
* Fixed black screen caused by switching back from background to room

#### AV_Android_SDK 1.8.1 (6/6/2016)
** 1. New SDK Features**

* Video hardware encoding
* Supported the aspect ratio of 16:9 when capturing videos
* Added support for beauty filter API
* Optimized loading time when joining a room
* Video quality was optimized, resolution/frame rate was synched with Web configurations, and video (soft) encoding output was improved to 720P
* Optimized audio quality and supported 64 Kbps bitrate
* Added the API for directly receiving existing screen videos instead of making additional requests when joining a room
* Added the API for switching roles without joining room again
* Added the API for customizing sound effects in real time and supported custom sampling rates
* Added sound engine terminal and recovery feature
* Added the API for externally querying whether beauty filter is supported
* Added the API for obtaining version number
* Added the API for obtaining timestamp

**2. SDK Bug Fixes**

* Optimized the effect of encoding video software under VJ mode
* Fixed issues of blurred screen, green screen, reversed playback in videos
* Fixed occasional inconsistency between display and sound
* Fixed the issue regarding video images being compressed/stretched on certain models
* Fixed the issue that audio is stopped briefly when video is closed
* Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios
* Fixed several Crash issues
* Fixed the issue that screen sharing and camera video primary screen can be sent simultaneously
* Fixed the issue that a user cannot request video image with downstream permission only
* Fixed the issue that the remote end of the camera cannot see the video status after a user is given upstream permission
* Fixed the crash occasionally occurs when calling getqualityparas API
* Fixed the issue that too much logs are printed after enabling hardware encoding
* Fixed blurred screen on LG NEXUS6 Android 6.0 when switching camera
* Fixed frequent video memory GC in VJ mode on Android


#### AV_Android_SDK 1.7 (3/17/2016)

** 1. New SDK Features**

* Added beauty filter API
* Added the API for pre-processing local video capturing
* Added the API for obtaining room status parameters
* Added the API for modifying permissions in plaintext
* Added the API for exposing system camera object to allow App to control the flash light on the device

**2. SDK Bug Fixes**

* Fixed the crash caused by calling DestroyContext after calling StopContext
* Fixed the issue that App becomes unresponsive when enabling front camera and flash light after joining a room
* Fixed the crash caused by requestviewlist

#### AV_Android_SDK 1.6 (1/11/2016)

** 1. New SDK Features**

* Added screen sharing feature to allow receiving videos on screen shared by PC
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
* Added terminal network type reporting
* Improved the content, display format and style of tips about call quality
* Reduced the SDK size by approximately 80 KB

**2. SDK Bug Fixes**

* Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
* Changed to synchronized volume adjustment to fix the problem that quick volume adjustment may not take effect
* Fixed the crash occurs when enabling camera after executing the logic for external capturing
* Fixed the crash that occasionally occurs when repeating the "Join Room - Enable Camera - Exit Room" procedure



## AV_WIN_SDK 1.8.1.1 (6/21/2016)
* Fixed the issue that packet receiving logic may potentially cause a significant memory leak
* Fixed the crash that occurs when the following conditions are all true after joining a room
* Fixed the issue that the shared screen may not be rendered after the operations "Join room - Start screen sharing - Exit room - Join room again - Request screen sharing from other viewers" are performed


## AV_Windows_SDK1.8.1 (6/6/2016)
** 1. New SDK Features**

* Supported the aspect ratio of 16:9 when capturing videos
* Optimized loading time when joining a room
* Video quality was optimized, resolution/frame rate was synched with Web configurations, and video (soft) encoding output was improved to 720P
* Optimized audio quality and supported 64 Kbps bitrate
* Added high-quality chat API for "Broadcast" mode in VJ scenarios
* Added low-latency listening API
* Added the API for directly receiving existing screen videos instead of making additional requests when joining a room
* Added the API for switching roles without joining room again
* Added the API for customizing sound effects in real time and supported custom sampling rates
* Added the API for obtaining version number

**2. SDK Bug Fixes**

* Fixed the issue that screen sharing and camera video primary screen can be sent simultaneously
* Fixed the issue that a user cannot request video image with downstream permission only
* Fixed the issue that the remote end of the camera cannot see the video status after a user is given upstream permission
* Fixed the 1301 error caused by enabling screen sharing after hot-plugging the microphone

## AV_Windows C++SDK1.7 (3/17/2016)

**1. New SDK Features**

* Added support for joining a room by accepting an invitation
* Added the API for obtaining room status parameters
* Added the API for modifying permissions in plaintext

**2. SDK Bug Fixes**

* Fixed the issue that no sound can be heard on a hot-plugging USB speaker when the default speaker of the system is disabled

## AV_Windows C++_SDK1.6 (1/11/2016)

**1. New SDK Features**

* Added screen sharing feature to allow sending and receiving videos on screen
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
* Improved the content, display format and style of tips about call quality
* Reduced the SDK size by approximately 200 KB

**2. SDK Bug Fixes**

* Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
* Changed to synchronized volume adjustment to fix the problem that quick volume adjustment may not take effect
* Fixed the crash occurs when enabling camera after executing the logic for external capturing

