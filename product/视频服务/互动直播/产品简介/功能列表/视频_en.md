
## 1. Video Quality Control
### Configure Video Encoding/Decoding Parameters
Supported systems: Windows/iOS/Android
Note:
"These parameters include encoder/decoder type, image width/height, frame rate, bitrate, maximum QP, minimum QP, GOP, sharpening switch, sharpening level and FEC switch. For more information regarding the value range of these parameters, please see the API documents.
Note:
. Configure these parameters by using the web configuration tool.
. Maximum encoding/decoding definition supported by different platforms are as follows:

**Windows** 
Encoding: 1280*720 
Decoding: 1280*720
Requirement:
 . Good network connection.
 . You need to use the web parameter configuration tool to configure the encoding definition as 640*480.

**iOS**
Encoding: 1280*720 
Decoding: 1280*720
Requirement: Good network connection.

**Android**
Encoding: 1280*720 
Decoding: 1280*720
Requirement: Good network connection."

## 2. Camera Control
### Enable
Supported systems: Windows/iOS/Android
Note: Enable device. It is not allowed to enable multiple devices of the same type at the same time (if they exist). When you enable a device when another device of the same type is already enabled, the SDK will disable that device by default.

### Disable
Supported systems: Windows/iOS/Android

### Switch Camera
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Render
Supported systems: **iOS/Android**
Note: The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.

### Acquire System Camera Object
Supported systems: **iOS/Android**
Note: You can realize camera zooming by using this object.

### Image Preprocess
Supported systems: **iOS/Android**
Note: Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.

### Beauty Filter
Supported systems: **iOS/Android**

### Acquire Remote Video Data
Supported systems: **iOS/Android**
Note: The client can acquire remote data if the data needs to be rendered from the client.

### Acquire Data Captured by Camera
Supported systems: **iOS/Android**
Note: The client can acquire camera data if the data needs to be rendered from the client.

## 3. External Video Capturing Device (Virtual Device)
### Description
External video capturing device is a virtual device which is used for users to capture their own videos and send the videos to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file. Currently, only one external video capturing device is supported.

### Enable
Supported systems: Windows/iOS/Android

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Input Video Stream
Supported systems: Windows/iOS/Android
Note:
Input your own video streams based on business requirement and send them to other room members through the SDK. You can use any video source, for example, video from user's camera, or video from a certain file.
Note:

. The input video stream must comply with the conventions of SDK APIs. To be specific, the video must be converted into individual image frames to be passed in, the only supported color format now is I420, there is no limit to image size, image width and height must be multipliers of 4, optimal video frame rate is between 10-15. Furthermore, the SDK does not preprocess or render the input video stream.
. External image capturing device and camera device are exclusive, that is, only one of them can be enabled at a time.


## 4. Remote Room Member Video Device (Virtual Device)
### Description
Remote room member video device is a virtual device used to operate the video stream of remote member, which means requesting for remote member video data for rendering.
Only one remote room member video device can be supported on PC platform, which is shared by all remote room members. In other words, you need to create a remote device with "new", then the SDK throws the data to the upper layer. Android and iOS platforms made another encapsulation layer, in which case Apps in the upper layer don't have to consider about devices. You can simply configure a callback and the SDK will throw data of other members to Apps.

### Enable
Supported systems: Windows/iOS/Android

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Render
Supported systems: **iOS/Android**
Note:
Render the video of remote member.
Note:
. The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, you need to realize the rendering from the client at the moment. The rendering modules provided by iOS and Android SDKs now support multi-channel rendering (for Windows platform, the client needs to acquire video stream data and perform rendering on their own).

### Acquire Video Stream
Supported systems: Windows/iOS/Android
Note: Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.

### Render Event Notification for Each Frame
Supported systems: Windows/iOS/Android
Note: Render event notification for each frame. The client can use this feature to improve UI and send useful notifications to users via UI. For example, whether to send them notification about this event, notification interval, and so on.

## 5. Local Screen Video Device (Virtual Device)

### Enable
Supported system: **Windows**
Note:
. Only one member can enable local screen video device and send screen videos at the same time, in the same room. The other people need to wait for the current user to disable the local screen video device before enabling it.
. The highest encoding definition supported by the screen video display is 1920*1200.
. For more information on things to note when using screen video device, please refer to API documentation.

### Disable
Supported system: **Windows**

### Acquire Device Information
Supported system: **Windows**

### Render
Note:
. The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.

### Image Preprocess
Supported system: **Windows**
Note:
Preprocess the images captured by the local screen.
Note:
. Both you and room members can view the preprocessing outcome. Sending a video means to send the preprocessed video. Room members will also see the preprocessed video.

## 6. Remote Screen Video Device (Virtual Device)

### Enable
Supported systems: Windows/iOS/Android
Note:
. Since screen video displays usually have high definition (such as 1920*1200), user experience can be affected if devices (especially devices with low hardware configuration) receive and decode such images. Thus evaluation is recommended during actual use.

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported system: **Windows**
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Render
Supported systems: **iOS/Android**
Note:
. The currently provided internal SDK rendering module only has simple features, you cannot freely configure the rendered image (such as image size and position). If your business requires you to do so, it is recommended to realize the rendering from the client.

### Acquire Video Stream
Supported systems: Windows/iOS/Android
Note: Acquire video stream of room member. You can acquire video streams of any member who has sent videos before. If the client needs to render videos on their own to meet business requirement, they can use this feature to acquire the video streams.








