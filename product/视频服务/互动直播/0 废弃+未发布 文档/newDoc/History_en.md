## `iLive SDK PC 1.4.0    2017-07-07`

* Optimized APIs for easy connection.
* Added integration support for each version of VS;
* All APIs have callback in the main thread;
* With the SDK's automatic request, users no longer need to request screen display manually;
* Better effect with optimized beauty filter;


## `iLive SDK IE 1.0.0    2017-05-11`

* Added support for LVB and messaging with Android and iOS rooms.
* Beauty filter and whitening features
* Added support for recording and non-interactive push

## `AVSDK 1.8.5  2017-03-022`
**New Features of SDK**  
* 1. Optimized loading time when joining a room in LVB scenarios. 
* 2. Added VJ voice changer feature.
* 3. Beside IMSDK channel, AVSDK implemented a new channel internally. Android can use the HTTP channel implemented by AVSDK, and iOS can use HTTPS channel.
* 4. Automatically request shared video data from screen.

** SDK Bug Fixes
* Fixed residual bugs and improved SDK's stability.

## `iLive SDK 1.3  2017-03-06`
* Integrated AVSDK 1.8.5.44
* Optimized loading time when joining a room in LVB scenarios
* Automatically request shared video data from screen
* Dynamically change the shared region of screen (Windows)
* Supports non-interactive broadcasting and recording under LVB code mode
* Fixed status exception and bugs in quick room joining for Android
* Android can now configure whether to enable AVSDK room when joining a room
* Fixed a bug of duplicated logging on Android 7.0.
* Fixed black screen bug on OPPO R9S for Android
* Fixed deadlock issue on iOS
* Upgraded FreeShow's cover uploading feature
* Added WeChat sharing feature in FreeShow

## `Updates on Common Issues    2017-01-18`

