## 1. 接口描述

功能：单条或者批量提交物料数据接口  
测试接口： `https://sdtj.y.qq.com:8008/cre_test_upload`    
正式接口： `https://sdtj.y.qq.com:8008/upload`  
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
		<td colspan="2">version</td>
		<td>是</td>
		<td>String</td>
		<td>上报接口版本（1，2，3，4）</td>
	</tr>
	<tr>
		<td colspan="2">seq_no</td>
		<td>否</td>
		<td>String</td>
		<td>请求标识，接口原样返回</td>
	</tr>
	<tr>
		<td colspan="2">data_type</td>
		<td>是</td>
		<td>String</td>
		<td>协议类型： "1" - item， "2" - action，物料上报传 "1"</td>
	</tr>
	<tr>
		<td colspan="2">token</td>
		<td>是</td>
		<td>String</td>
		<td>用作鉴权，由云推荐引擎分配</td>
	</tr>
	<tr>
		<td colspan="2">busi_id</td>
		<td>是</td>
		<td>String</td>
		<td>业务 ID。由云推荐引擎分配</td>
	</tr>
	<tr>
		<td colspan="2">test_id</td>
		<td>是</td>
		<td>String</td>
		<td>推荐场景 ID。如果不同场景有不同的物料库，可以用该字段区分</td>
	</tr>
	<tr>
		<td colspan="2">item_id</td>
		<td>是</td>
		<td>String</td>
		<td>物料 ID，物料唯一标识， 数值和字符串都可以</td>
	</tr>
	<tr>
		<td colspan="2">publish</td>
		<td>否</td>
		<td>String</td>
		<td>"1" - 上架（默认）， "2" - 下架</td>
	</tr>
	<tr>
		<td colspan="2">describe</td>
		<td>否</td>
		<td>String</td>
		<td>物料的描述信息，云推荐引擎使用  NLP 技术，进行分词、提取关键词，作为 item 的特征使用。例如物料属于资讯类，这里可以是文章内容。长度不能超过 30k</td>
	</tr>
	<tr>
		<td colspan="2">pool_id</td>
		<td>是</td>
		<td>String</td>
		<td>物料池，多个物料池用分号分割。注意不要使用  "0" 作为  pool_id，"0" 表示全局  pool_id， 任意物料都会加一个为 "0" 的 pool_id</td>
	</tr>
	<tr>
		<td rowspan="2">tags</td>
		<td>tags1</td>
		<td>否</td>
		<td>String</td>
		<td>作为模型的特征使用，是对物品的一个重要的区分特征，tags 的丰富、区分程度，很大程度上决定了模型训练的好坏。tags 要有区分性，主要用在新 item 的冷启动。tags 不能太粗，否则没有区分性，特征作用不大；也不能太细，否则没有共性，曝光不充分，起不到冷启动的目的。</td>
	</tr>
	<tr>
		<td>tags2</td>
		<td>否</td>
		<td>String</td>
		<td>更多 tags 请自行扩充</td>
	</tr>
	<tr>
		<td colspan="2">item_time</td>
		<td>否</td>
		<td>String</td>
		<td>item 生成时间，UTC 时间，默认是系统当前时间；例如 "1483200000"（2017年01月01日 00:00:00）</td>
	</tr>
	<tr>
		<td colspan="2">expire_time</td>
		<td>否</td>
		<td>String</td>
		<td>item 的过期时间，推荐结果会进行商品的过期过滤。如果不填，默认是 item_time+1  年；例如 "1514736000"（2018年01月01日 00:00:00）</td>
	</tr>
	<tr>
		<td colspan="2">free</td>
		<td>否</td>
		<td>String</td>
		<td>"0" - 免费（默认） "1" - 付费</td>
	</tr>
	<tr>
		<td colspan="2">score</td>
		<td>否</td>
		<td>String</td>
		<td>物料打分， 默认"0"；可以把 item 的 cvr 信息填写到 score，在 rerank 时，对排序进行加权</td>
	</tr>
	<tr>
		<td colspan="2">price</td>
		<td>否</td>
		<td>String</td>
		<td>物料价格，默认 "0"</td>
	</tr>
	<tr>
		<td colspan="2">platform</td>
		<td>否</td>
		<td>String</td>
		<td>"ios" - iOS 平台，"android" - Android 平台，"h5" - H5 </td>
	</tr>
	<tr>
		<td colspan="2">lv1class</td>
		<td>否</td>
		<td>String</td>
		<td>一级类目</td>
	</tr>
	<tr>
		<td colspan="2">lv2calss</td>
		<td>否</td>
		<td>String</td>
		<td>二级类目</td>
	</tr>
	<tr>
		<td colspan="2">lv3class</td>
		<td>否</td>
		<td>String</td>
		<td>三级类目</td>
	</tr>
	<tr>
		<td colspan="2">url</td>
		<td>否</td>
		<td>String</td>
		<td>物料相关的 URL。一个作用是使用 DNN 提取图片的特征，放入到模型使用；另一个作用，URL 的域名，本身就可以作为特征使用，有一定的区分性</td>
	</tr>
	<tr>
		<td colspan="2">vender</td>
		<td>否</td>
		<td>String</td>
		<td>可以传品牌，商家，店铺，广告主</td>
	</tr>
	<tr>
		<td rowspan="4">geo</td>
		<td>latitude</td>
		<td>否</td>
		<td>String</td>
		<td>LBS 数据，有些 O2O 的商家，需要知道 item 可以在哪些商圈投放，因此需要填写 item 所属的商圈的经纬度数据；没有这个需求的，可以不填写；例如 "22.558220"</td>
	</tr>
	<tr>
		<td>longitude</td>
		<td>否</td>
		<td>String</td>
		<td>物料相关地域维度，例如 "114.084778"</td>
	</tr>
	<tr>
		<td>country</td>
		<td>否</td>
		<td>String</td>
		<td>物料相关国家，ISO 3166-1 alpha-3 编码，例如 "CHN"（中国）</td>
	</tr>
	<tr>
		<td>city</td>
		<td>否</td>
		<td>String</td>
		<td>物料相关城市，例如 "深圳"</td>
	</tr>
	<tr>
		<td rowspan="2">extend</td>
		<td>key</td>
		<td>否</td>
		<td>String</td>
		<td>自定义字段 </td>
	</tr>
</table>



## 3. 输出参数

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|--------|------------|
| seq_no | 否 | String | 请求标识，接口原样返回 | 
| code | 是 | String | 错误码，"0" 表示成功，非 "0"  表示失败 |
| message | 否 | String| 错误信息 |


## 4. 示例

输入： 
```
{
"version" :"1",
"seq_no":"1",
 "data_type":"1",
 "token":"7d10d09d-be62-4979-9ee0-414f7a23086a",
 "data":[
   {
     "busi_id":"1000191",
     "test_id":"201008",
     "item_id":"abcde",
     "describe":"这是个物料上报测试接口，神盾推荐效果就是好",
     "pool_id":"1",
     "tags":{
     	"男装":"1",
     	"休闲裤":"0.8",
     	"情侣装":"0.5"
     },
     "platform":"h5",
     "lv1class":"1",
     "lv2class":"2",
     "lv3class":"3",
     "rule_id":"200723",
     "url":"https://www.qq.com",
     "vender":"腾讯",
     "geo":{
     	"latitude":"22.558220",
     	"longitude":"114.084778",
     	"country":"CHN",
     	"city":"深圳"
     },
     "extend":{
     	"key":"value"
     }
   }
 ]
}
```


输出： 
```
{
    "code": "0",
    "message": "success",
    "seq_no": "1"
}
```
