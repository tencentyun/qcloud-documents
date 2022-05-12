; 注意：
;   1.数据结构的名称体现在文件名中
;   2. 分号开头是注释
;
; 下一行是描述
媒体基础信息。

; 接下来是参数说明
字段 | 类型 | 描述
------- | ------- | -------
MaterialId | String | 素材 ID。
MaterialType | String | 素材类型，取值如下：<li>VIDEO：视频 </li><li>AUDIO：音频</li><li>IMAGE：图片 </li><li>STICKER：图片转场 </li><li>SUBTITLE：字幕</li><li>TRANSITION：转场</li><li>FILTER：滤镜</li><li>TEXT：文本</li><li>TEXT_IMAGE：图文动效</li><li>LINK：链接</li><li>EFFECT_VIDEO：动效</li><li>STYLE：风格</li><li>WATERMARK：水印</li><li>SWITCHER_LAYOUT：导播台布局</li><li>SWITCHER_EFFECT_TEXT：导播台文字特效</li><li>THIRD_PARTY_PUBLISH_CHANNEL：第三方发布通道</li><li>VIDEO_EDIT_TEMPLATE：视频编辑模板</li>
Name | String | 素材名称。
ClassPath | String | 素材 ID。
CreateTime | String | 创建时间 ,标准ISO格式。
UpdateTime | String | 更新时间 ,标准ISO格式。
TagInfoSet | Array of [MaterialTagInfo](#MaterialTagInfo) | 素材预置标签信息。
TagSet | Array of String | 素材人工标签。
PreviewUrl | String | 素材人工标签。
MediaUrl | Array of String | 素材媒体url。
Owner | [Entity](https://cloud.tencent.com/document/api/1156/40360#Entity) | 素材归属。