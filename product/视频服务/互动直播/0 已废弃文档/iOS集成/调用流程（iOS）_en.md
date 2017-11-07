## Key Modules
1. QAVContext: Context module whose object represents a running instance of the SDK. The application only needs to create a QAVContext object to use all the features of the SDK.
2. QAVRoom: Room module that provides the callback API for joining and exiting a room.
3. QAVMultiRoom:  Multi-member room module that inherits the features from QAVRoom and provides the operation API for obtaining attributes of multi-member room, such as member list.
4. QAVEndpoint:  Room member module that provides the operation API for requesting the room member video views or cancelling such request.
5. QAVAudioCtrl:  Audio control module that provides the operation API for managing audio devices and customizing audios.
6. QAVVideoCtrl:  Video control module that provides the operation API for managing video devices and customizing videos.
7. Video rendering module: Used to render and display the acquired video stream on the screen.

## How to Call the Audio/Video SDK
The following shows the steps for calling the audio/video SDK to implement ILVB and the classes for the methods used in these steps.
App users are divided into VJs and viewers, who use different steps to open a video.
### 1. Open a video
#### VJ mode
(1) Create QAVContext (QAVContext)
(2) Start QAVContext (QAVContext)
(3) Join the room (QAVContext, QAVRoom)
(4) Enable the microphone (QAVAudioCtrl)
(5) Enable the camera and upload the local video data (QAVVideoCtrl)
(6) Acquire the data of room members (QAVMultiRoom, QAVEndpoint)
(7) Request the remote user's video data (QAVEndpoint, QAVVideoCtrl)
(8) Render video view (video rendering module)

#### Viewer mode
(1) Create QAVContext (QAVContext)
(2) Start QAVContext (QAVContext)
(3) Join the room (QAVContext, QAVRoom)
(4) Acquire the data of room members (QAVMultiRoom, QAVEndpoint)
(5) Request the remote user's video data (QAVEndpoint, QAVVideoCtrl)
(6) Render video view (video rendering module)

### 2. Close the video
(1) Stop video rendering (video rendering module)
(2) Exit the room (QAVContext)
(3) Stop QAVContext (QAVContext)
(4) Terminate QAVContext (QAVContext)
