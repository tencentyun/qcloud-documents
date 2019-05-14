
Tencent Cloud video service is built on Tencent's years of technical expertise and experience in infrastructure construction, providing customers with a one-stop solution covering cloud video storage, video transcoding service, video playback acceleration and video communication service.

Currently, Tencent Cloud video solution is available for registered users of Tencent Cloud.

## Core Capabilities

Cloud video storage, video transcoding service and video playback acceleration are the core components of Tencent Cloud video solution. Tencent Cloud provides one-stop VPaaS (Video Platform as a Service) service by delivering a complete range of core capabilities throughout all the stages of VOD service from upload, storage, management, transcoding, processing, publishing, statistics and playback. With flexible, fast, high-quality video publishing service, users can, by choosing services as needed, obtain the reliable video publishing capability quickly, thus focusing on the business and responding to market changes agilely.

#### Various Options for Video Upload
To meet the upload requirements in various scenarios, a wide selection of modes for video upload are available, including local upload, URL video pull, upload by API, and upload on client. Switching from LVB recording to VOD is also supported.

Videos in various formats can be uploaded, and resuming from break point, upload of large files and multiple file backups are supported.

#### Secure and stable storage
Redundant storage of video files across multiple architectures and devices is provided to support remote disaster recovery and isolation between user resources. Separation of cold-backup and hot-backup storages for video files provides more choices for customers' storage needs.

#### Visualized Video Management
List-based video management, online preview, and fuzzy search for video files are supported;

You can manage video files through the console or API by performing operations such as classification, tagging, and configuration of transcoding and hotlink protection. All the information can be exported for viewing.

#### Powerful Transcoding Capability
Over 12,000 distributed transcoding clusters and 2,000 concurrent transcodes ensure transcoding quality and efficiency. Watermarks can be added and different transcoding formats can be set to accommodate various application scenarios.

#### Intelligent Video Processing
Intelligent video clipping, stitching, screenshot processing and AI porn detection on videos.

#### Spectacular Acceleration Experience
The nation-wide BGP network provides a coverage of more than 800 CDN video acceleration nodes of over 17 ISPs.
   
#### Video Ecology
It provides the resources interfaced with Tencent QQLive V+ channel to set up a diversified platform for users to publish and monetize videos. The integration with WeChat and other products allows Tencent Cloud Video to directly generate the links to be published via WeChat official accounts, helping users publish videos to WeChat official accounts.
  
#### Video Delivery
The video playback URL and custom player code can be quickly obtained, allowing the fast CDN delivery.
 
#### Custom Player SDK
Web/Android/iOS player SDKs are provided to help customers quickly build highly-customized video publishing capabilities across all platforms.
  
#### Security Features
Security features such as blacklist & whitelist, playback password and hotlink protection, video DRM encryption are provided to protect customers' video contents.
  
#### Statistical Features
Various fine-granularity statistical features are provided, including time dimension and other detailed information, allowing customers to quickly view video publication information and evaluate the results.

## Product Architecture

![](https://mc.qcloudimg.com/static/img/fc43e00b3b950221afea8f4e625c7025/image.png)

Typical product architecture is as shown above:

#### Cloud Video Storage:
Users can store videos in the media asset management backend by uploading and pulling them, and use cold-backup and hot-backup storages as needed.

#### Video Transcoding Service:
Users can transcode, intelligently audit and process files through API and console.

#### Video Playback Acceleration:
Fast and flexible playback methods are provided for users via the CDN system across the country. Users can integrate self-developed player SDKs or those provided by Tencent Cloud with their own business. Users can also generate video links exclusive to WeChat official accounts, and publish them via the WeChat.

