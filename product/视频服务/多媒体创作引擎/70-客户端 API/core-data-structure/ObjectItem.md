; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
物体识别结果。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
ItemId | String | 物体识别版本号。
Name | String | 识别的物体名称。
SegmentItemSet | Array of [ObjectSegmentItem](#ObjectSegmentItem) | 物体出现的片段列表。