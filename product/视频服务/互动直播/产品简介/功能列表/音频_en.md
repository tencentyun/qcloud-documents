## 1. Microphone Control
### Enable
Supported systems: Windows/iOS/Android

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Acquire/Configure Digital Volume
Supported systems: Windows/iOS/Android
Note: Digital volume refers to the digital signal value of App's audio data. To put it simple, digital value is the App volume, which is different from system volume. Adjusting digital volume means to increase/decrease the digital signal value.

### Acquire Dynamic Volume
Supported systems: Windows/iOS/Android
Note: Dynamic volume refers to the maximum audio signal value (peak value) among the entire time period of each frame in the audio data. The client can acquire the dynamic volume in order to draw the dynamic volume waveform.

### Hot Plug Detection
Supported system: **Windows**
Note: Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.

## 2. Speaker Control
### Enable
Supported systems: Windows/iOS/Android

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Acquire/Configure Volume
Supported systems: Windows/iOS/Android

### Acquire Dynamic Volume
Supported system: **Windows**

### Hot Plug Detection
Supported system: **Windows**
Note: Hot plug detection. Device detects hot-plugging behaviors during messaging and handles them accordingly.

## 3. Remote Room Member Voice Device (Virtual Device)
### Enable
Supported systems: Windows/iOS/Android
Note: The backend supports sending voices in six channels at most. If there are more than six channels, the backend will select six of them based on a certain strategy and forward them to the receiving members.

### Disable
Supported systems: Windows/iOS/Android

### Acquire Device Information
Supported systems: Windows/iOS/Android
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

## 4. External Audio Capturing Device (Virtual Device)
### Description
External audio capturing device is a virtual device which is used for users to capture their own videos and send the audios to other room members through the SDK. The audio can be from any source. For example, from the user's microphone or from an audio file. Currently, only one external audio capturing device is supported.

### Enable
Supported systems: **iOS/Android**

### Disable
Supported systems: **iOS/Android**

### Acquire Device Information
Supported systems: **iOS/Android**
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Input Audio Stream
Supported systems: **iOS/Android**
Note: Input your own audio streams based on business requirement and send them to other room members through the SDK. The audio can be from any source. For example, from the user's microphone or from an audio file.
Note:
. The input audio stream must comply with the conventions of SDK APIs. To be specific, the audio data format must be PCM, and an audio frame should be passed about every 20 ms.
. External audio capturing device and microphone device are exclusive, that is, only one of them can be enabled at a time.

## 5. Input Mixed Audio (Virtual Device)
### Enable
Supported system: **Windows**

### Disable
Supported system: **Windows**

### Acquire Device Information
Supported system: **Windows**
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Acquire Mixed Audio Stream
Supported systems: Windows/iOS/Android
Note: Audio mixing is to mix audio sources from multiple channels into a single-channel audio source.

### Add Multiple Devices to Mix Audio
Supported system: **Windows**
Note: Add multiple audio devices as input sources and acquire their mixed audio stream. Currently, only two devices can be added at a time (a microphone and an accompaniment).

## 6. Output Mixed Audio (Virtual Device)
### Enable
Supported system: **Windows**

### Disable
Supported system: **Windows**

### Acquire Device Information
Supported system: **Windows**
Note: Acquire device information, such as ID, name, type, whether the device is enabled and so on.

### Acquire Audio Streams Prior to Being Mixed
Supported system: **Windows**
Note: Currently, the Output Mixed Audio feature can only acquire each audio stream before they're mixed, instead of the final mixed audio stream. That is to say, audio mixing is not actually realized.

### Add Remote Members from Multiple Channels
Supported system: **Windows**
Note: You can add the voices from remote members of one channel or multiple channels in order to acquire the audio streams from each channel before they're mixed.
 




