; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
媒体元信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
Size | Integer | 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
Container | String | 容器类型，例如 m4a，mp4 等。
Bitrate | Integer | 视频流码率平均值与音频流码率平均值之和，单位：bps。
Height | Integer | 视频流高度的最大值，单位：px。
Width | Integer | 	视频流宽度的最大值，单位：px。
Duration | Float | 视频时长，单位：秒。
Rotate | String | 视频拍摄时的选择角度，单位：度。
VideoStreamSet | Array of [MediaVideoStreamItem](#MediaVideoStreamItem) | 视频流信息。
AudioStreamSet | Array of [MediaAudioStreamItem](#MediaAudioStreamItem) | 音频流信息。
