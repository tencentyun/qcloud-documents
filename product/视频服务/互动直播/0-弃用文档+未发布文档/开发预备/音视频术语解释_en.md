This chapter caters for the technical personnel who just get started with development of video/video Apps.

### Video-related Terminology
#### Video Encoding
A process of converting video files from a certain format into another format using specific compression technology. The most important encoding/decoding standards for video stream transmission are H.261, H.263 and H.264 of International Telecommunication Union, M-JPEG of the Motion Joint Photographic Experts Group and MPEG series of the ISO Moving Picture Expert Group. In addition, such standards as RealVideo from RealV Networks, WMV from Microsoft, and QuickTime from Apple are also widely applied across the Internet. ILVB currently supports H.264 standard.
#### Bitrate
Bitrate is the number of data bits transmitted per second during sampling and varies with video encoding, resolution and sampling. With the same encoding format, sampling and resolution, a higher bitrate per unit of time means a smaller compression ratio and a better video quality that is closer to what we see. But a bitrate higher than a set value produces a negligible effect on the video quality.
#### Bitrate Calculation Formula
[Bitrate] (kbps) = [File Size] (MB) x 1024 KB/[Time] (sec)
#### Frame Rate
Frame Rate (fps) is the number of image frames displayed per second. Theoretically, when capturing dynamic video content, a higher frame rate means a clearer image and a larger occupied space. Actually, a frame rate of over 12 fps can deliver a very smooth watching experience for human eyes. Currently, 25 fps is wide used in domestic radio and television industry, and 24 fps is used for films. The effect of frame rate on video quality depends on the frame rate used in video playback. For example, if we shoot a 96 fps video in high-speed mode, and play the video using a frame rate of 24 fps, the playback speed is slowed down 4 times, with all the actions in the scene slowed down. This is often called the "upgrade". On the contrary, if an 8 fps video is played at 24 fps, a speed-up effect is produced.
#### Relationship and Differences Between Bitrate, Frame Rate and Resolution
**Bitrate:** Is directly proportional to volume - the higher the bitrate, the larger the volume; the lower the bitrate, the smaller the volume.
**Frame rate:** Is directly proportional to the video smoothness - a higher frame rate can deliver a more smooth image; a smaller frame rate can result in a jittering image. If bitrate is variable, the volume is also affected by frame rate. The higher the frame rate is, the more the images displayed per second are, thus the higher the bitrate is required, which means a larger volume.
**Resolution:** Is directly proportional to the image size - the higher the resolution is, the larger the image is; the lower the resolution is, the smaller the image is.
#### Relationship Between Sharpness, Bitrate and Resolution
With a constant bitrate, resolution is inversely proportional to sharpness - a higher resolution delivers a less clear image; a lower resolution delivers a clearer image.
With a constant resolution, bitrate is directly proportional to sharpness - a higher bitrate delivers a clearer image; a lower resolution delivers a less clear image.
#### GOP
GOP refers to Group Of Pictures. A GOP is a group of consecutive pictures. Based on MPEG encoding, pictures (frames) are categorized into I, P and B. I stands for internally encoded frame, P for forward prediction frame, and B for bidirectional interpolation frame. To put it simply, I frame is a complete picture, while P and B frames record changes relative to the I frame. P and B frames cannot be decoded without I frame.

### Audio-related Terminology
#### AGC
AGC (Automatic Gain Control) is used to automatically adjust the microphone volume to a value suitable for listener to prevent the volume from varying between a strong level and a weak level with the change of distance between speech maker and microphone.
#### AEC
AEC (Acoustic Echo Canceler) works by modeling the output of speech maker and eliminate it from the signal captured by the microphone. AEC helps ensure that the other side cannot hear the echo. Based on the correlation between the speaker signal and the multipath echo produced by the signal, AEC builds the voice model of remote signal and uses the model to estimate the echo. Then AEC constantly modifies the coefficients of filter to make the estimated value closer to the real echo. Then, the echo estimate is eliminated from the input signal of the microphone to cancel out the echo. AEC also compares the microphone input with the previous values of speaker to cancel out the acoustic echo caused by multiple reflections that lead to a larger delay. AEC can cancel out various echoes with delay based on speaker's previous output values stored in the storage.
#### ANC
ANC (Automatic Noise Suppression) can detect and eliminate the background noise with a fixed frequency, for example, filtering out fan, air conditioning noises.
