<span id = "celueyufa"></span>
## 策略语法
CAM 策略：
```
{	 
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"effect", 
              "action":["action"], 
              "resource":["resource"], 
               "condition": {"key":{"value"}} 
           } 
       ] 
} 
```
- **版本 version：** 必填，目前仅允许值为"2.0"。
- **语句 statement：** 描述一条或多条权限的详细信息。该元素包括 effect、action、resource、condition 等多个其他元素的权限或权限集合。一条策略有且仅有一个 statement 元素。
 - **操作 action：**必填，描述允许或拒绝的操作。操作可以是 API（以 name 前缀描述）或者功能集（一组特定的 API，以 permid 前缀描述）。
 - **资源 resource：**必填，描述授权的具体数据。资源是用六段式描述。每款产品的资源定义详情会有所区别。有关如何指定资源的信息，请参阅您编写的资源声明所对应的产品文档。
 - **生效条件 condition：**非必填，描述策略生效的约束条件。条件由操作符、操作键和操作值组成。条件值可以是客户端 IP 地址。
 - **影响 effect：**必填，描述声明产生的结果是“允许”还是“显式拒绝”，即 allow（允许）和 deny（显式拒绝）两种情况。

<span id = "caozuo"></span>
## ASR 的操作
在 CAM 策略语句中，您可以从支持 CAM 的任何服务中指定任意的 API 操作。对于 ASR，请使用以 `name/asr:` 为前缀的 API。例如：`name/asr:CreateModel` 或者 `name/asr:CreateAsrVocab`。
- 如果您要在单个语句中指定多个操作的时候，请使用逗号将它们隔开，如下所示：
```
"action":["name/asr:action1","name/asr:action2"]
```
您也可以使用通配符指定多项操作。例如，您可以指定名字以单词"Describe"开头的所有操作，如下所示：
```
"action":["name/cvm:Describe*"]
```
- 如果您要指定 ASR 中所有操作，请使用 * 通配符，如下所示：
```
"action"：["name/asr:*"]
```

<span id = "ziyuanlujing"></span>
## ASR 的资源路径
每个 CAM 策略语句都有适用于自己的资源。资源路径的一般形式如下：
```
qcs:project_id:service_type:region:account:resource
```
- **project_id**：描述项目信息，仅为了兼容 CAM 早期逻辑，无需填写。
- **service_type**：产品简称，填写 asr。
- **region**：地域信息，ASR 无需填写。
- **account**：资源拥有者的根帐号信息，如 uin/164256472。
- **resource**：各产品的具体资源详情，如 model/model_id1 或者 `model/*`。

例如，您可以使用特定自学习模型 (15b96676edb211ea9301b49691037310) 在语句中指定它，如下所示：
```
"resource":[ "qcs::asr::uin/164256472:model/15b96676edb211ea9301b49691037310"]
```
您还可以使用 * 通配符指定属于特定账户的所有自学习模型，如下所示：
```
"resource":[ "qcs::asr::uin/164256472:model/*"]
```
您要指定所有资源，或者如果特定 API 操作为接口级权限，请在 resource 元素中使用 * 通配符，如下所示：
```
"resource": ["*"]
```
如果您想要在一条指令中同时指定多个资源，请使用逗号将它们隔开，如下所示为指定两个资源的示例：
```
"resource":["resource1","resource2"]
```
下表描述了 ASR 能够使用的资源和对应的资源描述方法。在下表中，$为前缀的单词均为代称。其中，account 指代的是账户 ID。

| 资源 | 授权策略中的资源描述方法 |
|---------|---------|
| 自学习模型 | `qcs::asr::$account:model/$ModelId` |
| 热词表 | `qcs::asr::$account:vocab/$VocabId` |
