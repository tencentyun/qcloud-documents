## Main Features

### Video Messaging

Support up to 720P high-definition video. With optimized cloud traffic control strategy, we ensure high quality video messaging experience.

### Audio Messaging

Support to receive up to 6 audio channels simultaneously. The service is of excellent quality both on narrow-band and broadband networks.

### Cross-platform Interconnection

Support broadcasting and playback across Android, iOS, PC and mainstream web platforms. Our one-to-many and many-to-many ILVB services are suitable for many application scenarios such as video socialization, online education and remote medical services.

### Non-Interactive Broadcasting

With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.

### PC Desktop Sharing

Support sharing the whole screen or a specific region of the screen in HD mode (1920×1200) or SD mode (960×720).

### SPEAR Cloud Configuration

Based on their application scenario, users can create independent audio, video and network parameter configurations for different platforms and roles, and flexibly customize their traffic control strategy. They can also use default strategies for instant messaging and ILVB, etc.

### Cloud Recording

With our cloud recording feature, Tencent Cloud VOD service and its comprehensive APIs, you can implement features such as record storage, transcoding and distribution.


## Basic Features

### ILVB Windows C++/iOS/Android SDK

<table style="display:table;width:100%;">
	<tbody>
		<tr>
			<th rowspan="2">Module</th>
			<th colspan="2" rowspan="2" style="width: 123px;">Sub-function</th>
			<th rowspan="2" style="width: 200px;">Detailed description/Notes</th>
			<th colspan="3" style="width: 180px;">Supported</th>
		</tr>
		<tr>
			<th style="width: 25px;">PC</th>
			<th style="width: 25px;">iOS</th>
			<th style="width: 150px;">Android</th>
		</tr>
		<tr>
			<td rowspan="13" style="text-align:center">Room</td>
			<td rowspan="8" style="text-align: center; width: 56px;">Room Operations</td>
			<td colspan="2" style="text-align: center; width: 300px;">Service-end room and audio/video-SDK-end room: Service-end rooms are maintained by the client and have a uniqueness. For example, the client can maintain by itself the room numbers, discussion group numbers, group numbers, game seat numbers, etc. Audio/video SDK-end rooms are maintained by the audio/video SDK end and also have a uniqueness. Such a room is dynamically assigned each time a user joins the room. You need to enter the service-end room number when joining an audio/video SDK-end room to establish a mapping between the both rooms. In addition, the numbers of audio/video SDK-end rooms are visible to the client, so you don't need to care about them.</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Create room</td>
			<td style="text-align: center; width: 382px;">Before the first member of a room joins the room, the room is automatically created at the audio/video backend. When subsequent members join the room, the creation process is eliminated.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Join a room</td>
			<td style="text-align: center; width: 382px;">Join a room.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Exit a room</td>
			<td style="text-align: center; width: 382px;">Exit a room.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Terminate a room</td>
			<td style="text-align: center; width: 382px;">When the last member has exited the room, the room is terminated automatically at audio/video backend.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Maximum number of room members</td>
			<td style="text-align: center; width: 382px;">50,000</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Obtain the list of members sending voice/video</td>
			<td style="text-align: center; width: 382px;">Version 1.2: supported.<br />
			Version 1.3 or above: supported.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Obtain the member list of all rooms</td>
			<td style="text-align: center; width: 382px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, only the first 50 members are returned in the list.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">Event Notification</td>
			<td style="text-align: center; width: 65px;">Event notification of you joining the room</td>
			<td style="text-align: center; width: 382px;">Supported.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Event notification of others joining the room</td>
			<td style="text-align: center; width: 382px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, you'll receive only the notifications of the first 50 members' joining the room.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Event notification of you exiting the room</td>
			<td style="text-align: center; width: 382px;">Supported.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Event notification of others exiting the room</td>
			<td style="text-align: center; width: 382px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, you'll receive only the notifications of the first 50 members' exiting the room .</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Event notification of status change about whether a member has sent a voice/video</td>
			<td style="text-align: center; width: 382px;">Supported.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">Room Members</td>
			<td colspan="2" style="text-align: center; width: 123px;">Send Voice</td>
			<td style="text-align: center; width: 382px;">Supported. Up to 6 members can send audio at the same time.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Send Video</td>
			<td style="text-align: center; width: 382px;">Supported. Up to 4 members can send videos captured by cameras or external capture devices simultaneously. On Windows, an additional member, regardless of whether he/she is one of the aforementioned 4 members or not, can send screen video. In other words, on Windows, sending up to 4 camera/external capture device videos and 1 screen video are supported.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Request Screen Display</td>
			<td style="text-align: center; width: 382px;">Request user(s)' video data from cameras/external capture devices/screen capture.<br />
			Note:<br />
			Up to 4 camera/external capture device videos and 1 screen video can be requested simultaneously. If the client is sending video data itself, the remaining number of members that can still send video data decreases accordingly. Similarly, the number of video the client itself can request decreases accordingly.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Cancel Display</td>
			<td style="text-align: center; width: 382px;">Cancel the requested display for a certain member or all members.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Accept Voice</td>
			<td style="text-align: center; width: 382px;">You can configure to receive the voices of a certain member (on condition that he or she has sent voices before). Voices from all members are accepted by default.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Reject Voice</td>
			<td style="text-align: center; width: 382px;">You can choose to reject the voices from one or more members.<br />
			Note:<br />
			This configuration only affects yourself. The members you rejected can still send voices, and other members can still receive their voices as usual.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 56px;">　</td>
			<td style="text-align: center; width: 65px;">Modify Your Permissions Dynamically</td>
			<td style="text-align: center; width: 382px;">You can dynamically modify your uplink/downlink audio and video permissions during chat to achieve permission control and management from third-party aspect.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire Member Status</td>
			<td style="text-align: center; width: 382px;">Acquire member status. Current statuses include whether the member is sending voice, whether the member is sending video and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="7" style="text-align:center">Voice Quality Control</td>
			<td colspan="2" style="text-align: center; width: 123px;">Audio Stream-control Parameters</td>
			<td style="text-align: center; width: 382px;">The parameters include encoder/decoder type, sample rate, number of channels, packet length and bitrate.<br />
			Note:<br />
			Configure these parameters by Web stream-control configuration system.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="6" style="text-align: center; width: 123px;">Audio data input and output</td>
			<td style="text-align: center; width: 382px;">Capture audio data from local microphones.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">The audio data that are eventually sent by the senders.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">Capture audio data from local speakers.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">The audio data received by the receivers.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">Mix local playing audio with additional input audio data to play on speakers.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">Mix local sending audio with additional input audio data for sending.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align:center">Video Quality Control</td>
			<td colspan="2" style="text-align: center; width: 123px;">Video Stream-control Parameters</td>
			<td style="text-align: center; width: 382px;">These parameters include encoder/decoder type, image width/height, frame rate, bitrate, maximum QP, minimum QP, GOP, sharpening switch, sharpening level and FEC switch.<br />
			Note:<br />
			Configure these parameters through the Web stream-control configuration system. For details on supported parameters, please see the pages of the system.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="11" style="text-align:center">Basic Audio Devices</td>
			<td rowspan="6" style="text-align: center; width: 56px;">Microphone</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire/Configure Digital Volume</td>
			<td style="text-align: center; width: 382px;">Digital volume refers to the digital signal value of App's audio data. To put it simple, digital value is the App volume, which is different from system volume. Adjusting digital volume means to increase/decrease the digital signal value.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Dynamic Volume</td>
			<td style="text-align: center; width: 382px;">Dynamic volume refers to the maximum audio signal value (peak value) among the entire time period of each frame in the audio data. The client can acquire the dynamic volume in order to draw the dynamic volume waveform.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Hot Plug Detection</td>
			<td style="text-align: center; width: 382px;">Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 56px;">Speaker</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire/Configure Volume</td>
			<td style="text-align: center; width: 382px;">Acquire/configure volume.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Dynamic Volume</td>
			<td style="text-align: center; width: 382px;">Acquire dynamic volume.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align:center">　</td>
			<td style="text-align: center; width: 65px;">Hot Plug Detection</td>
			<td style="text-align: center; width: 382px;">Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align:center">Advanced Audio Devices</td>
			<td rowspan="3" style="text-align: center; width: 56px;">Remote Room Member Voice Device (Virtual Device)</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.<br />
			Note:<br />
			The backend supports sending voices in 6 channels at most. If there are more than 6 channels, the backend will select 6 of them based on a certain strategy and forward them to the receiving members.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align:center">Basic Video Devices</td>
			<td rowspan="6" style="text-align: center; width: 56px;">Camera</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device. It is not allowed to enable multiple devices of the same type at the same time (if they exist). When you enable a device when another device of the same type is already enabled, the SDK will disable that device by default.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Render</td>
			<td style="text-align: center; width: 382px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire System Camera Object</td>
			<td style="text-align: center; width: 382px;">You can implement camera zooming by using this object.</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Image Preprocess</td>
			<td style="text-align: center; width: 382px;">You can preprocess camera video images.<br />
			Note:<br />
			Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td rowspan="21" style="text-align:center">Advanced Video Devices</td>
			<td rowspan="5" style="text-align: center; width: 56px;">External Video Capturing Device (Virtual Device)</td>
			<td colspan="2" style="text-align: center; width: 448px;">External video capturing device is a virtual device which is used for users to capture their own videos and send the videos to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file. Currently, only one external video capturing device is supported.</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Input Video Stream</td>
			<td style="text-align: center; width: 382px;">Input your own video streams based on business requirement and send them to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file.<br />
			Note:<br />
			The input video stream must comply with the conventions of SDK APIs. To be specific, the video must be converted into individual image frames to be passed in; the only supported color format now is I420; the largest video resolution is 640×480; image width and height must be multipliers of 4; optimal video frame rate is between 10-15. Furthermore, the SDK does not preprocess or render the input video stream.<br />
			External image capturing device and camera device are exclusive, that is, only one of them can be enabled at a time.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 56px;">Remote Room Member Video Device (Virtual Device)</td>
			<td colspan="2" style="text-align: center; width: 448px;">Remote room member video device is a virtual device used to operate the video stream of remote member. Currently, only one remote room member video device is supported, which is shared by remote room members.</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Render</td>
			<td style="text-align: center; width: 382px;">Render the video of remote member.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to implement the rendering from the client. The rendering modules provided by iOS and Android SDKs now support multi-channel rendering (for Windows platform, the client needs to acquire video stream data and perform rendering on their own).</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Video Stream</td>
			<td style="text-align: center; width: 382px;">Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">Local Screen Video Device (Virtual Device)</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.<br />
			Note:<br />
			Only one member can enable local screen video device and send screen videos at the same time, in the same room. The other people need to wait for the current user to disable the local screen video device before enabling it.<br />
			The highest encoding definition supported by the screen video display is 1920*1200.<br />
			For more information on things to note when using screen video device, please refer to API documentation.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Render</td>
			<td style="text-align: center; width: 382px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Image Preprocess</td>
			<td style="text-align: center; width: 382px;">Preprocess the images captured by the local screen.<br />
			Note:<br />
			Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">Remote Screen Video Device (Virtual Device)</td>
			<td style="text-align: center; width: 65px;">Enable</td>
			<td style="text-align: center; width: 382px;">Enable the device.<br />
			Note:<br />
			Since screen video displays usually have high definition (such as 1920*1200), user experience can be affected if devices (especially devices with low hardware configuration) receive and decode such images. Thus evaluation is recommended during actual use.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Disable</td>
			<td style="text-align: center; width: 382px;">Disable the device.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Device Information</td>
			<td style="text-align: center; width: 382px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Render</td>
			<td style="text-align: center; width: 382px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Acquire Video Stream</td>
			<td style="text-align: center; width: 382px;">Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">Device Management</td>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the Number of Input and Output Devices</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the List of Input and Output Devices</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the Number of Enabled Devices</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the List of Enabled Devices</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire Device by Device ID</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the List of Devices of a Certain Type</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Availability Check of <br />
			Microphones, Speakers and Cameras Before Messaging</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Acquire the List of Voice/Video Devices</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">×</td>
			<td style="text-align: center; width: 206px;">×</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">Others</td>
			<td colspan="2" style="text-align: center; width: 123px;">Recording</td>
			<td style="text-align: center; width: 382px;">With our cloud recording feature, Tencent Cloud VOD service and its comprehensive APIs, you can implement features such as record storage, transcoding and distribution.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Non-interactive Broadcasting</td>
			<td style="text-align: center; width: 382px;">With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Owned Account System</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Open Account System from Third Party</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 56px;">Log</td>
			<td style="text-align: center; width: 65px;">Print Log</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Configure Log Storage Directory</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">Report Log</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">Report Crash</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 25px;">√</td>
			<td style="text-align: center; width: 206px;">√</td>
		</tr>
	</tbody>
