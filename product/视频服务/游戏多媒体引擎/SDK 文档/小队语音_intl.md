## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for developers to debug and integrate the GME APIs for team chatting.

### Enter a room
This function is used to enter a room with the generated authentication data.


### Voice chat room
#### Function prototype
```
ITMGContext EnterRoom(string roomId, ITMG_ROOM_TYPE roomType, byte[] authBuffer)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| roomId		|string    		| Room number supports Int32 type (which is passed after being converted to a string) |
| roomType 			|ITMG_ROOM_TYPE	|Audio type of the room |
| authBuffer    	|Byte[]  		| Authentication data					|

| Audio Type | Meaning | Parameter | Application Scenario | Volume Type | Recommended Sampling Rate on the Console |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA.								| Speaker: chat volume; headset: media volume 	| 16k (if there is no special requirement for sound quality)					|
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games.													| Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality				|
| ITMG_ROOM_TYPE_HIGHQUALITY		|HD	|3|With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	| Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	|

- If you have special requirements for volume types or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.


### Team chatting room
#### Description:
Team chatting: Players form a team before the game starts, and the team chatting can only be heard by team members;
Global chatting: A player can set this mode before the game starts and during the game. After setting, this player can be heard by all the players within a certain range of his/her voice.
The voice mode can be switched at any time during the game.

#### Suppose player A is in a global chatting mode, the interaction status between player A and player B varies with the scenario and player B's voice chat mode, as shown below:

| In the Same Team | Within the Range | B's Voice Chat Mode | A Can Hear B | B Can Hear A |
| -----------------	| ------------ | ------------ |--------------------------	|--------------------------	|
| Yes | Yes | Global | Yes | Yes |
| Yes | Yes | Team | Yes | Yes |
| Yes | No | Global | Yes | Yes |
| Yes | No | Team | Yes | Yes |
| No | Yes | Global | Yes | Yes |
| No | Yes | Team | No | No |
| No | No | Global | No | No |
| No | No | Team | No | No |

#### Suppose player A is in a team chatting mode, the interaction status between player A and player B varies with the scenario and player B's voice chat mode, as shown below:

| In the Same Team | Within the Range | B's Voice Chat Mode | A Can Hear B | B Can Hear A |
| -----------------	| ------------ | ------------ |--------------------------	|--------------------------	|
| Yes | Yes | Global | Yes | Yes |
| Yes | Yes | Team | Yes | Yes |
| Yes | No | Global | Yes | Yes |
| Yes | No | Team | Yes | Yes |
| No | Yes | Global | No | No |
| No | Yes | Team | No | No |
| No | No | Global | No | No |
| No | No | Team | No | No |

### Notes about range of voice
**Notes:**
>- Whether a member is within the range of voice does not affect the interactions between the team members in the same team.
>- To set the range for receiving voice, refer to API: SetGameAudioRecvRange.

#### Function prototype
```
ITMGContext  EnterTeamRoom(string roomId,ITMG_ROOM_TYPE roomType, byte[] authBuffer,int teamId, int audioMode)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| roomId		|string    		| Room number supports Int32 type (which is passed after being converted to a string)|
| roomType 			|ITMG_ROOM_TYPE	| Audio type of the room (only 1 is allowed) |
| authBuffer    	|Byte[] 		| Authentication data					|
| teamId    		|int    	| The ID of the team that enters the room (0 is not allowed)	|
| audioMode    		|int    	| 0 is for global chatting, and 1 for team chatting		|






### Modify team chatting mode
This function is used to modify the team chatting mode.
#### Function prototype  
```
ITMGRoom int ChangeGameAudioMode(Type_AudioMode gameAudioMode)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| Type_AudioMode    |int    	| 0 is for global chatting, and 1 for team chatting		|

#### Sample code  
```
ITMGContext.GetInstance().GetRoom().ChangeGameAudioMode(1);
```

### Set range for receiving voice
This function is used to set the range for receiving voice (the unit depends on the distance unit of the game engine).

#### Function prototype  
```
ITMGRoom int SetGameAudioRecvRange(int range)
```
| Parameter | Type | Description |
| ------------- |-------------|-------------
| range    |int         | Maximum audio frequency that can be received				|


#### Sample code  
```
ITMGContext.GetInstance().GetRoom().SetGameAudioRecvRange(300);
```

