## Overview
WeChat sharing is just a saying to facilitate communication, and this document aims to help you with the situation where you wish to use social tools (WeChat, QQ, Moments and Sina Weibo) to share your LVB videos or recorded videos and allow viewers without your App to **view the videos and perform text-based interaction on the web page**, when your App is not widely installed by users.
![](//mc.qcloudimg.com/static/img/c7ae656ffdc8f84bf060d7e1e5148edf/image.png)

## Splitting Tasks
Don't underestimate WeChat sharing, there are many jobs to be done:
- Official account management: WeChat platform enforces strict restrictions on embedded videos. For example, unverified domain names cannot play videos on embedded website in WeChat (So far, no other platforms have such restriction so we only need to consider this problem for WeChat). To avoid the restriction, the best approach is to bind a playback domain name to the official account.

- Backend engineer: Add an external query API for room list service to provide video URL and chat room related information for the web page.

- Web engineer: Implement web page sharing, realize video playback and text interaction features on the page. There are a lot of traps here (especially for Android platform), so it's recommended to use our source code for development.

## Required Knowledge
There are many restrictions on web pages compared to RTMP SDK which can play videos of any formats with ease. This is due to the fact that video playback feature relies on mobile phone browsers, and these browsers don't support many video formats "with ease". LVB and VOD video formats supported by various mobile phones are listed below.

| Mobile Phone Model | RTMP | MP4 | HLS |
|---------|---------|---------|----------|
| iPhone | text 2 | text 3 |  |



