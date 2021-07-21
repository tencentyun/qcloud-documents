; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
视频编辑任务信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
ErrCode | Integer | 返回码。
ErrMsg | String | 返回错误信息。
VideoEditProjectInput | [VideoEditProjectInput](#VideoEditProjectInput) | 视频编辑导出任务输入信息。
VideoEditProjectOutput | [VideoEditProjectOutput](#VideoEditProjectOutput) | 视频编辑导出任务输出信息。