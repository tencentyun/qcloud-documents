### 1. 简介

腾讯云数字营销服务（pCTR，pCVR，流量优选，物料优选等）基于实时上报的item（物料）和action（行为），结合15亿+腾讯用户画像进行机器学习并实时返回服务结果。为简化开发者上报item和action两类数据，同时方便获取数字服务结果，腾讯云提供了相关协议标准。

### 2 item上报

**接口描述**

上报物料信息， 包括物料id， 物料有效期， 物料标签，物料池等信息。相同的item_id可以重复上报， 字段信息以最后一次上报为准。开发者基于http-post上报物料，URL：http://data.dm.qcloud.com:8088

**输入参数**

post报文body部分为JSON数据格式，如下所示

item上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳_随机数”
	"data_type":1, //1：item，2：action
	"bid":"BID" , //腾讯云为该业务分配的业务标识
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
		"key3":"value3",
		…
		}

}
```

item上报返回JSON数据格式
```
{
   "request_id":"request_id", //request_id 原样返回
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "msg":"true"
}
```

### 3 action上报

**接口描述**

上报某一用户在特定场景下的行为，用户的行为包括曝光、点击、转换、点赞等， 上报用户行为时，必须指定用户行为的会话id。用户行为可以在客户端和服务端上报，建议在客户端上报，可控性更强些，遇到协议变更或者问题排查时，更容易处理。开发者基于http-post上报行为，URL：http://data.dm.qcloud.com:8088

**输入参数**

Post报文body部分为JSON数据格式，如下所示

action上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳_随机数”
	"data_type":2, //1：item，2：action 
	"bid":"BID" , //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，2：opened，3：设备号imei/idfa或其MD5值（默认）
	"uid":"userId", //QQ，微信号，openid，imei/idfa或其MD5值
	"item_id":"item_id1;item_id2;item_id3", //物料列表,多个物料用 ; 号隔开
	"scene_id":"1001", //推荐展示场景。
	"action_type":1, //行为类型。1：曝光（浏览）,2：点击（播放）,3：转化（购买）,4：点赞 
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
		"key3":"value3",
		…
		}
}
```

action上报返回JSON数据格式
```
{
   "request_id":"request_id",
   "code":0, //-1：格式错误，-2：系统错误，-3：算法错误
   "msg":"true"
}
```

### 4 请求服务

开发者发送http-post获取服务结果，服务URL：http://service.dm.qcloud.com:8088

Post报文body部分为JSON数据格式，如下所示

**1) pCTR服务**

pCTR 请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"service_type":0, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，2：opened，3：设备号imei/idfa或其MD5值（默认）
	"uid":"userId", //QQ，微信号，openid，imei/idfa或其MD5值
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

错误返回如下所示
```
{
	"request_id":"request_id",
	"code":-3, //-1：格式错误，-2：系统错误，-3：算法错误
	"msg":"empty result"
}
```

**2) pCVR服务**

pCVR 请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7"， //md5(bid&request_id&TOKEN)
	"service_type":2, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选 
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，2：opened，3：设备号imei/idfa或其MD5值（默认） 
	"uid":"userId", //QQ，微信号，openid，imei/idfa或其MD5值
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
	"code":-3, //-1：格式错误，-2：系统错误，-3：算法错误
	"msg":"empty result"
}
```

**3) 物料优选服务**

物料优选请求服务JSON数据格式
```
{
	"MD5":"40379db889f9124819228947faaeb1f7"， //md5(bid&request_id&TOKEN)
	"service_type":4, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选
	"request_id":"request_id", //request_id 为”毫秒级时间戳_随机数”,
	"bid":"BID", //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，2：opened，3：设备号imei/idfa或其MD5值（默认）
	"uid":"userId", //QQ，微信号，openid，imei/idfa或其MD5值
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