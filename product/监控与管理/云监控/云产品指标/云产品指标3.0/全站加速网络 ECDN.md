

## 命名空间

Namespace=QCE/DSA

## 监控指标

>!拉取全站加速网络监控指标数据时，Region 请统一选择“广州”地域。

| 指标英文名          | 指标中文名        | 指标含义                     | 单位 | 维度                  | 统计周期  |
| ------------------- | ----------------- | ---------------------------- | ---- | --------------------- | --------- |
| Bandwidth           | 访问带宽          | 访问带宽                     | Mbps | domain、<br>projectid | 60s、300s |
| HttpStatus200       | 状态码 (200)      | 状态码 (200)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus206       | 状态码 (206)      | 状态码 (206)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus302       | 状态码 (302)      | 状态码 (302)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus304       | 状态码 (304)      | 状态码 (304)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus404       | 状态码 (404)      | 状态码 (404)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus403       | 状态码 (403)      | 状态码 (403)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus502       | 状态码 (502)      | 状态码 (502)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus500       | 状态码 (500)      | 状态码 (500)次数             | 个   | domain、<br>projectid | 60s、300s |
| RequestTotal        | 总请求次数        | 总请求次数                   | 次   | domain、<br>projectid | 60s、300s |
| ProcessTime         | 平均响应时间      | 平均响应时间                 | ms   | domain、<br>projectid | 60s、300s |
| BackOriginTotal     | 总回源次数        | 总回源次数                   | 次   | domain、<br>projectid | 60s、300s |
| BackOriginFailTotal | 回源失败次数      | 回源失败次数                 | 次   | domain、<br>projectid | 60s、300s |
| BackOriginFailRate  | 回源失败率        | 回源失败率                   | %    | domain、<br>projectid | 60s、300s |
| BackOriginBandwidth | 回源带宽          | 回源带宽                     | Mbps | domain、<br>projectid | 60s、300s |
| FluxDownstream      | 下行流量          | 由 ECDN 平台流向客户端的总流量 | byte | domain、<br>projectid | 60s、300s |
| FluxUpstream        | 上行流量          | 由客户端流向 ECDN 平台的总流量 | byte | domain、<br>projectid | 60s、300s |
| HttpStatus401       | 状态码 (401)      | 状态码 (401)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus405       | 状态码 (405)      | 状态码 (405)次数             | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus416       | 状态码 (416)      | 状态码 (416)次数             | 个   | domain、<br>projectid | 60s、300s |
| DsaHttp200Rate      | 状态码比例（200） | 200状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp206Rate      | 状态码比例（206） | 206状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp302Rate      | 状态码比例（302） | 302状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp304Rate      | 状态码比例（304） | 304状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp401Rate      | 状态码比例（401） | 401状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp403Rate      | 状态码比例（403） | 403状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp405Rate      | 状态码比例（405） | 405状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp416Rate      | 状态码比例（416） | 416状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp500Rate      | 状态码比例（500） | 500状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp502Rate      | 状态码比例（502） | 502状态码占比                | %    | domain、<br>projectid | 60s、300s |
| HttpStatus0         | 状态码（0）       | 状态码 (0)次数               | 个   | domain、<br>projectid | 60s、300s |
| DsaHttp0Rate        | 状态码比例（0）   | 0状态码占比                  | %    | domain、<br>projectid | 60s、300s |
| HttpStatus2xx       | 状态码（2xx）     | 状态码（2xx）次数            | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus_3xx      | 状态码（3xx）     | 状态码（3xx）次数            | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus_4xx      | 状态码（4xx）     | 状态码（4xx）次数            | 个   | domain、<br>projectid | 60s、300s |
| HttpStatus_5xx      | 状态码（5xx）     | 状态码（5xx）次数            | 个   | domain、<br>projectid | 60s、300s |
| DsaHttp2xxRate      | 状态码比例（2xx） | 2xx状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp3xxRate      | 状态码比例（3xx） | 3xx状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp4xxRate      | 状态码比例（4xx） | 4xx状态码占比                | %    | domain、<br>projectid | 60s、300s |
| DsaHttp5xxRate      | 状态码比例（5xx） | 5xx状态码占比                | %    | domain、<br>projectid | 60s、300s |



## 各维度对应参数总览

| 参数名称                       | 维度名称  | 维度解释             | 格式                                                         |
| ------------------------------ | --------- | -------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | domain    | 网站域名的维度名称   | 输入 String 类型维度名称：domain                             |
| Instances.N.Dimensions.0.Value | domain    | 具体网站域名         | 输入具体网站域名，例如：test.com，可以通过 [DescribeDomains](https://cloud.tencent.com/document/product/570/42462) 接口获取 |
| Instances.N.Dimensions.0.Name  | projectid | 项目ID的具体维度名称 | 输入 String 类型维度名称：projectid                          |
| Instances.N.Dimensions.0.Value | projectid | 具体项目 ID           | 输入具体项目 ID，例如：0，可以通过 [DescribeDomains](https://cloud.tencent.com/document/product/570/42462) 接口获取 |

## 入参说明

**查询全站加速网络监控数据，支持下列两种方式入参：**

1. 通过网站域名入参：

&Namespace=QCE/DSA
&Instances.N.Dimensions.0.Name=domain
&Instances.N.Dimensions.0.Value=具体网站域名

2. 通过项目ID入参：

&Namespace=QCE/DSA
&Instances.N.Dimensions.0.Name=projectid
&Instances.N.Dimensions.0.Value=具体项目ID
