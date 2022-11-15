#!/usr/local/bin/python3
#coding=utf-8

########################################################
#此行以下，至 #REMOVE-CONTENT-BEFORE-HERE 这一行，均为单独执行本脚本时的实例代码。真正被调用时会被干掉


## 接口名称
Action = '/FirstName/SecondName'

## 接口描述
Description = '这是接口描述这是接口描述这是接口描述'

## 接口分类，最后会依照分类进行汇总，生成接口概览
Class = '接口分类接口分类'

## 接口输入
Input = '''
字段 | 类型 | 必填 | 描述
------- | ------- | ------- | -------
AAAA | BBBB | CCCC | DDDD
'''

## 接口输出
Output = '''
字段 | 类型 | 描述
------- | ------- | -------
AAAA | BBBB | CCCC
'''

## 接口示例
Examples = []

### 示例1
e = {}

e['Name'] = '这是示例说明这是示例说明'
e['Description'] = '这是接口描述'

e['Input'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

e['Output'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

Examples.append(e)


### 示例2
e = {}

e['Name'] = '这是示例说明这是示例说明'
e['Description'] = '这是接口描述'

e['Input'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

e['Output'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

Examples.append(e)

########################################################
#此行以上的代码，均为示例代码
#REMOVE-CONTENT-BEFORE-HERE
import os
import string
import json

## 读取模板
docTemplate = ''
exampleTemplate = ''
with open('./tool/doc-template.md') as f:
	docTemplate = string.Template(f.read())

with open('./tool/example-template.md') as f:
	exampleTemplate = string.Template(f.read())


## 渲染 Examples
exampleStringAry = []
exampleIndex = 1

for e in Examples:
	exampleStringAry.append(exampleTemplate.substitute(
		Action = Action,
		Index = exampleIndex,
		Name = e['Name'],
		Description = e['Description'],
		Input = json.dumps(e['Input'], indent=4, ensure_ascii=False),
		Output = json.dumps(e['Output'], indent=4, ensure_ascii=False),
	))
	exampleIndex += 1

## 渲染文档
if len(Output.strip()) == 0:
  Output = '>! 除公共返回字段外，该接口无其他返回字段。'

docContent = docTemplate.substitute(
	Action = Action,
	Description = Description,
	Input = Input,
	Output = Output,
	Example = '\n'.join(exampleStringAry)
)
print("%s" % docContent)