In scenarios such as LVB recording and UGC short videos, the video content is unpredictable. To prevent non-compliant contents from appearing on the VOD platform, developers need to review the uploaded video, and then transcode and distribute it only after it is confirmed to be compliant. Tencent Cloud Short Video solution provides the AI porn detection capability, which can automatically identify pornographic contents in videos.
## How to Use AI Porn Detection
The AI porn detection feature needs to be integrated into the video processing task flow. The detection result is sent to the App backend server via an event notification. Tencent Cloud VOD builds in a task flow named QCVB_ProcessUGCFile for UGC short video porn detection scenarios. When a user uses this task flow and specifies to perform AI porn detection, the porn detection is executed first, and the performance of subsequent processing (transcoding, watermarking, and capturing screenshots, etc.) is determined based on the detection result. The flow chart is as follows:
![Figure description](https://main.qcloudimg.com/raw/6b05d91e221481b34c28da69cf90433c.jpg)

## AI Porn Detection Template Overview

| Template ID | How to Deal with Videos Detected to Be Porny | Sampling Frequency |
| ------ | -------------------------------------------- | ------------------------------------------------------------ |
| 10 | Terminate the task flow (transcoding, watermarking, capturing screenshots, etc. will not be performed) | For videos with a duration less than 500 seconds, sampling is performed once per second; for videos with a duration longer than or equal to 500 seconds, sampling is performed at an interval of 1% of the video duration. |
| 20 | Continue the task flow | None |







## Example of AI Porn Detection Access
 __[Step 1] Submit an AI porn detection task when generating an upload signature__ 
``` 
/**
 * Respond to the signature request and upload the video with the AI porn detection task
 */
function getUploadSignature(req, res) {
    res.json({
        code: 0,
        message: 'ok',
        data: {
            //Specify the template parameter and the task flow for the uploaded video
            signature: gVodHelper.createFileUploadSignature({ procedure: 'QCVB_SimpleProcessFile({1,1,1,1})' })
        }
    });
}
``` 
 __[Step 2] Obtain the AI porn detection result via the event notification__ 

``` 
/**
 * Obtain the AI porn detection result via the event notification
 */
function getAiReviewResult(event){
    let data = event.eventContent.data;
    if(data.aiReview){
        return data.aiReview;
    }
    return {};
}
``` 



