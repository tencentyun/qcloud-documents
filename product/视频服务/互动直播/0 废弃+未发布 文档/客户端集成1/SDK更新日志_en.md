## AV_iOS_SDK1.7    March 17, 2016

**1. New SDK Features**

. Added beauty filter APIs
. Split IMSDK to reduce installation package size
. Added the API for obtaining room status parameters
. Added the API for modifying permissions in plaintext

**2. SDK Bug Fixes**

. Fixed blue screen caused by hardware encoding at backend
. Fixed potential crashes caused by network status change
. Fixed the problem that it sometimes takes long to load videos in case of a request for screen sharing

## AV_Android_SDK1.7   March 17, 2016

**1. New SDK Features**

. Added beauty filter APIs
. Added the API for pre-processing local video capturing
. Added the API for obtaining room status parameters
. Added the API for modifying permissions in plaintext
. Added the API for exposing system camera object to allow App to control the flash light on the device

**2. SDK Bug Fixes**

. Fixed the crash caused by calling DestroyContext after calling StopContext
. Fixed the problem that App becomes unresponsive when enabling front camera and flash light after joining a room
. Fixed the crash caused by requestviewlist

## AV_Windows C++SDK1.7   March 17, 2016

**1. New SDK Features**

. Added support for joining a room by accepting an invitation
. Added the API for obtaining room status parameters
. Added the API for modifying permissions in plaintext

**2. SDK Bug Fixes**

. Fixed the problem that no sound can be heard on a hot-plugging USB speaker when the default speaker of the system is disabled


## AV_Web_SDK1.2    Feb 29, 2016

**1. New SDK Features**

(1) Added recording feature


## AV_iOS_SDK1.6    Jan 11, 2016

**1. New SDK Features**

(1) Added screen sharing feature to allow receiving videos on screen shared by PC
(2) Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
(3) Terminal network type reporting
(4) Improved the content, display format and style of tips about call quality

**2. SDK Bug Fixes**

(1) Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
(2) Fixed the crash that occurs when enabling camera after executing logic for external capturing

## AV_Android_SDK1.6    Jan 11, 2016

**1. New SDK Features**

(1) Added screen sharing feature to allow receiving videos on screen shared by PC
(2) Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
(3) Added terminal network type reporting
(4) Improved the content, display format and style of tips about call quality
(5) Reduced the SDK size by approximately 80 KB

**2. SDK Bug Fixes**

(1) Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
(2) Changed to synchronized volume adjustment to fix the problem that quick volume adjustment may not take effect
(3) Fixed the crash occurs when enabling camera after executing the logic for external capturing
(4) Fixed the crash that occasionally occurs when repeating the "Join Room - Enable Camera - Exit Room" procedure

## AV_Windows C++_SDK1.6   Jan 11, 2016

**1. New SDK Features**

(1) Added screen sharing feature to allow sending and receiving videos on screen
(2) Added support for audio data input/output capacities Features such as recording, accompaniment, KTV feedback and custom sound effects can be implemented.
(3) Improved the content, display format and style of tips about call quality
(4) Reduced the SDK size by approximately 200 KB

**2. SDK Bug Fixes**

(1) Fixed the potential crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure
(2) Changed to synchronized volume adjustment to fix the problem that quick volume adjustment may not take effect
(3) Fixed the crash occurs when enabling camera after executing the logic for external capturing

## AV_iOS_SDK1.5 Dec 21, 2015

**1. Multi-Person**

(1) Added OC version APIs
(2) Crash reporting
(3) 2S log reporting
(4) Added the API for modifying permissions to the SDK
(5) Support adjusting digital volume

> Note: After version 1.5, two-person SDK will no longer be released and updated. Two-person audio/video messaging can be implemented by multi-person SDK.

## AV_Android_SDK1.5 Dec 21, 2015

**1. Multi-Person**

(1) Crash reporting
(2) 2S log reporting
(3) Added the API for modifying permissions to the SDK
(4) Support adjusting digital volume

