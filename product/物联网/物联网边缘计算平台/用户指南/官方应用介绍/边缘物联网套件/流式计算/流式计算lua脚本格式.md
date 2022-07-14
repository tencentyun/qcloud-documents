格式：输入（选择指定产品和设备所产生的消息）-> 过滤/计算（采用表达式对消息进行判断）-> 输出（处理过后的消息输出到数据源），其中 lua 脚本中的 \_filter 代表一条流计算对象。


例如：
``` 
fn = function(result)
    -- 过滤,在回调函数里做条件判断
    result=_filter:select(result, function(item) return (item:getValue("temperature")> 100) end)

    -- 过滤后结果不为空就输出到id为1000000的数据源
    if result ~= nil then
        _filter:output(result, 1000000)
    end
end

-- 输入数据,在回调函数里处理消息
_filter:input("AVH61RXGPP",{"device01"},{"ProductID","DeviceName","Timestamp","2020-12-12 08:30:00"},fn)
```


## 目前 \_filter 有以下成员函数

### 消息输入函数
\_filter:input(productID, deviceNameList, propertyIDList, callback)
输入参数:

|参数 | 描述 |
| ------ | ------ |
|ProductID | 产品 id,string 类型 |
| DeviceNameList | 设备列表,table 类型 |
| PropertyIDList | 属性列表(json 消息字段) |

返回参数: 无

### 消息过滤函数
\_filter:select(result, callback)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result | 上级处理结果，userdata 类型 |
| callback | 回调函数，在这里做条件判断， 入参为 item 对象, 返回类型为 bool, item 成员函数为 getValue("属性id") |

返回参数：

|参数 | 描述 |
| ------ | ------ |
|result | 处理结果，userdata 类型 |

### 聚合计算函数
\_filter:aggregate(result, unit, winType, winLen, winStep, max, min, sum, mean)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result | 上级处理结果，userdata 类型 |
|unit | 统计粒度, "one"或"all",string 类型 |
|winType | 窗口移动方式, sliding、rolling, string 类型 |
| winLen| 窗口时长,单位是秒,数值类型|
| winStep| 滑动步长,单位是秒,数值类型|
|max | 计算最大值,string 类型|
| min| 计算最小值,string 类型 |
|sum | 计算总和,string 类型|
|mean | 计算平均值,string 类型|

返回参数：

|参数 | 描述 |
| ------ | ------ |
|result | 处理结果，userdata 类型 |

### 连续大于比较函数
\_filter:morethan(result,continuous,propertyID,value)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result | 上级处理结果，userdata 类型 |
|continuous|连续多少次大于 value 值,数值类型|
|propertyID|属性 id, string 类型|
|value|比较值, 数值类型|

返回参数：

|参数 | 描述 |
| ------ | ------ |
|result | 处理结果，userdata 类型 |

### 连续小于比较函数
\_filter:lessthan(result,continuous,propertyID,value)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result | 上级处理结果，userdata 类型 |
|continuous| 连续多少次小于 value 值,数值类型 |
|propertyID|属性 id, string 类型|
|value|比较值, 数值类型|

返回参数：

|参数 | 描述 |
| ------ | ------ |
|result | 处理结果，userdata 类型 |

### 结果合并函数
\_filter:merge(result1,result2)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result1|处理结果，userdata 类型|
|result2|处理结果，userdata 类型|

返回参数：

|参数 | 描述 |
| ------ | ------ |
|result|result1 和 result2 合并后的结果，userdata 类型|

### 结果输出函数
\_filter:output(result, datasourceID)
输入参数：

|参数 | 描述 |
| ------ | ------ |
|result|上级处理结果，userdata 类型|
|datasourceID|数据源 id,数值类型|
 
