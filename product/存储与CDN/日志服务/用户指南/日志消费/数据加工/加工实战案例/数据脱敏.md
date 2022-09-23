## 场景描述

小王将日志采集到日志服务（Cloud Log Service，CLS），日志数据中含有用户 ID（**dev@12345**）、登录的 IP 地址（**11.111.137.225**）、手机号码（**13912345678**），小王想将这些敏感信息脱敏。

## 场景分析

该日志本身是一个结构化的日志，因此可以直接对字段进行脱敏处理。

## 原始日志
``` 
    {
        "Id": "dev@12345",
        "Ip": "11.111.137.225",
        "phonenumber": "13912345678"
    }
```

## DSL 加工函数

```
fields_set("Id",regex_replace(v("Id"),regex="\d{3}", replace="***",count=0))
fields_set("Id",regex_replace(v("Id"),regex="\S{2}", replace="**",count=1))
fields_set("phonenumber",regex_replace(v("phonenumber"),regex="(\d{0,3})\d{4}(\d{4})", replace="$1****$2"))
fields_set("Ip",regex_replace(v("Ip"),regex="(\d+\.)\d+(\.\d+\.\d+)", replace="$1***$2",count=0))
```

## DSL 加工函数详解 

1. 对 **Id** 字段进行脱敏处理，结果为dev@\*\*\*45。
```
fields_set("Id",regex_replace(v("Id"),regex="\d{3}", replace="***",count=0))
```
2. 对 **Id** 字段进行二次脱敏处理，结果为\*\*v@\*\*\*45。
```
fields_set("Id",regex_replace(v("Id"),regex="\S{2}", replace="**",count=1))
```
3. 对 **phonenumber** 字段进行脱敏处理，将中间的4位数替换为\*\*\*\*，结果为139\*\*\*\*5678。
```
fields_set("phonenumber",regex_replace(v("phonenumber"),regex="(\d{0,3})\d{4}(\d{4})", replace="$1****$2"))
```
4. 对 **IP** 字段进行脱敏处理，将第二段替换为\*\*\*，结果为11.\*\*\*137.225。
```
fields_set("Ip",regex_replace(v("Ip"),regex="(\d+\.)\d+(\.\d+\.\d+)", replace="$1***$2",count=0))
```

## 加工结果

```
{"Id":"**v@***45","Ip":"11.***.137.225","phonenumber":"139****5678"} 
```
