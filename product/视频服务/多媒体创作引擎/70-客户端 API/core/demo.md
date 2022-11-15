# 客户端 API 文档骨架，将根据该文档生成最终的文档。
# 注意：整个文件遵从 python3 语法规范，井号（#）开头的都是注释，而不是 markdown 的标题。
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
AAA | String | AAAA
BBB | String | BBB。 
'''

## 接口示例
Examples = []

### 示例1
e = {}

e['Name'] = '这是示例说明，不能为空，结尾无句号'
e['Description'] = '这是接口描述，可以为空'

#### 注意这里是 python dict，不是裸 JSON
#### 	https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
e['Input'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

#### 注意这里是 python dict，不是裸 JSON
#### 	https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
e['Output'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

Examples.append(e)


### 示例2
e = {}

e['Name'] = '这是示例说明，不能为空，结尾无句号'
e['Description'] = '这是接口描述，可以为空'

#### 注意这里是 python dict，不是裸 JSON
#### 	https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
e['Input'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

#### 注意这里是 python dict，不是裸 JSON
#### 	https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
e['Output'] = {
	'key1' : 'value1',
	'key2' : 'value2'
}

Examples.append(e)