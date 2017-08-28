## AV_iOS_SDK1.8.2    8/12/2016
•Added video watermark feature.
•Added SDK node reporting feature.
•Refactored audio/video packet's sending/receiving module.
•Added support for switching audio scenario in rooms.
•Added room timeout callbacks.
•Added notifications about changes in room camera capture settings.
•The SDK now automatically applies for video bits to prevent invalid videos caused by missing video bits.
•Added notifications for setting camera capture parameters.
•Adjusted some APIs.

## AV_Android_SDK1.8.2    8/12/2016
•Added video watermark feature.
•Added SDK node reporting feature.
•Refactored audio/video packet's sending/receiving module.
•Added support for switching audio scenario in rooms.
•Added room timeout callbacks.
•Added notifications about changes in room camera capture settings.
•The SDK now automatically applies for video bits to prevent invalid videos caused by missing video bits.
•Added notifications for setting camera capture parameters.
•Adjusted some APIs.

## AV_iOS_SDK1.8.1.1    6/21/2016
•Fixed some crash issues.
•Fixed the blackscreen issue after switching back from background.

## AV_Android_SDK1.8.1.1    6/21/2016
•Added main thread protection for "creating context".
•Fixed the blackscreen issue caused by the desynchronization between stream control parameter and encoder status. 
•Fixed the crash caused by modifying "change role".
•Fixed a bug that user cannot join rooms after switching the account due to the mismatched "create" and "destroy".
•Fixed potential memory leak when receiving packets.
•Fixed the blackscreen issue after switching back from background.

## AV_WIN_SDK1.8.1.1    6/21/2016
•Fixed the bug on receiving logic that could potentially cause a significant memory leakage.
•Fixed the crash issue that happened if the following conditions were all true after joining a room.
•Fixed a bug that after "Join room - Start screen sharing - Exit room - Join room again - Request screen sharing from other people" operations, the shared screen may not be rendered.

## AV_iOS_SDK1.8.1    6/6/2016
**1. New SDK features**

•Video hardware encoding
•The aspect ratio of 16:9 is supported when capturing videos.
•Added support for beauty filter APIs.
•Room joining speed optimization.
•Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P.
•Audio quality optimization. 64kbps bitrate is now available.
•Added high quality audio API for "Broadcast" mode in VJ scenarios.
•Optimized listening APIs and lowered latency.
•Added APIs that directly receive existing videos instead of making additional requests when joining a room.
•Added APIs that switch roles without re-joining the room.
•Added APIs that customize real-time sound effects and custom sample rates is supported.
•Added sound engine terminal and recovery feature.
•Added external APIs to query whether beauty filter is enabled.
•Added APIs to set local video pre-process callbacks.
•Added APIs to set notifications when a room member uses certain audio feature without having proper permissions.
•Added APIs to obtain version number.
•Added API to obtain time stamp.

**2. SDK Bug Fixes**

•Encoding effects for video softwares under VJ mode have been optimized.
•Issues regarding blurred screen, green screen, reversed playback in videos have been fixed.
•Issues regarding blurred screen, green screen, reversed playback in videos have been fixed.
•Issues regarding video display being reduced/stretched on certain models have been fixed.
•Fixed the issue that audio is stopped briefly when video is closed.
•Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios.
•Fixed a bug that some viewers can't hear any sound in VJ scenarios.
•Issues regarding audio accompaniment memory not being released have been fixed.
•Several Crash issues have been fixed.
•Now the SDK switches from hardware encoding to software encoding when the VJ is answering a call.
•Fixed occasional crashes when exiting a room.
•Added protection for calling stopcontext in a room.
•Fixed the crash caused by continuing sending packets after exiting a room.
•Fixed potential memory leak when receiving packets.
•Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously.
•Fixed a bug that a user couldn't request video image when he/she had only downlink permissions.
•Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions.
•Fixed the likely crash caused by network interruptions when beauty filter is enabled.
•Fixed a bug that room members couldn't hear sound from microphones on iOS 7.1.2.
•Fixed a bug that iPod touch 6 couldn't enable beauty filter.
•Fixed a bug that the SDK process is manually terminated when requesting other people's videos on iOS.
•Fixed the issue of occasional blue screen reboots.