> Note: After version 1.5, two-person SDK will no longer be released and updated. Two-person audio/video messaging can be implemented by multi-person SDK.

## AV_Windows C++_SDK1.5 Dec 21, 2015

1. Crash reporting
2. 2S log reporting
3. Added the API for modifying permissions to the SDK
4. Support adjusting digital volume

## AV_Web_SDK1.0.1 Dec 1, 2015

1. Support rotating video images (Reset; 90°, 180° and 270° clockwise)
2. Screenshot (Save as local BMP image files. Returning base64-encoded screenshots is supported)
3. Support full-screen mode in demo (Press the **ESC** button to return the image to its original size)

## AV_iOS_SDK1.4 Nov 18, 2015

**1. Multi-Person**

(1) Support non-interactive broadcasting which allows live broadcasting streaming based on HLS and RTMP with Tencent Cloud's LVB service
(2) Support multi-channel rendering
(3) Added self-monitoring for audio
(4) The API for obtaining platform system camera object
(5) The option to set whether to print SDK logs to command line window
(6) Optimized the audio parameters configured on SPEAR cloud

**2. Two-Person**

(1) The API for obtaining platform system camera object
(2) The option to set whether to print SDK logs to command line window

## AV_Android_SDK1.4 Nov 18, 2015

**1. Multi-Person**

(1) Support non-interactive broadcasting which allows live broadcasting streaming based on HLS and RTMP with Tencent Cloud's LVB service
(2) Added self-monitoring for audio
(3) Optimized the audio parameters configured on SPEAR cloud
(4) The API for obtaining platform system camera object
(5) The option to set whether to print SDK logs to command line window

**2. Two-Person**

(1) The API for obtaining platform system camera object
(2) The option to set whether to print SDK logs to command line window 

## AV_Windows C++_SDK1.4 Nov 18, 2015

**1. Multi-Person**

(1) Support non-interactive broadcasting which allows live broadcasting streaming based on HLS and RTMP when combined with Tencent Cloud's LVB service
(2) SDK is provided in the form of dynamic library
(3) Added availability check for microphone, speaker, camera and other devices before a chat
(4) Optimized the audio parameters configured on SPEAR cloud

## AV_iOS_SDK1.3 Sep 25, 2015

**1. Multi-Person**

(1) Notification of joining/exiting room by the first 50 room members
(2) Log optimization
(3) Log report
(4) The API for setting storage directory of log files
(5) Support input and output of video streams
(6) Improved design of SDK error codes
(7) Three audio/video modes: VOIP mode, media playback mode, and media capturing and playback mode
(8) Support input of audio streams
(9) Support for recording

**2. Two-Person**

(1) Log optimization
(2) Log report
(3) The API for setting storage directory of log files
(4) Improved design of SDK error codes

## AV_Android_SDK1.3 Sep 25, 2015

**1. Multi-Person**

(1) Notifications of joining/exiting room by the first 50 room members
(2) Log optimization
(3) Log report 
(4) The API for setting storage directory of log files
(5) Support input and output of video streams
(6) Improved design of SDK error codes
(7) Three audio/video modes: VoIP mode, media playback mode, and media capturing and playback mode
(8) Support input of audio streams
(9) Support for recording

**2. Two-Person**

(1) Log optimization
(2) Log report
(3) The API for setting storage directory of log files
(4) Improved design of SDK error codes

## AV_Windows C++_SDK1.3 Sep 25, 2015

**1. Multi-Person**

(1) Notifications of joining/exiting room by the first 50 room members
(2) Log optimization
(3) Log report 
(4) The API for setting storage directory of log files
(5) Support input and output of video streams
(6) Added hot plug detection (HPD) for microphone/speaker
(7) Improved design of SDK error codes
(8) Three audio/video modes: VOIP mode, media playback mode, and media capturing and playback mode
(9) Support for recording

## AV_Web_SDK1.0 Sept 18, 2015

