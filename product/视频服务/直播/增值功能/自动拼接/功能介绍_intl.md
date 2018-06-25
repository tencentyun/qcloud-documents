### Background
**Why video stitching is necessary?**
Switching from LVB to VOD is a common application scenario for LVB events. That is, record the LVB stream for VOD playback. This switching relies on LVB recording feature. A file URL is generated upon the completion of the LVB recording, and the video is available for VOD playback after the file URL is published. Recording mechanism: recording starts as push starts, and ends when push is suspended with a recording file and a file URL generated.

Recording may be suspended due to poor network, VJ-side exception or other factors, and consequently, a LVB event may be recorded as multiple files. This means that multiple VOD URLs have to be published for end users to watch the complete video, which is obviously unreasonable. Therefore, multiple recording files must be stitched into a complete file before publishing.
		
**Why automatic stitching is necessary?**
The old file stitching feature provided in Tencent Cloud LVB service requires manual calling of APIs, which takes long and cost a lot. To make file stitching more convenient and efficient, LVB service launches HLS automatic stitching feature.
### Description
#### Automatic Stitching Overview
When push is suspended due to VJ-side exception, the recording module continues the recording as long as the push renews within a specified time, rather than creating another recording file. After the push is completed (no push occurs in a specified period), a complete recording file (instead of multiple clips) is generated.

#### Feature Description
1. Requirements for automatic file stitching
 - The type of recording files must be HLS, that is, the source files to be stitched must be HLS files. MP4 and FLV are not supported for now.
 - The files can only be stitched as HLS files.
 - Audio files to be stitched must be consistent in encoding type, sampling rate, and number of tracks, and video files to be stitched must be consistent in encoding type. Otherwise player compatibility issues may occur.
 - The video files to be stitched may have different bitrate and resolution.
2. No limit on number of times recording is suspended
No matter how many times a push is suspended, the recording will continue as long as the push renews within a specified time. 
3. Suspending duration can be configured
You can configure how long a push is allowed to be suspended for the automatic stitching feature. The current setting is 5 minutes.   
4. URL of recording file
The URL of the recording file is the URL of the m3u8 file. One URL is generated each time the push is suspended. The content of the m3u8 URL is the video content till the push is suspended. The m3u8 URL generated after the push completes is the complete video content. 
5. Automatic stitching feature does not work
Generally, if the automatic stitching feature is enabled and the push renews within the specific time, files will be automatically stitched. However, if push is suspended by calling the ban API, files will not be automatically stitched, and the recording will restart after push renews.
6. Obtaining the recording file's URL
The URL of recording file is returned via a callback. Now, you will receive a callback of the recording file URL each time the push is suspended. Note: to ensure the completeness of published VOD file, we recommend that you publish the last callback URL when there is no push for the specified suspending period.
7. File display
Just as ordinary recording files, automatically stitched files are also displayed on the VOD console.
