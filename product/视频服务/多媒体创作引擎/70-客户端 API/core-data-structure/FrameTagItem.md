; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
帧标签项信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
ItemId | String | 标签项 ID。
StartTimeOffset | Float | 起始时间偏移量，单位：秒。
EndTimeOffset | Float | 结束时间偏移量，单位：秒。
Tags | Array of String | 帧标签。