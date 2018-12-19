### 1. How does LVB recording work?
![](//mc.qcloudimg.com/static/img/cbb2aae6b5e767db1d30cb51d147948d/image.png)
When recording is enabled, the audio/video data of a stream will be bypassed to recording system. Every frame pushed from VJ's mobile phone will be written into the recording file by the recording system.

If an LVB push is interrupted, the access layer will immediately notify the recording server to implement the file being written, store it into VOD system and generate an index. Then you can find the new recorded file in VOD system. If you have configured recording event notification on a server, the recording system will send the index ID and online playback URL to the server.

However, an error will occur in the processes of transferring and processing of a large file on the cloud. To ensure success, the maximum recording length of a file is set to 90 minutes, and you can specify a shorter fragment using parameter record_interval.


### 2. How many recording files are generated in an LVB process?
- If the duration of an LVB is too short (for example, shorter than 1 second), there may be no file recorded.
- If the duration of an LVB is not long (shorter than record_interval), and the push is not interrupted during LVB, only one recorded file will be generated.
- If the duration of an LVB is very long (longer than record_interval), the video will be fragmented based on the length of time specified in record_interval, to avoid the time uncertainty of the flow of the file with a longer duration in a distributed system.
- If the push is interrupted during an LVB (SDK will re-push later), a new fragment will be generated every time the interruption occurs.

### 3. How do I know which files belong to a certain LVB?
As PAAS, Tencent Cloud does not know how you defined your LVB. If one of your LVBs lasted for 20 minutes, during which a push interruption caused by network switching occurred, and the LVB was stopped and restarted once manually. Should we calculate the number of LVBs as one or three?

For normal MLVB scenarios, the period between the following two interfaces is defined as one LVB session:
![](//mc.qcloudimg.com/static/img/1df26077a3e59479b658aef63ab7f83d/image.png)
Therefore, the time information sent from APP client is very important. If you wish to define that all the files recorded during this period belong to this LVB, you just need to retrieve received recording notification using LVB code and time information (each recording notification event will come with information such as stream_id, start_time and end_time).

### 4. How to stitch several fragments?
Tencent Cloud allows you to use cloud API to stitch video fragments. For more information about this API, please see [Video Stitching](https://cloud.tencent.com/document/product/266/7821).
 

