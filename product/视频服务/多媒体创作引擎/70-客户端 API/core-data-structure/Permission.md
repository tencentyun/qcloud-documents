; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
权限信息。

; 接下来是参数说明
字段 | 类型 | 必填 | 描述
------- | ------- | ------- | -------
PrimeResource | String | 是 | 一级资源，取值：<li>Material：素材</li><li>Class：分类</li>
SubResource | String | 否 | 二级资源，对应各资源的属性。
PrimeRight | String | 是 | 一级权限,取值：<li>Read：读</li><li>Write：写</li><li>Execute:导出</li><li>Copy:复制</li>
SubRight | String | 否 | 二级权限，取值：<li>Create：新建</li><li>Modify：修改</li><li>Delete：删除</li><li>Download：下载</li>