* [Adapt to more rotating and cropping scenarios](https://cloud.tencent.com/document/product/268/7647)
* [Support background music in LVB](https://cloud.tencent.com/document/product/268/8297)

## `Suixinbo Backend 2.0.0    2017-01-18`

* FreeShow backend in standalone account mode has finally been released. It needs to be used along with iLive SDK 1.2.0.
* [QuickStart documentation](https://cloud.tencent.com/document/product/268/7603)
* Account integration uses standalone mode
* Added support for querying recording files
* Added callbacks for non-interactive push and recording
* Refined the interaction protocol with FreeShow which could be used as a reference for business process design

## `iLive SDK PC 1.0.0    2017-01-18`

* Integrated AVSDK version 1.8.4 and IMSDK version 2.5.0. Optimized loading time when joining a room and screen sharing speed
* Added support for LVB and messaging with Android and iOS rooms.
* Added support of screen sharing and camera switching
* iLive SDK 1.2.0 is needed when switching account integration mode to standalone mode.

## `iLive SDK Android ios 1.2.0    2017-01-18`

* Integrated AVSDK version 1.8.4 and IMSDK version 2.5.0. Optimized loading time when joining a room and screen sharing speed
* Added support for PC iLiveSDK's screen sharing LVB
* Optimized the handling of landscape screen rotation
* Added support for pulling non-interactive broadcasting lists
* Added support for pulling recording lists and local playback
* Added support for uploading covers to COS, "like" animation and message animation
* iLive SDK 1.2.0 is needed when switching account integration mode to standalone mode.

## `Release of Screenshot Porn Detection Feature 2017-01-05`

It's common knowledge that screenshot porn detection is a must in LVB industry.

Tencent Video Cloud provides powerful screenshot and porn detection features for our clients. For usage details, please see the [documentation](https://cloud.tencent.com/document/product/268/8109).

## `AV_iOS_SDK1.8.4    2016-12-28`
* Optimized loading time when joining a room in LVB scenarios
* Added high-quality joint broadcasting feature on Android
* Switched from HTTP channel to HTTPS (iOS)
* Optimized stream management strategy and screen sharing frame rate to improve user experience
* Added APIs to control playback of specified user audio streams
* Added support for capturing external audio data (Android/iOS)
* Added option of local rendering for external video input stream collection API (Android/iOS)
* Added client IP to API that obtains quality parameters

## `iLive SDK 1.0.0 2016-11-25`
* Wrapped the main operations of AVSDK and IMSDK in LVB scenario and therefore lowered accessing difficulty significantly.
* Extracted LVB business logic as the framework for easy reference and extension

## `AV_iOS_SDK1.8.2    2016-08-12`
* Added video watermark feature
* Added SDK node reporting feature
* Refactored audio/video packet's receiving/sending module
* Added support for switching audio scenarios in rooms
* Added room timeout callbacks
* Added notifications for changes in camera capture settings in rooms
* The SDK now automatically applies for video bits to prevent invalid videos caused by missing video bits
* Added notifications for setting camera capture parameters
* Adjusted some APIs

## `AV_Android_SDK1.8.2    2016-08-12`
* Added video watermark feature
* Added SDK node reporting feature
* Refactored audio/video packet's receiving/sending module
* Added support for switching audio scenarios in rooms
* Added room timeout callbacks
* Added notifications for changes in camera capture settings in rooms
* The SDK now automatically applies for video bits to prevent invalid videos caused by missing video bits
* Added notifications for setting camera capture parameters
* Adjusted some APIs

## `AV_iOS_SDK1.8.1.1    2016-06-21`
* Fixed some crash issues
* Fixed the blackscreen issue after switching back from background

## `AV_Android_SDK1.8.1.1    2016-06-21`
* Added main thread protection for "create context"
* Fixed the blackscreen issue caused by the desynchronization between stream control parameter and encoder status 
* Fixed the crash caused by modifying "change role"
* Fixed a bug that user cannot join rooms after switching the account due to the mismatched "create" and "destroy"
* Fixed potential memory leak when receiving packets
* Fixed the blackscreen issue after switching back from background

## `AV_WIN_SDK1.8.1.1    2016-06-21`
* Fixed the bug on receiving logic that could potentially cause a significant memory leakage
* Fixed the crash issue that happened if the following conditions were all true after joining a room
* Fixed a bug that after "Join room - Start screen sharing - Exit room - Join room again - Request screen sharing from other people" operations, the shared screen may not be rendered

## `AV_iOS_SDK1.8.1    2016-06-06`
**1. New SDK features**

* Video hardware encoding
* The aspect ratio of 16:9 is supported when capturing videos
* Added support for beauty filter APIs
* Room joining speed optimization
* Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P
* Audio quality optimization. 64kbps bitrate is now available
* Added high quality audio API for "Broadcast" mode in VJ scenarios
* Optimized listening APIs and lowered latency
* Added APIs that directly receive existing videos instead of making additional requests when joining a room
* Added APIs that switch roles without re-joining the room
* Added APIs that customize real-time sound effects and custom sample rates is supported
* Added sound engine terminal and recovery feature
* Added external APIs to query whether beauty filter is enabled
* Added APIs to set local video pre-process callbacks
* Added APIs to set notifications when a room member uses certain audio feature without having proper permissions
* Added APIs to obtain version number
* Added API to obtain time stamp

**2. SDK Bug Fixes**

* Encoding effects optimization for video softwares under VJ mode
* Issues regarding blurred screen, green screen, reversed playback in videos have been fixed
* Issues regarding occasional inconsistency between display and sound have been fixed
* Issues regarding video display being reduced/stretched on certain models have been fixed
* Fixed the issue that audio is stopped briefly when video is closed
* Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios
* Fixed a bug that some viewers can't hear any sound in VJ scenarios
*•Issues regarding audio accompaniment memory not being released have been fixed
* Several Crash issues have been fixed
* Now the SDK switches from hardware encoding to software encoding when the VJ is answering a call
* Fixed occasional crashes when exiting a room
* Added protection for calling stopcontext in a room
* Fixed the crash caused by continuing sending packets after exiting a room
* Fixed potential memory leak when receiving packets
* Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously
* Fixed a bug that a user couldn't request video image when he/she had only downlink permissions
* Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions
* Fixed the likely crash caused by network interruptions when beauty filter is enabled
* Fixed a bug that room members couldn't hear sound from microphones on iOS 7.1.2
* Fixed a bug that iPod touch 6 couldn't enable beauty filter
* Fixed a bug that the SDK process is manually terminated when requesting other people's videos on iOS
* Fixed the issue of occasional blue screen reboots

## `AV_Android_SDK1.8.1    2016-06-06`
**1. New SDK features**

* Video hardware encoding
* The aspect ratio of 16:9 is supported when capturing videos
* Added support for beauty filter APIs
* Room joining speed optimization
* Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P
* Audio quality optimization. 64kbps bitrate is now available
* Added APIs that directly receive existing videos instead of making additional requests when joining a room
* Added APIs that switch roles without re-joining the room
* Added APIs that customize real-time sound effects and custom sample rates is supported
* Added sound engine terminal and recovery feature
* Added external APIs to query whether beauty filter is enabled
* Added APIs to obtain version number
* Added API to obtain time stamp

**2. SDK Bug Fixes**

* Encoding effects optimization for video softwares under VJ mode
* Issues regarding blurred screen, green screen, reversed playback in videos have been fixed
* Issues regarding occasional inconsistency between display and sound have been fixed
* Issues regarding video display being reduced/stretched on certain models have been fixed
* Fixed the issue that audio is stopped briefly when video is closed
* Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios
* Several Crash issues have been fixed
* Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously
* Fixed a bug that a user couldn't request video image when he/she had only downlink permissions
* Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions
* Fixed occasional crashes when calling getqualityparas API
* Fixed the problem that too much logs are printed after enabling hardware encoding
* Fixed a bug that caused blurred camera screen on LG NEXUS6 Android 6.0
* Fixed frequent video memory GC in VJ mode on Android

## `AV_Windows_SDK1.8.1    2016-06-06`
**1. New SDK features**

* The aspect ratio of 16:9 is supported when capturing videos
* Room joining speed optimization
* Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P
* Audio quality optimization. 64kbps bitrate is now available
* Added high quality audio API for "Broadcast" mode in VJ scenarios
* Added low-latency listening API
* Added APIs that directly receive existing videos instead of making additional requests when joining a room
* Added APIs that switch roles without re-joining the room
* Added APIs that customize real-time sound effects and custom sample rates is supported
* Added APIs to obtain version number

**2. SDK Bug Fixes**

* Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously
* Fixed a bug that a user couldn't request video image when he/she had only downlink permissions
* Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions
* Fixed the 1301 error caused by enabling screen sharing after hot-plugging microphones

## `AV_iOS_SDK1.7    2016-3-17`

**1. New SDK features**

* Added beauty filter API
* Splitted IMSDK to reduce installation package size
* Added APIs to obtain room status parameters
* Added APIs for permissions to modify plaintext

**2. SDK Bug Fixes**

* Fixed a blue screen bug caused by enabling backend hardware encoding
* Fixed potential crashes caused by changing network status
* Fixed a problem that the video may take long to load after requesting screen sharing

## `AV_Android_SDK1.7   2016-3-17`

**1. New SDK features**

* Added beauty filter APIs
* Added APIs to pre-process local video capture
* Added APIs to obtain room status parameters
* Added APIs for permissions to modify plaintext
* Added APIs to expose system camera object, so that the App can control the flash lights on the device

**2. SDK Bug Fixes**

* Fixed the crash caused by calling DestroyContext after calling StopContext.
* Fixed a bug that the App becomes unresponsive when enabling both front camera and flash light after joining a room.
* Fixed the crash caused by requestviewlist.

## `AV_Windows C++SDK1.7   2016-3-17`

**1. New SDK features**

* Added support for joining a room by accepting an invitation
* Added APIs to obtain room status parameters
* Added APIs for permissions to modify plaintext

**2. SDK Bug Fixes**

* Fixed a bug that no sound was played on a hot-plugging USB speaker when the default speaker of the system was disabled.



## `AV_iOS_SDK1.6    2016-1-11`

**1. New SDK features**

* Added screen sharing feature. The SDK can now receive screen video shared by PC.
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
* Added terminal network type reporting feature.
* Improved the content, display format and style of tips about call quality.

**2. SDK Bug Fixes**

* Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure.
* Fixed the crash caused by enabling cameras after executing related logics of external capture.

## `AV_Android_SDK1.6    2016-1-11`

**1. New SDK features**

* Added screen sharing feature. The SDK can now receive screen video shared by PC.
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
* Added client network type reporting feature.
* Improved the content, display format and style of tips about call quality.
* Reduced the SDK size by approximately 80KB.

**2. SDK Bug Fixes**

* Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure.
* Synchronized volume adjustment to fix the bug that quick volume adjustment may have no effect.
* Fixed the crash caused by enabling cameras after executing related logics of external capture.
* Fixed the occasional crashes when repeating the "Join Room - Enable Camera - Exit Room" procedure.

## `AV_Windows C++_SDK1.6    2016-1-11`

**1. New SDK features**

* Added screen sharing feature. The SDK can now send and receive screen video.
* Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
* Improved the content, display format and style of tips about call quality.
* Reduced the SDK size by approximately 200 KB.

**2. SDK Bug Fixes**

* Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure.
* Synchronized volume adjustment to fix the bug that quick volume adjustment may have no effect.
* Fixed the crash caused by enabling cameras after executing related logics of external capture.

