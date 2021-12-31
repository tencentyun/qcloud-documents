; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
媒体链接。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
LinkType | String | 链接类型，取值：<li>MATERIAL：媒体</li> <li>CLASS：目录</li>
LinkStatus | String | 链接状态，取值：<li>NOT FOUND：链接找不到</li><li>NORMAL：正常</li><li>FORBIDDEN：禁止访问</li>
LinkMaterialInfo | [MaterialInfo](#MaterialInfo) | 链接媒体信息。
LinkClassInfo | [ClassInfo](#ClassInfo) | 链接素材分类信息。