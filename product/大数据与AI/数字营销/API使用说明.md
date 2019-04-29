### 1. 简介

腾讯云数字营销服务（pCTR，pCVR，流量优选，物料优选等）基于实时上报的item（物料）和action（行为），结合15亿+腾讯用户画像进行机器学习并实时返回服务结果。为简化开发者上报item和action两类数据，同时方便获取数字服务结果，腾讯云提供了相关协议标准。

### 2. item上报

**接口描述**

上报物料信息， 包括物料id， 物料有效期， 物料标签，物料池等信息。相同的item_id可以重复上报， 字段信息以最后一次上报为准。开发者基于http-post上报物料，URL：`http://data.dm.qcloud.com:8088`

**输入参数**

post报文body部分为JSON数据格式，如下所示

item上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳_随机数”
	"data_type":1, //1：item，2：action
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"item_id":"item_id", //物料标识
	"publish":1, //1：上架（默认），0：下架
	"describe":"最新款黑色苹果7", //物料描述  
	"pool_id":"pool_id1;pool_id2;pool_id3", //物料池，多个池子用 ; 号隔开
	"tags":"电器;科技;电子;手机", //物料标签，多个tag用 ; 号隔开
	"item_time":"1386817569", //物料生成时间（秒级时间戳，默认为当前时间）
	"expire_time":"1386917763", //物料过期时间（秒级时间戳，默认item_time + 一个月）
	"free":0, //0：免费（默认），1：付费
	"score":9.99, //物料打分（默认为0.0）
	"price":88.88, //物料价格（默认为0.0）
	"platform":1, //平台，1：android（默认），2：iphone，3：PC
	"big_type":"大类",
	"middle_type":"中类",
	"small_type ":"小类",
	"url":"URL",
	"vender":"店铺，广告主",
	"geo":{
		"latitude":-90.0~90.0,
		"longitude":-180.0~180.0,
		"country":"country code using ISO-3166-1-alpha-3",
		"city":"city name"
	  },
	"extend":{
		"key1":"value1",
		"key2":"value2",
		"key3":"value3"
		…
		}

}
```
**字段含义**
字段类型及含义如下表所示：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| data_type  | integer | Y | 协议类型： 1 - item, 2 – action， 物料上报取1 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| item_id  | string | Y | 物料id，物料唯一标识，数值和字符串都可以  | 
| publish  | integer | N | 1 - 上架（默认）， 2 - 下架  | 
| describe  | string | N | 商品的描述信息，推荐系统会对商品的描述信息，使用NLP技术，进行分词、提取关键词，作为item的特征使用  | 
| pool_id  | string | N | 物料池，多个物料用分号分割， 注意不要使用0作为pool_id,0表示全局pool_id, 任意物料我们都会加一个为0的pool_id  | 
| tags  | string | N | 作为模型的特征使用，是对物品的一个重要的区分特征，tags的丰富、区分程度，很大程度上决定了模型训练的好坏，默认tags字段需要上报：三级类目、品牌；另外，如果有标签描述信息，也可以上报过来。tags要有区分性，主要用在新item的冷启动，因此tag不能太粗，否则没有区分性，则特征作用不大；也不能太细，否则没有共性，曝光不充分，起不到冷启动的目的  | 
| item_time  | string | N | item生成时间，10位的秒级时间戳；如果不填，默认是系统当前时间  | 
| expire_time  | nteger | N | item的过期时间，推荐结果会进行商品的过期过滤。如果不填，默认是item_time + 1个月  | 
| free  | string | N | 0 - 免费（默认） 1 - 付费  | 
| score  | float | N | 物料打分， 默认 0.0，没有可以不填写；推荐这边，离线可以把item的cvr信息填写到score，在rerank时，对排序进行加权  | 
| price  | float | N | 物料价格，默认0.0  | 
| platform  | nteger | N | 平台， 0 – 全平台， 1 - Android （默认）， 2 - iphone， 3- pc  | 
| big_type  | string | N | 大类，需要类目的中文， 不能使用id  | 
| middle_type  | string | N | 中类, 需要类目的中文， 不能使用id  | 
| small_type  | string | N | 小类, 需要类目的中文， 不能使用id  | 
| url  | string | N | 物料相关的url。一个作用是使用DNN提取图片的特征，放入到模型使用；一个作用是：URL的域名，本身就可以作为特征使用，有一定的区分性  | 
| vender  | string | N | 可以传品牌，商家，店铺，广告主  | 
| geo.latitude  | float | N | LBS数据，有些O2O的商家，需要知道item可以在哪些商圈投放，因此需要填写item所属的商圈的经纬度数据；没有这个需求的，可以不填写  | 
| geo.longitude | float | N | 物料相关地域维度  | 
| geo.country  | string | N | 物料相关国家  | 
| geo.city  | string | N | 物料相关城市  | 
| extend.key  | string | N | 扩展字段  | 

item上报返回JSON数据格式
```
{
   "request_id":"request_id", //request_id 原样返回
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "msg":"true"
}
```
 
### 3. action 上报

**接口描述**

上报某一用户在特定场景下的行为，用户的行为包括曝光、点击、转换、点赞等， 上报用户行为时，必须指定用户行为的会话id。用户行为可以在客户端和服务端上报，建议在客户端上报，可控性更强些，遇到协议变更或者问题排查时，更容易处理。开发者基于http-post上报行为，URL：`http://data.dm.qcloud.com:8088`

