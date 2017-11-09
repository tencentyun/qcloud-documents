### Version 2.0.3
- Android: Added UGC cropping/stitching features.
- Android: Optimized player and render views. Animation, floating window and big/small screen switching features become supported.
- Android: Added "Auto" option for software/hardware encoding. The SDK will automatically choose hardware or software encoding based on mobile phone performance.
- iOS: Optimized exposure mechanism to address overexposure problems. Exposure will look more natural.
- iOS & Android: Optimized bit rate control adaption for weak network environments and added two low push resolutions (180*320, 270*480).
- iOS & Android: Optimized directory and code structure for Demos, reducing interfacing cost. Added simple-to-use Demos for short video recording, cropping, stitching and joint broadcasting.

### Version 2.0.2
- iOS: Added UGC cropping/stitching features.
- iOS: Bitcode became supported by the simplified version.
- Android: Added eye enlargement/face slimming features for VIP version.
- Android: Optimized hardware coding and increased encoding quality.
- Android: Developed data APIs for player end. Hardware decoding data is provided in the form of Surface, while software decoding data is provided in the form of buffer.
- iOS & Android: Optimized front camera performance when image altering or green screen is enabled.
- iOS & Android: Optimized UGC upload protocols.

### Version 2.0.1
- iOS & Android: Optimized joint broadcasting. Multiple users may participate in joint broadcasting.
- iOS & Android: Users can now add background music to UGC short videos.
- iOS & Android: Added audio-only push feature.
- iOS & Android: Added screenshot feature for player end.
- iOS & Android: Updated FFMPEG library to secure version.
- iOS & Android: Optimized FLV, RTMP data packet resolution.
- Android: Added reverb feature and multiple preset reverb effects.
- Android: Added green screen feature for VIP version.
- iOS: Optimized software decoding performance. Data callback APIs became available for users and can be used to customize playback rendering.

### Version 2.0.0
- iOS & Android: Users can now collect and publish UGC short videos.
- iOS & Android: Added stream capture recording feature. Viewers can capture a portion of the LVB video they are viewing as UGC short video and share it.
- iOS: Added "whitening" filter, which is suitable for users who prefer beautify features.

### Version 1.9.2
- iOS & Android: Users can now play local files. (Configure PLAY_TYPE_LOCAL_VIDEO in startPlay)
- iOS & Android: Re-designed buffer solution for the player, optimizing audio fluency for low-delay linkages.
- iOS: Added setReverbType API, which is used to configure multiple audio reverb effects.
- iOS: Optimized performance when adding watermarks during LVB.

### Version 1.9.1
- iOS & Android: Optimized beauty filter effect and video quality during camera LVB.
- iOS & Android: Added beauty filter feature. VJs may use various filter effects.
- iOS & Android: Added setVideoQuality API, which can be used to choose video quality in a simpler manner.
- iOS: Addressed overexposure problem on iOS platform as reported by users. You will see bigger difference when there are strong artificial light sources.
- iOS: Further optimized microphone feedback delay. This is not completed due to bugs in the reverb feature. Release is delayed by one week.
See Update History for features in previous versions.

### Version 1.9.0
- iOS: Users can now enable Bitcode to reduce the size of AppStore installation packages;
- iOS: Software/hardware encoding and beauty filter feature now all use GPU acceleration solutions;
- iOS + Android: Optimized audio module. Users can now play background music in joint broadcasting scenarios;
- iOS + Android: Optimized multi-thread feature for VOD scenarios (multi-instance is already supported for LVB in the previous version)
- iOS + Android: Addressed problem where stopPlay will block the UI thread for a long time when the network stutters;
- iOS: Added microphone feedback feature. VJs can now hear their own voices in real time when singing with their earphones on;
- Android: This is currently not supported due to delay problems of system APIs. We will be working on this.

### Version 1.9.0
- iOS: Users can now enable Bitcode to reduce the size of AppStore installation packages;
- iOS: Software/hardware encoding and beauty filter feature now all use GPU acceleration solutions;
- iOS + Android: Optimized audio module. Users can now play background music in joint broadcasting scenarios;
- iOS + Android: Optimized multi-thread feature for VOD scenarios (multi-instance is already supported for LVB in the previous version)
- iOS + Android: Addressed problem where stopPlay will block the UI thread for a long time when the network stutters;
- iOS: Added microphone feedback feature. VJs can now hear their own voices in real time when singing with their earphones on;
- Android: This is currently not supported due to delay problems of system APIs. We will be working on this.

### Version 1.8.2
- Joint broadcasting can be achieved through Tencent Cloud accelerated linkages, while 1v1 server stream mixing is also supported (audio mixing is currently not supported in joint broadcasting scenarios. This is solved in 1.8.3)
- Multi-instance playback is supported for LVB (this is currently not supported for VOD);

### Version 1.8.1
- Addressed naming conflict problem for iOS;
- Multi-instance playback is supported for LVB on iOS and Android platforms (this is currently not supported for VOD);
- Optimized playback performance in weak network environments;
- Optimized audio mixing feature;

### Version 1.8.0
- Added simplified version for iOS, which includes LVB push and playback features;
- Optimized hardware decoding for Android, addressing Crash and ANR problems caused by multi-thread feature;
- Optimized dynamic bit rate adjustment feature, increasing adjustment accuracy;
- Added mirror APIs used for push;
- Optimized high-level collection for iOS;
- Optimized new beauty filter feature for Android. FPS control is now more accurate;
- Added progress callback API for audio mixing feature;
- SDK now supports HTTPS;

