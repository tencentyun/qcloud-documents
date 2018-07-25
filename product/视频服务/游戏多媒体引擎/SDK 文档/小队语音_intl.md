## Overview
Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides a detailed description that makes it easy for developers to debug and integrate the GME APIs for team voice chat.

### Join a room
This function is used to enter a room with the generated authentication data.
>**Note:**
>Microphone and speaker are not enabled by default after a user enters the room.


### Voice chat room
#### Function prototype
```
ITMGContext EnterRoom(int relationId, ITMG_ROOM_TYPE roomType, byte[] authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| relationId		|int    		| Room number, which is an integer made up of 6 or more digits |
| roomType 			|ITMG_ROOM_TYPE	| Audio type of the room |
| authBuffer    	|Byte[]  		| Authentication data |

|ITMG_ROOM_TYPE     	| Description (sound quality) | Parameter |
| ------------- |------------ | ---- |
| ITMG_ROOM_TYPE_FLUENCY			| Fluent | 1|
| ITMG_ROOM_TYPE_STANDARD			| Standard | 2|
| ITMG_ROOM_TYPE_HIGHQUALITY		| High-Quality | 3|

#### Sample code  
```
ITMGContext.GetInstance().EnterRoom(roomId,ITMG_ROOM_TYPE_FLUENCY, authBuffer);
```

### Team voice chat room
#### Description:
Team voice chat: Players form a team before the game starts, and the team voice can only be heard by team members;
Global voice chat: A player can set this mode before the game starts and during the game. After setting, this player can be heard by all the players within a certain range of his/her voice.
The voice mode can be switched at any time during the game.

#### Suppose player A is in a global voice chat mode, the interaction status between player A and player B varies with the scenario and player B's voice chat mode, as shown below:

| In the Same Team | Within the Range | B's Voice Chat Mode | A can hear B | B can hear A |
| -----------------	| ------------ | ------------ |--------------------------	|--------------------------	|
| Yes | Yes | Global | Yes | Yes |
| Yes | Yes | Team | Yes | Yes |
| Yes | No | Global | Yes | Yes |
| Yes | No | Team | Yes | Yes |
| No | Yes | Global | Yes | Yes |
| No | Yes | Team | No | No |
| No | No | Global | No | No |
| No | No | Team | No | No |

#### Suppose player A is in a team voice chat mode, the interaction status between player A and player B varies with the scenario and player B's voice chat mode, as shown below:

| In the Same Team | Within the Range | B's Voice Chat Mode | A can hear B | B can hear A |
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
>- To set the range for receiving voice, refer to API: UpdateCoordinate.

#### Function prototype
```
ITMGContext  EnterTeamRoom(int relationId,ITMG_ROOM_TYPE roomType, byte[] authBuffer,int teamId, int audioMode)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| relationId		|int    		|Room number	|
| roomType 			|ITMG_ROOM_TYPE	| Audio type of the room (only 1 is allowed) |
| authBuffer    	|Byte[] 		| Authentication data |
| teamId    		|int    		| The ID of the team that enters the room (0 is not allowed) |
| audioMode    		|int    		| 0 is for global voice chat, and 1 for team voice chat |

#### Sample code  
```
ITMGContext.GetInstance().EnterTeamRoom(roomId,ITMG_ROOM_TYPE_FLUENCY, authBuffer,1000,1);
```




### Modify team voice chat mode
This function is used to modify the team voice chat mode.
#### Function prototype  
```
ITMGRoom int ChangeTeamAudioMode(int audioMode)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| audioMode    |int     | 0 is for global voice chat, and 1 for team voice chat |

#### Sample code  
```
ITMGContext.GetInstance().GetRoom().ChangeTeamAudioMode(1);
```

### Set range for receiving voice
This function is used to set the range for receiving voice (the unit depends on the distance unit of the game engine).

>**Note:**
>- This function needs to be called for each frame.
>- This function can only be called after a user enters a room.
>- This function is required for each user in the game.

#### Function prototype  
```
ITMGRoom int UpdateCoordinate(int pos_x, int pos_y, int pos_z, int range)
```
| Parameter | Type | Description |
| ------------- |-------------|-------------
| pos_x    |int         | The x coordinate of the user |
| pos_y    |int         | The y coordinate of the user |
| pos_z    |int         | The z coordinate of the user |
| range 	 |int 	  | The range for receiving voice (the unit depends on the distance unit of the game engine) |

#### Sample code  
```
ITMGContext.GetInstance().GetRoom().UpdateCoordinate(pos_x,pos_y,pos_z,10);
```

