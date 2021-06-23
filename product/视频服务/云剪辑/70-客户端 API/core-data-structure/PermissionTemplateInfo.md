; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
; TODO

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
Id | String | 模板 ID。
Name | String | 模板名称。
Owner | [Entity](https://cloud.tencent.com/document/api/1156/40360#Entity) | 归属者。
PermissionSet | Array  [Permission](#Permission) | 符合条件的权限集合。
CreateTime | String | 创建时间，格式按照 ISO 8601 标准表示。
UpdateTime | String | 最后更新时间，格式按照 ISO 8601 标准表示。