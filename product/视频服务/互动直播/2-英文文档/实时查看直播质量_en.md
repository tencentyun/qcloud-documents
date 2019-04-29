# Feature and Usage of AV_Monitor

## Summary

AV\_Monitor is a real-time monitoring tool used to help users locate and troubleshoot network problems. Address is [http://avq.avc.qcloud.com/monitor.html](http://avq.avc.qcloud.com/monitor.html).

## Basic Features

![Basic Interface](https://mc.qcloudimg.com/static/img/3be70ac5c099785144a2209e5b8ada2d/1.jpg)

On the top of the interface, you can find a text box in which you can enter query conditions, SdkAppid, ID, start and end time of query, which are all required. Both vertical text boxes to the left of the interface are used to display some reported values to help developers to locate problems. As shown in the figure below, you can see some basic information in the left text box by clicking the red dot for joining room, such as CPU, operating system, network type, model, SDK version, etc.
![Basic Interface](https://mc.qcloudimg.com/static/img/8a46acbbfb69ab95dc75622c2442ef6e/2.jpg)

In this figure, some commonly-used basic information of the queried user are listed above the curves, and you should note about the following items:

* Tinyid: The uin:xxxxxx at the bottom left corner of the Basic Information, which is sometimes required for locating problems
* Whether proxy machine is used. "No" for users on DC, and "Yes" for users on OC
* Transmission protocol. VJ type is generally UDT
* Client IP. You can see the province and ISP at client side
* API machine IP. You can check whether the assigned access machine IP is matched with the client. Currently, only private IP is displayed, which can be queried by Tencent developers on the internal website tnm2.oa.com

Finally, the List of Graphs to the right of the above figure is a quick entry for various curve charts. You can click one to get the monitoring data you have interest in

## Downlink Quality Monitoring Charts

They are mainly used to display various actions and statuses at viewer end. Please note about the content and application scenarios displayed in the charts below.

### Overall Downlink Packet Loss

![Basic Interface](https://mc.qcloudimg.com/static/img/6e591a59fbce40ae67288180221363d6/3.jpg)

* Packet loss curve
The purple curve at the bottom is the packet loss curve, with one point per 2 seconds, to reflect user's current network condition. High packet loss can cause stutters to audio and video, which indicates a poor network quality at the user side. For example, as shown in the above packet loss curve, packet loss occurs over a very short time when a user starts broadcasting, and the packet loss is 0 for other times, which indicates that the overall network condition is good.

* Red dot
The red dot indicates the action that a user joins a room once. After you click the red dot, the basic information carried by the user when he/she joins the room this time is refreshed and displayed in the Basic Information above the chart and the text box on the left.

* Blue dot
The blue dot indicates the action that a user exits a room once. Since a user may directly kill a process without exiting a room, the blue dot may be 90 seconds later than the actual situation (timeout period at the backend). A message is popped up when you hover the mouse over the blue dot, which indicates whether you exit the room normally or after the timeout.

* Yellow dot
Yellow dot indicates that IP is changed during use, which is probably because the network is switched when the user is in the room.

### Overall Downlink Bitrate

![Basic Interface](https://mc.qcloudimg.com/static/img/b9ff74ce4eebc604bc4cc29efbbcd8b0/4.jpg)

Overall downlink bitrate=Download video bitrate+Download audio bitrate (their FECs are included). You can get the VJ's TinyID by clicking on any point of the overall downlink bitrate. With this TinyID, you can check VJ's status information, without the need to ask VJ's ID from business developers. Facts prove that this feature is very useful.

### Download Audio Bitrate

Please note that the FEC of audios may be as high as 100%, so the bitrate could be twice the normal bitrate in case of poor network conditions.

#### Other Downlink Charts

* Overall downlink frame rate of primary screen
* Overall downlink frame rate of primary screen. The lower the frame rate, the less smooth the screen.
* Overall download frame rate/bitrate of downlink side channel, which is the frame rate/bitrate shared among the screens.

## Uplink Quality Monitoring Charts

### Overall Uplink Packet Loss

![Basic Interface](https://mc.qcloudimg.com/static/img/ffabf311e59c99646782dc4d1411997f/5.jpg)

Compared to the downlink packet loss view, only a pink dot is added, indicating acquiring/clearing video bit. This operation can only be performed by VJ who should apply for the video bit from the backend before starting broadcasting, and then the backend pushes the video stream of the VJ to the viewers. If no uplink video data is transferred by the VJ within 30 seconds, the video bit is cleared at the backend. If VJ wants to transfer the uplink data, he/she needs to apply for new video bit.

### Latency (ms)

![Basic Interface](https://mc.qcloudimg.com/static/img/f32e79a8a9e6395ddc21641a03193478/6.jpg)

Latency is RTT of Hello packet from client to access machine. Latency may increase in case of poor network conditions, which can lead to video stutter. Please note that, high CPU can also give rise to high latency, because response packet cannot be normally processed by Hello packet processing process due to high CPU utilization.

## Other Monitoring Charts

![Basic Interface](https://mc.qcloudimg.com/static/img/cec6522e4e762f480350ea0b82e8022f/7.jpg)

The CPU utilization of application refers to that of SDK, while the CPU utilization of device is the overall CPU utilization of App. Please note that, recently, the overall CPU utilization is too high due to CPU frequency decreases in some scenarios for iPhone, so problem varies in different situations.


# ILVB Audio/Video Backend Q&A

## About "Room"

For ILVB audio/video backend, rooms are mainly used to isolate user groups. Users in different room can watch video streams of different VJs. The concept of room is similar to that of Beauty Show in real life. A room is identified by `room ID`, with a type of 32-digit integer numbers, which is **_generated and managed at business side_**. Different room should use different `room ID`.

Note: Audio/Video `room ID` is not associated with IM group ID. However, audio/video `room ID` generally corresponds to IM group ID in the use of service. So an IM group ID can be used as an audio/video `room ID`, or a mapping can be created between these two IDs, depending on the actual needs of business side.