1. Support multi-person audio/video messaging
2. Support configuring audio/video encoding/decoding parameters on the cloud
3. Support integration of self-owned/third-party account login

## AV_Windows C++_SDK1.2.1 Sept 10, 2015

**1. Bug Fixes**

**1.1 Multi-Person**

(1) Fixed the bug that multi-channel video images have incorrect IDs
(2) Fixed the potential crash caused by conversion between openid and tinyid

## AV_Android_SDK1.2.1 Sept 10, 2015

**1. Bug Fixes**

**1.1 Multi-Person**

(1) Fixed the bug that multi-channel video images have incorrect IDs
(2) Fixed the crash caused by the rendering module's attempt to render released frame data

## AV_iOS_SDK1.2.1 Sept 10, 2015

**1. Bug Fixes**

**1.1 Multi-Person**

(1) Fixed the bug that multi-channel video images have incorrect IDs
(2) Fixed the crash caused by the rendering module's attempt to render released frame data


## AV_Windows C++_SDK1.2 Aug 5, 2015

**1.	New SDK Features**

**1.1 Multi-Person**
(1)	Support encoding and decoding videos with a resolution of up to 480×360 and 640×480 respectively
(2) Support configuring audio/video encoding/decoding parameters on the cloud
(3)	Support inputting video stream from the service end
(4)	Support outputting video streams of other room members to the service end for processing and rendering
(5)	Support per-processing of camera videos by service end, which can set pre-processing function pointer to be called by AVSDK to preprocess the video data	
(6)	Support requesting video streams of other room members in multi-channel rooms. A user who has joined the broadcasting can request 3-channel video streams of other room members, while a user who has not can request 4-channel ones
(7)	Support returning part of IMSDK module's error codes
(8) Disabled Assert notification
(9)	Improved log module: The maximum size of log files was changed to 50 MB; Old log files can be deleted. By default, any logs other than the ones for the last three days are deleted
(10) Added more content to key logs to help pinpoint problems
(11) Implemented event notification of the other side's frame rendering

**2.	SDK Bug Fixes**

**2.1. Multi-Person**
(1)	Improved the reliability of operations such as sending/receiving signals and ID conversion and fixed the problem that such operations are prone to fail
(2)	Fixed the bug that the user's image is not shown occasionally [reported by customers]
(3)	Fixed the bug that audio/video encoding/decoding parameters are not configurable in real-time mode [reported by customers]
(4)	Fixed the bug that when the network is restored after an interruption the user can't join the room again [reported by customers]
(5)	Fixed the bug that ID conversion often fails. Such failure could cause the SDK to fail to send notifications of status changes of members to the service end
(6)	Fixed the bug that sometimes after a failure to enable/disable camera, no further operations can be performed

**3.	New Demo Features**

(1) Implemented the example of requesting multi-channel video images

**4.	Demo Bug Fixes**

(1)	Fixed the problem that the demo doesn't support overlong usersig
(2)	Fixed the crash caused by identity with a length of more than 64 characters
(3)	Eliminated the need to disable devices such as camera, microphone and speaker when exiting a room for saving time

## AV_Android_SDK1.2 Aug 5, 2015

**1.	New SDK Features**

1.1	Two-Person
(1)	Improved two-person video messaging quality
(2)	Support encoding and decoding videos with a resolution of up to 640×480
(3)	Support returning part of IMSDK module's error codes	
(4)	Improved log module: The maximum size of log files was changed to 50 MB; Old log files can be deleted. By default, any logs other than the ones for the last three days are deleted
(5)	Added more content to key logs to help pinpointing problems
(6) SDK enables microphone/speaker and sets speaker to receiver mode by default
(7) Implemented event notification of the other side's frame rendering
(8)	Implemented speaking status detection of the other side and relevant event notification
(9)	Removed unwanted APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS
(10) Support capturing camera video with a 640×480 resolution
(11) Added network type configuration logic to make full use of network resources

