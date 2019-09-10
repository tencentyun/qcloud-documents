视频处理除了可以对转码文件的输出路径和输出 Bucket 进行设置外，还提供了丰富的变量来对输出文件名进行设置。视频处理支持的文件名变量及含义如下表：

| 变量名称 | 含义 | 配置示例 | 输出示例<br>（源文件名以`video.mp4`为例） |
| :--: | :--: | :--: | :--- |
| {inputName} | 表示源文件名<br>（不包含目录及后缀名） |  `{inputName}_transcode`  | MP4 转码：<br>`video_transcode.mp4`<br> FLV 转码：<br>`video_transcode.flv` |
| {number} | 用于输出文件编号 | `{inputName}_snapshot_{number}` | JPG 采样截图：<br>`video_snapshot_0.jpg`<br>**...**<br>`video_snapshot_20.jpg` |
| {format}  | 表示文件输出格式  | `{inputName}_transcode.{format}`| HLS 转码：<br>`video_transcode.m3u8`<br>MP4 转码：<br>`video_transcode.mp4`  |
| {definition} | 表示参数模板 ID | `{inputName}_transcode_{definition}` | 高清 MP4 转码：<br>`video_transcode_30.mp4`<br>流畅 MP4 转码：<br>`video_transcode_10.mp4`  |

文件名变量一般用于标记和识别转码输出文件，避免文件重名引起的文件被覆盖问题，可以只使用一个变量，也可以同时使用多个变量，您可以根据需要自由选择。您也可以加入任意常量字符串来标记文件名，例如上表中的"transcode"和"snapshot"等。
