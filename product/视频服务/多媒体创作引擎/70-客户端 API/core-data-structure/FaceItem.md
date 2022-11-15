; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
人脸信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
Id | String | 人物唯一标识 ID。
Name | String | 人物名称。
Type | String | 人物库类型，表示识别出的人物来自哪个人物库 <li> Default：默认人物库；</li> <li>UserDefine：用户自定义人物库。</li>
FaceUrl | String | 人脸图片地址。
SegmentSet | 	Array of [FaceSegmentItem](#FaceSegmentItem) | 人脸识别结果片段。