1.2	Multi-Person
(1)	Support encoding and decoding videos with a resolution of up to 480×360 and 640×480 respectively
(2) Support configuring audio/video encoding/decoding parameters on the cloud
(3)	Support inputting video stream from the service end
(4)	Support outputting video streams of other room members to the service end for processing and rendering
(5)	Support per-processing of camera videos by service end, which can set pre-processing function pointer to be called by AVSDK to preprocess the video data	
(6)	Support requesting video streams of other room members in multi-channel rooms. A user who has joined the broadcasting can request 3-channel video streams of other room members, while a user who has not can request 4-channel ones
(7)	Support returning part of IMSDK module's error codes	
(8)	Improved log module: The maximum size of log files was changed to 50 MB; Old log files can be deleted. By default, any logs other than the ones for the last three days are deleted
(9)	Unified log file naming for Windows and Android to QAVSDK.date.log
(10) Added more content to key logs to help pinpointing problems
(11) SDK enables microphone/speaker and sets speaker to receiver mode by default
(12) Implemented event notification of the other side's frame rendering
(13) Implemented speaking status detection of the other side and relevant event notification
(14) Removed unwanted APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS
(15) Support capturing camera video with a 640×480 resolution
(16) Added network type configuration logic to make full use of network resources

**2.	SDK Bug Fixes**

2.1	Two-Person
(1) Improved the reliability of operations such as sending/receiving signals and ID conversion and fixed the problem that such operations are prone to fail
(2) Fixed the problem that camera is not disabled when user exits a room
(3) Fixed the bug that video recording is unavailable when user exits a room [reported by customers]
(4) Fixed the bug that when the network is restored after an interruption the user can't join the room again [reported by customers]
(5) Fixed the problem that SDK may freeze when both persons exit the room

2.2 Multi-Person
(1) Improved the reliability of operations such as sending/receiving signals and ID conversion and fixed the problem that such operations are prone to fail
(2) Fixed the problem that camera is not disabled when user exits a room
(3) Fixed the bug that video recording is unavailable when user exits a room [reported by customers]
(4) Fixed the bug that when the network is restored after an interruption the user can't join the room again [reported by customers]

**3. New Demo Features**

(1) Added the feature to modify UidType and AppId
(2) Modified related demo code based on modifications of SDK APIs
(3) Added network type configuration logic to make full use of network resources
(4) Support for Android 5.0 and 5.1	

**4. Demo Bug Fixes**

(1) Support returning detailed error codes for the invitation module	
(2) Fixed the memory leakage of AVActivity

## AV_iOS_SDK1.2 Aug 5, 2015

**1. New SDK Features**

1.1 Two-Person
(1) Improved two-person video messaging quality
(2) Support encoding and decoding videos with a resolution of up to 640×480
(3) Support returning part of IMSDK module's error codes	
(4) Improved log module: The maximum size of log files was changed to 50 MB; Old log files can be deleted. By default, any logs other than the ones for the last three days are deleted
(5) Added more content to key logs to help pinpoint problems
(6) SDK enables microphone/speaker and sets speaker to receiver mode by default
(7) Implemented event notification of the other side's frame rendering
(8) Implemented speaking status detection of the other side and relevant event notification
(9) Removed unwanted APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS
(10) Support capturing camera video with a 640×480 resolution
(11) Added network type configuration logic to make full use of network resources

1.2 Multi-Person
(1) Support encoding and decoding videos with a resolution of up to 480×360 and 640×480 respectively
(2) Support configuring audio/video encoding/decoding parameters on the cloud
(3) Support inputting video stream from the service end
(4) Support outputting video streams of other room members to the service end for processing and rendering
(5) Support per-processing of camera videos by service end, which can set pre-processing function pointer to be called by AVSDK to preprocess the video data	
(6) Support requesting video streams of other room members in multi-channel rooms. A user who has joined the broadcasting can request 3-channel video streams of other room members, while a user who has not can request 4-channel ones
(7) Support returning part of IMSDK module's error codes	
(8) Improved log module: The maximum size of log files was changed to 50 MB; Old log files can be deleted. By default, any logs other than the ones for the last three days are deleted
(9) Unified log file naming for Windows and Android to QAVSDK.date.log
(10) Added more content to key logs to help pinpointing problems
(11) SDK enables microphone/speaker and sets speaker to receiver mode by default
(12) Implemented event notification of the other side's frame rendering
(13) Implemented speaking status detection of the other side and relevant event notification
(14) Removed unwanted APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS
(15) Support capturing camera video with a 640×480 resolution
(16) Added network type configuration logic to make full use of network resources

