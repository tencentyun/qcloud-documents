##  1. What is ILVB?

**ILVB** (Interactive Live Video Broadcasting) is a "**Real-time Multi-Stream Audio and Video Interaction**" solution. Please see [Typical Scenarios](https://cloud.tencent.com/doc/product/268/3160)

- Compared to one-way live broadcasting, ILVB allows **viewers to "show themselves and speak"**, thus has a higher requirement for real-timeness and anti-echo capability.

- With ILVB SDK, developers can build **one-to-one, one-to-many or many-to-many** audio/video communications which have a good quality as QQ audio/video.

- ILVB supports up to 10 streams of joint broadcasting videos and unlimited audio streams (a common mobile device can support 6-8 video streams) in a multi-person live broadcasting. A single room allows a concurrence up to **one million** people. These make ILVB a perfect choice for such applications as large live show, social video, online education, remote consulting, and multi-camera online media broadcasting.
</br>


## 2. Differences Between ILVB and LVB

If **LVB** is compared to a signal transmitter, then **ILVB** is like a theater with stage.

![](//mccdn.qcloud.com/static/img/684a6a66a62cb830c9cfb29848987210/image.png)

- You can watch the shows transmitted by the "signal transmitter" wherever you are, as long as you know the signal frequency band (channel ID or URL) of the transmitter.

- But if you want to enjoy a stage show, you need to seat yourself in the theater, which may offer only one spectator seat or thousands of spectator seats, and may be invited to the stage to join the show.

- To allow the viewers to see the show on the stage in real time, ILVB has a millisecond-level latency, much lower than the second-level latency of LVB.

- In particular, the show on the stage can also be broadcasted through transmitter to the people outside of the theatre. This is called "non-interactive broadcasting".
 </br>



## 3. Capability Integration

#### ILVB is like a "capability container" that incorporates various capabilities of Tencent Cloud products to implement a diversity of scenarios for video Apps.

| Capability | Description | Scenarios |
|---------|---------|---------|
| **Multi-stream audio/video** | Audio/video chat among multiple people in one room | 1. In a large live broadcasting, VJ invites viewers to join the broadcasting for interactions</br> 2. Large ILVB with multiple VJs, such as remote debate, guest commenting, and so on </br>3. One-to-one, or many-to-many video communications |
| **Instant Messaging** | IMSDK, used for user group management and message handling in live room. Please see [ Activation and Integration Guide](https://cloud.tencent.com/doc/product/269/3794) | Group chat, gift-giving, red-packet-giving and other features in large live broadcasting |
| **Screen Sharing** | A user shares screen</br> (designated area in Windows) to others in the same room | Presentation of courseware in distance learning; presentation of trend charts in finance and securities; presentation of real-time game views by game VJ |
| **Beauty Filter** | noise canceling, dermabrasion, whitening | Large live show, visual communication |
| **Face Recognition** | Recognize the captured face image and facial features | Face positioning, oriented beauty filter, face-transforming filter |
| **Quick Room Switching** | Allow viewers to switch between live rooms seamlessly | Change room with a slide |
| **Recording** | Record audio/video in a room at the cloud (multi-stream mixing is not supported currently). [VOD service] needs to be activated (http://console.cloud.tencent.com/vod/portal) | Playback of live broadcasting and management & storage of broadcasting content |
| **Non-interactive Broadcasting** | Push the audio/video in ILVB room to more viewers outside of the room through CDN acceleration (FLV and HLS formats are used. 5 channels are provided by default). For more information, please see [Non-interactive Broadcasting](https://cloud.tencent.com/document/product/268/7612) | Promote broadcasting content to users without the App. When the number of room members exceeds 1 million, this allows more people outside of the room to watch the video |
| **Mixing and Recording** | The two video streams in joint broadcasting are mixed into one for push and recorded as one video | Promotion and storage of video content in joint broadcasting | 
| **Porn Detection** | Capture and store frames from live videos at cloud and automatically detect porn content in images | Audit of content of large live show |
| **Watermark** | Add logo images to ILVB screen | Policy, content and brand promotion |
| **Playback of RTMP Video Stream** | In the ILVB room, play the video streams from a third party or captured by professional relaying device | Multi-camera video relaying in large events; VJ commentary views embedded in the signals relayed from a third-party event |

[Click here for more scenarios](https://cloud.tencent.com/doc/product/268/3160)

## 4. Key Audio/Video Parameters

| Parameter Type | Tencent Cloud ILVB Specification |
|---------|---------|---------|
| Maximum concurrent audio/video streams | 10 video streams and unlimited audio streams |
| Maximum number of viewers in one room | 1 million |
| Video resolution | 320×240, 480×360, 640×368, 640×480, 960×540, 1280×720 |
| Image coding rate | 30-1500 kbps |
| Delay | 150-400 ms |
| Anti-packet loss rate | 35% |
| Audio sampling rate | 8000, 16000, 48000 |
| Room access speed | WiFi: 950 ms; 4G: 1504 ms |
