</table>


Interactive LVB Web SDK

<table style="display:table;width:100%;">
	<tbody>
		<tr>
			<th rowspan="2" style="width: 18px;">Module</th>
			<th colspan="2" rowspan="2" style="width: 116px;">Sub-function</th>
			<th rowspan="2" style="width: 307px;">Detailed description/Notes</th>
			<th colspan="3" style="width: 146px;">Supported</th>
		</tr>
		<tr>
			<th style="width: 42px;">PC</th>
			<th style="width: 49px;">iOS</th>
			<th style="width: 58px;">Android</th>
		</tr>
		<tr>
			<td rowspan="13" style="text-align: center; width: 18px;">Room</td>
			<td rowspan="8" style="text-align: center; width: 49px;">Room Operations</td>
			<td colspan="2" style="text-align: center; width: 376px;">Service-end room and audio/video-SDK-end room: Service-end rooms are maintained by the client and have a uniqueness. For example, the client can maintain by itself the room numbers, discussion group numbers, group numbers, game seat numbers, etc. Audio/video SDK-end rooms are maintained by the audio/video SDK end and also have a uniqueness. Such a room is dynamically assigned each time a user joins the room. You need to enter the service-end room number when joining an audio/video SDK-end room to establish a mapping between the both rooms. In addition, the numbers of audio/video SDK-end rooms are visible to the client, so you don't need to care about them.</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Create room</td>
			<td style="text-align: center; width: 307px;">Before the first member of a room joins the room, the room is automatically created at the audio/video backend. When subsequent members join the room, the creation process is eliminated.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Join the room</td>
			<td style="text-align: center; width: 307px;">Join the room.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Exit the room</td>
			<td style="text-align: center; width: 307px;">Exit the room.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Terminate the room</td>
			<td style="text-align: center; width: 307px;">When the last member has exited the room, the room is terminated automatically at audio/video backend.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Maximum number of room members</td>
			<td style="text-align: center; width: 307px;">50,000</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Obtain the list of members sending voice/video</td>
			<td style="text-align: center; width: 307px;">Version 1.2: supported.<br />
			Version 1.3 or above: supported.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Obtain the member list of all rooms</td>
			<td style="text-align: center; width: 307px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, only the first 50 members are returned in the list.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">Event Notification</td>
			<td style="text-align: center; width: 67px;">Event notification of you joining the room</td>
			<td style="text-align: center; width: 307px;">Supported.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Event notification of others joining the room</td>
			<td style="text-align: center; width: 307px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, you'll receive only the notifications of the first 50 members' joining the room.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Event notification of you exiting the room</td>
			<td style="text-align: center; width: 307px;">Supported.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Event notification of others exiting the room</td>
			<td style="text-align: center; width: 307px;">Version 1.2: not supported.<br />
			Version 1.3 or above: fully supported when there are fewer than 50 room members; otherwise, you'll receive only the notifications of the first 50 members' exiting the room .</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Event notification of status change about whether a member has sent a voice/video</td>
			<td style="text-align: center; width: 307px;">Supported.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">Room Members</td>
			<td colspan="2" style="text-align: center; width: 116px;">Send Voice</td>
			<td style="text-align: center; width: 307px;">Supported. Up to 6 members can send audio at the same time.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Send Video</td>
			<td style="text-align: center; width: 307px;">Supported. Up to 4 members can send videos captured by cameras or external capture devices simultaneously. On Windows, an additional member, regardless of whether he/she is one of the aforementioned 4 members or not, can send screen video. In other words, on Windows, sending up to 4 camera/external capture device videos and 1 screen video are supported.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Request Screen Display</td>
			<td style="text-align: center; width: 307px;">Request user(s)' video data from cameras/external capture devices/screen capture.<br />
			Note:<br />
			Up to 4 camera/external capture device videos and 1 screen video can be requested simultaneously. If the client is sending video data itself, the remaining number of members that can still send video data decreases accordingly. Similarly, the number of video the client itself can request decreases accordingly.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Cancel Display</td>
			<td style="text-align: center; width: 307px;">Cancel the requested display for a certain member or all members.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Accept Voice</td>
			<td style="text-align: center; width: 307px;">You can configure to receive the voices of a certain member (on condition that he or she has sent voices before). Voices from all members are accepted by default.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Reject Voice</td>
			<td style="text-align: center; width: 307px;">You can choose to reject the voices from one or more members.<br />
			Note:<br />
			This configuration only affects yourself. The members you rejected can still send voices, and other members can still receive their voices as usual.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 49px;">　</td>
			<td style="text-align: center; width: 67px;">Modify Your Permissions Dynamically</td>
			<td style="text-align: center; width: 307px;">You can dynamically modify your uplink/downlink audio and video permissions during chat to achieve permission control and management from third-party aspect.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire Member Status</td>
			<td style="text-align: center; width: 307px;">Acquire member status. Current statuses include whether the member is sending voice, whether the member is sending video and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="7" style="text-align: center; width: 18px;">Voice Quality Control</td>
			<td colspan="2" style="text-align: center; width: 116px;">Audio Stream-control Parameters</td>
			<td style="text-align: center; width: 307px;">The parameters include encoder/decoder type, sample rate, number of channels, packet length and bitrate.<br />
			Note:<br />
			Configure these parameters by Web stream-control configuration system.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="6" style="text-align: center; width: 116px;">Audio data input and output</td>
			<td style="text-align: center; width: 307px;">Capture audio data from local microphones.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">The audio data that are eventually sent by the senders.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">Capture audio data from local speakers.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">The audio data received by the receivers.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">Mix local playing audio with additional input audio data to play on speakers.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">Mix local sending audio with additional input audio data for sending.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 18px;">Video Quality Control</td>
			<td colspan="2" style="text-align: center; width: 116px;">Video Stream-control Parameters</td>
			<td style="text-align: center; width: 307px;">These parameters include encoder/decoder type, image width/height, frame rate, bitrate, maximum QP, minimum QP, GOP, sharpening switch, sharpening level and FEC switch.<br />
			Note:<br />
			Configure these parameters through the Web stream-control configuration system. For details on supported parameters, please see the pages of the system.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="11" style="text-align: center; width: 18px;">Basic Audio Devices</td>
			<td rowspan="6" style="text-align: center; width: 49px;">Microphone</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire/Configure Digital Volume</td>
			<td style="text-align: center; width: 307px;">Digital volume refers to the digital signal value of App's audio data. To put it simple, digital value is the App volume, which is different from system volume. Adjusting digital volume means to increase/decrease the digital signal value.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Dynamic Volume</td>
			<td style="text-align: center; width: 307px;">Dynamic volume refers to the maximum audio signal value (peak value) among the entire time period of each frame in the audio data. The client can acquire the dynamic volume in order to draw the dynamic volume waveform.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Hot Plug Detection</td>
			<td style="text-align: center; width: 307px;">Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 49px;">Speaker</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire/Configure Volume</td>
			<td style="text-align: center; width: 307px;">Acquire/configure volume.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Dynamic Volume</td>
			<td style="text-align: center; width: 307px;">Acquire dynamic volume.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 18px;">　</td>
			<td style="text-align: center; width: 67px;">Hot Plug Detection</td>
			<td style="text-align: center; width: 307px;">Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 18px;">Advanced Audio Devices</td>
			<td rowspan="3" style="text-align: center; width: 49px;">Remote Room Member Voice Device (Virtual Device)</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.<br />
			Note:<br />
			The backend supports sending voices in 6 channels at most. If there are more than 6 channels, the backend will select 6 of them based on a certain strategy and forward them to the receiving members.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 18px;">Basic Video Devices</td>
			<td rowspan="6" style="text-align: center; width: 49px;">Camera</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device. It is not allowed to enable multiple devices of the same type at the same time (if they exist). When you enable a device when another device of the same type is already enabled, the SDK will disable that device by default.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Render</td>
			<td style="text-align: center; width: 307px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 42px;">×</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire System Camera Object</td>
			<td style="text-align: center; width: 307px;">You can implement camera zooming by using this object.</td>
			<td style="text-align: center; width: 42px;">×</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Image Preprocess</td>
			<td style="text-align: center; width: 307px;">You can preprocess camera video images.<br />
			Note:<br />
			Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td rowspan="21" style="text-align: center; width: 18px;">Advanced Video Devices</td>
			<td rowspan="5" style="text-align: center; width: 49px;">External Video Capturing Device (Virtual Device)</td>
			<td colspan="2" style="text-align: center; width: 376px;">External video capturing device is a virtual device which is used for users to capture their own videos and send the videos to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file. Currently, only one external video capturing device is supported.</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Input Video Stream</td>
			<td style="text-align: center; width: 307px;">Input your own video streams based on business requirement and send them to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file.<br />
			Note:<br />
			The input video stream must comply with the conventions of SDK APIs. To be specific, the video must be converted into individual image frames to be passed in; the only supported color format now is I420; the largest video resolution is 640×480; image width and height must be multipliers of 4; optimal video frame rate is between 10-15. Furthermore, the SDK does not preprocess or render the input video stream.<br />
			External image capturing device and camera device are exclusive, that is, only one of them can be enabled at a time.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 49px;">Remote Room Member Video Device (Virtual Device)</td>
			<td colspan="2" style="text-align: center; width: 376px;">Remote room member video device is a virtual device used to operate the video stream of remote member. Currently, only one remote room member video device is supported, which is shared by remote room members.</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Render</td>
			<td style="text-align: center; width: 307px;">Render the video of remote member.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to implement the rendering from the client. The rendering modules provided by iOS and Android SDKs now support multi-channel rendering (for Windows platform, the client needs to acquire video stream data and perform rendering on their own).</td>
			<td style="text-align: center; width: 42px;">×</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Video Stream</td>
			<td style="text-align: center; width: 307px;">Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">Local Screen Video Device (Virtual Device)</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.<br />
			Note:<br />
			Only one member can enable local screen video device and send screen videos at the same time, in the same room. The other people need to wait for the current user to disable the local screen video device before enabling it.<br />
			The highest encoding definition supported by the screen video display is 1920*1200.<br />
			For more information on things to note when using screen video device, please refer to API documentation.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Render</td>
			<td style="text-align: center; width: 307px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 42px;">×</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Image Preprocess</td>
			<td style="text-align: center; width: 307px;">Preprocess the images captured by the local screen.<br />
			Note:<br />
			Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">Remote Screen Video Device (Virtual Device)</td>
			<td style="text-align: center; width: 67px;">Enable</td>
			<td style="text-align: center; width: 307px;">Enable the device.<br />
			Note:<br />
			Since screen video displays usually have high definition (such as 1920*1200), user experience can be affected if devices (especially devices with low hardware configuration) receive and decode such images. Thus evaluation is recommended during actual use.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Disable</td>
			<td style="text-align: center; width: 307px;">Disable the device.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Device Information</td>
			<td style="text-align: center; width: 307px;">Acquire device information, such as ID, name, type, whether the device is enabled and so on.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Render</td>
			<td style="text-align: center; width: 307px;">Render video frames.<br />
			Note:<br />
			The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.</td>
			<td style="text-align: center; width: 42px;">×</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Acquire Video Stream</td>
			<td style="text-align: center; width: 307px;">Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">Device Management</td>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the Number of Input and Output Devices</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the List of Input and Output Devices</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the Number of Enabled Devices</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the List of Enabled Devices</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire Device by Device ID</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the List of Devices of a Certain Type</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Availability Check of<br />
			Microphones, Speakers and Cameras Before Messaging</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Acquire the List of Voice/Video Devices</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">×</td>
			<td style="text-align: center; width: 58px;">×</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">Others</td>
			<td colspan="2" style="text-align: center; width: 116px;">Recording</td>
			<td style="text-align: center; width: 307px;">With our cloud recording feature, Tencent Cloud VOD service and its comprehensive APIs, you can implement features such as record storage, transcoding and distribution.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Non-interactive Broadcasting</td>
			<td style="text-align: center; width: 307px;">With our non-interactive broadcasting feature and Tencent Cloud's LVB service, you can implement the distribution of LVB by HLS and RTMP.</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Owned Account System</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Open Account System from Third Party</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 49px;">Log</td>
			<td style="text-align: center; width: 67px;">Print Log</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Configure Log Storage Directory</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">Report Log</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">Report Crash</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">√</td>
			<td style="text-align: center; width: 49px;">√</td>
			<td style="text-align: center; width: 58px;">√</td>
		</tr>
	</tbody>
</table>