## AV_Android_SDK1.8.1    6/6/2016
**1. New SDK features**

•Video hardware encoding
•The aspect ratio of 16:9 is supported when capturing videos.
•Added support for beauty filter APIs.
•Room joining speed optimization.
•Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P.
•Audio quality optimization. 64kbps bitrate is now available.
•Added APIs that directly receive existing videos instead of making additional requests when joining a room.
•Added APIs that switch roles without re-joining the room.
•Added APIs that customize real-time sound effects and custom sample rates is supported.
•Added sound engine terminal and recovery feature.
•Added external APIs to query whether beauty filter is enabled.
•Added APIs to obtain version number.
•Added API to obtain time stamp.

**2. SDK Bug Fixes**

•Encoding effects for video softwares under VJ mode have been optimized.
•Issues regarding blurred screen, green screen, reversed playback in videos have been fixed.
•Issues regarding blurred screen, green screen, reversed playback in videos have been fixed.
•Issues regarding video display being reduced/stretched on certain models have been fixed.
•Fixed the issue that audio is stopped briefly when video is closed.
•Fixed the issue that the actual bitrate is lower than the bitrate configured in the cloud under high bitrate video scenarios.
•Several Crash issues have been fixed.
•Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously.
•Fixed a bug that a user couldn't request video image when he/she had only downlink permissions.
•Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions.
•Fixed occasional crashes when calling getqualityparas API.
•Fixed the problem that too much logs are printed after enabling hardware encoding.
•Fixed a bug that caused blurred camera screen on LG NEXUS6 Android 6.0.
•Fixed frequent video memory GC in VJ mode on Android.

## AV_Windows_SDK1.8.1    6/6/2016
**1. New SDK features**

•The aspect ratio of 16:9 is supported when capturing videos.
•Room joining speed optimization.
•Video quality is optimized, resolution/framerate are synchronized with Web configurations, and video (software) encoding output is improved to 720P.
•Audio quality optimization. 64kbps bitrate is now available.
•Added high quality audio API for "Broadcast" mode in VJ scenarios.
•Added low-latency listening API.
•Added APIs that directly receive existing videos instead of making additional requests when joining a room.
•Added APIs that switch roles without re-joining the room.
•Added APIs that customize real-time sound effects and custom sample rates is supported.
•Added APIs to obtain version number.

**2. SDK Bug Fixes**

•Fixed a bug that screen sharing and camera video primary screen could be sent simultaneously.
•Fixed a bug that a user couldn't request video image when he/she had only downlink permissions.
•Fixed a bug that the remote end of the camera couldn't see the video status after a user was given uplink permissions.
•Fixed the 1301 error caused by enabling screen sharing after hot-plugging microphones.

## AV_iOS_SDK1.7    3/17/2016

**1. New SDK features**

. Added beauty filter APIs.
. Splitted IMSDK to reduce installation package size.
. Added APIs to obtain room status parameters.
. Added APIs for permissions to modify plaintext.

**2. SDK Bug Fixes**

. Fixed a bluescreen bug caused by enabling backend hardware encoding.
. Fixed crashes caused by changing network status.
. Fixed a problem that the video may take long to load after requesting screen sharing.

## AV_Android_SDK1.7    3/17/2016

**1. New SDK features**

. Added beauty filter APIs.
. Added APIs to pre-process local video capture.
. Added APIs to obtain room status parameters.
. Added APIs for permissions to modify plaintext.
. Added APIs to expose system camera object, so that the APP can control the flash lights on the device.

**2. SDK Bug Fixes**

