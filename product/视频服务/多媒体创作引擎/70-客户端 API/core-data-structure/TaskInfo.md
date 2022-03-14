; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
任务信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
TaskId | String | 任务 ID。
Status | String | 任务状态 ，取值：<li>PROCESSING:处理中；</li><li>SUCCESS：成功</li><li>FAIL：失败 </li> 
Progress | Integer | 任务进度。
CreateTime | String | 创建时间，标准ISO格式。
