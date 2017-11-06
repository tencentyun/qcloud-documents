## 1. 接口描述
 
本接口(GetRedisPerformance)用于查询CRS实例在[beginTime,endTime]时间段内的性能，包括qps、连接数、慢查询日志。
1. 只支持查询主从版实例的性能；
2. 为方便用户分析慢日志，接口不支持批量查询；
3. 为了提升查询效率，建议查询的时间跨度不超过2个小时，即 [beginTime,endTime] 时间跨度不超过2个小时，默认查询最近1个小时内实例性能；
4. 为保证服务稳定性，单次查询结果最多不超过30条慢查询日志，如果返回值isTruncate 为true，表示有超过30条慢查询日志，仅返回了前30条记录，如要查询更多慢日志，请联系工程师；
5. 为保证服务稳定性，请勿频繁调用该接口，限制每秒不超过10次调用，每分钟不超过200次调用。

接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为GetRedisPerformance。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| redisId | 是 | String | 实例Id，可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisId 获取|
| beginTime | 否 | String | 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内的性能，如果beginTime，endTime 都不传，默认查询最近1个小时内实例性能。为提升查询效率，建议[beginTime, endTime] 的时间跨度不超过2个小时 |
| endTime | 否 | String | 结束时间，格式如：2017-02-08 17:46:34。查询实例在 [beginTime, endTime] 时间段内的性能，如果beginTime，endTime 都不传，默认查询最近1个小时内实例性能。为提升查询效率，建议[beginTime, endTime] 的时间跨度不超过2个小时 |

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Array | 查询结果 |
| data.beginTime | String | 开始时间，[beginTime,endTime]时间段内实例性能 |
| data.endTime | String | 结束时间，[beginTime,endTime]时间段内的实例性能 |
| data.redisPerformance | Array | 实例性能  | 
| data.redisPerformance.redisId | String | 实例Id，如：crs-edevql5z | 
| data.redisPerformance.max_qps | Float | 实例最大qps， 如：12356.03 | 
| data.redisPerformance.qps | Array | [beginTime,endTime]时间段内，实例每分钟的qps，由于监控数据有4分钟延迟，所以不能查询到最近4分钟的qps | 
| data.redisPerformance.max_conn | Int | [beginTime,endTime]时间段内，实例最大连接数 | 
| data.redisPerformance.connection | Array | [beginTime,endTime]时间段内，实例每分钟的连接数，由于监控数据有4分钟延迟，所以不能查询到最近4分钟的连接数|
| data.redisPerformance.totalCountSlowLog | Int | [beginTime,endTime]时间段内，实例慢查询总数 |
| data.redisPerformance.isTruncate | bool | isTruncate 取值为true、false。如果isTruncate为true，表示有超过30条慢查日志，为保证服务稳定性，仅返回了前30条慢日志，如要查询更多慢日志，请联系工程师； 如果isTruncate为false，表示返回了所有的慢查询日志 |
| data.redisPerformance.slowlog | Array | 实例的慢查询日志，默认情况，执行命令超过10毫秒为慢查询 |
| data.redisPerformance.slowlog.exectime | String | 执行命令的时间点，如：2017-04-13 15:29:50 |
| data.redisPerformance.slowlog.duration | Int | 命令耗时，单位：微秒 |
| data.redisPerformance.slowlog.command | String | 慢查询命令 |
| data.redisPerformance.slowlog.first_key | String | 慢查询相关数据 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|11101|TimeFormatError|beginTime或者endTime时间格式错误，正确格式：2006-01-02 15:04:05|
|11216|InvalidBeginTime|开始时间 beginTime 大于当前时间|
|11217|InvalidQueryTime|有结束时间endTime，没有开始时间beginTime，只能查询[beginTime,endTime] 内实例性能|
|11218|QueryTimeRangeError|开始时间beginTime 大于结束时间endTime|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetRedisPerformance
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-edevql5z
&beginTime=2017-04-13 18:59:35
&endTime=2017-04-13 19:59:35
</pre>
返回示例如下：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "beginTime": "2017-04-13 18:59:35",
        "endTime": "2017-04-13 19:59:35",
        "redisPerformance": [
            {
                "redisId": "crs-edevql5z",
                "max_qps": 0.13,
                "qps": [
                    0.07,
                    0.13,
                    0.13,
                    0,
                    0.13,
                    0.07,
                    0,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.13,
                    0.13,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.13,
                    0.07,
                    0.07,
                    0.13,
                    0,
                    0.07,
                    0.13,
                    0,
                    0.07,
                    0.13,
                    0,
                    0.07,
                    0.07,
                    0,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.07,
                    0.13
                ],
                "max_conn": 10,
                "connection": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    10,
                    10,
                    9,
                    8,
                    0,
                    6,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
				"totalCountSlowLog": 50,
                "isTruncate": true,
                "slowlog": [
                    {
                        "exectime": "2017-04-13 19:28:20",
                        "duration": 150060,
                        "command": "DEL",
                        "first_key": "global:classificHotshops:ja_JP:0:566"
                    },
                    {
                        "exectime": "2017-04-13 19:29:47",
                        "duration": 121803,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    },
                    {
                        "exectime": "2017-04-13 19:33:10",
                        "duration": 300190,
                        "command": "DEL",
                        "first_key": "91dj:58df609440e13501b529fbbc10c520f5"
                    },
                    {
                        "exectime": "2017-04-13 19:35:03",
                        "duration": 12047,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    },
                    {
                        "exectime": "2017-04-13 19:38:52",
                        "duration": 38804,
                        "command": "ZREMRANGEBYSCORE",
                        "first_key": "sessionCacheDao:invalidSessionCache:"
                    },
                    {
                        "exectime": "2017-04-13 19:40:03",
                        "duration": 11855,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    },
                    {
                        "exectime": "2017-04-13 19:29:06",
                        "duration": 12039,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    },
                    {
                        "exectime": "2017-04-13 19:29:48",
                        "duration": 11459,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    },
                    {
                        "exectime": "2017-04-13 19:34:01",
                        "duration": 11878,
                        "command": "SETEX",
                        "first_key": "global:classificHotshops:pt_PT:3:0"
                    },
                    {
                        "exectime": "2017-04-13 19:35:04",
                        "duration": 12882,
                        "command": "HGETALL",
                        "first_key": "plf-kz-purl:6931316353"
                    }
                ]
            }
        ]
    }
}
```