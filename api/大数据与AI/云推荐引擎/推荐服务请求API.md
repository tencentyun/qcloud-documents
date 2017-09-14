## 1. 接口描述

功能：获取推荐结果  
接口：   

1. 测试： `https://sdtj.y.qq.com:8008/test-query`    
2. 正式： `https://sdtj.y.qq.com:8008/query](https://sdtj.y.qq.com:8008/query`  

方法：POST  

## 2. 输入参数  
| 参数名称 | 必选 | 类型 | 描述 |        
|---------|---------|--------|------------|  
| seq_no | 否 | String | 请求标识，接口原样返回| 
| token| 是| String| 用作鉴权，由云推荐引擎分配| 
| proj_id| 是| String| 项目 ID。由 CRE 分配给客户| 
| scn_id| 是| String| 场景 ID。由 CRE 分配给客户|
| uid_type| 是| String| "0" - QQ, "1" - 微信号， "2" - openid, "3" - IMEI/IDFA， "4" – 手机号，"5" - APP 唯一用户| 
| user_id| 是| String| 用户 ID。标识请求中对应的用户。uid_type 指定类型的用户标识，QQ 号，微信号等等。若为空则当冷启动处理| 
| pool_id| 否| String| 推荐池子 ID。多个池子以;分割，例如 "pool_id1； pool_id2； pool_id3"。当传入带排序物品列表（带 pool 字段）时忽略该字段|
| pool.item_type| 否| String| 物品 ID 类型。"0" - 整数，"1" - 字符串。当传入物品列表时必填|
| pool.items| 否| Array| 待排序物品列表，例如"["1", "2", "3"]"。此时忽略 pool_id| 
| request_num| 否| String| 指定排序后的物料返回个数，取 topN 。默认返回全部物料| 
| geo.latitude| 否| String| 用户发生行为的经纬度地理位置| 
| geo.longitude| 否| String| 用户发生行为的经纬度地理位置| 
| geo.country| 否| String| 用户发生行为的经纬度地理位置| 
| geo.city| 否| String| 用户发生行为的经纬度地理位置| 
| extend.key| 否| String| 自定义字段| 


## 3. 输出参数
| 参数名称 | 必选 | 类型 | 描述 |        
|---------|---------|--------|------------|  
| seq_no | 否 | String | 请求序列号。请求接口原样返回该字段|         
| code | 是 | String |错误码，"0" 表示成功，非 "0" 表示失败|
| message | 否 | String| 错误信息 |
|test_id|是|String|推荐场景 ID，比如有"猜你喜欢"。例如 "1000190"|
|abtag|是|String|策略 ID。通常一个推荐场景下会有多个算法 ID，用于算法迭代|
|trace_id|是|String|跟踪串，系统自动分配的唯一标识单次推荐请求的 ID|
|rec.id|是|String|物品 ID。rec 为数组，数组大小等于传入的推荐池子 ID 个数，数组元素为打分排序后的物品列表，数组元素顺序与传入的推荐池子 ID 顺序一一对应|
|rec.score|是|String|物品分数|


## 4. 示例

输入： 
```
{
  "seq_no":"987654321",
  "token":"61f6b4db-e680-4765-941c-39ad004e12fd",
  "proj_id":"100001",
  "scn_id":"123456789",
  "uid_type":"2",
  "user_id":"000000000000000000000000401EEEC1",
  "pool_id":"11016775",
  "request_num":"500"
}
```

输出： 
```
{
  "code": "0",
  "message": null,
  "abtag": "123456789",
  "trace_id": "737213799686931157",
  "seq_no": "987654321",
  "test_id": "123456789",
  "rec": {
    "11016775": [
      {
        "id": "0",
        "score": "100"
      },
      {
        "id": "1",
        "score": "99"
      }
    ]
  }
}
```