. Fixed the crash caused by calling DestroyContext after calling StopContext.
. Fixed a bug that the App becomes unresponsive when enabling both front camera and flash light after joining a room.
. Fixed the crash caused by requestviewlist.

## AV_Windows C++SDK1.7   3/17/2016

**1. New SDK features**

. Added support for joining a room by accepting an invitation.
. Added APIs to obtain room status parameters.
. Added APIs for permissions to modify plaintext.

**2. SDK Bug Fixes**

. Fixed a bug that no sound was played on a hot-plugging USB speaker when the default speaker of the system was disabled.


## AV_Web_SDK1.2    2/29/2016

**1. New SDK features**

(1) Added recording feature.


## AV_iOS_SDK1.6    1/11/2016

**1. New SDK features**

(1) Added screen sharing feature. The SDK can now receive screen video shared by PC.
(2) Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
(3) Added terminal network type reporting feature.
(4) Improved the content, format and style of tips about call quality.

**2. SDK Bug Fixes**

(1) Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure..
(2) Fixed the crash caused by enabling cameras after executing related logics of external capture.

## AV_Android_SDK1.6    1/11/2016

**1. New SDK features**

(1) Added screen sharing feature. The SDK can now receive screen video shared by PC.
(2) Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
(3) Added terminal network type reporting feature.
(4) Improved the content, format and style of tips about call quality.
(5) Reduced the SDK size by approximately 80KB.

**2. SDK Bug Fixes**

(1) Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure..
(2) Synchronized volume adjustment is supported to fix the bug that quick volume adjustment may have no effect.
(3) Fixed the crash caused by enabling cameras after executing related logics of external capture.
(4) Fixed the occasional crashes when repeating the "Join Room - Enable Camera - Exit Room" procedure.

## AV_Windows C++_SDK1.6    1/11/2016

**1. New SDK features**

(1) Added screen sharing feature. The SDK can now send and receive screen videos.
(2) Added support for audio data input/output capacities. Features such as recording, accompaniment, KTV listening and custom sound effects can now be implemented.
(3) Improved the content, format and style of tips about call quality.
(4) Reduced the SDK size by approximately 200KB.

**2. SDK Bug Fixes**

(1) Fixed the possible crash or blurred screen caused by image resolution change when processing video frames from the same user during "Decoding - Rendering" procedure..
(2) Synchronized volume adjustment is supported to fix the bug that quick volume adjustment may have no effect.
(3) Fixed the crash caused by enabling cameras after executing related logics of external capture.

## AV_iOS_SDK1.5   12/21/2015

**1. Multiperson**

(1) Added OC version APIs.
(2) Added crash reporting feature.
(3) Added 2S log reporting feature.
(4) Added permission modifying APIs to the SDK.
(5) Added support for adjusting digital volume.

>Note: After version 1.5, two-person SDK is not released and updated anymore. Two-person audio/video messaging can be implemented by multi-person SDK.

## AV_Android_SDK1.5   12/21/2015

**1. Multiperson**

(1) Added crash reporting feature.
(2) Added 2S log reporting feature.
(3) Added permission modifying APIs to the SDK.
(4) Added support for adjusting digital volume.

>Note: After version 1.5, two-person SDK is not released and updated anymore. Two-person audio/video messaging can be implemented by multi-person SDK.

## AV_Windows C++_SDK1.5   12/21/2015

1 Added crash reporting feature.
2. Added 2S log reporting feature.
3. Added permission modifying APIs to the SDK.
4. Added support for adjusting digital volume.

## AV_Web_SDK1.0.1   12/1/2015

1. Added support for rotating videos. (Reset, or turn 90°, 180° and 270° clockwise)
2. Screencap (The screenshots are saved to local BMP image files. Returning screenshots encoded by base64 is also supported.)
3. Demo now supports full screen mode. (Press ESC key to return to the original size.)

## AV_iOS_SDK1.4   11/18/2015

**1. Multiperson**

