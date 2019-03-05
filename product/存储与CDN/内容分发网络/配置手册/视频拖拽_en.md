## Overview

The action of video dragging mainly occurs in VOD scenarios. When a user drags the video progress bar, a request (similar to the one shown below) will be sent to the server end:

```
http:///www.test.com/test.flv?start=10
```

In this case, data will be returned starting from the 10th byte. Video files in VOD scenarios are all cached at various CDN nodes, thus the nodes can directly respond to such requests once this configuration is enabled.


## Configuration Instructions

### Note About Configuration

**Note**
+ The origin server is required to support Range requests
+ Currently supported file types are: mp4, flv, ts
+ You need to enable parameter filtering feature before enabling video dragging.

**Parameter Description**

| File Type | meta Info                                | start Parameter Description              | Request Example                          |
| --------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| MP4       | For videos on the origin server, the meta info must be located at the file header. Videos with their meta info located at the file tail are not supported | The start parameter specifies a time (in seconds) and uses decimal to specify millisecond (for example, start=1.01 means the starting time is 1.01s). CDN will locate the last key frame before the time specified by the start parameter (if the specified time is not a key frame) | ``` http://www.test.com/demo.mp4?start=10``` means the video will be played from the 10th second |
| FLV       | Videos on the origin server must include meta info | The start parameter specifies a byte. CDN will automatically locate the last key frame before the byte specified by the start parameter (if the specified byte is not a key frame) | ``` http://www.test.com/demo.flv?start=10``` means the video will be played from the 10th byte |
| TS        | No special requirements                  | The start parameter specifies a time (in seconds) and uses decimal to specify millisecond (for example start=1.01 means the starting time is 1.01s). CDN will locate the last key frame before the time specified by the start parameter (if the specified time is not a key frame) | ```http://www.test.com/demo.ts?start=10``` means the video will be played from the 10th second |

### Default Configuration

By default, video dragging configuration is disabled.

### Enabling Video Dragging

Video dragging configuration is located in **Access Control** in domain management.

If parameter filtering is disabled, it will be <font color="red">automatically</font> enabled when video dragging has been enabled.

![](https://mc.qcloudimg.com/static/img/21ade68c0db893f9faf2a0d23a0a5fd0/1.png)


