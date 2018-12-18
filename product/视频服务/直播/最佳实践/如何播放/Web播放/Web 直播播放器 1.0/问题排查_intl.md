### Error Codes

List of error codes during the use of SDK<span id="errorcode"></span>

- Error messages returned from the frontend

| Message | Description |
|-------|--------------------------------------------|
| An error occurred while parsing video information. Check whether the parameter is correct. | No JSON data is returned from API. Data cannot be parsed. |
| Video information error. Check whether the parameter is correct. | An error occurred while parsing video information |
| Failed to connect the service. Check the network settings. | Failed to obtain the video channel information. |
| Connection to service is denied. | Flash request triggered a security exception. |
| Video data is missing. | Video source data is missing. |
| LVB has finished. Try again later. | NetStream.Play.Stop event |
| LVB has finished. Try again later. | Failed to connect to the LVB source. The LVB source has not pushed video content |


- Error messages returned from the backend

| Code  | Message | Description |
|-------|-----------|---------------------------------------|
| 1   	| Database error | Database connection timed out or an error occurred during query. |
| 2     | Failed to connect to LVB source. LVB source has not pushed video content (hls). | M3U8 file cannot be obtained due to LVB source connection failure. |
| 3     | LVB has finished (hls). | Manifest is not a valid M3U8 file, or LVB source has finished. |
|113	| Connection timeout. Try again later. | The parameter is incorrect. |
|1000 | Incorrect channelID or APPID | The app_id is incorrect (length error). |
|1001 | Invalid parameter. Failed to obtain the bizid. | The app_id is incorrect (with a correct length but wrong content). |                  
| 1009  | LVB source has expired. | The broadcast address is invalid. LVB source has expired. |
| 10000 | Request timeout | Timeout when pulling player configuration and video information. Check your network and try again. Timeout is 10 seconds. |
| 10001 | Failed to parse data | Failed to parse the data obtained by pulling player configuration and video information. It may be caused by a network problem or server exception |
| 10002 | Connection timeout. Try again later | Failed to pull player configuration and video information. It may be caused by a network problem or server exception |
| 10008 | Wrong password. Enter again. | Invalid password |
|10020 | Insufficient balance in LVB account. Top up it in time | The balance is insufficient. |
| 11044 | Invalid request | The APPID is missing |
| 11045 | Channel ID is missing in the request parameter. | Channel ID is missing |
| 11046 | Wrong password. Enter again. | Password is missing |
| 20110 | Wrong password. Enter again. | Invalid password |
| 20113 | LVB has finished. Try again later. | Pulling stream does not exist (downstream type is not exist). |
|20201  | LVB has finished. Try again later. | An error occurred while querying pushing stream (get upstream info error). |
|20301  | LVB channel does not exist. Check the channel ID. | Incorrect channel_id (app_id is correct). |

>**Note:**
>Note: In case of any error code that is not listed in this table, contact customer service. Our engineers can help you solve the problem.

### FAQs

- **Why is the screen distortedly stretched when the video is played in H5?**
 Video stretching is not supported when playing video in H5. Check if the player container has right width/height configuration.

- **Why did I receive the message that "The LVB has finished. Try again later"?**
 If you get no response from the LVB address when attempting to connect to this address and fail to connect to it even after five attempts, this message appears. In this case, you need to verify whether the video stream is being pushed and whether the network connectivity is normal.

-  **The video cannot be hidden on the QQ browser.**
 QQ browser takes over the video playback feature from H5, and the X5 kernel uses self-developed player to play videos. QQ browsers use a unified playback interface to ensure a good user experience. For more information, please see [QQ Browser Documentation](https://x5.tencent.com/tbs/guide.html).

-  **Video is automatically played in full screen mode on iOS.**
 By default, video is played in full screen mode on iOS system due to the webkit setting. To achieve inline playback within an App, you can set the webkit-playsinline attribute. Any Safari browser on iOS below 10 is unable to disable the automatic use of full screen mode.

-  **Why does the Flash player have two play buttons in Chrome on PC?**
 Flash is no longer automatically played starting from Chrome 42. Chrome only plays major Flash contents automatically, while other Flash contents are paused, unless users enable them manually.

-  **Why can I play LVB videos in browsers on PC, but not on mobile devices?**
 Only HLS videos are supported in the browsers on mobile devices. Check whether the LVB pulling address contains an HLS pulling URL.

