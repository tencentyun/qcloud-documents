## How Does Joint Broadcasting Work

![](//mc.qcloudimg.com/static/img/f68f2faed79f80e515d33310675635f6/image.png)
- **Ordinary LVB**
VJ pushes video streams to Tencent Cloud, and viewers pull the streams from the CDN.

- **Joint Broadcasting**
A low-delay two-way video linkage is established between Viewer A (or the VJ of another room) and the current VJ so that other viewers can watch the videos of both of them at the same time. Tencent Cloud uses a super linkage to build a low-delay video connection between those involved in the joint-broadcasting, and adopts 3A (AEC, ANS, AGC) technologies built in SDK to eliminate the echoes.

- **Joint Broadcasting + Server Stream Mixing**
With above solution, viewers pull multiple video streams from the CDN, leading to an increase of bandwidth cost. In addition, the sound synchronization of multiple video streams is unsatisfactory. Therefore, Tencent Cloud introduces a server stream mixing solution where the multiple video streams are mixed into a single video stream at server side to be pulled by viewers.


## Key Technologies
- **Super Linkage**
For two VJs in different locations, Tencent Cloud's super linkage that is built with **super nodes** and **private network-based Direct Connect** can minimize the transfer delay between the two VJs.
![](//mc.qcloudimg.com/static/img/022656b52419215b030a4d37ad132247/image.png)

- **Delay Control**
With common players (such as ffplay), the network lags can lead to the cumulation of delays. For low-delay chatting scenario, Tencent Cloud SDK introduces the proven dynamic delay control and cumulative delay correction technologies used in QQ voice calls to keep the buffer delay of player within 500 ms without creating frame skip and other problems that affect playback experience.

- **Acoustic Echo Cancellation**
For general LVB solutions, there is no need for AEC (Acoustic Echo Cancellation) because of the one-way transmission of voice (VJ speaks to viewers). But in joint broadcasting scenarios that feature two-way or multi-way transmission of voice, when the primary VJ's voice is transmitted to the secondary VJ's speaker, it will be captured by microphone and then transmitted back to the primary VJ, if AEC is not implemented.
![](//mc.qcloudimg.com/static/img/31fb2031789350bc88e886b75c03a02d/image.png)

- **Multi-Stream Mixing**
Tencent Cloud multi-stream mixing technology allows multiple audio and video streams to be mixed in real time, and supports multiple sets of custom templates so that you can adjust the position and coordinates of each video image based on these parameters.


