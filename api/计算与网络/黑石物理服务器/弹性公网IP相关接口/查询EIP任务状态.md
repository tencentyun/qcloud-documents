## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipBmQueryTask

查询弹性公网IP异步任务的状态。

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| requestId|是|Int|EIP异步任务返回的requestId，可以参考[EipBmDelete]()的输出|

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码]()。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.status | Int | 当前任务状态：0-成功，1-失败，2-进行中|

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmQueryTask
  &<公共请求参数>&requestId=2383049
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": 0
    }
}

```