**输入参数**

Post报文body部分为JSON数据格式，如下所示

action上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳_随机数”
	"data_type":2, //1：item，2：action 
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"item_id":"item_id1;item_id2;item_id3", //物料列表,多个物料用 ; 号隔开
	"scene_id":"1001", //推荐展示场景。
	"action_type":1, //行为类型。1：曝光（浏览）,2：点击（播放）,3：转化（购买）,4：点赞
	"source":"tx", //流量标记。tx：腾讯流量, bus：业务流量, def：默认流量 
	"trace_id":"trace_id", //跟踪点击和曝光的自定义跟踪id
	"action_time":"1386817569" , //行为发生时间（秒级时间戳，默认当前时间） 
	"geo":{
		"latitude":-90.0~90.0,
		"longitude":-180.0~180.0,
		"country":"country code using ISO-3166-1-alpha-3",
		"city":"city name"
		},
	"extend":{
		"key1":"value1",
		"key2":"value2",
		"key3":"value3"
		…
		}
}
```
**字段说明**
输入参数各字段的含义如下表所示：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| data_type  | integer | Y | 协议类型： 1 - item, 2 – action， 行为上报传2 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| uid_type  | integer | N | 0 - qq, 1 - 微信号， 3 - imei/icfa或其他md5（默认），4 - 手机号  | 
| uid  | string | Y | qq，微信号，imei/icfa，手机号，如果是imei号，则是15位数字字符串；如果是IFA号，则是8-4-4-4-12，32个字符串；如果是MD5（uid），则是32位的0-f的字符串，且需要是大写的IDFA进行的MD5 | 
| item_id  | string | Y | 物料id，物料唯一标识，数值和字符串都可以  | 
| scene_id  | string | Y | 推荐场景ID, 比如有“猜你喜欢”，“热门商品”等推荐模块，每一个模块都有一个scene_id来表示。 场景创建和场景id查看在控制台操作  | 
| action_type  | integer | Y | 用户行为：1 - 曝光 2 - 点击（播放） 3 - 转换（购买） 4 点赞  | 
| source  | string | Y | 用于分流的标识字段；区分用户的行为是哪个算法， 取值为 ：bus，tx，def 三者之一；其中：bus 表示业务自己的算法（business）；tx 为腾讯算法；def 为默认算法（default），可以理解为随机算法，或者对照组 | 
| trace_id  | string | Y | 跟踪点击和曝光的自定义会话ID，为了保证点击跟曝光是同一个用户对同一个 item 的操作行为；强烈建议每次曝光分配一个 trace_id trace_id | 
| action_time  | string | Y | 行为发生的时间戳， 秒级时间戳（默认为当前时间）,不能延迟太久，尽量实时上报，否则会影响推荐结果的准确性  | 
| geo.latitude  | float | N | 用户发生行为的经纬度地理位置  | 
| geo.longitude | float | N | 用户发生行为的经纬度地理位置  | 
| geo.country  | string | N | 用户发生行为的国家  | 
| geo.city  | string | N | 用户发生行为的城市  | 
| extend.key  | string | N | 扩展字段  | 

action上报返回JSON数据格式
```
{
   "request_id":"request_id",
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "msg":"true"
}
```

### 4. 请求服务

开发者发送http-post获取服务结果，服务URL：`http://service.dm.qcloud.com:8088`

