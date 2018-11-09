## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides FAQs about Game Multimedia Engine (GME) SDK to make it easier for developers to debug and integrate the APIs of GME. The following are FAQs and common concepts about GME. This document will be updated with more FAQs from time to time.

## General FAQs

### What features are supported by GME?

GME supports real-time voice chat, voice message and voice-to-text converting.

### What game scenarios does GME apply to?

E-sports, commander games, casual games, Werewolf, etc.

### Which game engines and platforms are supported by GME?

GME supports Unity, Unreal and Cocos2d engines, and Windows, Mac, iOS and Android platforms.

### How do I get started with GME?

[Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782) will guide you through the initial integration of GME before you can use the engine.

### Is armv8 available in Android's so library?

It is not supported for now, and will be supported in later versions.

### How do I ensure the security of authentication?

It is recommended to deploy authentication feature on the client at the early stage, and later deploy it at the game App backend.

| Solution | Advantage | Disadvantage |
| ---------- | -------- | ---------------- |
| Deployment at backend | Higher security	| Joint testing by backend developers is required |
| Deployment on client | Quick integration | Lower security |

### What should I do for the authentication failure?
When the authentication failure happens, check if the voice service on the console is enabled. If it is enabled, please check the following, 
1. If sdkappid is the same as that of the console.
2. OpenID only support Int64 type(convert to string), it must be greater than 10000. 
3. The room ID parameter for voice message must be set to "null".
4. If the permission key match the one from Tencent Cloud console.  


## FAQs about Downloading and Modifying sample code

### Where should I download the GME sample code and SDK?

