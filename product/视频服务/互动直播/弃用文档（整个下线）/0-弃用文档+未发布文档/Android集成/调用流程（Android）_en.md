## Key Modules
1. AVContext: Context module whose object represents a running instance of the SDK. The application only needs to create a QAVContext object to use all the features of the SDK.

2. AVRoom: Room module that provides the callback API for joining and exiting a room.

3. AVRoomMulti:  Multi-member room module that inherits the features from QAVRoom and provides the operation API for obtaining attributes of multi-member room, such as member list.

4. AVEndpoint:  Room member module that provides the operation API for requesting the room member video views or cancelling such request.

5. AVAudioCtrl:  Audio control module that provides the operation API for managing audio devices and customizing audios.

6. AVVideoCtrl:  Video control module that provides the operation API for managing video devices and customizing videos.

7. Video rendering module: Used to render and display the acquired video stream on the screen.

## How to Call the Audio/Video SDK
The following shows the steps for calling the audio/video SDK to implement ILVB and the classes for the methods used in these steps.

App users are divided into VJs and viewers, who use different steps to open a video:

**At VJ side:**

1. Create AVContext (AVContext)

2. Start AVContext (AVContext)

3. Join the room (AVContext, AVRoom, AVRoomMulti)

4. Enable the microphone (AVAudioCtrl)

5. Enable the camera and upload local video data (AVVideoCtrl)

6. Acquire room member status (AVRoomMulti, AVEndpoint)

7. Request remote user video data (AVEndpoint)

8. Render video views (video rendering module)


**At viewer side:**

1. Create AVContext (AVContext)

2. Start AVContext (AVContext)

3. Join the room (AVContext, AVRoom, AVRoomMulti)

4. Acquire room member data (AVRoomMulti, AVEndpoint)

5. Request remote user video data (AVEndpoint)

6. Render video views (video rendering module)


**Close video:**

1. Stop video rendering (video rendering module)

2. Exit the room (AVContext)

3. Stop AVContext (AVContext)

4. Terminate AVContext (AVContext)
