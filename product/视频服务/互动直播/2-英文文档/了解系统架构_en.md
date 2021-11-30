## ILVB System Architecture
With years of experience in audio/video area, Tencent Video Cloud has designed this powerful low-latency ILVB product to cope with complex and ever-changing network environment.
### Architecture
1. Low Latency. Custom protocol based on UDP or UDT ensures minimum latency.
2. High Level of Privacy. Custom protocol can perfectly protect the high-valued videos from being monitored by hotlink.
3. High Expansibility. If you need custom data that is precisely synced with audio/video stream, e.g. real-time face recognition, it can also be expanded through custom protocol.
4. Good Compatibility. Users who watch videos at viewer end or through web and H5 can also use non-interactive push to use services provided through generic streaming protocol.
5. For users who use custom protocol and general protocol, signaling and messaging can also be interconnected in real time.

![Tencent ILVB System Architecture](https://mc.qcloudimg.com/static/img/50aafdfc8b501b497075e74b0b5f1128/1.png)

### Data Interaction Timing Sequence
1. Step 1 and 2 describe how app users complete the ILVB identity verification under independent account mode.<br/>
	Under hosting account mode, developer's server is not required, so you can directly call the ILVB's sdk login API.
2. Audio/video APIs, such as starting broadcasting, watching, joining broadcasting, can be called only after you join the room;
3. As long as the app business logic permits, any user is able to join broadcasting after calling the relevant API.
4. Developer's backend server can push messages to users or groups in app through Tencent ILVB.

![Tencent ILVB Data Interaction](https://mc.qcloudimg.com/static/img/4094feaf383cf1e3c5714bd3f9dbfc8e/hudongzhibo.png)

### ILVB Code Structure
1. iLive SDK has encapsulated many SDK APIs to provide basic capabilities in a uniform manner, such as account, message and audio/video;
2. For the convenience of developers, we wrap some business logics common in ILVB based on iLive SDK to provide Live SDK. We recommend developers to develop based on Live SDK directly.
3. Based on Live SDK, we provide a demo app, FreeShow. This demo app allows developers to directly use ILVB scenario features, which can also be used as a reference for the development of app UI.


![Tencent ILVB Code Structure](https://mc.qcloudimg.com/static/img/0e11b392263468750268184075781f23/6.png)