**2. SDK Bug Fixes**

2.1 Two-Person
(1) Improved the reliability of operations such as sending/receiving signals and ID conversion and fixed the problem that such operations are prone to fail
(2) Fixed the problem that audio/video devices may not be disabled when user exits a room
(3) Fixed the problem that SDK may freeze when both persons exit the room
(4) Fixed the crash caused by running two-person SDK deployed on target 7.0 (reported by customers)
(5) Fixed the bug that recording video with UIImagePicker is impossible after video is enabled and then be disabled [reported by customers]
(6) Fixed the bug that when the network is restored after an interruption the user can't join the room again [reported by customers]

2.2 Multi-Person
(1) Improved the reliability of operations such as sending/receiving signals and ID conversion and fixed the problem that such operations are prone to fail
(2) Fixed the problem that audio/video devices may not be disabled when user exits a room
(3) Fixed the bug that audio/video encoding/decoding parameters are not configurable in real-time mode [reported by customers]
(4) Fixed the bug that recording video with UIImagePicker is impossible after video is enabled and then be disabled [reported by customers]
(5) Fixed the bug that when the network is restored after an interruption the user can't join the room again [reported by customers]

**3. New Demo Features**

(1) Added support for switching between test/release environments
(2) Optimized the operations to initiate two-person chat
(3) Modified related demo code based on modifications of SDK APIs
(4) Added network type configuration logic to make full use of network resources

**4. Demo Bug Fixes**

(1) Support returning detailed error codes for the invitation module
(2) Show the error code in case of a failure of login

## AV_Android_SDK1.1.1 June 18, 2015

**1. Multi-Person Audio/Video Messaging**

(1) Support obtaining and displaying audio/video tips in multi-person messaging
(2) Fixed the problem of duplicate profile photos of multiple persons
(3) Fixed the bug that in a multi-person chat the camera may be disabled automatically
(4) Multi-person Application can directly inherit from system's Application, instead of IMBASEApplication

**2. Two-Person Audio/Video Messaging**

(1) Support obtaining and displaying audio/video tips in two-person messaging
(2) Added the API for adding accounts in two-person account list
(3) Notification of network interruption in two-person messaging
(4) When either of two persons loses connection, another person wouldn't exit the interface
(5) Two-person Application can directly inherit from system's Application, instead of IMBASEApplication

## AV_iOS_SDK1.1.1 June 18, 2015

**1. Multi-Person Audio/Video Messaging**

(1) Support processing video stream input and output
(2) Only provide voice packets for multi-person messaging
(3) Modified thread switching mechanism of SDK to avoid crash caused by thread switching callback to upper-layer when a room is closed
(4) Added tips on adding accounts
(5) Added notification of appid configuration modification
(6) Added a switch between test and release environments in the demo

**2. Two-Person Audio/Video Messaging**

(1) Support obtaining quality tips
(2) Support processing video stream input and output
(3) Modified thread switching mechanism of SDK to avoid crash caused by thread switching callback to upper-layer when a room is closed
(4) Added tips on adding accounts
(5) Added notification of appid configuration modification
(6) Support displaying two-person messaging tips in the demo
(7) Added a switch between test and release environments in the demo

**3. Bug Fixes**