(1) With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.
(2) Added support for multi-channel rendering in rendering modules.
(3) Added self-listening function to audio.
(4) Provided APIs to access to camera object on platform system.
(5) Provided features for setting whether the SDK logs prints to command line window.
(6) Optimized the audio parameters configuration of the SPEAR cloud configuration.

**2. Two-person**

(1) Provided APIs to access to camera object on platform system.
(2) Provided features for setting whether the SDK logs prints to command line window.

## AV_Android_SDK1.4   11/18/2015

**1. Multiperson**

(1) With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.
(2) Added self-listening function to audio.
(3) Optimized the audio parameters configuration of the SPEAR cloud configuration.
(4) Provided APIs to access to camera object on platform system.
(5) Provided features for setting whether the SDK logs prints to command line window.

**2. Two-person**

(1) Provided APIs to access to camera object on platform system.
(2) Provided features for setting whether the SDK logs prints to command line window. 

## AV_Windows C++_SDK1.4   2015-11-18

**1. Multiperson**

(1) With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.
(2) The SDK is available in the form of a dynamic library.
(3) Added availability check of microphones, speakers and cameras before messaging.
(4) Optimized the audio parameters configuration of the SPEAR cloud configuration.

## AV_iOS_SDK1.3   9/25/2015

**1. Multiperson**

(1) Notifications about the first 50 members' joining/exiting the room.
(2) Added log optimization feature.
(3) Added log reporting feature.
(4) Added APIs to set storage directory of log files.
(5) Added support for input/output video streams.
(6) Improved SDK error code design.
(7) Added three audio/video modes: VoIP mode, media playback mode, and media capture and playback mode.
(8) Added support for input audio stream.
(9) Added recording feature.

**2. Two-person**

(1) Added log optimization feature.
(2) Added log reporting feature.
(3) Added APIs to set storage directory of log files.
(4) Improved SDK error code design.

## AV_Android_SDK1.3   9/25/2015

**1. Multiperson**

(1) Notifications about the first 50 members' joining/exiting the room.
(2) Added log optimization feature.
(3) Added log reporting feature.
(4) Added APIs to set storage directory of log files.
(5) Added support for input/output video streams.
(6) Improved SDK error code design.
(7) Added three audio/video modes: VoIP mode, media playback mode, and media capture and playback mode.
(8) Added support for input audio stream.
(9) Added recording feature.

**2. Two-person**

(1) Added log optimization feature.
(2) Added log reporting feature.
(3) Added APIs to set storage directory of log files.
(4) Improved SDK error code design.

## AV_Windows C++_SDK1.3   9/25/2015

**1. Multiperson**

(1) Notifications about the first 50 members' joining/exiting the room.
(2) Added log optimization feature.
(3) Added log reporting feature.
(4) Added APIs to set storage directory of log files.
(5) Added support for input/output video streams.
(6) Added microphone/speaker hot-plug detection feature.
(7) Improved SDK error code design.
(8) Added three audio/video modes: VoIP mode, media playback mode, and media capture and playback mode.
(9) Added recording feature.

## AV_Web_SDK1.0   9/18/2015

1. Added support for multi-person audio/video messaging.
2. Added support for configuring audio/video encoding/decoding parameters on the cloud.
3. Added support for login with owned/3rd-party account.

## AV_Windows C++_SDK1.2.1   9/10/2015

**1. Bug Fixes**

**1) Multiperson**

(1) Fixed a bug that displays of multi-channel video have incorrect IDs.
(2) Fixed a potential crash caused by openid/tinyid conversion.

## AV_Android_SDK1.2.1   9/10/2015

**1. Bug Fixes**

**1) Multiperson**

(1) Fixed a bug that displays of multi-channel video have incorrect IDs.
(2) Fixed the crash caused by the rendering module's attempts to render released frame data.

## AV_iOS_SDK1.2.1   9/10/2015

**1. Bug Fixes**

**1) Multiperson**

