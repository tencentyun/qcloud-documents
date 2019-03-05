## 1. 接口描述

功能：获取推荐结果   
测试接口： `https://sdtj.y.qq.com:8008/test-query`    
正式接口： `https://sdtj.y.qq.com:8008/query`  
请求方式：POST  

## 2. 输入参数  
<table>
	<tr>
		<th colspan="2">参数名称</th>
		<th>必选</th>
		<th>类型</th>
		<th>含义</th>
	</tr>
	<tr>
		<td colspan="2">seq_no</td>
		<td>否</td>
		<td>String</td>
		<td>请求标识，接口原样返回</td>
	</tr>
	<tr>
		<td colspan="2">token</td>
		<td>是</td>
		<td>String</td>
		<td>用作鉴权，由云推荐引擎分配</td>
	</tr>
	<tr>
		<td colspan="2">proj_id</td>
		<td>是</td>
		<td>String</td>
		<td>项目 ID。由 CRE 分配给客户</td>
	</tr>
	<tr>
		<td colspan="2">scn_id</td>
		<td>是</td>
		<td>String</td>
		<td>场景 ID。由 CRE 分配给客户</td>
	</tr>
	<tr>
		<td colspan="2">uid_type</td>
		<td>是</td>
		<td>String</td>
		<td>"0" - QQ， "1" - 微信号， "2" - openid， "3" - IMEI/IDFA， "4" –
			手机号，"5" - App 唯一用户</td>
	</tr>
	<tr>
		<td colspan="2">user_id</td>
		<td>是</td>
		<td>String</td>
		<td>用户 ID。标识请求中对应的用户。uid_type 指定类型的用户标识，QQ 号，微信号等等。若为空则当冷启动处理</td>
	</tr>
	<tr>
		<td colspan="2">pool_id</td>
		<td>否</td>
		<td>String</td>
		<td>推荐池子 ID。不填时默认为全局池子 ID "0"。多个池子以，分割，例如 "pool_id1，pool_id2，pool_id3"。当传入带排序物品列表（带 pool 字段）时忽略该字段</td>
	</tr>
	<tr>
		<td rowspan="2">pool</td>
		<td>item_type</td>
		<td>否</td>
		<td>String</td>
		<td>物品 ID 类型。"0" - 整数，"1" - 字符串。当传入物品列表时必填</td>
	</tr>
	<tr>
		<td>items</td>
		<td>否</td>
		<td>Array</td>
		<td>待排序物品列表，例如"["1"， "2"， "3"]"。此时忽略 pool_id</td>
	</tr>
	<tr>
		<td colspan="2">request_num</td>
		<td>否</td>
		<td>String</td>
		<td>指定排序后的物料返回个数，取 topN 。默认返回全部物料</td>
	</tr>
	<tr>
		<td rowspan="4">geo</td>
		<td>latitude</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的经度，例如 "22.558220"</td>
	</tr>
	<tr>
		<td>longitude</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的纬度，例如 "114.084778"</td>
	</tr>
	<tr>
		<td>country</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的国家，ISO 3166-1 alpha-3 编码，例如 "CHN" （中国）</td>
	</tr>
	<tr>
		<td>city</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的城市，例如"深圳"</td>
	</tr>
	<tr>
		<td rowspan="2">extend</td>
		<td>key1</td>
		<td>否</td>
		<td>String</td>
		<td>自定义字段 1</td>
	</tr>
	<tr>
		<td>key2</td>
		<td>否</td>
		<td>String</td>
		<td>自定义字段 2，业务自行扩充</td>
	</tr>
</table>



## 3. 输出参数
<table>
	<tr>
		<th  colspan="2">参数名称</th>
		<th>必选</th>
		<th>类型</th>
		<th>含义</th>
	</tr>
	<tr>
		<td colspan="2">seq_no</td>
		<td>否</td>
		<td>String</td>
		<td>请求序列号。请求接口原样返回该字段</td>
	</tr>
	<tr>
		<td colspan="2">code</td>
		<td>是</td>
		<td>String</td>
		<td>错误码，"0" 表示成功，非 "0" 表示失败</td>
	</tr>
	<tr>
		<td colspan="2">message</td>
		<td>否</td>
		<td>String</td>
		<td>错误信息</td>
	</tr>
	<tr>
		<td colspan="2">test_id</td>
		<td>是</td>
		<td>String</td>
		<td>推荐场景 ID，比如有"猜你喜欢"。例如 "1000190"</td>
	</tr>
	<tr>
		<td colspan="2">abtag</td>
		<td>是</td>
		<td>String</td>
		<td>策略 ID。通常一个推荐场景下会有多个算法 ID，用于算法迭代</td>
	</tr>
	<tr>
		<td colspan="2">trace_id</td>
		<td>是</td>
		<td>String</td>
		<td>跟踪串，系统自动分配的唯一标识单次推荐请求的  ID</td>
	</tr>
	<tr>
		<td rowspan="2">rec</td>
		<td>id</td>
		<td>是</td>
		<td>String</td>
		<td>物品 ID。rec 为 JsonObject，每个元素是 key-value 对，key 为 pool_id ，value 为对当前池子（pool_id）打分后的物品列表</td>
	</tr>
	<tr>
		<td>score</td>
		<td>是</td>
		<td>String</td>
		<td>物品分数</td>
	</tr>
</table>


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
  "pool":{
    "item_type":"1",
    "items":["100", "101", "102"]
  },
  "request_num":"500",
 "geo":{
    "latitude":"22.558220",
    "longitude":"114.084778",
    "country":"CHN",
    "city":"深圳"
  },
  "extend":{
    "key1":"val1",
    "key2":"val2"
  }
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
