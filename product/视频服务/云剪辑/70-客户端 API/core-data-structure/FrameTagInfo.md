; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
帧标签。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
Version | String | 帧标签版本标识。
FrameTagSet | Array of [FrameTagItem](#FrameTagItem) | 帧标签。
LastTimeOffset | Float | 本次结果的最大偏移时间，返回值不为-1则下次从该时间开始查询，单位：秒。