(1) Fixed a bug that displays of multi-channel video have incorrect IDs.
(2) Fixed the crash caused by the rendering module's attempts to render released frame data.


## AV_Windows C++_SDK1.2   8/5/2015

**1. New SDK features**

1) Multiperson
(1) Now the SDK supports resolutions as high as 480×360 in encoding, and 640×480 in decoding.
(2) Added support for configuring audio/video encoding/decoding parameters on the cloud.
(3) Implemented video stream input from the client.
(4) Implemented outputting video streams of other room members to the client, which can then process and render the streams, etc.
(5) Implemented service-end camera video preprocess feature. The client can set preprocess function pointer, and the AVSDK would call it to preprocess video data.	
(6) Implemented requesting the videos of other room members in multi-channel rooms. If one is on the broadcast, he/she can request 3 video channels of other members; otherwise, he/she can request 4.
(7) Returned a part of IMSDK module's error codes.
(8) Disabled assertion notifications.
(9) Improved logging module. The maximum size of log files is now 50M. Old log files can now be deleted. By default, the log files three days ago are all deleted.
(10) Added more content into critical logs to help pinpointing problems.
(11) Implemented event notifications of the peer's frame rendering.

**2. SDK Bug Fixes**

1) Multiperson
(1) Improved the reliability of operations such as sending/receiving signals and id conversion. Fixed the issue that operations such as sending/receiving signals and id conversion are prone to failure.
(2) Fixed the occasional bug that the video of the user itself is not shown. (Reported by clients.)
(3) Fixed a bug that audio/video encoding/decoding parameters can't be configured in real-time mode. (Reported by clients.)
(4) Fixed a bug that after the network is interrupted and later restored, one can't join the room again. (Reported by clients.)
(5) Fixed a bug that id conversion operations often fail, and therefore the SDK may not send notifications about changes of member status to the client.
(6) Fixed a bug that sometime after enabling/disabling camera device operation fails no further operations can be executed.

**3. New Demo Features**

(1) Implemented the example of requesting multi-channel videos.

**4. Demo Bug Fixes**

(1) Fixed the issue that the demo doesn't support overlength usersig.
(2) Fixed the crash caused by identify over 64 in length.
(3) The devices such as camera, microphone and speaker are not disabled any more when exiting a room to save time.

## AV_Android_SDK1.2   8/5/2015

**1. New SDK features**

1) Two-person
(1) Improved two-person video quality.
(2) Now the SDK supports resolutions as high as 640×480 in encoding, and 640×480 in decoding.
(3) Returned a part of IMSDK module's error codes.	
(4) Improved logging module. The maximum size of log files is now 50M. Old log files can now be deleted. By default, the log files three days ago are all deleted.
(5) Added more content into critical logs to help pinpointing problems.
(6) The SDK now enables microphones/speakers and sets speakers to receiver mode by default.
(7) Implemented event notifications of the peer's frame rendering.
(8) Implemented voice detection of the peer and event notifications.
(9) Deleted unnecessary APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS.
(10) Added support for capturing camera video of 640×480 resolution.
(11) Added configuration logics for network type to make full use of network resources.

2) Multiperson
(1) Now the SDK supports resolutions as high as 480×360 in encoding, and 640×480 in decoding.
(2) Added support for configuring audio/video encoding/decoding parameters on the cloud.
(3) Implemented video stream input from the client.
(4) Implemented outputting video streams of other room members to the client, which can then process and render the streams, etc.
(5) Implemented service-end camera video preprocess feature. The client can set preprocess function pointer, and the AVSDK would call it to preprocess video data.	
(6) Implemented requesting the videos of other room members in multi-channel rooms. If one is on the broadcast, he/she can request 3 video channels of other members; otherwise, he/she can request 4.
(7) Returned a part of IMSDK module's error codes.	
(8) Improved logging module. The maximum size of log files is now 50M. Old log files can now be deleted. By default, the log files three days ago are all deleted.
(9) Standardized log file naming for Windows and Android to QAVSDK.<date>.log.
(10) Added more content into critical logs to help pinpointing problems.
(11) The SDK now enables microphones/speakers and sets speakers to receiver mode by default.
(12) Implemented event notifications of the peer's frame rendering.
(13) Implemented voice detection of the peer and event notifications.
(14) Deleted unnecessary APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS.
(15) Added support for capturing camera video of 640×480 resolution.
(16) Added configuration logics for network type to make full use of network resources.

