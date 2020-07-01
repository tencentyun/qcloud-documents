## 查询软件类商品兑换码信息

### 1.接口描述

域名: market.api.qcloud.com
接口名: QueryVoucherData

查询云市场软件类的兑换码关联的商品信息，包括商品，规格周期，是否有效等信息。

### 2.输入参数

| 参数名称        | 必选   | 类型     | 描述   |
| ----------- | ---- | ------ | ---- |
| voucherCode | 是    | String | 兑换码  |

### 3.输出参数

| 参数名称          | 类型     | 描述                      |
| ------------- | ------ | ----------------------- |
| code          | Int    | 错误码, 0: 成功, 其他值: 失败     |
| message       | String | 错误信息                    |
| data          | Array  | 商品信息                    |
| data.name     | String | 商品名称                    |
| data.spec     | String | 商品规格                    |
| data.cycle    | String | 周期                      |
| data.add_time | String | 兑换码生成时间                 |
| data.use_time | String | 兑换码使用时间，未使用为空           |
| data.status   | String | 兑换码是否已使用 0已使用，1未使用，2已退款 |

### 4.示例

输入

```
 https://market.api.qcloud.com/v2/index.php?Action=QueryVoucherData
 &voucherCode=tkwbyeg8j2n6wi155j
 &COMMON_PARAMS
```

输出

```
{
    "code": 0,
    "message": "",
    "data": {
        "name": "听云",
        "spec": "5T",
        "cycle": "1个月",
        "add_time": "2015-10-16 11:58:37",
        "use_time": "2015-10-16 12:12:39",
        "status": "1"
    }
}
```
