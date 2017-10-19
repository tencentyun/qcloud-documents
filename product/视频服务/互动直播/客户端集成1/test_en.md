<table>
   <tr>
      <td>Module</td>
      <td>Sub-feature</td>
      <td></td>
      <td>Description/Notes</td>
      <td>PC</td>
      <td>iOS</td>
      <td>Android</td>
   </tr>
   <tr>
      <td>Room</td>
      <td>Room Operations</td>
      <td>Service-end and audio/video SDK-end rooms: Service-end room is maintained by the service end and has a uniqueness. For example, the service end can maintain by itself the room numbers, discussion group numbers, group numbers, game seat numbers, etc. Audio/video SDK-end room is maintained by the audio/video SDK end and also has a uniqueness. Such a room is dynamically assigned each time a user joins the room. You need to enter the service-end room number when joining an audio/video SDK-end room to establish a mapping between the rooms at both ends. In addition, the number of audio/video SDK-side room is visible to the service end, so you don't need to care about it.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Create a room</td>
      <td>Before the first member of a room joins the room, the room is automatically created at the audio/video backend. When subsequent members join the room, the creation process is eliminated.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Join the room</td>
      <td>Join the room.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Exit the room</td>
      <td>Exit the room.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Terminate the room</td>
      <td>When the last member has exited the room, the room is terminated automatically at audio/video backend.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Maximum number of room members</td>
      <td>50,000</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire the list of members sending voice/video</td>
      <td>"Version 1.2: supported.</td>
   </tr>
   <tr>
      <td>Version 1.3: supported."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire the list of all room members</td>
      <td>"Version 1.2: not supported.</td>
   </tr>
   <tr>
      <td>Version 1.3: supported when the number of room members is not more than 50; when the number exceeds 50, only the list of the first 50 members is returned."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Event notification</td>
      <td>Event notification of user joining the room</td>
      <td>Yes.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Event notification of others joining the room</td>
      <td>"Version 1.2: not supported.</td>
   </tr>
   <tr>
      <td>Version 1.3: supported when the number of room members is not more than 50; when the number exceeds 50, only the event notifications of the first 50 members joining the room are issued."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Event notification of user exiting the room</td>
      <td>Yes.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Event notification of others exiting the room</td>
      <td>"Version 1.2: not supported.</td>
   </tr>
   <tr>
      <td>Version 1.3: supported when the number of room members is not more than 50; when the number exceeds 50, only the event notifications of the first 50 members exiting the room are issued."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Event notification of status change about whether a member has sent audio/video</td>
      <td>Yes.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td>Room Members</td>
      <td>Send voice</td>
      <td></td>
      <td>Yes. A maximum of 6 members can send voice at the same time.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Send video</td>
      <td>Send video</td>
      <td>Yes. A maximum of 4 members can send videos at the same time.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Request for video images</td>
      <td></td>
      <td>"Request one person's/multiple persons' video images.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>A user can request the video images of a maximum of 4 members at the same time if the user does not join the broadcasting. If the user has joined the broadcasting, then only 3 other members can join the broadcasting, that is, the user can only request the video images of 3 members.</td>
   </tr>
   <tr>
      <td>Currently, the SDK only supports requesting multi-channel video images, but does not support rendering multi-channel video images. If you need to do so, you can do it at service end."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Cancel video images</td>
      <td></td>
      <td>Cancel the requested video images of a member or all members.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Accept voice</td>
      <td></td>
      <td>You can configure to receive the voice of a member, if he or she has sent voice. Voice from all members are accepted by default.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Reject voice</td>
      <td></td>
      <td>"You can choose to reject the voice from one or more members.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>This configuration only affects yourself. The members you reject can still send voice, and other members can still receive their voice."</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Modify your permissions dynamically</td>
      <td></td>
      <td>You can dynamically modify your permissions for upstream/downstream audio and video during chat to allow permission control and management by third-party.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire member status</td>
      <td></td>
      <td>Acquire member status. Current statuses include whether the member is sending voice, video and so on.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td>Voice Quality Control</td>
      <td>Set the audio encoding/decoding parameters</td>
      <td></td>
      <td>"The parameters include encoder/decoder type, sampling rate, number of channels, packet length and bitrate.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td> Configure these parameters using the Web configuration tool."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Audio data input and output</td>
      <td></td>
      <td>Acquire the audio data captured from local microphone.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>The audio data sent by the sender.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Acquire the audio data played from local speaker.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>The audio data received by the receiver.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Mix the audio data played locally with the additional audio data input and play the mixed audio on speaker.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Mix the audio data sent locally with the additional audio data input and send the mixed audio.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td>Video Quality Control</td>
      <td>Set video encoding/decoding parameters</td>
      <td></td>
      <td>"These parameters include encoder/decoder type, image width/height, frame rate, bitrate, maximum QP, minimum QP, GOP, sharpening switch, sharpening level and FEC switch. For more information about the value ranges of these parameters, please see the API documents.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. Configure these parameters using the Web configuration tool.</td>
   </tr>
   <tr>
      <td>. Maximum encoding/decoding resolution supported by different platforms are as follows:</td>
   </tr>
   <tr>
      <td>Windows     </td>
   </tr>
   <tr>
      <td>Encoding: 640*480 </td>
   </tr>
   <tr>
      <td>Decoding: 640*480</td>
   </tr>
   <tr>
      <td>Requirements:</td>
   </tr>
   <tr>
      <td> . Good network connection.</td>
   </tr>
   <tr>
      <td> . The encoding resolution needs to be set to 640*480 using the Web parameter configuration tool.</td>
   </tr>
   <tr>
      <td></td>
   </tr>
   <tr>
      <td>iOS</td>
   </tr>
   <tr>
      <td>Encoding: 640*480 </td>
   </tr>
   <tr>
      <td>Decoding: 640*480</td>
   </tr>
   <tr>
      <td>Requirements:</td>
   </tr>
   <tr>
      <td> . Good network connection.</td>
   </tr>
   <tr>
      <td> . For iPhone5S and above, encoding to 480*360 is supported.</td>
   </tr>
   <tr>
      <td></td>
   </tr>
   <tr>
      <td>Android </td>
   </tr>
   <tr>
      <td>Encoding: 640*480 </td>
   </tr>
   <tr>
      <td>Decoding: 640*480</td>
   </tr>
   <tr>
      <td>Requirements:</td>
   </tr>
   <tr>
      <td> . Good network connection.</td>
   </tr>
   <tr>
      <td> . For 4-core 2.6G CPU and above, encoding to 480*360 is supported."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td>Basic Audio Devices</td>
      <td>Microphone</td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire/ configure digital volume</td>
      <td>Digital volume refers to the digital signal value of App's audio data. To put it simply, digital value is the App volume, which is different from system volume. Adjusting digital volume means increasing/decreasing the digital signal value.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire dynamic volume</td>
      <td>Dynamic volume refers to the maximum audio signal value (peak) throughout the time period of each audio data frame. The service end can acquire the dynamic volume to draw the dynamic volume waveform.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Hot Plug Detection</td>
      <td>Hot Plug Detection. Perform Hot Plug Detection (HPD) on device during a chat and handle the problems found.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Speaker</td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire/configure volume</td>
      <td>Acquire/configure volume.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire dynamic volume</td>
      <td>Acquire dynamic volume.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Hot Plug Detection</td>
      <td>Hot Plug Detection. Perform Hot Plug Detection (HPD) on device during a chat and handle the problems found.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td>Advanced Audio Devices</td>
      <td>Remote room member audio device (virtual device)</td>
      <td>Enable</td>
      <td>"Enable the device.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. The backend supports sending 6 audio streams at most. If there are more than 6 audio streams, the backend will select 6 of them based on a certain strategy and forward them to the receiving members."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>External audio capturing device (virtual device)</td>
      <td>Note: External audio capturing device is a virtual device used to capture user's own audio, which then is sent to other room members through the SDK. The audio can come from any source, for example, the user's microphone or an audio file. Currently, only one external audio capturing device is supported.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Input audio stream</td>
      <td>"Input user's own audio streams based on business requirement and send them to other room members through the SDK. The audio can come from any source, for example, the user's microphone or an audio file.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. The input audio stream must comply with the conventions of SDK APIs. To be specific, the audio data format must be PCM, and the audio frames are transmitted at a frequency of one per 20 ms.</td>
   </tr>
   <tr>
      <td>. External audio capturing device and microphone are exclusive, that is, only one of them can be enabled at a time."</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Input mixed audio (virtual device)</td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire the mixed audio stream</td>
      <td>Audio mixing is about mixing audio sources from multiple channels into a single-channel audio source.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Add multiple devices to mix audio</td>
      <td>Add multiple audio devices as input sources and acquire their mixed audio streams. Currently, only a microphone and an accompaniment can be added.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Output mixed audio (virtual device)</td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire the unmixed audio streams</td>
      <td>The Output Mixed Audio feature can only acquire the unmixed audio streams, instead of the mixed audio streams. That is to say, audio mixing is not actually implemented.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Add remote members from multiple channels</td>
      <td>You can add the audios from remote members of one or more channels to acquire the unmixed audio streams.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td>Basic Video Devices</td>
      <td>Camera</td>
      <td>Enable</td>
      <td>Enable the device. It is not allowed to enable multiple devices of the same type at the same time. If you enable a device when another device of the same type is already enabled, the SDK will disable the enabled device by default.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Rendering</td>
      <td>"Render the camera video image.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. Currently, the rendering module supplied with SDK has very simple features, making it impossible to configure the rendered image (such as image size and position) as needed. If the business needs can't be met, it is recommended to implement the rendering at the service end."</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire system camera object</td>
      <td>The service end can implement camera zooming using the object.</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Image preprocessing</td>
      <td>"Camera video images can be preprocessed.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. User and other room members can view the effect of preprocessed video. The video sent by user and seen by room members is the preprocessed one.</td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td>Advanced Video Devices</td>
      <td>External video capturing device (virtual device)</td>
      <td>External video capturing device is a virtual device used to capture user's own video, which then is sent to other room members through the SDK. The video can come from any source, for example, the user's camera or a video file. Currently, only one external video capturing device is supported.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Input video stream</td>
      <td>"Input user's own video streams based on business requirement and send them to other room members through the SDK. The video can come from any source, for example, the user's camera or a video file.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>The input video stream must comply with the conventions of SDK APIs. To be specific, the video must be converted into image frames before input; only I420 is supported as the color format; the maximum video resolution is 640×480; image width and height must be multipliers of 4; recommended video frame rate is between 10-15. Furthermore, the SDK does not preprocess or render the input video streams.</td>
   </tr>
   <tr>
      <td>. External image capturing device and camera are exclusive, that is, only one of them can be enabled at a time."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Remote room member video device (virtual device)</td>
      <td>Note: Remote room member video device is a virtual device used to work with the video streams of remote members. Currently, only one remote room member video device is supported, which is shared by all the remote room members.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Enable</td>
      <td>Enable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Rendering</td>
      <td>"Render the video of remote member.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. Currently, the rendering module supplied with SDK has very simple features, making it impossible to configure the rendered image (such as image size and position) as needed. If the business needs can't be met, it is recommended to implement the rendering at the service end. The rendering modules provided by iOS and Android SDKs support multi-channel rendering (for Windows platform, the service end needs to acquire the video stream data and perform rendering on their own)."</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire video streams</td>
      <td>Acquire video streams of room members. You can acquire video streams of any member who has sent videos. The service end which needs to render videos on their own to meet business needs can use this feature to acquire the video streams.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Event notification of rendering of each video frame</td>
      <td>Event notification of rendering of each video frame. The service end can use this feature to improve UI and send user-friendly notifications via UI based on, for example, whether to send event notification, notification interval, and so on.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Local screen video device (virtual device)</td>
      <td>Enable</td>
      <td>"Enable the device.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. In the same room, only one member is allowed to enable local screen video device and send screen videos at a time. It is not until the member has disabled his/her local screen video device that another member can enable his/her local screen video device.</td>
   </tr>
   <tr>
      <td>The supported maximum encoding resolution of screen video is 1920*1200.</td>
   </tr>
   <tr>
      <td>For more information on considerations when using screen video device, please see API documentation."</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Rendering</td>
      <td>"Render video images.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. Currently, the rendering module supplied with SDK has very simple features, making it impossible to configure the rendered image (such as image size and position) as needed. If the business needs can't be met, it is recommended to implement the rendering at the service end."</td>
      <td>×</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Image preprocessing</td>
      <td>"The images captured from local screen can be preprocessed.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. User and other room members can view the effect of preprocessed video. The video sent by user and seen by room members is the preprocessed one.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Remote screen video device (virtual device)</td>
      <td>Enable</td>
      <td>"Enable the device.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>When terminals (especially those with low hardware configuration) receive, decode and render screen videos that have a high resolution (such as 1920*1200), user experience can be affected. Therefore, it is recommended to conduct an evaluation for this during actual use."</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Disable</td>
      <td>Disable the device.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire device information</td>
      <td>Acquire device information, such as ID, name, type, whether the device is enabled, etc.</td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Rendering</td>
      <td>"Render video images.</td>
   </tr>
   <tr>
      <td>Note:</td>
   </tr>
   <tr>
      <td>. Currently, the rendering module supplied with SDK has very simple features, making it impossible to configure the rendered image (such as image size and position) as needed. If the business needs can't be met, it is recommended to implement the rendering at the service end."</td>
      <td>×</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Acquire video streams</td>
      <td>Acquire video streams of room members. You can acquire video streams of any member who has sent videos. The service end which needs to render videos on their own to meet business needs can use this feature to acquire the video streams.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td>Device Management</td>
      <td>Acquire the number of input and output devices</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire the list of input and output devices</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire the number of enabled devices</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire the list of enabled devices</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire a device by device ID</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire the list of devices of a certain type</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>"    Availability check of microphone, speaker and camera before a chat"</td>
   </tr>
   <tr>
      <td> </td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>×</td>
      <td>×</td>
   </tr>
   <tr>
      <td></td>
      <td>Acquire the list of audio/video devices</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>×</td>
   </tr>
   <tr>
      <td>Others</td>
      <td>Recording</td>
      <td></td>
      <td>With cloud recording, Tencent Cloud VOD service and its APIs, features such as storage, transcoding and distribution can be implemented.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Non-interactive Broadcasting</td>
      <td></td>
      <td>Support non-interactive broadcasting which allows live broadcasting streaming based on HLS and RTMP when combined with Tencent Cloud LVB service.</td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Self-owned account system</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Open account system from a third party</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Log</td>
      <td>Log printing</td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Configure log storage directory</td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td>Log reporting</td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
      <td>Crash reporting</td>
      <td></td>
      <td></td>
      <td>√</td>
      <td>√</td>
      <td>√</td>
   </tr>
   <tr>
      <td></td>
   </tr>
</table>

