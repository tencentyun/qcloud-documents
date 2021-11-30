## 命名空间

Namespace=QCE/WAF


>?拉取 Web 应用防火墙指标数据时，Region 请统一选择“广州”地域。

## 监控指标

| 指标英文名  | 指标中文名      | 单位 | 维度            |
| ----------- | --------------- | ---- | --------------- |
| Access      | 访问总次数      |  次    | domain、edition   |
| Attack      | Web 攻击次数    |    次  | domain、edition |
| Cc          | CC 攻击         |  次    | domain、edition |
| Down        | 下行带宽        | B/S  | domain、edition |
| Qps         | 每秒请求数      | 次   | domain、edition |
| Up          | 上行带宽        | B/S  | domain、edition |
| 4xx         | 4xx 状态码      |    次  | domain、edition |
| 5xx         | 5xx 状态码      |    次  | domain、edition |
| U4xx        | 源站 4xx 状态码 |    次  | domain、edition |
| U5xx        | 源站 5xx 状态码 |     次 | domain、edition |
| Bot         | BOT 攻击数      | 次   | domain、edition |
| Ratio5xx    | 5XX 占比        |  %    | domain、edition |
| Ratio4xx    | 4XX 占比        |   %   | domain、edition |
| RatioAttack | Web 攻击占比    |  %    | domain、edition |
| RatioBot    | BOT 攻击占比    |  %    | domain、edition |
| RatioCc     | CC 攻击占比     |   %   | domain、edition |

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释                      | 格式                                                    |
| ------------------------------ | -------- | ----------------------------- | ------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | domain   | 客户端攻击的域名维度名称      | 输入 String 类型维度名称：domain                        |
| Instances.N.Dimensions.0.Value | domain   | 客户端攻击的具体域名          | 输入客户端攻击的具体域名，例如：`www.cloud.tencent.com`          |
| Instances.N.Dimensions.0.Name  | edition  | Web 应用防火墙实例类型维度名称 | 输入 String 类型维度名称：edition                       |
| Instances.N.Dimensions.0.Value | edition  | Web 应用防火墙实例具体类型     | 输入 Web 应用防火墙实例具体类型，例如：SaaS WAF（入参值为0）或 CLB WAF（入参值为1） |

## 入参说明

**按客户端攻击的域名查询监控数据，入参取值如下：**
&Namespace=QCE/WAF
&Instances.N.Dimensions.0.Name=domain
&Instances.N.Dimensions.0.Value=客户端攻击的具体域名

**按Web应用防火墙实例查询监控数据，入参取值如下：**
&Namespace=QCE/WAF
&Instances.N.Dimensions.0.Name=edition
&Instances.N.Dimensions.0.Value=Web应用防火墙实例具体类型

