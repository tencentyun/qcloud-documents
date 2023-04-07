## 功能描述
iOS 端 `TUIKit`默认自带 **简体中文** 和 **英语** 语言包，作为界面展示语言。

根据此文档指引，您可以使用默认语言包，也可自定义语言翻译表述和增加其他语言包。

<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">简体中文<br></th>
    <th style="text-align:center;" width="300px">英文<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/d4ff4c9f9d245f9c015b5e59e7d88f6b.jpeg"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/1bca636bdfe402d4054485b285d20fd0.jpeg" />     </td>
	 </tr>
</table>


## 使用自带语言

如果您的 App 需要的语言仅包括 **简体中文** 和 **英语**，请参考本部分。

### 跟随系统语言

直接使用 `TUIKit` 即可，无需额外步骤。组件内部语言会跟随系统语言。

### 指定显示的语言

如果您需要指定`TUIKit`界面语言，请在`[TUIGlobalization setCustomLanguage:@""]`中传入需要的语言，指定语言后，组件内部不再跟随系统语言。
语言可选项，取值为：

```Java
@"zh-Hans" ,//简体中文 
@"en", // 英文
```

>? 语言代码清单见 [附录](#code)。

## 使用更多语言/自定义翻译表述

如果您的 App 需要支持更多语言，或更改部分词条的翻译，请参考本部分。

>? 本方案仅适用于新增语言阅读方向为从左至右（LTR）的情况。对于阅读方向从右至左（RTL）的语言，如阿拉伯语，请自行在 [GitHub](https://github.com/TencentCloud/TIMSDK) 下载源码，完成 RTL 适配。

本章节以添加韩语语言包为例，讲解新增语言包和自定义翻译的流程。

### 新增语言资源文件

我们自带的所有语言包，以String文件模板的形式，存储于您项目里Pods中`TUICore`组件的`TUIKitLocalizable/Localizable/` 路径。

<img src="https://qcloudimg.tencent-cloud.cn/raw/3c6141f0413a54f2f553b5f97f58edb1.png" style="zoom:40%;"/>


请新建目录并命名为`{语言编码}.lproj`，在此目录下新增 `Localizable.strings`文件，其中，`${语言编码}` 需要替换为 [ISO 639-1 语言代码](#code)。（可以直接复制您熟悉的语言文件，如zh-Hans.lproj，并直接修改目录名称）
如果您需要兼容支持多个新语言，复制多份，并准确指定每一份的语言编码即可。

以韩语为例，新增`ko.lproj/Localizable.strings`的语言资源文件：
<img src="https://qcloudimg.tencent-cloud.cn/raw/2e16061a7fe4fec49e19412b8f093ae8.png" style="zoom:50%;"/>

### 个性化自定义翻译
上一步已经创建好了韩语资源文件 `ko.lproj/Localizable.strings`，
不同语言资源文件中语言的 `key` 是相同的，具体内容可以自定义翻译。

### 跟随系统语言
如果是简体中文、繁体中文、英文、韩语、俄语、乌克兰语，添加完lproj资源包后直接使用TUIKit即可，无需额外步骤。

如果是其他语种，则需要在 `TUIGlobalization.m`中的`+ (NSString *)tk_localizableLanguageKey`

新增的语言词条包命名需要 [符合标准](#code)，组件内部会跟随系统语言自适应。

<img src="https://qcloudimg.tencent-cloud.cn/raw/4c62dfce72cf3148141f5bab1ae1bad7.png" style="zoom:40%;"/>

>? 语言代码清单见 [ISO 639-1 语言代码](#code)。

### 指定显示的语言
如果您需要指定`TUIKit`界面语言，请在`[TUIGlobalization setCustomLanguage:@""]`中传入需要的语言，指定语言后，组件内部不再跟随系统语言。
语言可选项，取值为 [ISO 639-1 语言代码](#code) 
以韩语为例如`[TUIGlobalization setCustomLanguage:@"ko"];`

效果如图所示：
<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/0969ee07a0e552c3566b9b7be75f7674.png" />

[](id:code)
## 附录：语言代码表

| 语言     | 代码     | 语言     | 代码     |
|--------|--------|--------|--------|
| 阿拉伯语   | ar  | 保加利亚语  | bg     |
| 克罗地亚语  | hr     | 捷克语    | cs     |
| 丹麦语    | da     | 德语     | de     |
| 希腊语    | el     | 英语     | en     |
| 爱沙尼亚语  | et     | 西班牙语   | es     |
| 芬兰语    | fi     | 法语     | fr     |
| 爱尔兰语   | ga     | 印地语    | hi     |
| 匈牙利语   | hu     | 希伯来语   | he     |
| 意大利语   | it     | 日语     | ja     |
| 朝鲜语/韩语    | ko     | 拉脱维亚语  | lv     |
| 立陶宛语   | lt     | 荷兰语    | nl     |
| 挪威语    | no     | 波兰语    | pl     |
| 葡萄牙语   | pt     | 瑞典语    | sv     |
| 罗马尼亚语  | ro     | 俄语     | ru     |
| 塞尔维亚语  | sr  | 斯洛伐克语  | sk     |
| 斯洛文尼亚语 | sl     | 泰语     | th     |
| 土耳其语   | tr     | 乌克兰语   | uk  |
| 中文（简体） | zh-Hans | 中文（繁体） | zh-Hant |

完整版 [请见此处](https://quickref.me/iso-639-1)。



## 交流与反馈[](id:feedback)
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/>
