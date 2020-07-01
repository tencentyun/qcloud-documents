## 使用兑换码

### 1.接口描述

域名: market.api.qcloud.com
接口名: UseVoucherData

云市场SaaS类使用兑换码

### 2.输入参数


| 参数名称        | 必选   | 类型     | 描述   |
| ----------- | ---- | ------ | ---- |
| voucherCode | 是    | String | 兑换码  |


### 3.输出参数


| 标题1           | 标题2    | 标题3                 |
| ------------- | ------ | ------------------- |
| code          | Int    | 错误码, 0: 成功, 其他值: 失败 |
| message       | String | 错误信息                |
| data          | Array  | 兑换码信息               |
| data.name     | String | 商品名称                |
| data.spec     | String | 商品规格                |
| data.cycle    | String | 商品周期                |
| data.add_time | String | 兑换码生成时间             |
| data.use_time | String | 兑换码使用时间             |
| data.msg      | String | success 表示使用成功      |

### 4.示例

输入


```
 https://market.api.qcloud.com/v2/index.php?Action=UseVoucherData
 &voucherCode=tkwbyeg8j2n6wi155j
 &COMMON_PARAMS
```

输出


```
{
    "code": 0,
    "message": "",
    "data": {
        "name": "听云工具",
        "spec": "5T",
        "cycle": "1个月",
        "add_time": "2015-10-16 11:58:37",
        "use_time": "2015-10-16 12:12:39",
        "msg": "success"
    }
}
```