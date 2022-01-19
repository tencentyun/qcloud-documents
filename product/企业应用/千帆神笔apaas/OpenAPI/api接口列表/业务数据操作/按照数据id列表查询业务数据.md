1. **接口说明**

接口请求地址：/metadata/DescribeEntityRecordsById

该接口用于通过业务数据Id查询数据，单次请求数据量上限为1000条。

Id值来自于应用系统业务数据RecordId，如创建业务数据成功后返回结果。



2. **输入参数**

| 参数名称 | 必选 | 类型             | 描述                                                         |
| -------- | ---- | ---------------- | ------------------------------------------------------------ |
| Entity   | 是   | String           | 对象 ID                                                      |
| Ids      | 是   | Array of Integer | 业务数据的id列表                                             |
| Fields   | 否   | Array of String  | 期望查询结果返回的字段ID，<br />若不传此参数，则默认展示所有字段ID |

3. **输出参数**

| 参数名称     | 类型            | 描述                                           |
| ------------ | --------------- | ---------------------------------------------- |
| TotalCount   | Integer         | 返回数据总数                                   |
| EntityRecord | Array of Object | 返回的数据信息，<br />下方表格进一步展示其内容 |

**EntityRecord**

| 参数名称   | 类型    | 描述                                             |
| ---------- | ------- | ------------------------------------------------ |
| Id         | Integer | 业务数据Id                                       |
| Entity     | String  | 对象ID                                           |
| MainField  | String  | 对象主字段值                                     |
| FieldValue | Object  | 具体返回的数据信息映射，<br />格式：{字段ID: 值} |



4. **示例**

> 查询id为123和456的订单信息

```json
{
  // 省略通用请求部分，参考调用前须知
  "Entity": "order",
  // 业务数据RecordId, 当前值来自于批量创建业务数据返回值
  "Ids": [1481167475391438890, 1481167475391438891, 1481167475391438892],
  "Fields": ["orderNumber", "orderPrice", "status"]
}
```

> 返回结果

```json
{
  TotalCount: 2,
  EntityRecordSet:[
    {
      "Id": 1481167475391438890, // 该条业务数据对应的RecordId
      "Entity": "order",
      "MainField": "1",
      "FieldValue": {
        "orderNumber": {
          "value": "A001",
          "displayValue": "A001"
        },
        "orderPrice": {
          "value": 19.9,
          "displayValue": 19.9
        },
        "status": {
          "value": [10001],
          "displayValue": ["已下单"]
        }
      }
    },
    {
      "Id": 1481167475391438891, // 该条业务数据对应的RecordId
      "Entity": "order",
      "MainField": "2",
      "FieldValue": {
        "orderNumber": {
          "value": "A002",
          "displayValue": "A002"
        },
        "orderPrice": {
          "value": 1999,
          "displayValue": 1999
        },
        "status": {
          "value": [10009],
          "displayValue": ["已评论"]
        }
      }
    },
    {
      "Id": 1481167475391438892, // 该条业务数据对应的RecordId
      "Entity": "order",
      "MainField": "2",
      "FieldValue": {
        "orderNumber": {
          "value": "A003",
          "displayValue": "A003"
        },
        "orderPrice": {
          "value": 0.2,
          "displayValue": 0.2
        },
        "status": {
          "value": [10010],
          "displayValue": ["已取消"]
        }
      }
    }
  ]
}
```

说明：value为内部值，如无需要，只关心displayValue即可