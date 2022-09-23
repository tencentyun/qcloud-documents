; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
; TODO

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
ProjectId | String | 项目 ID。
Definition | Integer | 模板 ID。
ExportDestination | String | 导出目标。
VODExportInfo | [VODExportInfo](#VODExportInfo) | VOD导出信息。
CMEExportInfo | [CMEExportInfo](#CMEExportInfo) | CME导出信息。