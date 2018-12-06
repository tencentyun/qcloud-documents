Select whether to transcode in real time. After selecting, you can get the corresponding link addresses in subsequent steps.
![](https://main.qcloudimg.com/raw/359df4c0dc49d7c9a85d3a5b641c6893.png)
**HD:** Resolution 1280x720. Bitrate 900 kbps
**SD:** Resolution 960x540. Bitrate 550 kbps
**Original:** Original resolution. Bitrate is the original bitrate (always presented).
After the resolution is specified, the backend provides different addresses corresponding to different bitrates when it generates the playback address, so that you can choose one to call. Since the generated video resolution is strictly in line with the above ratio, the original push resolution should be as close as possible to the above ratio to avoid extension or distortion of views.
When users access a new bitrate address for the first time, the user who first triggers the link may experience a long load time, which is normal. Users who access the address subsequently can enjoy a consistent experience.

**You can use the real-time transcoding feature by following the method below:**
1. If you use Tencent Cloud Web player SDK, after the transcoding is enabled, the player automatically displays the appropriate bitrate according to the channel settings at the location where the resolution is selected in the lower right corner. You can make adjustments manually. Default settings are as follows:
	1. PC: The original resolution is preferred.
	2. Mobile: **High definition** with resolution of 900 Kbps is preferred. If it is unavailable, the original resolution is used.
2. Directly access to the corresponding bitrate address, and play videos using a third-party player.
