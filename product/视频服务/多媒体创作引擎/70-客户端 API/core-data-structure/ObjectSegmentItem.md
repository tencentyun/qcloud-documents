; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
物体识别片段。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
StartTimeOffset | Float | 识别片段起始的偏移时间，单位：秒。
EndTimeOffset | Float | 识别片段终止的偏移时间，单位：秒。
Confidence | Float | 识别片段置信度。取值：0~100。
AreaCoordSet | Array of Integer	 | 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。