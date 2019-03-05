## SDK1.8.1
**1. Add**
- The aspect ratio 16:9 is now supported when capturing videos
- iOS8.0 and above support hardware codec.
- xPlatform is updated to the version that supports IPv6-Only.
- Uplink bitrate is added for audio 2s reporting.

**2. Modify**
- Aspect ratio for capturing videos is aligned with the aspect ratio in cloud configuration. You can switch between 4:3 and 16:9;
- Encoding effects for video softwares under VJ mode have been optimized.

**3. Fix**
- Issues regarding blurred screen, green screen, reversed playback in videos have been fixed;
- Issues regarding occasional inconsistency between display and sound have been fixed;
- Issues regarding video display being reduced/stretched on certain models have been fixed;
- Previously, when video is closed, audio is also stopped briefly. This issue has been fixed;
- When video bitrate is high, the actual bitrate is lower than the bitrate configured in the cloud. This issue has been fixed;
- In the VJ scenario, some of the audience can not hear the sound. This issue has been fixed;
- Issues regarding audio accompaniment memory not being released have been fixed;
- Several Crash issues have been fixed.

**4. API Changes**

(1) QAVAudioCtrl
- Added pauseAudio method which is used to stop the audio engine.
- Added resumeAudio method which is used to restart the audio engine.

(2) QAVRoom
- Modified getStatParam method which is used to change the API to getQualityParam.
- Added getStatisticsParam method which is used to acquire distribution and average value information of audios and videos without reference scores.

(3) QAVVideoCtrl
- Deleted setExternalCamAbility method which is used to modify the PC video flow control, and it is not required now.
- The enableBeauty method has been deleted. When you call the isEnableBeauty to determine if Beauty Filter is supported, you can directly call the inputBeautyparam API to pass parameters and enable Beauty Filter.

(4) QAVEndpoint 
- Added lastVideoStampRecv attribute which is used to acquire video frame receiving time stamps.
- Added lastVideoStampSend attribute which is used to acquire video frame sending time stamps.
- Deleted requestView method which is used to modify the requestViewList method.
- Deleted cancelView method which is used to modify the cancelAllView method.

## API Changes for SDK1.8.0 and 1.7
1. QAVAudioCtrl
	- Added audioDataDispose method which is used for audio data preprocessing callback;
	- Added enableHighQuality method which is used to enhance the call quality of broadcast mode in the VJ scenario.
2. QAVContext
 - Added getVersion method which is used to acquire the SDK version information.
3. QAVRoomDelegate
 - Added OnPrivilegeDiffNotify method which is used to show the exception notification caused by the room member who used the certain call capacity without relavant permission;
 - Added OnSemiAutoRecvCameraVideo method which is used to automatically receive camera video event notifications.
4. QAVRoomParam
 - Added videoRecvMode parameter which is used to control video receive mode.
5. QAVMultiRoom
 - Added ChangeAVControlRole method which is used to switch the user roles without re-joining the room.
6. QAVVideoCtrl
 - Added isEnableBeauty method which is used to query (externally) whether Beauty Filter is supported for the model;
 - Added OnLocalVideoPreProcess method which is used for local view preprocessing video callback.
7. QAVEndpoint 
 - Added lastAudioStampSend attribute which is used to acquire the uplink time stamp of current audio;
 - Added lastAudioStampRecv attribute which is used to acquire the downlink time stamp of current audio.                       
