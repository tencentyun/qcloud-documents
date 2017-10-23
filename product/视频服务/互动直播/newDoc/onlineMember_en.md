# Online Member Statistics Solutions

> * Solution 1: Use business server for management (recommended)
> Solution 2: Use IMSDK API

## Solution 1: Use business server for management
### Flow chart

![](http://mc.qcloudimg.com/static/img/8da0f13a73d87e2970e5e4603d3ca61d/image.png)

### Steps

1. Viewer 2 calls the business server API for joining a room and the record of joining room is generated.
2. Viewer 2 calls imsdk API to send a custom message indicating joining the group. This step can be performed at the same time as Step 1.
3. When the record of Viewer 2 joining the room is generated, the business server returns the current number of members in the room.
4. Viewer 1 receives the custom message indicating joining the group from Viewer 2, and the number of online members increases by 1.
5. Viewer 2 calls the business server API for exiting a room, and the record of exiting room is generated.
6. Viewer 2 calls imsdk API to send a custom message indicating exiting the group. This step can be performed at the same time as Step 5.
7. Viewer 1 receives the custom message indicating exiting the group from Viewer 2, and the number of online members decreases by 1.

## Solution 2: Use IMSDK API

There are two ways to get the number of online members in a live room through IMSDK API:

* AVChatRoom acquires the number of members from group data
    * This is not real-time, with a latency of about 1 minute
    * Only number of members is returned
* AVChatRoom registers API TIMGroupEventListener to obtain the number of members when receiving the joining/exiting event
    * Imsdk2.4 is supported
    * A certain latency exists in the statistical result
    * Only number of members is returned
    * Suitable for scenarios with fewer people (e.g. dozens of people). The statistical result has an obvious deviation.

For more information, click [here](https://cloud.tencent.com/doc/product/269/4104#5.3-.E8.8E.B7.E5.8F.96.E8.A7.82.E7.9C.8B. E7.9B.B4.E6.92.AD.E7.9A.84.E4.BA.BA.E6.95.B0).


**Note:**

* Currently, the solution is not available in ILiveSDK. Solution 1 is recommended.

### Flow chart

![](http://mc.qcloudimg.com/static/img/b16adf18652b99993810d07054ec7c9b/image.png)

### Steps
1. Viewer 2 joins the live room.
2. Viewer 1 and Viewer 2 receive the event notification of Viewer 2 joining the group, and the number of online members is updated with the supplied field memberNum.
3. Viewer 2 exits the live room.
4. Viewer 1 receives the event notification of Viewer 2 exiting the group, and the number of online members is updated with the supplied field memberNum.

