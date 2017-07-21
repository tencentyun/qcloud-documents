
## System Overview
A complete MLVB solution consists of three aspects: device, backend and web page. These three aspects need to work together to construct a close-loop solution.

Mini LVB App is a demonstration prototype created by Tencent Cloud video terminal development team, aiming to provide a whole set of reference source codes that include basic features such as VJ stream push, viewing, recorded video playback, interactive messaging, "liking", on-screen commenting and so on. You can [Obtain the Service](https://console.qcloud.com/live/mlvbsdkdownload) for free as long as you are a verified user of Tencent Cloud and have activated LVB service.

![](//mc.qcloudimg.com/static/img/a3511a5130d71605d62dd613cfceeca8/image.png)

It's difficult to reduce the cost for learning and using source codes. In this section, we will segment the major features of Mini LVB and introduce them separately, to reduce your interfacing cost and R&D workload as best as we can.

## Major Features

### Part. 1 Live Room List
Live Room List is an essential component if you are not the kind of customer who only have one event LVB channel at a time. The Mini LVB App is for external demonstration, so there are few rooms that are broadcasting at the same time. We mixed the LVB list with VOD playback list to make the whole list look more filled.

![001](//mc.qcloudimg.com/static/img/1e6d141a053482e568110d1c1cfc7344/image.png)


### Part. 2 Push & Playback
The RTMP SDK of Tencent Cloud is able to implement push, LVB and VOD on mobile device within a day. These three features all follow one single principle: **driven by simply using one URL (push URL, LVB URL or VOD URL)**.

![002](//mc.qcloudimg.com/static/img/cfb85d079d28e63e56904d22acf2d160/image.png)


### Part. 3 Interactive Messaging
You can quickly set up LVB chat room scenario using Tencent Cloud IM SDK. Mini LVB App utilizes Tencent Cloud IM service to achieve the following features:
(1) Plain text messaging
(2) On-screen messaging
(3) "Like" messaging
(4) System notification, for example "XXX has joined the room" or "The VJ has left".

![003](//mc.qcloudimg.com/static/img/0749d445c4e15bcf9dc2617299ae5cf5/image.png)


### Part. 4 Record Playback
Record playback means you can record the LVB process as a VOD video and play it later. The number of VJs is often small at the early stage of introduction of an App. Adding record replay feature in the LVB list can give more information on the App to viewers. The Mini LVB App is for external demonstration, so there are few rooms that are broadcasting at the same time, thus it also adopted this interaction method.

![](//mc.qcloudimg.com/static/img/e9875c1a519eebd53b68938fb9535e92/image.png)

### Part. 5 WeChat Sharing
Web page adaption is a headache that makes WeChat sharing difficult. Differences between playback protocols is not the only problem, in addition, video compatibility issues on various mobile browsers can make the matter very complicated. We've provided some Web players and relevant source codes customized for easy sharing, to enhance your product experience regarding sharing videos on social media.

![](//mc.qcloudimg.com/static/img/c7ae656ffdc8f84bf060d7e1e5148edf/image.png)







