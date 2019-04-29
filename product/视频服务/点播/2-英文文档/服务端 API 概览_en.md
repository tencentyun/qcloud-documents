### Video Upload
| Feature | API Name | Description |
|-|-|-|
| Initiate upload | [ApplyUpload](https://cloud.tencent.com/document/product/266/9756) | Initiate video upload and obtain meta-information used to upload files to Tencent Cloud COS. |
| Upload file | | Upload video (and cover) file. |
| Confirm upload | [CommitUpload](https://cloud.tencent.com/document/product/266/9757) | Confirm upload of video files (and cover files), and obtain playback URLs and IDs of the files. |
| Upload Video via URL Pull | [MultiPullVodFile](https://cloud.tencent.com/document/product/266/7817) | Pull a batch of video files to Tencent Cloud from existing resource library using the URL passed by the user. |
### Video Processing
| Feature | API Name | Description |
|-|-|-|
| Process videos using task flows |	[RunProcedure](https://cloud.tencent.com/document/product/266/11030) | Process a video file based on specified process parameters. For more information on specific process parameters, contact Tencent Cloud VOD. |
| Process video files |	[ProcessFile](https://cloud.tencent.com/document/product/266/9642) | Developers can use this API to initiate various processing tasks for a single video. |
| Video transcoding |	[ConvertVodFile](https://cloud.tencent.com/document/product/266/7822) | Transcode the video file based on the transcoding configuration in the console. |
| Video clipping |	[ClipVideo](https://cloud.tencent.com/document/product/266/10156) | Clip the source video file based on the specified time offset. |
| Video Stitching |	[ConcatVideo](https://cloud.tencent.com/document/product/266/7821) | Stitch multiple video files into a new video file, and add it to the VOD system. |
| Capture screenshots at specified time points |	[CreateSnapshotByTimeOffset](https://cloud.tencent.com/document/product/266/8102) | Obtain screenshots of a video file at specified time points. |
| Capture Image Sprite Screenshots |	[CreateImageSprite](https://cloud.tencent.com/document/product/266/8101) | Capture screenshots of a video file and generate image sprites. |
### Media Asset Management
| Feature | API Name | Description |
|-|-|-|
| Get video information |	[GetVideoInfo](https://cloud.tencent.com/document/product/266/8586) | Acquire various information of a single video, or specify that only partial information is returned. |
| Get video information according to video name prefix |	[DescribeVodPlayInfo](https://cloud.tencent.com/document/product/266/7825) | Search videos according to name prefixes and return the playback information list. |
| Query video information according to VID |	[DescribeRecordPlayInfo](https://cloud.tencent.com/document/product/266/8227) | The recorded video files from Tencent Cloud LVB and ILVB enter the VOD system. Each recorded file has a unique video_id (vid). |
| Add video tags |	[CreateVodTags](https://cloud.tencent.com/document/product/266/7826) | Add video tags. |
| Delete video tags |	[DeleteVodTags](https://cloud.tencent.com/document/product/266/7827) | Delete video tags. |
| Delete videos |	[DeleteVodFile](https://cloud.tencent.com/document/product/266/7838) | Delete video files. |
| Modify video attributes |	[ModifyVodInfo](https://cloud.tencent.com/document/product/266/7828) | Modify the description information of video files, such as category, name, description and expiration time. |
| Add video keyframe descriptions |	[AddKeyFrameDesc](https://cloud.tencent.com/document/product/266/14190) | Add video keyframe description. A maximum of 100 keyframe descriptions can be added for each video file. |
| Delete video keyframe descriptions |	[DeleteKeyFrameDesc](https://cloud.tencent.com/document/product/266/13442) | Delete video keyframe descriptions. Multiple keyframe descriptions of a single video can be deleted at one time. |
### Video Category Management
| Feature | API Name | Description |
|-|-|-|
| Create video categories |	[CreateClass](https://cloud.tencent.com/document/product/266/7812) | Create categories to manage video files. |
| Acquire video category hierarchy |	[DescribeAllClass](https://cloud.tencent.com/document/product/266/7813) | Acquire all category class relationships of the current user. |
| Acquire video category information |	[DescribeClass](https://cloud.tencent.com/document/product/266/7814) | Acquire global category list, as well as detailed information of each category. |
| Modify video categories |	[ModifyClass](https://cloud.tencent.com/document/product/266/7815) | Modify attributes of a video category, including name. |
| Delete video categories |	[DeleteClass](https://cloud.tencent.com/document/product/266/7816) | Delete video categories. |
### Event Notification and Task Management
| Feature | API Name | Description |
|-|-|-|
| Pull event notifications |	[PullEvent](https://cloud.tencent.com/document/product/266/7818) | Obtain event notifications from the VOD server. |
| Confirm event notifications |	[ConfirmEvent](https://cloud.tencent.com/document/product/266/7819) | Confirm that the message has been received after the developer calls to pull the event notification and gets the event. |
| Query task list |	[GetTaskList](https://cloud.tencent.com/document/product/266/11722) | Query task list. Tasks within the last three days (72 hours) can be queried. |
| Query task information |	[GetTaskInfo](https://cloud.tencent.com/document/product/266/11724) | Obtain task execution status. Only tasks within the last three days (72 hours) can be queried. |
| Retry tasks |	[RedoTask](https://cloud.tencent.com/document/product/266/11725) | Only tasks finished within the last three days (72 hours) can be retried. Retrying the task does not change the task ID, and data will be overwritten if the retry succeeds. |
### Parameter Template Management
| Feature | API Name | Description |
|-|-|-|
| Create transcoding template |	[CreateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9910) | Create a transcoding template. |
| Query transcoding template list |	[QueryTranscodeTemplateList](https://cloud.tencent.com/document/product/266/9913) | Query transcoding template list. |
| Query transcoding template |	[QueryTranscodeTemplate](https://cloud.tencent.com/document/product/266/9912) | Query transcoding template details. |
| Update transcoding template |	[UpdateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9911) | Update a transcoding template. |
| Delete transcoding template |	[DeleteTranscodeTemplate](https://cloud.tencent.com/document/product/266/9914) | Delete a transcoding template. |
### Watermark Template Management
| Feature | API Name | Description |
|-|-|-|
| Apply for uploading watermark files |	[ApplyUploadWatermark](https://cloud.tencent.com/document/product/266/11607) | When creating a watermark template, you can use this API to obtain the upload URL of the watermark file. |
| Create watermark template |	[CreateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11599) | Create a watermark template. |
| Query watermark template list |	[QueryWatermarkTemplateList](https://cloud.tencent.com/document/product/266/11608) | Query watermark template list. |
| Query watermark template |  [QueryWatermarkTemplate](https://cloud.tencent.com/document/product/266/11606) | Query the watermark template details according to its ID. |
| Update watermark template |	[UpdateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11605) | Update a watermark template. |
| Delete watermark template |	[DeleteWatermarkTemplate](https://cloud.tencent.com/document/product/266/11604) | Delete a watermark template. |
### Key Management
| Feature | API Name | Description |
|-|-|-|
| Obtain video decryption key |	[DescribeDrmDataKey](https://cloud.tencent.com/document/product/266/9643) | After the video encryption task is completed successfully, you can call the API to obtain the data key of video encryption, and save the data key. |
### Data Statistics
| Feature | API Name | Description |
|-|-|-|
| Obtain storage |	[DescribeVodStorage](https://cloud.tencent.com/document/product/266/10012) | Obtain the billed VOD storage till the last 23:59:59. |
| Obtain download URL of playback statistics file |	[GetPlayStatLogList](https://cloud.tencent.com/document/product/266/12624) | Query the download URLs of playback statistics files in each day. |
## Appendix
The following server APIs are discarded. For more information on the reasons, please see the corresponding documents.

| Feature | API Name | Description |
|-|-|-|
| Acquire video information |	[DescribeVodPlayUrls](https://cloud.tencent.com/document/product/266/7824) | Acquire the playback information of the current video, including playback URLs, format, bit rate, height, and width. |
| Acquire video information in batches|	[DescribeVodInfo](https://cloud.tencent.com/document/product/266/7823) | Acquire video attributes via FileID, including name, tag and creation time. |
| Process video according to specified process |	[ProcessFileByProcedure](https://cloud.tencent.com/document/product/266/9045) | Process a video file according to specified process parameters. The main processes include transcoding, creating image sprites, taking screenshots, etc. For more information on specific process parameters, contact Tencent Cloud VOD. |
| Simple HLS video clipping |	[SimpleClipHls](https://cloud.tencent.com/document/product/266/8859) | Clip the source video file based on the specified time offset to generate a new video file (target file) with a new FileID. |
| Set screenshot URL as video cover |	[DescribeVodCover](https://cloud.tencent.com/document/product/266/8814)|-|

















