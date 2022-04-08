; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
搜索空间。

; 接下来是参数说明
字段 | 类型 | 必填 | 描述
------- | ------- | ------- | -------
Platform | String | 是 | 平台。
Owner | [Entity](https://cloud.tencent.com/document/api/1156/40360#Entity) | 是 | 归属。
ClassId | String | 否 | 分类 ID，从该分类路径检索。 不填则默认按根分类路径检索。
SearchOneDepth | bool | 否 | 是否仅搜索 ClassId 这一级分类路径。