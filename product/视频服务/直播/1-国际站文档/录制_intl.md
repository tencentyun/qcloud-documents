You can record LVB channels through the API. For more information, please see [LVB API](http://cloud.tencent.com/doc/api/258/API%E6%A6%82%E8%A7%88). Recorded files are automatically stored on the VOD platform. Therefore, before using the recording feature, you need to activate VOD service in advance and purchase space and traffic for storing and playing recorded video files. For more information, please see [Video on Demand](http://cloud.tencent.com/product/vod.html).

**Steps:**
1. Activate VOD service.
2. Use the API for creating a recording task.
3. Use the API for ending a recording task.
4. Use the API for querying recorded fragments to get fileID.
5. Obtain the playback address or perform operations such as transcoding on the VOD platform according to fileID (optional).

For more information on APIs for performing operations on files on the VOD platform, please see [VOD API Overview](https://cloud.tencent.com/document/product/266/7788).

**Specifications:**
1. Videos are recorded based on the original LVB bitrate. The output format is FLV.
2. Recording format: The maximum recording length of a single file is 30 minutes. A new file is created for recording if the limit is exceeded.
3. The maximum recording length of a single recording task is 24 hours.
4. During the LVB, you can obtain a recorded file in about 5 minutes upon the end of recording process. For example, if an LVB is recorded from 12:00, the corresponding fragment from 12:00 to 12:30 is available around 12:35, and so on.
5. **Note:** Fees for the recorded file are generated in the VOD platform. Pay attention to the relevant costs based on your actual needs. For more information on billing methods, please see [Video on Demand](http://cloud.tencent.com/product/vod.html).
