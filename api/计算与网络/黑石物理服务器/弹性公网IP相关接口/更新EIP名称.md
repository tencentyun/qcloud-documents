## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: ModifyEipAlias

更改弹性公网EIP别名。

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipId|否|String|EIP实例ID，可以通过[DescribeEipBm]()接口查询|
| eipName|否|String|待设定的EIP名称，仅可以使用英文、汉字、数字、连接线"-"或下划线"_"|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码]()。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |


## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &<公共请求参数>&eipId=eip-test&eipName=test
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {}
}

```