Please download applicable sample code and SDK from [Downloading Instructions](https://intl.cloud.tencent.com/document/product/607/18521). The sample code for Unity Engine, Cocos2D Engine, sample Android native App and iOS native App are available on the official website.

### After downloading the GEM sample code, can I change the account to the one I applied for?

1. Yes. You need to get two numbers from the console: sdkappid and permission key.
2. To use voice message, you need to get the TLS signature key. For more information on how to obtain the above numbers, see [Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
3. To use your own appid in Voice Chat, you need to modify the key for voice chat in GetAuthBuffer in AVChatViewController.

### I received the error message "errinfo=priv map info error" when using the Demo.

If an error occurs with the parameter for entering a room, check whether the sdkappid and the permission key have been replaced.



## Billing-Related FAQs

### What are the billing methods for the voice chat service of GME? How do I select the billing method?

The voice chat service of GME supports two billing methods: Bill by DAU and Bill by Usage Duration. The billing method cannot be modified once being selected. For detailed price information, see [Purchase Guide](https://intl.cloud.tencent.com/document/product/607/17808).
If you select Bill by DAU, the validity of a voice chat room is 90 minutes. When the validity expires, the system closes the room automatically. This billing method is recommended for PVP and casual games.
If you select Bill by Duration, no limit is imposed on the validity of room. This billing method is recommended for social, VJ and team speak game scenarios.

### What will happen when a room's 90-minute validity expires if I select Bill by DAU?

When the 90-minute validity expires, the room will be closed and you will receive a callback function.

### How is the DAU for GME voice chat calculated?

When a user in the App enters the room, he/she is counted as a DAU for voice chat. The DAU is calculated by UserId on a de-duplication basis (A UserId is the unique identifier of a user in the App).

### When does the billable duration of voice chat service in GME begin?

The billable duration begins at the moment when a user in the App enters the room.

### What are the billing methods for GME's voice message and voice-to-text services? How do I select the billing method?

Voice message and voice-to-text services are billed by voice message DAU. For detailed price information, see [Purchase Guide](https://intl.cloud.tencent.com/document/product/607/17808).

### How is the DAU for GME's voice message and voice-to-text services calculated?

When a user in the App sends a voice message, he/she is counted as a DAU for voice message. The DAU is calculated by UserId on a de-duplication basis (A UserId is the unique identifier of a user in the App).



## FAQs About Voice Chat

### What game scenarios does the voice chat service support?

The following three scenarios are supported:
**Speak-in-sequence:** Users take turns to speak. This mode allows a high sound quality and fluency and is suitable for such scenarios as Werewolf.
**Free Chat:** Multiple people can speak at the same time. This mode has a very low delay and is suitable for competitive game scenarios such as multiplayer team speak.
**Command:** Suitable for one-to-many commanding, audio interaction with VJ and other scenarios in large-scale commander games.

### How do I choose the audio type that suits me?

As shown below, the audio type you select varies with different application scenarios.

| Audio Type | Description | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| -------------------------- | -------- | ---- | -------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| ITMG_ROOM_TYPE_FLUENCY     |Fluent	| 1    |Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | Fluent sound quality and ultra-low delay which is suitable for team speak scenarios in games like FPS and MOBA. |
| ITMG_ROOM_TYPE_STANDARD    |Standard	| 2    |Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality	| Good sound quality and medium delay which is suitable for voice chat scenarios in casual games like Werewolf and board games.	|
| ITMG_ROOM_TYPE_HIGHQUALITY |HD	| 3    |Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| Super-high sound quality and relative high delay which is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

Please select a sampling rate (16k or 48k) in the console based on the actual application scenario. In the integration process, you can change the audio type by using APIs, but the sampling rate you use will not exceed the sampling rate selected in the console. For example, if you select a sampling rate of 16k on the console and the audio type is changed to HD on the client, the sampling rate is still 16k; If you select a sampling rate of 48k on the console and the audio type is changed to Fluent on the client, the sampling rate is 16k.



### Calling poll function periodically is required for triggering events. Can I open a new thread to wake up it periodically and then call the poll function?

Theoretically, all of our APIs need to be called in the same thread. If you choose to call them in a child thread, make sure to call them in the same child thread, especially for Init and Poll.

### How frequent should I call the poll function?

Call the poll function as described in the sample code if there is no special requirement.

### Is there a limit on the number of voice chat rooms and the number of members in a room?

There is no limit on the number of voice chat rooms and the number of users in a room.

### Why is Http Invalid id returned when a user enters a room?

Although the parameter userid on the API is a string type, in fact we'll internally convert the string type to the uint64 type. If the conversion fails or the converted result is less than 10000, the entry to the room fails and Http Invalid id is returned.
If your account ID starts from 0, it is recommended to add 10000 to your account ID. For example, if your account ID is 999, the number entered is 10999.

### Is there an API used to reclaim room IDs?

No. After the last member exits the room, the room is terminated automatically.

### Is there a requirement for the value of room ID?

Only a 32-bit unsigned integer is allowed for roomid. Convert it into a string type before passing it to SDK.

### Is there a requirement for the value of openid?

Only a 64-bit unsigned integer is allowed for openid. Convert it into a string type before passing it to SDK.

### Can I enter multiple rooms at the same time using a single openid?

No. You can only enter one room using an openID at a time.

### Are the exitroom and enterroom operations asynchronous with each other? Can these two APIs be called at the same time?

You need to call exitroom first, and then call enterroom after receiving a callback indicating exitroom operation is successful.

### When is the member status synchronized? Will a user receive the status notification when the user enters the room for the first time?

Audio events are subject to a threshold above which the notification "A member sent audio packets" is sent. Only when the member in the room does not speak within 2 seconds will the notification "A member stopped sending audio packets" be sent. A user will receive the status notification when the user enters the room for the first time.

### Can the microphone volume be set before a user enters a room?

No. The voice chat-related API ITMGAudioCtrl ITMGAudioEffectCtrl can only be called after a user enters the room.

### How do I get and release the microphone permission?

You can get the microphone permission after calling the function EnterRoom successfully, and other programs cannot capture audio data from the microphone during your use of microphone.
Calling EnableMic(false) does not release the microphone.
If you really need to release the microphone, call PauseAudio, which will pause the engine entirely. To resume audio capturing, call ResumeAudio.

### Is there an API to obtain the microphone status before the function EnableMic is called?

You can verify whether the microphone is available by using the API getMicCount.

### What should I do if I don't want the viewers listening to the chat of players to join the chat?

The developer can implement a feature on client that prevents other viewers from enabling the microphone.

### How does a developer determine whether the background music is being played?

Use the API IsAccompanyPlayEnd().

#### When I used the SDK, I was unable to play music and the PC's sound card did not work after I logged in to the simulator.

The simulator does not support mp3.

### Does the SDK support playing sound from receiver?

The voice chat service does not support receiver.

### What local audio file formats are supported by the SDK?

Three formats are supported: m4a, wav, and mp3.

### How do I integrate the team chatting mode of GME voice chat? Does distance attenuation (the sound level decreases with distance from the sound source) exist in the team chatting mode?

For more information on how to integrate team chatting in voice chat, see the [Team Chatting](https://intl.cloud.tencent.com/document/product/607/17972) document. When the team chatting is enabled, distance attenuation does not exist in the same team, but exist in global chatting. For the attenuation coefficient, see the documentation.

### What are the requirements for the user's microphone and speaker if I want to realize 3D sound effect?

Dual-channel output devices are required to realize 3D sound effect.

### How do I integrate 3D sound effect of GME voice chat?

For more information on how to integrate 3D sound effect of voice chat, see the [3D Sound Effect](https://intl.cloud.tencent.com/document/product/607/18218) document.

### There is no Authbuffer file in the downloaded SDK document and sample code.

The Authbuffer file has been incorporated into another file. Please search for it globally in the SDK.

### Is the lib file available for TEA encryption?

We have provided [Authbuffer compiled document and zip package](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20Authbuffer%20Manual.md).

### ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT occurs in case of network disconnection. When does it occur after the network disconnection?

This occurs if no heartbeat packet is received within 30 seconds after the network is disconnected completely.

## FAQs About Voice Message and Voice-to-Text Service

### Which languages are supported by the GME's voice message and voice-to-text converting services?

The voice message and voice-to-text converting services activated in the Tencent Cloud console only supports Chinese. For voice-to-text converting service in other languages, contact the customer service personnel.

### Can the voice message and voice-to-text converting services of GME be used with voice chat?

Yes. You can switch between them by calling the relevant APIs.

### OK is returned in the voice message and voice-to-text converting services of GME, but the features do not work.

You need to export the executable files of the voice message and voice-to-text converting services of GME for testing on the mobile devices.

### After I upload a voice file successfully by calling the API for uploading voice file, the fileid in the returned value is a URL. How do I use it?

You can use this URL to download the file by calling the API for downloading file.

## FAQs about Getting Logs and Troubleshooting

### How do I get the log?

The file named QAVSDK_date.log is the log. It is located in the following directories depending on the operating system:

| Platform | Path |
| ------- | ------------------------------------------------------------ |
| Windows | %appdata%\Tencent\GME\ProcessName                            |
| iOS     | Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents   |
| Android | /sdcard/Android/data/xxx.xxx.xxx/files                       |
| Mac     | /Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents |

### What are the main reasons for sound stutter?

1. **Stutter during music playback:** The VJ plays music using speaker on a phone, and captures and broadcasts the audio data through another phone. (This can inevitably cause stutter. It is recommended for the VJ to use a headset).
2. **Network stutter:** The viewers will experience the stutter when the upstream packet loss rate is too high or the upstream delay fluctuates greatly.
