Post报文body部分为JSON数据格式，如下所示

**1) pCTR服务**

pCTR 请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
	"service_type":0, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"scene_id":"1001", //广告展示场景。请求pCTR服务时scene_id与上报数据时保持一致。
	"cid":"ItemId1;ItemId2;ItemId3;ItemId4;...;ItemId200", //候选素材集合（不超过200个） 
	"site_name":"媒体网站名称或域名",
	"site_url":"当前页面url",
	"site_content":"当前页面描述",
	"app_name":"当前app名称",
	"rtb_extend":{
		"maker":{
			"publisher":"发布商",
			"producer":"生产商"
			},
		"site":{
			"name":"网站名字",
			"domain":"网站域名",
			"page":"广告展示页面 url"
			},
		"app":{
			"name":"app名字",
			"storeurl":"app store URL"
			},
		"content":{
			"type":"保留，暂时不用",
			"value":"当前上下文文本描述,例如网页内容摘要"
			},
		"dev":{
			"ip":"ip 地址",
			"maker":"设备生产商,例如 华为",
			"model":"设备类型,例如 荣耀",
			"os":"操作系统 例如 1:android 2:ios",
			"osv":"操作系统版本号",
			"imeimd5":"IMEI hashed via MD5",
			"idfamd5":"IDFA hashed via MD5"
			},
		"geo":{
			"latitude":-90.0~90.0,
			"longitude":-180.0~180.0,
			"country":"country code using ISO-3166-1-alpha-3",
			"city":"city name"
			},
		"user":{
			"gender":"M:男,F:女,O:未知",
			"age":"用户年龄",
			"agent":"用户代理，例如浏览器产品版本号"
			}	  
		}
}
```
**字段含义**
各个字段的含义如下：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| service_type  | integer | Y | 服务场景： 0 - pCtr 1 - 流量优选 2 - pCvr 3 - 智能推荐（默认） 4 物料优选 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| uid_type  | integer | N | 0 - qq, 1 - 微信号， 3 - imei/icfa或其他md5（默认），4 - 手机号  | 
| uid  | string | Y | qq，微信号，imei/icfa，手机号，如果是imei号，则是15位数字字符串；如果是IFA号，则是8-4-4-4-12，32个字符串；如果是MD5（uid），则是32位的0-f的字符串，且需要是大写的IDFA进行的MD5 | 
| scene_id  | string | Y | 推荐场景ID，请求服务的场景Id，需要跟行为上报时的ID一致  | 
| cid  | string | Y | 当前页面的物料id， 用于详情页面 | 
| geo.latitude  | float | N | 用户发生行为的经纬度地理位置  | 
| geo.longitude | float | N | 用户发生行为的经纬度地理位置  | 
| geo.country  | string | N | 用户行为相关的国家信息  | 
| geo.city  | string | N | 用户行为相关的城市信息  | 

pCTR 请求服务返回JSON数据格式
```
{ 
	"request_id":"request_id",
	"algid":18,
	"code":0, //-1：格式错误，-2：系统错误，-3：算法错误
	"scene_id":"1001",
	"data":[
	{
		"item":"ItemId10",
		"weight":1974
	 },
	 {
		"item":"ItemId41",
		"weight":1864
	 },
	 {
		"item":"ItemId7",
		"weight":997		
	 },
	 ...
	 {
		 "item":"ItemId86",
		 "weight":889
	 }
   ]   
}
```
**返回值**

| 返回值名称 | 类型 |  含义 |
|---------|---------|---------|
| algid  | Integer | 算法id， 可以在后续的行为上报中回传， 跟踪算法效果  | 
| scene_id  |string | 场景id  | 
| data.item  | Istring | 推荐的物品id，即item上报中的item_id  | 
| data.weigth  | Integer | 推荐物品的权重，取值范围[0,1000000] | 

错误返回如下所示
```
{
	"request_id":"request_id",
	"code":-3,
	"msg":"empty result"
}
```

**2) pCVR服务**

pCVR 请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
	"service_type":2, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选 
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"scene_id":"1001", //广告展示场景。请求服务时scene_id与上报数据时保持一致。
	"cid":"ItemId1;ItemId2;ItemId3;ItemId4;..;ItemId200", //候选素材集合（不超过200个）
	"site_name":"媒体网站名称或域名",
	"site_url":"当前页面url",
	"site_content":"当前页面描述",
	"app_name":"当前app名称",
	"rtb_extend":{
		"maker":{
			"publisher":"发布商",
			"producer":"生产商"
			},
		"site":{
			"name":"网站名字",
			"domain":"网站域名",
			"page":"广告展示页面 url"
			},
		"app":{
			"name":"app名字",
			"storeurl":"app store URL"
			},
		"content":{
			"type":"保留，暂时不用",
			"value":"当前上下文文本描述,例如网页内容摘要"
			},
		"dev":{
			"ip":"ip 地址",
			"maker":"设备生产商,例如 华为",
			"model":"设备类型,例如 荣耀",
			"os":"操作系统 例如 1:android 2:ios",
			"osv":"操作系统版本号",
			"imeimd5":"IMEI hashed via MD5",
			"idfamd5":"IDFA hashed via MD5"
			},
		"geo":{
			"latitude":-90.0~90.0,
			"longitude":-180.0~180.0,
			"country":"country code using ISO-3166-1-alpha-3",
			"city":"city name"
			},
		"user":{
			"gender":"M:男,F:女,O:未知",
			"age":"用户年龄",
			"agent":"用户代理，例如浏览器产品版本号"
			}	  
		}
}
```
**字段含义**
各个字段的含义如下：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| service_type  | integer | Y | 服务场景： 0 - pCtr 1 - 流量优选 2 - pCvr 3 - 智能推荐（默认） 4 物料优选 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| uid_type  | integer | N | 0 - qq, 1 - 微信号， 3 - imei/icfa或其他md5（默认），4 - 手机号  | 
| uid  | string | Y | qq，微信号，imei/icfa，手机号，如果是imei号，则是15位数字字符串；如果是IFA号，则是8-4-4-4-12，32个字符串；如果是MD5（uid），则是32位的0-f的字符串，且需要是大写的IDFA进行的MD5 | 
| scene_id  | string | Y | 推荐场景ID，请求服务的场景Id，需要跟行为上报时的ID一致  | 
| cid  | string | Y | 当前页面的物料id， 用于详情页面 | 
| geo.latitude  | float | N | 用户发生行为的经纬度地理位置  | 
| geo.longitude | float | N | 用户发生行为的经纬度地理位置  | 
| geo.country  | string | N | 用户行为相关的国家信息  | 
| geo.city  | string | N | 用户行为相关的城市信息  | 

