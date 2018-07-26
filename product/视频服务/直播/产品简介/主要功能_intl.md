
This page provides a list of features supported for LVB products. For more information on their description and usage, please see relevant documents.


| Category | Feature Name | Details |
|---------|---------|---------|
| LVB access | Push protocol | RTMP push is supported |
|  | Push software | Apps integrated with Tencent LVB SDKs or common push software from third parties are supported, including OBS/XSplit/FMLE, etc. |
|  | Push device | Common RTMP push hardware and encoders from third parties are supported |
| LVB distribution | Distribution protocol | RTMP, FLV and HLS pull are supported |
|  | Specification of original bitrate to be distributed | Audio/Video encoding, bitrate to be distributed must be consistent with that of the input stream |
|  | Real-time transcoding | Real-time transcoding is supported: HD resolution 1280x720 (bitrate: 900 Kbps); SD resolution 960x540 (bitrate: 550 Kbps) |
| LVB watching | Viewer's software | Common FLV, RTMP, and HLS players from third parties are supported |
|  | Viewer's SDK | Android/iOS player SDKs (FLV, RTMP) and Web player SDKs (FLV, RTMP, HLS) are provided |
| Channel management | Management solution | Graphic management on the console, API management, "domain name + LVB code" management are supported |
|  | API management | Create, modify, delete, enable, disable LVB channels; query current viewers of an LVB channel; create and stop recording; create and terminate screenshot tasks |
|  | Console | Create, modify, delete, enable, disable LVB channels; statistics query; LVB test |
|  | Watermark management | The pattern and location of a watermark can be customized through the console or Android/iOS SDK (recommended) |
| LVB security | Blacklist/Whitelist | Management and customization of receiver's blacklist/whitelist URLs are supported |
|  | Hotlink protection | Push/pull URL hotlink protection is supported |
| LVB recording | Record via API | You can record the LVB via API and stored the recorded video in VOD platform |
| LVB screenshot | Take screenshot via API | You can take screenshots of LVB via API and store the screenshot pictures in COS system |
| Statistics | Calculate through the console | Statistics of real-time downstream bandwidth, downstream traffic, the number of online users, number of LVB requests (operator/region dimension), LVB channels |
|  | API statistics | Query the current viewers of an LVB channel |



