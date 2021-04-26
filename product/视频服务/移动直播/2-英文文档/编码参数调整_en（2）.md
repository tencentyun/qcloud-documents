## Parameter Customization
You can customize video/audio encoding parameters by setting the Config object. The following setting APIs are supported for now:

| Parameter Name           |    Description                                          |   Default Value  | 
| :-------------- | :-----------------------------------------------| :------: |
| audioSampleRate |   Audio sampling rate: count of audio signal captures by the recording device per second   |  44100   |  
| enableNAS          |   Noise suppression: When this is enabled, background noises can be filtered out (applicable when the sampling rate is below 32,000) |  Off     |
| enableHWAcceleration|   Video hard-coding: When this is enabled, video capture up to 720 p, 30 fps is supported.   |  On   |  
| videoFPS     |   Video frame rate: Number of frames produced by the video encoder per second. Most of the phones don't support encoding above 30 FPS, so you're recommended to set FPS to 20.           |  20      |
| videoResolution |   Video resolution: Four types of 16:9 resolutions are available      |  640 * 360 |
| videoBitratePIN |   Video bitrate: Number of data bits produced by the video encoder per second (in Kbps) |  800 |
| enableAutoBitrate |   bitrate adaptation: Adjust the video bitrate automatically based on the network condition |   Off |
| videoBitrateMax | Maximum output bitrate: This option takes effect only when bitrate adaption is enabled. |   1,200 |
| videoBitrateMin | Minimum output bitrate: This option takes effect only when bitrate adaption is enabled. |   800 |
| videoEncodeGop | Keyframe interval (in second): The interval at which one I frame is output | 3 seconds |
| homeOrientation | Set the rotation angle of video image, e.g., whether to push in a landscape mode  |   0: home is on the right; 1: home is at the bottom; 2: home is on the left; 3: home is at the top   |
| beautyFilterDepth | Beauty filter level: levels 1 to 9 are supported; the higher the level, the more obvious the effect. 0 means Off  |   Off   |
| FrontCamera | Front or rear camera by default | Front |
| Watermark | Watermark image (UIImage object) | Tencent Cloud Logo (demo)  |    
| watermarkPos | The position of the watermark image relative to the coordinate in the upper-left corner | (0, 0)  |                                                                        


## Configuration
You are recommended to specify these parameter settings before enabling push, since most of the settings do not take effect until the push is re-performed. The reference code is as follows:

```objectivec
//Declare _config and _pusher in member variables
....
//Initialize _config
_config = [[TXLivePushConfig alloc] init];

// Modify the audio sampling rate to 44100 and fixed video bitrate to 800
_config.audioSampleRate = 44100;
_config.enableAutoBitrate = NO;
_config.videoBitratePIN = 800;

//Initialize _pusher
_pusher = [[TXLivePush alloc] initWithConfig: _config];
```