**2. SDK Bug Fixes**

1) Two-person
(1) Improved the reliability of operations such as sending/receiving signals and id conversion. Fixed the issue that operations such as sending/receiving signals and id conversion are prone to failure.
(2) Fixed the issue that cameras are not disabled when exiting a room. (Reported by clients.)
(3) Fixed a bug that users can't record video when they exit a room. 
(4) Fixed a bug that after the network is interrupted and later restored, one can't join the room again. (Reported by clients.)
(5) Fixed the issue that the SDK may freeze when two people exit a room.

2) Multiperson
(1) Improved the reliability of operations such as sending/receiving signals and id conversion. Fixed the issue that operations such as sending/receiving signals and id conversion are prone to failure.
(2) Fixed the issue that cameras are not disabled when exiting a room. (Reported by clients.)
(3) Fixed a bug that users can't record video when they exit a room.
(4) Fixed a bug that after the network is interrupted and later restored, one can't join the room again. (Reported by clients.)

**3. New Demo Features**

(1) Added the features to modify UidType and AppId.
(2) Modified related demo code according to modifications of SDK APIs.
(3) Added configuration logics for network type to make full use of network resources.
(4) Added support for Android 5.0 and 5.1.	

**4. Demo Bug Fixes**

(1) Added detailed error codes returned for the invitation module.	
(2) Fixed memory leaks of AVActivity

## AV_iOS_SDK1.2   8/5/2015

**1. New SDK features**

1) Two-person
(1) Improved two-person video quality.
(2) Now the SDK supports resolutions as high as 640×480 in encoding, and 640×480 in decoding.
(3) Returned a part of IMSDK module's error codes.	
(4) Improved logging module. The maximum size of log files is now 50M. Old log files can now be deleted. By default, the log files three days ago are all deleted.
(5) Added more content into critical logs to help pinpointing problems.
(6) The SDK now enables microphones/speakers and sets speakers to receiver mode by default.
(7) Implemented event notifications of the peer's frame rendering.
(8) Implemented voice detection of the peer and event notifications.
(9) Deleted unnecessary APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS.
(10) Added support for capturing camera video of 640×480 resolution.
(11) Added configuration logics for network type to make full use of network resources.

2) Multiperson
(1) Now the SDK supports resolutions as high as 480×360 in encoding, and 640×480 in decoding.
(2) Added support for configuring audio/video encoding/decoding parameters on the cloud.
(3) Implemented video stream input from the client.
(4) Implemented outputting video streams of other room members to the client, which can then process and render the streams, etc.
(5) Implemented service-end camera video preprocess feature. The client can set preprocess function pointer, and the AVSDK would call it to preprocess video data.	
(6) Implemented requesting the videos of other room members in multi-channel rooms. If one is on the broadcast, he/she can request 3 video channels of other members; otherwise, he/she can request 4.
(7) Returned a part of IMSDK module's error codes.	
(8) Improved logging module. The maximum size of log files is now 50M. Old log files can now be deleted. By default, the log files three days ago are all deleted.
(9) Standardized log file naming for Windows and Android to QAVSDK.<date>.log.
(10) Added more content into critical logs to help pinpointing problems.
(11) The SDK now enables microphones/speakers and sets speakers to receiver mode by default.
(12) Implemented event notifications of the peer's frame rendering.
(13) Implemented voice detection of the peer and event notifications.
(14) Deleted unnecessary APIs such as AVAudioCtrl::EnableBoost/EnableAEC/EnableNS.
(15) Added support for capturing camera video of 640×480 resolution.
(16) Added configuration logics for network type to make full use of network resources.