(1) Fixed the potential crash that occurs when a room member exits the room
(2) Fixed the potential crash that occurs when creation of room fails
(3) Fixed the crash that occurs when receiving videos shared from side-channel screen
(4) Fixed the bug of repeated logout in the demo
(5) Fixed the bug of deletion of accounts in the demo

## AV_Windows C++_SDK1.1.1 June 18, 2015

**1. New Features**

(1) Added the API for the upper-layer to preprocess video data captured from the camera before sending it out
(2) Added the API for inputting custom video stream from outside to SDK and sending them to others. The video stream can either be captured by camera and then be preprocessed, or comes from other video sources
(3) Added self-help solution to "no sound can be heard/no video can be seen" situation
(4) Added some usage tips for "Add Try-out Scenario Configuration" and "Add Account" windows
(5) Added the API for setting chatting scenarios
(6) Modified the API for member status notification. The notification is sent only when the user status about whether sending audio/video changes

**2. Bug Fixes**

(1) Fixed the bug that the user is still in the video for about 15s when the camera fails to be enabled
(2) Fixed a potential bug caused by the failure to disable the camera from outside of SDK when a user exits the room
(3) Fixed a potential bug caused by calling StopContext when resources are being released due to the failure to join a room
(4) Fixed the bug that no notification of timeout or network port is received in case of a network interruption during a chat
(5) Fixed the potential crash that occurs in case of a network interruption during a chat
(6) Updated IMSDK to solve several login-related bugs

## AV_Android_SDK1.0.1 June 1, 2015

**1. Multi-Person Audio/Video Messaging**

(1) Added notification of timeout that occurs when multiple people join a room
(2) Added the API for setting audio/video encoding/decoding parameters
(3) Added the API for obtaining audio/video quality information
(4) Solved the problem that media volume cannot be adjusted after switching to background or hanging up audio/video calls
(5) Unified the field names of AVContext::Config of demo and SDK
(6) Fixed the ANR problem that occurs when a user joins/exits a room

**2. Two-Person Audio/Video Messaging**

(1) Added notification of conflict between invitations from both persons
(2) Solved the problem that media volume cannot be adjusted after switching to background or hanging up audio/video calls
(3) Unified the field names of AVContext::Config of demo and SDK
(4) Fixed the flickering screen that occurs when switching between the screens of two sides

## AV_iOS_SDK1.0.1 June 1, 2015

**1. Multi-Person Audio/Video Messaging**

(1) Added notifications of demo login error and room creation timeout
(2) Added the API for setting audio/video encoding/decoding parameters
(3) Added the API for obtaining audio/video quality information
(4) Unified the field names of AVContext::Config of demo and SDK
(5) Fixed the SDK's timeout logic for joining room
(6) Fixed the namespace conflict that occurs when using protobuf open-source library synchronously with customers

**2. Two-Person Audio/Video Messaging**

(1) Added notifications of demo login error and room creation timeout
(2) Fixed the problem of getting stuck in prompt box when joining a room in demo
(3) Unified the field names of AVContext::Config of demo and SDK
(4) Fixed the SDK's timeout logic for joining room
(5) Fixed the namespace conflict that occurs when using protobuf open-source library synchronously with customers

## AV_Windows C++_SDK1.0.1 June 1, 2015

1. Added crash reporting feature
2. Added the API for obtaining audio/video quality information
3. Fixed memory leakage during chat
4. Fixed the problem that the SDK needs to be recompiled due to the addition of some SdkAppIds hardcoded in the SDK

## AV_Android_SDK1.0 May 11, 2015

1. Support two-person audio/video messaging
2. Support multi-person audio/video messaging
3. Support integration of self-owned/third-party account login

## AV_iOS_SDK1.0 May 11, 2015

1. Support two-person audio/video messaging
2. Support multi-person audio/video messaging
3. Support integration of self-owned/third-party account login

## AV_Windows C++_SDK1.0 May 11, 2015

1. Support multi-person audio/video messaging
2. Support integration of self-owned/third-party account login

For more information on the audio/video messaging SDK, please see [Feature List](/doc/product/268/功能列表).
