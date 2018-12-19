### Can GVoice be connected to non-game Apps?
Yes.
### Can GVoice be connected to PC games?
Yes.
### Can GVoice be used in Flash browser games?
No. GVoice is only supported for IE browser of ActivityX.
### Is there a limit on the number of rooms?
No.
### Is there a limit on the number of users in a room?
A maximum of 20 users are allowed to join a team voice room. No limit is set on the number of users in a national war voice room, but only 5 users can enable the microphone at the same time.
### How many users can simultaneously join a national war voice room per second?
A maximum of 3,000 users are allowed to join a room per second, and more users than this number may result in a higher failure rate. The game can automatically control the number of users who join a room per second.
### Can a single user join multiple rooms?
No. An OpenID can be used to join only one room at a time.
### Can I re-join a room when the callback for exiting the room is not performed?
No. "joinroom" can be called only after callback is performed. Both "joinroom" and "quitroom" must be called in pairs. An error occurs when you join a room without calling "quitroom".
### Is a room with no user in it automatically reclaimed?
An empty room is reclaimed automatically after 30 minutes.
### Can offline voice mode coexist with voice chat mode?
Yes. You can switch between these two modes.
### Can "roomid" contain special characters?
Yes for national war voice room, but for team voice room, "roomid" can only consists of letters, underscores or numbers.
### Does a room ID precisely correspond to a region server ID?
The mapping relation between a region server ID and a room ID is stored by the game itself.
### Which scenarios where I need to call "quitroom" before I can call the "joinroom"?
The following scenarios are applicable:
- Room switching.
- A "quitroom" callback must be received to exit a room before joining the room again.

### Which scenarios where I can directly implement "joinroom" without calling "quitroom"?
The following common scenarios are applicable:
- The program crashes.
- The program exits.
- The callback function OnstatusUpdate is called, and you have been kicked out of the room.

### What if the callback cannot be received after ApplyMessageKey is called?
Check whether Poll is called and cyclically called in a tick. The polling interval is limited to around 100ms.
### How to get microphone volume of the voice message?
Call the API GetMicLevel.
### Can GVoice be connected to UE4 engine?
Yes. Connect using the API C++ of cocos.
### Can I create two rooms with the same name?
You cannot create rooms with the same name when you have only one game ID.
### Can multiple offline voice messages be played at a time? Is the playback of voice messages implemented in sequence?
Multiple messages cannot be played at the same time. The sequence of playback is determined by the game.
### Does Token expire? How to determine its expiration time? Which value is returned?
Token expires after 5 minutes. An error code "ERR_SVR" is returned upon its expiration.
### Is the encoding format for the name of a room where Token is generated affected?
The name is encoded with GB2312.
### Does Key need to be specified for the initialization of Android?
Two steps are needed for the initialization of Android. One of which is implemented in Activity, where Key is not required but needs to be specified.
### What if timeout occurs when you connect to the server in overseas environment for the first time?
 For the first connection, if the account is found to be new, the server reads the database first. Therefore, timeout occurs for first connection attempts until data is returned from the database.
### Does "init" need to be called again in case of switching from voice chat mode to voice message mode?
No. You can directly call "setmode". "init" is required once for connecting to the entire process.
### Do I need to delete the voice file downloaded through voice messaging?
Yes.
### Can the function PlayRecordedFile be called to play local MP3 ogg files of Unity?
No. It can only be used to play your local files.
### Is it normal that the recording starts in a second?
Yes. Like WeChat voice, it is recommended to make some adjustments to the UI. The period from the time you press the recording button until the recording button is displayed to be pressed can be delayed.
### Is there a limit on the length of "fileid" for voice API?
It is limited to 260 Bytes. The size of FilelD can be reserved in the protocol.
### How to set the mode when offline voice coexists with speech recognition?
Set the mode to speech recognition.
### How to obtain client logs?
- For Windows, use Debugview or use attach of vs to view logs in the process outputwindow after the running of Debugview.
- For Android, use logcat.
- For iOS, use Xcode to obtain logs.
### How to obtain the length of recording files?
Obtain C# using the API GetFileParam, as shown below: 
```
    int [] bytes = new int[1];
    bytes [0] = 0;
    float [] seconds = new float[1];
    seconds [0] = 0;
    m_voiceengine.GetFileParam (m_recordpath, bytes, seconds);
```

### Does a piece of recording correspond to a recording file?
Yes.

