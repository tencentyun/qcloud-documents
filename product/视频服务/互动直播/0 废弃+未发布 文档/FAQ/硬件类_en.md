#### Rear camera needs to be enabled for joining a room.  
The cameraId in enableCamera API is used to control the front/rear cameras.

#### No sound can be heard after joining the room, and the microphone volume is always 0.  
This is often caused by the occupied resources. Allow for a delay before enabling the microphone after joining the room.
	
#### How to deal with the Error 1002 reported when enabling the microphone in the room callback?  
Android:  
Call enableMic as true before joining the room.  
No conflict is triggered because enabling microphone before joining a room is allowed in Android.  
iOS:  
For iOS, microphone is disabled by default when someone is joining a room, so there may be a conflict between enabling microphone and joining the room (microphone is disabled).  
You can solve this problem by adding a delay of 1s before enabling the microphone.

#### How to solve the problem of being unable to adjust the volume to 0?
Android  
By simply setting enableSpeaker to false, you can go into mute mode.

iOS  
At VJ end, the volume of VJ cannot be adjusted to 0; at viewer end, you can go into mute mode by setting the `Audio Scenario` to `Watch` in audio parameter settings of console Spear engine, or by referring to the usage of the Mute button in sample 2.