**2. SDK Bug Fixes**

1) Two-person
(1) Improved the reliability of operations such as sending/receiving signals and id conversion. Fixed the issue that operations such as sending/receiving signals and id conversion are prone to failure.
(2) Fixed the issue that audio/video devices may not be disabled when exiting a room.
(3) Fixed the issue that the SDK may freeze when two people exit a room.
(4) Fixed a crash caused by the running two-person with SDK deployed on target 7.0. (Reported by clients.)
(5) Fixed a bug that after video is enabled and disabled, UIImagePicker can no longer be used to record video. (Reported by clients.)
(6) Fixed a bug that after the network is interrupted and later restored, one can't join the room again. (Reported by clients.)

2) Multiperson
(1) Improved the reliability of operations such as sending/receiving signals and id conversion. Fixed the issue that operations such as sending/receiving signals and id conversion are prone to failure.
(2) Fixed the issue that audio/video devices may not be disabled when exiting a room.
(3) Fixed a bug that audio/video encoding/decoding parameters can't be configured in real-time mode. (Reported by clients.)
(4) Fixed a bug that after video is enabled and disabled, UIImagePicker can no longer be used to record video. (Reported by clients.)
(5) Fixed a bug that after the network is interrupted and later restored, one can't join the room again. (Reported by clients.)

**3. New Demo Features**

(1) Added a feature to switch between test and release environments.
(2) Optimized the operations to initiate two-person call.
(3) Modified related demo code according to modifications of SDK APIs.
(4) Added configuration logics for network type to make full use of network resources.

**4. Demo Bug Fixes**

(1) Added detailed error codes returned for the invitation module.
(2) The interface now shows the error code when login fails.

## AV_Android_SDK1.1.1   6/18/2015

**1. Multi-person Audio/Video Messaging**

(1) Added the feature that multi-person can obtain and display tips on audio/video.
(2) Fixed the problem of duplicated profile photos.
(3) Fixed a bug that in a multi-person call the cameras may sometimes be disabled automatically.
(4) Multi-person Application doesn't need to inherit from IMBASEApplication anymore. Instead, it can directly inherit from system's Application.

**2. Two-person Audio/Video Messaging**

(1) Added the feature that two-person can obtain and display tips on audio/video.
(2) Added APIs to add accounts in two-person account list.
(3) Added network interruption notifications in two-person calls.
(4) When one side in the call losses connection, the other side wouldn't exit the interface.
(5) Two-person Application doesn't need to inherit from IMBASEApplication anymore. Instead, it can directly inherit from system's Application.

## AV_iOS_SDK1.1.1   6/18/2015

**1. Multi-person Audio/Video Messaging**

(1) Added support of input and output process of video streams.
(2) Only voice package is supported for multi-person messaging.
(3) Modified thread switching mechanism of the SDK to avoid crashes caused by upper-level callback of thread switching when a room is terminated.
(4) Added tips about adding accounts.
(5) Added notifications about modifying appid settings.
(6) Added a switch between test and release environments to the demo.

**2. Double-person Audio/Video Messaging**

(1) Obtaining quality tips is supported.
(2) Added support of input and output process of video streams.
(3) Modified thread switching mechanism of the SDK to avoid crashes caused by upper-level callback of thread switching when a room is terminated.
(4) Added tips about adding accounts.
(5) Added notifications about modifiying appid settings.
(6) Added support of displaying two-person call tips in the demo.
(7) Added a switch between test and release environments to the demo.

**3. Bug Fixes**

(1) Fixed an occasional crash when a room member exits the room.
(2) Fixed an occasional crash caused by failure to create a room.
(3) Fixed a crash caused by receiving side-channel screen sharing.
(4) Fixed the bug of repetitive logout in the demo.
(5) Fixed the bug of deleting accounts in the demo.