pCVR 请求服务返回JSON数据格式
```
{
	"request_id":"request_id",
	"algid":19,
	"code":0, //-1：格式错误，-2：系统错误，-3：算法错误
	"scene_id":"1001",
	"data":[
	{
		"item":"ItemId10",
		"weight":974
	},
	{
	    "item":"ItemId41",
		"weight":864
	},
	{
	    "item":"ItemId7",
		"weight":97		
	},
	 ...
	{
	    "item":"ItemId86",
		"weight":89
	}
   ]   
}
```


错误返回如下所示

```
{
	"request_id":"request_id",
	"code":-3,
	"msg":"empty result"
}
```

**3) 物料优选服务**

物料优选请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
	"service_type":4, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”,
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"scene_id":"1001", //广告展示场景。请求服务时scene_id与上报数据时保持一致
	"request_num":50, //物料优选个数。默认每次请求50个
	"pool_id":"pool_id1;pool_id2", //物料池，多个池子用 ; 号隔开
	"site_name":"媒体网站名称或域名",
	"site_url":"当前页面url",
	"site_content":"当前页面描述",
	"app_name":"当前app名称",
	"rtb_extend":{
		"maker":{
			"publisher":"发布商",
			"producer":"生产商"
			},
		"site":{
			"name":"网站名字",
			"domain":"网站域名",
			"page":"广告展示页面 url"
			},
		"app":{
			"name":"app名字",
			"storeurl":"app store URL"
			},
		"content":{
			"type":"保留，暂时不用",
			"value":"当前上下文文本描述,例如网页内容摘要"
			},
		"dev":{
			"ip":"ip 地址",
			"maker":"设备生产商,例如 华为",
			"model":"设备类型,例如 荣耀",
			"os":"操作系统 例如 1:android 2:ios",
			"osv":"操作系统版本号",
			"imeimd5":"IMEI hashed via MD5",
			"idfamd5":"IDFA hashed via MD5"
			},
		"geo":{
			"latitude":-90.0~90.0,
			"longitude":-180.0~180.0,
			"country":"country code using ISO-3166-1-alpha-3",
			"city":"city name"
			},
		"user":{
		"gender":"M:男,F:女,O:未知",
		"age":"用户年龄",
		"agent":"用户代理，例如浏览器产品版本号"
		}	  
   }
}
```
**字段含义**
各个字段的含义如下：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| service_type  | integer | Y | 服务场景： 0 - pCtr 1 - 流量优选 2 - pCvr 3 - 智能推荐（默认） 4 物料优选 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| uid_type  | integer | N | 0 - qq, 1 - 微信号， 3 - imei/icfa或其他md5（默认），4 - 手机号  | 
| uid  | string | Y | qq，微信号，imei/icfa，手机号，如果是imei号，则是15位数字字符串；如果是IFA号，则是8-4-4-4-12，32个字符串；如果是MD5（uid），则是32位的0-f的字符串，且需要是大写的IDFA进行的MD5 | 
| scene_id  | string | Y | 推荐场景ID，请求服务的场景Id，需要跟行为上报时的ID一致  | 
| request_num  | integer | N | 物料优选的结果， 默认50个，目前最多支持200个的item返回，如果返回个数更多，会影响性能，容易超时  | 
| pool_id  | string | Y | 物料池，需要展示哪个pool_id下的商品，要跟上报的item的pool_id一致  | 
| geo.latitude  | float | N | 用户发生行为的经纬度地理位置  | 
| geo.longitude | float | N | 用户发生行为的经纬度地理位置  | 
| geo.country  | string | N | 用户行为相关的国家信息  | 
| geo.city  | string | N | 用户行为相关的城市信息  | 

物料优选请求服务返回JSON数据格式
```
{
   "request_id":"request_id",
   "algid":17,
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "scene_id":"1001",
   "data":[
     {
	   "item":"ItemId10",
	   "weight":974
	 },
	 {
	    "item":"ItemId41",
		"weight":864
	 },
	 {
	    "item":"ItemId7",
		"weight":97		
	 },
	 ...
	 {
	    "item":"ItemId86",
		"weight":89
	 }
   ] 
}
```

错误返回如下所示
```
{
   "request_id":"request_id",
   "code":-3,
   "msg":"empty result"
}
```

**4) 流量优选服务**

流量优选请求服务JSON数据格式
```
{
   "MD5":"40379db889f9124819228947faaeb1f7", //md5(bid&request_id&TOKEN)
   "service_type":1, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选   
   "request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”
   "bid":"BID", //腾讯云为该业务分配的业务标识
   "scene_id":"1001", //广告展示场景。请求服务时scene_id与上报数据时保持一致。
   "media_id":"媒体ID" //媒体标识
}
```
**字段含义**
各个字段的含义如下：

| 参数名称 | 类型 | 必传 | 含义 |
|---------|---------|---------|---------|
| MD5  | string | Y | MD5(bid&request_id&TOKEN)  | 
| request_id   | string | Y | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上  |
| service_type  | integer | Y | 服务场景： 0 - pCtr 1 - 流量优选 2 - pCvr 3 - 智能推荐（默认） 4 物料优选 | 
| bid  | string | Y | 业务id，腾讯云分配的业务ID，可以在控制台查询  | 
| scene_id  | string | Y | 推荐场景ID，请求服务的场景Id，需要跟行为上报时的ID一致  | 
| media.id  | string | N | 媒体标识  | 

流量优选服务返回JSON数据格式
```
{
   "request_id":"request_id",
   "algid":20,
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "data":{
		"media_id": "媒体ID",
        "m_weight":7889,
		"scene_id": "1001",
        "s_weight":6879
    }
}
```

错误返回如下所示
```
{
   "request_id":"request_id",
   "code":-3,
   "msg":"empty result"
}
```
