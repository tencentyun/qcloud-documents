
腾讯云IM Flutter TUIKit默认自带 英文/简体中文/繁体中文/日语/韩语 语言包，作为界面展示语言。

根据此文档指引，您可以使用默认语言包，也可自定义语言翻译表述，并增添额外的非自带语言的支持。

![](https://qcloudimg.tencent-cloud.cn/raw/c34b74a556b448747369c26714ac9c68.png)

## 使用自带语言

如果您的App，需要的语言仅包括英语/简体中文/繁体中文/日语/韩语，请参考本部分。

### 跟随系统语言

直接使用TUIKit即可，无需额外步骤。插件内部会跟随系统语言自适应。

### 预指定显示的语言

如果您需要在初始化是，手动设置TUIKit界面语言，请在`TIMUIKitCore.getInstance()`中调用`init`方法时，传入需要的语言。

```dart
import 'package:tim_ui_kit/tim_ui_kit.dart';

final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();

final isInitSuccess = await _coreInstance.init(
  language: LanguageEnum.en, // 请在此处定义语言，枚举值见下方
  // ...其他配置
);
```

语言可选项，枚举值为：

```dart
enum LanguageEnum {
  zhHant, //繁体中文
  zhHans, //简体中文
  en, // 英文
  ko, // 韩语
  ja // 日语
}
```

### 实时动态修改

调用 `I18nUtils(null, language);` 即可。此处的 `language` 为 [ISO 639-1 语言代码](#code)。示例如下：

```dart
I18nUtils(null, "en");
```

>? 语言代码清单见[附录](#code)。

## 使用更多语言/自定义翻译表述

如果您需要支持，除 英文/简体中文/繁体中文/日语/韩语 外的更多语言，或更改我们部分词条的翻译，请参考本部分。

>? 本方案仅适用于，目标语言为的阅读方向为从左至右的语言。对于阅读方向从右至左的小语种，如阿拉伯语，请自行在[GitHub fork](https://github.com/TencentCloud/chat-uikit-flutter)一份我们的源码，完成自定义左右镜像开发适配。

### 新增语言词条包

本章节的核心为本部分， 即，将您自定义的国际化多语言词条库文件，注入腾讯云IM项目内。

#### 获取语言模板

在您的项目中，允许如下代码。

```shell
flutter pub run tencent_im_base
```

根据提示，选择 `A` 选项。

![](https://qcloudimg.tencent-cloud.cn/raw/01215e7861ed2736c0155c456ad2d0d6.png)

此时，我们自带的所有语言包，以JSON文件模板的形式，存储于您项目根目录下，`languages/` 路径内。

![](https://qcloudimg.tencent-cloud.cn/raw/2618d546ece854d93cfe21d1ad342ade.png)

请复制一份您熟悉的语言JSON模板文件，例如，简体中文版，`strings_zh-Hans.i18n.json`。

复制一份新的，并命名为 `strings_${语言编码}.i18n.json`。其中，`${语言编码}` 需要替换为 [ISO 639-1 语言代码](#code)。例如，丹麦语，`strings_da.i18n.json`。

如果您需要兼容支持多个新语言，复制多份，并准确指定每一份的语言编码即可。

#### 个性化自定义翻译

此时，您可以修改上一步 **复制新生成的目标语言模板**。

打开您复制生成的新文档，**保留不动JSON的md5 key值**，将所有的value值替换成对应目标翻译语言。

![](https://qcloudimg.tencent-cloud.cn/raw/540536815ec579ca4343a7013a768178.png)

>? 如果您需要修改默认语言模板的翻译文案，也可直接打开自动生成的语言模板，进行修改。**除简体中文版本外**，其他翻译文案，均可修改。

翻译完成后，`languages/` 内，包含原始提供的自带语言模板，及您复制生成的其他语言词条集。

![](https://qcloudimg.tencent-cloud.cn/raw/0b409d05e26b81b60a4babed07936cda.png)

#### 回装您的语言包

在您项目的根目录下，执行 `flutter pub run tencent_im_base` 命令，并选择 `B` 选项。

代码运行完成后，即可使您的语言包，在当前电脑本地生效。

![](https://qcloudimg.tencent-cloud.cn/raw/7823200ee5f323bc254aad61be122907.png)

>? 如果您是团队协同开发，或使用了远程流水线编译。需要在您同事电脑中或流水线编译命令脚本中，使用同样的方式，执行本章节所述方法。

### 跟随系统语言

直接使用TUIKit即可，无需额外步骤。

只要您新增的语言词条包命名[符合标准](#code)，插件内部会跟随系统语言自适应。

### 预指定显示的语言

如果您需要在初始化是，手动设置TUIKit界面语言，请在`TIMUIKitCore.getInstance()`中调用`init`方法时，传入需要的语言。

```dart
import 'package:tim_ui_kit/tim_ui_kit.dart';

final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();

final isInitSuccess = await _coreInstance.init(
  extraLanguage: "ja", // 请在此处定义语言，ISO 639-1 语言代码 见下方
  // ...其他配置
);
```

### 实时动态修改

调用 `I18nUtils(null, language);` 即可。此处的 `language` 为 [ISO 639-1 语言代码](#code)。示例如下：

```dart
I18nUtils(null, "ja");
```

>? 语言代码清单见[附录](#code)。

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

完整版[请见此处](https://quickref.me/iso-639-1)。

## 联系我们[](id:contact)

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)

