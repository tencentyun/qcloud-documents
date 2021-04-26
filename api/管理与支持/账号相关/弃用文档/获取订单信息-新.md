## 1. 接口描述
域名:trade.api.qcloud.com
接口名:DescribeDealsByCond

获取订单信息(新)

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| startTime | 是 | datetime | 开始时间|
| endTime | 是 | datetime | 结束时间|
| page | 否 | Int | 第多少页,从0开始，默认是0|
| pageSize | 否 | Int | 一页多少条数据，默认是20条|
| status | 否 | Int | 订单状态,默认为4（成功的订单）<br>订单的状态<br>1：未支付<br>2：已支付3：发货中<br>4：已发货<br>5：发货失败<br>6：已退款<br>7：已关单<br>8：订单过期<br>9：订单已失效<br>10：产品已失效<br>11：代付拒绝<br>12：支付中<br>|
| dealId | 否 | Int | 订单ID|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | |
| data.deals | Array | | 
| data.deals.goodsCategoryId | Int | 产品分类ID <br> 1 CVM 新购   <br> 19 带宽包购买   <br> 26 新购VPN包    <br> 27 续费VPN包    <br> 28 升级VPN包    <br> 29 新购云视频套餐    <br> 30 续费云视频套餐    <br> 31 升级云视频套餐    <br> 32 新购CDN包    <br> 34 新版负载均衡    <br> 35 新购大禹套餐    <br> 36 大禹流量包    <br> 40 视频直播购买    <br> 41 CVM降配    <br> 46 wenzhi购买 月套餐    <br> 47 wenzhi续费      <br> 48 wenzhi升级    <br> 51 SSLVPN购买 月套餐    <br> 52 SSLVPN续费    <br> 53 SSLVPN升级    <br> 75 域名新购   <br> 76 域名续费   <br> 79 CVM降配   <br> 100001 云搜新购   <br> 100002 云搜续费   <br> 100003 云搜变配   <br> 100004 MongoDB新购   <br> 100005 MongoDB续费   <br> 100006 MongoDB变配   <br> 100007 BGP高防服务包新购   <br> 100008 BGP高防服务包续费   <br> 100009 BGP高防服务包变配   <br> 100013 Redis新购   <br> 100014 Redis续费   <br> 100015 Redis变配 <br> 100016 MySQL新购 <br> 100017 MySQL续费 <br> 100018 MySQL变配 <br> 100019 CVM新购 <br> 100020 CVM续费 <br> 100021 CVM变配 <br> 100025 游戏兼容性测试新购 <br> 100036 BGP超级高防服务包新购 <br> 100037 BGP超级高防服务包续费 <br> 100039 SQLServer新购 <br>     100040 SQLServer续费 <br> 100041 SQLServer变配 <br> 100042 TdSQL新购 <br> 100043 TdSQL续费 <br> 100044 TdSQL变配 <br> 100045 独立宿主机新购 <br> 100046 独立宿主机续费 <br> 100048 独立宿主机子机新购 <br> 100050 独立宿主机子机变配 <br> 100051 黑石物理机新购 <br> 100052 黑石物理机续费 <br> 100058 独立云盘新购 <br> 100059 独立云盘续费 <br> 100060 独立云盘变配     <br> 100062 天御安全产品新购 <br> 100063 天御安全产品续费 <br> 100064 天御安全产品变配 <br> 100065 黑石MySQL新购 <br> 100066 黑石MySQL续费 <br> 100067 黑石MySQL变配 <br> 100069 物理专线新购 <br> 100070 物理专线续费 <br> 100072 BGP高防IP新购 <br> 100073 BGP高防IP续费 <br> 100074 BGP高防IP变配 <br> 100079 独享围笼数据库集群新购 <br> 100080 独享围笼数据库集群续费 <br> 100089 云解析套餐新购 <br> 100090 云解析套餐续费 <br> 100091 云解析套餐变配 <br> 100092 HBase新购 <br> 100093 HBase续费 <br> 100095 SSL证书购买 <br> 100096 分布式MongoDB新购 <br> 100097 分布式MongoDB续费 <br> 100098 分布式MongoDB变配 <br> 100099 服务市场新购 <br> 100101 postgresql新购 <br> 100102 postgresql续费 <br> 100103          postgresql变配 <br> 100107 永洪BI新购 <br> 100108 永洪BI续费 <br> 100109 永洪BI变配 <br> 100114 域名新购 <br> 100115 域名续费 <br> 100123 cdn流量包新购 <br> 100131 云监控增量短信配额新购 <br> 100133 HttpDNS流量包-1000万次新购 <br> 100141 HttpDNS流量包-3000万次新购 <br> 100143 分布式数据库新购 <br> 100144 分布式数据库续费 <br> 100146 wetest远程测试新购 <br>    100154 分布式数据库新购 <br> 100155 建站主机新购 <br> 100156 建站主机续费 <br> 100166 短信新购 <br> 100203 云市场商品新购 <br> 100206 cdn流量包新购 <br> 100215 网站管家新购 <br> 100218 消息服务CKafka新购 <br>|
| data.deals.goodsDetail | Array | 产品配置信息| 
| data.deals.taskDetail | Array | 部分产品信息，新购时产品ID存在此字段| 
| data.deals.realTotalCost | Int | 总消耗（单位分）| 
| data.deals.voucherDecline | Int | 代金卷消耗（单位分）| 
| data.deals.projectId | Int | 项目ID| 

goodsCategoryId 产品分类ID <br>
    

## 4. 示例
输入
<pre>
https://trade.api.qcloud.com/v2/index.php?Action=DescribeDealsByCond
&startTime=2016-01-01 00:00:00
&endTime=2016-02-01 00:00:00
&pageSize=2
&page=0
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "totalNum":"76",
        "deals":[
            {
                "dealName":"1",
                "dealId":"11",
                "goodsCategoryId":"100114",
                "goodsDetail":{
                    "domain":"dnspod.cn",
                    "years":"1",
                    "service":"DR_CN_NEW"
                },
                "creatTime":"2016-01-07 15:47:34",
                "billId":"20160107030000032133684280",
                "taskDetail":{
                    "flowId":"3333"
                },
                "realTotalCost":"1024",
                "voucherDecline":null,
                "projectId":"0"
            },
            {
                "dealName":"1",
                "dealId":"1",
                "goodsCategoryId":"100114",
                "goodsDetail":{
                    "type":"tdsql",
                    "action":"renewTDsql",
                    "appId":"1351000042",
                    "Memory":"6000",
                    "Storage":"100",
                    "Ids":"40590",
                    "instanceNames":"name40590",
                    "curDeadline":"2016-02-07",
                    "timeSpan":"4",
                    "timeUnit":"d",
                    "ProjectId":"0",
                    "userType":"1",
                    "operator":"909619400"
                },
                "creatTime":"2016-01-07 16:55:24",
                "billId":"2016010703000003213219435981",
                "taskDetail":{
                    "Ids":[
                        "40590"
                    ]
                },
                "realTotalCost":"10000",
                "voucherDecline":null,
                "projectId":"0"
            }
        ]
    }
}
```