## AV_Windows C++_SDK1.1.1   6/18/2015

**1. New Features**

(1) Added APIs for the upper-level to preprocess video data captured from the cameras before sending them out.
(2) Added APIs to input a custom external video stream to the SDK and send to the others. This video stream can be a stream captured and preprocess from the camera by oneself, and can also be other video sources.
(3) Added custom self-help solution manual for "no sound/no video" situations.
(4) Added some usage tips for "Add experience scenario configurations" and "Add account" windows.
(5) Added APIs to set call scenarios.
(6) Modified member status notification APIs. Now notifications are sent only when a user starts/stops sending audio/video.

**2. Bug Fixes**

(1) Fixed a bug that one is still about 15s in the video when the camera fails to be enabled.
(2) Fixed a possible bug caused by external SDK's not disabling the cameras when one exits a room.
(3) Fixed a possible bug caused by calling StopContext when resources are being released because of failure to join a room.
(4) Fixed a bug that during a call , timeout doesn't occur and no notifications are received from the network ports when the network is interrupted.
(5) Fixed potential crashes caused by network interruption during a call.
(6) Updated IMSDK and solved several login-related bugs.

## AV_Android_SDK1.0.1 2015-06-01

**1. Multi-person Audio/Video Messaging**

(1) Added timeout notifications when multiple people join a room.
(2) Added APIs to set audio/video encoding/decoding parameters.
(3) Added APIs to obtain audio/video-related quality information.
(4) Solved the problem that media volume cannot be adjusted after switching to background or hanging up audio/video calls.
(5) Unified the naming of the fields of demo and SDK's AVContext::Config.
(6) Fixed an issue related to ANR when joining/exiting a room.

**2. Two-person Audio/Video Messaging**

(1) Added notifications about two-person invitation conflicts.
(2) Solved the problem that media volume cannot be adjusted after switching to background or hanging up audio/video calls.
(3) Unified the naming of the fields of demo and SDK's AVContext::Config.
(4) Fixed the screen flickering issue when switching between the two screens in a two-person call.

## AV_iOS_SDK1.0.1   6/1/2015

**1. Multi-person Audio/Video Messaging**

(1) Added notifications about demo's login errors and room creation timeout.
(2) Added APIs to set audio/video encoding/decoding parameters.
(3) Added APIs to obtain audio/video-related quality information.
(4) Unified the naming of the fields of demo and SDK's AVContext::Config.
(5) Fixed the SDK's timeout logics related to joining rooms.
(6) Fixed the namespace collision caused by using protobuf open-source library together with the users.

**2. Two-person Audio/Video Messaging**

(1) Added notifications about demo's login errors and room creation timeout.
(2) Fixed the issue that when entering a room, the demo can't get pass the prompt.
(3) Unified the naming of the fields of demo and SDK's AVContext::Config.
(4) Fixed the SDK's timeout logics related to joining rooms.
(5) Fixed the namespace collision caused by using protobuf open-source library together with the users.

## AV_Windows C++_SDK1.0.1   6/1/2015

1. Added crash reporting feature.
2. Added APIs to obtain audio/video-related quality information.
3. Fixed memory leaks during calls.
4. Fixed the issue that the SDK needs to be recompiled because some SdkAppIds are hardcoded into the SDK.

## AV_Android_SDK1.0   5/11/2015

1. Added support for two-person audio/video messaging.
2. Added support for multi-person audio/video messaging.
3. Added support for login with owned/3rd-party account.

## AV_iOS_SDK1.0   5/11/2015

1. Added support for two-person audio/video messaging.
2. Added support for multi-person audio/video messaging.
3. Added support for login with owned/3rd-party account.

## AV_Windows C++_SDK1.0   5/11/2015

1. Added support for multi-person audio/video messaging.
2. Added support for login with owned/3rd-party account.


