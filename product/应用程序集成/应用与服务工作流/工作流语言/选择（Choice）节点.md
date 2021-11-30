## 概述

**Choice 节点**，也称**选择节点**，可以为工作流添加分支逻辑。Choice 节点会根据计算结果选择对应的分支，执行分支任务。

## 参数

除了 [常见字段](https://cloud.tencent.com/document/product/1272/51544#step3) 之外，Choice 节点还支持以下字段：

| 字段            | 描述                                                |
| --------------- | --------------------------------------------------- |
| Choices（必填） | 选项规则数组，确定状态节点可能的分支节点。          |
| Default（可选） | 没有匹配到 Choices 中的分支时，默认将要执行的分支。 |

> !Choice 状态不支持 **End** 和 **Next** 字段。具体分支节点的运行由 **Choices** 内部对应的分支定义。

### 选项规则

Choice 节点必须定义 "Choices" 键值，它对应一个数组，数组的每个元素是一个**选项规则**的数据类型。

**选项规则**包含以下内容：

- Variable：变量名，指定输入变量的路径名称。
- 比较运算：比较运算有很多类型，键名对应特定的比较运算类型，对应的数值可以为静态值或者指定路径
- Next：符合此分支的条件将进入的下一个节点名称，必须与工作流中的状态名相匹配。

下列示例检查字符串是否等于 Mathematics：

```
{
	"Variable": "$.subject",
	"StringEquals": "Mathematics",
	"Next": "Math"
}
```

**选项规则**支持以下比较运算符：

- BooleanEquals：比较布尔值是否等于设定值。
- NumericEquals：检查数值是否等于设定值。
- IsBoolean：检查变量类型，是否为布尔值。
- IsNumeric：检查数据类型，是否是数值。
- StringEquals：检查字符串是否等于设定值。

## 示例

以一个用于分支计算逻辑的数组为例，下面为 Choices 节点的使用示例：

```
{
	"Comment": "",
	"StartAt": "ChoiceGender",
	"States": {
		"ChoiceGender": {
			"Type": "Choice",
			"Choices": [{
					"Variable": "$.female",
					"BooleanEquals": true,
					"Next": "Gender"
				},
				{
					"Variable": "$.age",
					"NumericEquals": 18,
					"Next": "Age"
				}
			],
			"Default": "Other"
		},
		"Gender": {
			"Comment": "This is a female",
			"Type": "Pass",
			"End": true
		},
		"Age": {
			"Comment": "This is a adult",
			"Type": "Pass",
			"End": true
		},
		"Other": {
			"Comment": "Sorry,I can't judge it.",
			"Type": "Pass",
			"End": true
		}
	}
}
```

在此示例中，ChoicesGender 中含有两个分支逻辑，第一个逻辑检查变量 female 的值是否为真，如果为真，即进入此分支逻辑对应的 Next 节点。第二个分支逻辑检查变量 age 对应的值。此分支检查变量 age 的值是否为18，如果等于，则即进入此分支逻辑对应的 Next 节点。Choice 分支逻辑的检查按照 ChoiceGender 定义的顺序，如果进入第一个分支，则不会进入第二个分支。如果所有分支都不符合，则会进入 Default 键名对应的节点。

假设输入此节点的信息为：
```
{
	"name": "John",
	"female": false,
	"age": 18
}
```

那么此分支逻辑将进入第二个分支逻辑，并且进入 Age 节点。
