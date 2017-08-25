## 1. 接口描述
该接口用于更改弹性公网EIP的别名。用户通过该接口自定义申请到的EIP的别名，方便管理。
 
域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: ModifyEipAlias



## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipId|是|String|EIP实例ID，可以通过[DescribeEipBm](/doc/api/456/6671)接口查询|
| eipName|是|String|待设定的EIP名称，仅可以使用英文、汉字、数字、连接线"-"或下划线"_"|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |


## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30009|EipNotExist|操作的EIP记录不存在|

## 5. 示例
 
输入
```

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=ModifyEipAlias
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>&eipId=eip-test&eipName=test
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```

