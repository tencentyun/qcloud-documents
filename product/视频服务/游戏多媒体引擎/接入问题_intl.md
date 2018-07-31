## Overview

Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. To make it easier for developers to debug and integrate the APIs for GME, this document provides some FAQ on using the SDK. More FAQ will be provided on an ongoing basis.


## FAQ about Downloading and Modifying Demo 
#### Where should I download the GME Demo and SDK?
Please download them from [Tencent Cloud GME official website](https://intl.cloud.tencent.com/product/tmg?idx=1). The Unity Engine Demo, Cocos2D Engine Demo, Android Native Development Demo and iOS Native Development Demo are available on the official website.

#### After downloading the GEM Demo, can I change the account to the one I applied for?
1. Yes. You need to get two numbers from the console: sdkappid and permission key.
2. To use voice message, you need to get the TLS signature key. For more information on how to obtain the above numbers, please see [Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
3. To use your own appid in Voice Chat, you need to modify the key for Voice Chat in GetAuthBuffer in AVChatViewController.


#### I received the error message "errinfo=priv map info error" when using the Demo.
 If an error occurs with the parameter for entering a room, check whether the sdkappid and the permission key have been replaced.


## FAQ about SDK Features
#### Is armv8 available in Android's so library?
 It is not supported for now, and will be supported in later versions.


#### Calling poll function periodically is required for triggering events. Can I open a new thread to wake up it periodically and then call the poll function?
 Theoretically, our APIs need to be called in the same thread. If you choose to call them in a child thread, make sure to call them in the same child thread, especially for Init and Poll.

#### Why is Http Invalid id returned when a user enters a room?
 Although the parameter userid on the API is a string type, in fact we'll internally convert the string type to the uint64 type. If the conversion fails or the converted result is less than 10000, the entry to the room fails and Http Invalid id is returned.
If your account ID starts from 0, it is recommended to add 10000 to your account ID. For example, if your account ID is 999, the number entered is 10999.

#### Is there an API used to reclaim room IDs?
 No. After the last member exits the room, the room is terminated automatically.

#### Is there any requirement for the value of room ID?
 Only a 32-bit unsigned integer is allowed for roomid.

#### Is there any requirement for the value of openid?
 Only a 64-bit unsigned integer is allowed for openid. Please convert it into a string type before passing it to SDK.


#### Can the microphone volume be set before a user enters a room?
 No. The Voice Chat-related API ITMGAudioCtrl ITMGAudioEffectCtrl can only be called after a user enters the room.

#### Are the exitroom and enterroom operations asynchronous with each other? Can these two APIs be called at the same time?
 You need to call exitroom first, and then call enterroom after receiving a callback indicating exitroom operation is successful.


#### When is the notification of member status synchronization sent? Will the notification be sent when a user enters the room for the first time?
 Audio events are subject to a threshold above which a notification is sent. The notification will be sent when a user enters the room for the first time.

#### How do I get and release the microphone permission?
 You can get the microphone permission after calling the function EnterRoom successfully, and other programs cannot capture audio data from the microphone during your use of microphone.
Calling EnableMic(false) does not release the microphone.
If you really need to release the microphone, call PauseAudio, which can cause the engine to be paused entirely. To resume the use of microphone, call ResumeAudio.

#### When I used the SDK, I was unable to play music and the PC's sound card did not work after I logged in to the simulator.
 The simulator does not support mp3.

#### Does the SDK support playing sound from receiver?
 Tencent Mobile Gaming SDK does not support receiver.

#### What local audio file formats are supported by the SDK?
 Four formats are supported: m4a, AAC, wav, and mp3.




## FAQ about Getting Logs and Troubleshooting
#### How do I get the log?
 The file named QAVSDK_date.log is the log. It is located in the following directories depending on the operating system:

| Platform | Path |
| ------------- |-------------|
|Windows 	|%appdata%\Tencent\GME\ProcessName|
|iOS    		|Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents|
|Android	|/sdcard/Android/data/xxx.xxx.xxx/files|
|Mac    		|/Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents|

#### The main reasons for sound stutter
1. Stutter during music playback: The VJ plays music using speaker on a phone, and captures and broadcasts the audio data through another phone. (This can inevitably cause stutter. It is recommended for the VJ to use earphones).
2. Network stutter: The viewers will experience the stutter when the upstream packet loss rate is too high or the upstream delay fluctuates greatly.


