### Version 1.7.2
- Re-modeled video collection codes for Android;
- New beauty filter feature is now supported by software encoding on Android;
- Added cloud blacklist control for hardware encoding on Android;
- Addressed multi-thread problems which will occur when the camera is turned on and off frequently on Android;
- Added feature for pushing the VJ's audio when screen capping in privacy mode on Android;
- Addressed problems regarding blurred screens when switching between foreground/background, when playing HLS or MP4 videos in VOD scenarios on Android;
- Addressed problems regarding blurred screens during video playbacks in iOS simulators; 

### Version 1.7.1
- Fixed black screen problem which may occur during LVB on iOS;
- Fixed problem where compile would fail in iOS simulators;
- Fixed Crash problems on iOS where using physical key will sometimes cause screen lock or background switch;
- Fixed problems where the preview camera is inverted on certain Android models;
- Fixed problems where hardware encoding bit rate is too high on certain Android models;
- Optimized audio mixing APIs on Android, making them easier to use;

### Version 1.7.0
- Added ZoomIn and ZoomOut APIs for iOS and Android
- VOD now supports MPEG4 v3 decoding
- Added smart speed control mode, which will automatically adjust bit rate and resolution according to connection speed
- Fixed fast forward problems when recording HLS or MP4 videos, as well as various HLS/MP4 playback problems when the videos are recorded in exceptional modes
- Optimized video collection on iOS, completely eliminating problems such as flickering screen
- Optimized JNI on Android and fixed occasional callback failure problems

### Version 1.6.2
- Updated new beauty filter algorithm for iOS, significantly increasing performance and effect. (Only effective when hardware acceleration is enabled)
- Updated new beauty filter algorithm for Android and fixed problems where the algorithm is ineffective on certain models, while significantly increasing performance and effect. (Only effective for API 18 or above, and when hardware acceleration is enabled)
- replaykit screencap became supported for iOS SDK.
- Added Pause/Resume APIs for LVB playback which are used to pause or resume playback process.
- Addressed problem on Android where there will be no data after a long push process in hardware encoding mode.
- Addressed stream anomalies such as inconsistent audio/video, caused by jumping time stamps during long push processes.
- Addressed Crash problems caused by AAC decoding in certain scenarios.

### Version 1.6.1
- Added phone screencap feature for Android SDK. Users can now watch mobile game LVB (privacy mode is supported).
- Added background audio mixing feature. VJs may choose their favorite musics as background.
- Optimized push logic when switching App to background. We use video ad to address the problem where the viewer end will continue to reconnect (and disconnect in the end) when the VJ has switched the App to background;
- Enhanced video collection API customization features for users. Users may collect video data in different formats and provide the data to SDK;
- Added mute feature for VOD on iOS (suggestion from the mogujie team)
- Fixed flickering screen problems caused by incorrect releases of push playbacks

### Version 1.6.0
- Added fast audio data process feature in order to improve fast playback experience. Playback delay can be reduced without user's awareness;
- Added PUSH_WARNING_SERVER_DISCONNECT notification for situations where push is actively rejected by the backend;
- Addressed problem where black screen would occur when video is opened for the first time. Now OpenGL render layer is no longer presented before presenting the first frame;
- Added landscape screen push and local file playback features for iOS. See API Changes for how to use the features
- When App is switched to background, the RTMP push connection can now be maintained for a short time
- Introduced openGL conflict detection mechanism in order to prevent flickering screen on iOS, caused by player release issues;
- Optimized log performance and added external log callback APIs (the setLogLevel API does not affect the behaviors of log callback functions);

### Version 1.5.2
- Now HE-AAC V2 is supported by audio decoding;
- Users can now adjust the size of the VideoView in pushes and playbacks, as well as retain the last render frame;
- Optimized closest location access feature. The optimal path will be chosen automatically;
- Completely eliminated conflict issues when using Libyuv characters;
- Hardware encoding is now supported for top100 Android models;
- Addressed a bug regarding auto reconnection when the video stays still in hardware encoding mode;
- Addressed problem where StopPlay will become stuck for 2 seconds in VOD scenarios;
- Addressed a bug where the player end will keep reconnecting when the push end is switched to backend or the system fails to disconnect the network push

### Version 1.5.1
- Hardware acceleration is now supported when pushing on Android devices (we well be keep adding new models to the whitelist)
- Hardware decoding is now supported when playing MP4 or HLS videos in VOD scenarios
- Addressed conflict problems with LVB libraries
- Added reconnection mechanism for VOD scenarios

### Version 1.5.0
- Remodeled push SDK and player SDK to improve their stability
- Added GOP configuration parameters. It is recommended to configure it as 3 seconds (default) in ShowTime scenarios
- Addressed conflict problems with AVGSDK characters
- Fixed crash problems during push process in landscape screen mode

### Version 1.4.2
- Online VOD is now supported for MP4 and HLS videos
- aar is no longer used as the packaging method for Android SDK. This is changed to the traditional jar+lib method
- Added arm64 mode for Android SDK

### Version 1.4.1
- Improved push performance and audio encoding/decoding performance
- FLV VOD is now supported

### Version 1.3.1
- Improved playback performance
- Optimized cache policy and added various parameter configurations
- Watermark is now supported for the push end

### Version 1.2.1
- Optimized beauty filter and whitening effects
- Hardware decoding is now supported for iOS and Android platforms, while hardware encoding is now supported for iOS platform

### Version 1.1.1
- RTMP protocol, beauty filter/whitening, resolution configuration features are now supported by the push SDK
- FLV/RTMP protocol, image cropping, landscape/portrait screen switching features are now supported by the playback SDK



