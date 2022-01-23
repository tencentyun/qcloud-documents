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
Name | String | 项目名称。
Owner | [Entity](https://cloud.tencent.com/document/api/1156/40360#Entity) | 归属者。
Category | Array  String | 项目类别，取值有：<li>Default：编辑项目</li><li>Live：直播剪辑项目</li><li>StreamConnet：云转推项目</li>
Description | String | 描述信息。
WHRatio | String | 宽高比。
CoverUrl | String | 项目封面URL。
CoverSource | String | 项目封面来源。
FusionData | String | 轨道信息。
Version | Integer | 轨道信息版本号。
CreateTime | String | 创建时间，格式按照 ISO 8601 标准表示。
UpdateTime | String | 最后更新时间，格式按照 ISO 8601 标准表示。