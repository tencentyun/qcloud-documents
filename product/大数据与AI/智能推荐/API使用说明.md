### 1 简介

腾讯云智能推荐服务基于实时上报的item（物料）和action（行为），结合15亿+腾讯用户画像进行机器学习并实时返回推荐结果。为简化开发者上报item和action两类数据，同时方便获取智能推荐服务结果，腾讯云提供了相关协议标准。

#### 1) 术语表 

- Item：物料，即被推荐物品，推荐系统使用物料属性信息，用户标签及行为一起，生成推荐结果。物料分pool管理，一个物料可以属于一个或多个pool，获取推荐结果时，可以在指定pool中计算推荐结果。 

- Pool：物料池，被推荐物品的集合，用于管理只需要特定场景下出现的物料集合。如果物料只希望在某个场景下出现，可以在物料上报时指定pool，拉取推荐结果时，指定对应的pool即可。一个物料可以属于一个或多个pool。  

- TraceId： 用户行为ID，串联用户行为的会话ID，用户行为包括曝光、点击、效果转换、点赞等，用户行为按时序依次产生，需要业务传递traceId，标识点击、效果转换的动作是哪一次的曝光、点击产生的。 

#### 2) API快速入门

通过智能推荐API使用腾讯云推荐服务，您需要依次完成如下几个步骤：

1. 提交业务接入申请表； 
2. 开通业务白名单后， 在腾讯云控制台创建一个业务。 开通白名单和业务的审批请联系相关的同事； 
3. 使用Item物料上报API上报物料， 上报物料后， 联系联调的同学查看上报物料数据质量； 
4. 使用Action行为上报API上报用户行为，上报物料后， 联系联调的同学查看上报物料数据质量； 
5. 通过推荐结果API获取推荐结果； 
6. 联调完成后， 通知腾讯云联调同学配置上线算法； 
7. 上线观察业务指标。

### 2 API概览

- Item上报: 物料管理，包括物料上报、物料池划分、物料上下架等功能； 
- Action上报： 用户行为上报， 上报特定场景下，某个用户对某个物料产生的特定动作； 
- 推荐结果拉取： 从指定的物料池中获取特定场景下某个用户的推荐结果。

### 3 调用方式

智能推荐提供HTTP + JSON的服务，请求协议以Json格式序列化，作为HTTP请求的Body部分，客户端以POST方式访问服务。服务地址：
- 推荐结果拉取： http://service.dm.qcloud.com:8088 
- 物料与行为上报： http://data.dm.qcloud.com:8088 

**鉴权**

协议使用MD5字段来包签名，防止竞争对手伪造数据包进行流量攻击。MD5的计算方法为：BID，request_id, TOKEN 三个字符串用&字符链接，然后整个字符串的MD5值。

MD5（BID&request_id&TOKEN）

**注**：目前TOKEN验证正在完善，可以先用一个字符串代替，后续再找腾讯云分配。目前接收请求的CGI还没有对这块验证，因此前期数据接入，MD5可以随便填写。

### 4 Item上报

**接口描述**

上报物料信息， 包括物料id， 物料有效期， 物料标签，物料池等信息。相同的itemid可以重复上报， 字段信息以最后一次上报为准。 开发者发送http-post获取服务结果，服务URL：http://data.dm.qcloud.com:8088

**输入参数**

post报文body部分为JSON数据格式，如下所示：

item上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳随机数”
	"data_type":1, //1：item，2：action
	"bid":"BID" , //腾讯云为该业务分配的业务标识
	"item_id":"item_id", //物料标识
	"publish":1, //1：上架（默认），0：下架
	"describe":"最新款黑色苹果7", //物料描述
	"pool_id":"pool_id1;pool_id2;pool_id3", //物料池，多个池子用 ; 号隔开
	"tags":"电器;科技;电子;手机", //物料标签，多个tag用 ; 号隔开
	"item_time":"1386817569", //物料生成时间（默认为当前时间）
	"expire_time":"1386917763", //物料过期时间（默认item_time + 一个月）
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

### 5 Action上报

**接口描述**

上报某一用户在特定场景下的行为，用户的行为包括曝光、点击、转换、点赞等， 上报用户行为时，必须指定用户行为的会话id。用户行为可以在客户端和服务端上报，建议在客户端上报，可控性更强些，遇到协议变更或者问题排查时，更容易处理。 

开发者发送http-post获取服务结果，服务URL：http://data.dm.qcloud.com:8088

**输入参数**

Post报文body部分为JSON数据格式，如下所示：

action上报JSON数据格式
```
{

	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"request_id":"request_id", //request_id 为“毫秒级时间戳随机数”
	"data_type":2, //1：item，2：action 
	"bid":"BID" , //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"item_id":"item_id1;item_id2;item_id3", //物料列表,多个物料用 ; 号隔开
	"scene_id":"1001", //广告展示场景。
	"action_type":1, //行为类型。1：曝光（浏览）,2：点击（播放）,3：转化（购买）,4：点赞 
	"source":"tx", //流量标记。tx：腾讯流量, bus：业务流量, def：默认流量
	"trace_id":"trace_id", //跟踪点击和曝光的自定义跟踪id
	"action_time":"1386817569" , //行为发生秒级时间戳（默认当前时间） 
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

### 6 请求服务

**接口描述**

获取特定场景下， 给特定用户的推荐结果。 获取推荐时， 需要指定场景， 用户信息及需要使用的物料池，推荐系统返回用户在当前场景下，对各个物品喜好的权重。 

开发者发送http-post获取服务结果，服务URL：http://service.dm.qcloud.com:8088

**输入参数**

Post报文body部分为JSON数据格式，如下所示：

智能推荐服务请求JSON数据格式

```
{

	"MD5":"40379db889f9124819228947faaeb1f7"，//md5(bid&request_id&TOKEN)
	"service_type":3, //服务类型。0：pCTR，1：流量优选，2：pCVR，3：个性化推荐（默认），4：物料优选
	"request_id":"request_id", //request_id 为“毫秒级时间戳随机数”
	"bid":"BID" , //腾讯云为该业务分配的业务标识
	"uid_type":3, //0：QQ，1：微信号，3：设备号imei/idfa或其MD5值（默认），4：手机号
	"uid":"userId", //QQ，微信号，imei/idfa或其MD5值，手机号
	"scene_id":"1001", //广告展示场景,请求服务时scene_id与上报数据时保持一致
	"request_num":50, //物料优选个数。默认每次请求50个
	"pool_id":"pool_id1;pool_id2", //物料池，多个池子用 ; 号隔开
	"cid":"item_id", //当前物料（用于详情页推荐中指定当前物料）
	"geo":{//当前lbs信息（用于考虑lbs场景的推荐）
		"latitude":-90.0~90.0,
		"longitude":-180.0~180.0,
		"country":"country code using ISO-3166-1-alpha-3",
		"city":"city name"
	  },

}
```

智能推荐服务返回JSON数据格式
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