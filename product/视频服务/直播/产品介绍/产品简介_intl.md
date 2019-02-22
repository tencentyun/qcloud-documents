## Overview
Relying on Tencent's powerful technology platform, Live Video Broadcasting (LVB) provides users with core business underlying capabilities (such as v.qq.com) as well as professional, stable and fast LVB access and distribution services, so as to fully satisfy the strict requirements for ultra-low delay and large concurrency. It also offers self-developed pusher and player SDKs to help users customize their own pusher and player Apps at the client end. It features low delay, high security, high performance, easy to access, and supports multiple terminals and bitrates.

Core Competencies

#### Reliable conversion
It allows fast and reliable format conversion, and supports the distribution of FLV, RTMP and HLS LVB sources with ultra-low latency.

#### Extremely high capacity
It allows 1,000k viewers to watch LVB at the same time. Massive CDN nodes are provided to ensure overall coverage.

#### Pusher and player SDKs on mobile devices
Self-developed Android/iOS pusher and player SDKs support RTMP push, FLV/RTMP LVB, and FLV VOD. LVB push and playback capabilities as well as the integration of self-built mobile Apps can be easily implemented on mobile devices.

#### Channel management API
APIs for creating, modifying and querying LVB channels are provided, which can be seamlessly integrated to self-built video content management system.

#### Recording, screenshot and multi-bitrate
You can record or take screenshots of LVBs via APIs. Recorded videos are directly interfaced with VOD platform, and screenshot pictures are directly stored in COS system for subsequent processing, to ensure efficiency and convenience. Multiple bitrates and watermarking are supported.

#### LVB code management
Large-scale LVB events can be managed by using LVB code management solution.



## Product Architecture

![](https://main.qcloudimg.com/raw/62099c408b99d2def73d621033613eeb.png)

Typical product architecture is as shown above:

Push end: All RTMP push devices are supported to push videos to LVB system using Apps integrated with Tencent's self-developed LVB SDKs or third-party LVB software.
Playback end: Apps integrated with Tencent's self-developed LVB SDKs or third-party players supported.
Management components: Users can manage LVB events through APIs or the console, and query relevant statistical data.
Distribution components: Fast and flexible playback methods are provided for LVB users via the CDN system across the country. Users can use self-developed player SDKs or those provided by Tencent Cloud to integrate with their own business. Users can also watch HLS LVBs directly through H5 page.





