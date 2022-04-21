## 概述 

[对象存储（Cloud Object Storage，COS）](https://console.cloud.tencent.com/cos5) 访问日志记录了用户对 COS 资源的访问信息，包括上传对象（PUT），删除对象（DELETE），访问对象（GET）等。通过分析访问日志，用户可以完成审计回溯，如删除资源记录，同时也可以完成资源热门相关的资源统计等能力。本文介绍 COS 如何访问日志。


## 前提条件

已将 COS 日志采集至日志服务（Cloud Log Service，CLS），详情请参见 [COS 开启实时日志](https://cloud.tencent.com/document/product/614/62137)。


## 访问日志介绍

COS 访问日志记录了源存储桶，用户 ID，请求方法等信息。

| 字段序号 | 名 称              | 含 义                                                        | 示例                                                         |
| :------- | :----------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1        | eventVersion       | 记录版本                                                     | 1.0                                                          |
| 2        | bucketName         | 存储桶名称                                                   | examplebucket-1250000000                                     |
| 3        | qcsRegion          | 请求地域                                                     | ap-beijing                                                   |
| 4        | eventTime          | 事件时间（请求结束时间，UTC 0时 时间戳）                     | 2018-12-01T11:02:33Z                                         |
| 5        | eventSource        | 用户访问的域名                                               | examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com       |
| 6        | eventName          | 事件名称                                                     | UploadPart                                                   |
| 7        | remoteIp           | 来源 IP                                                      | 192.168.0.1                                                  |
| 8        | userSecretKeyId    | 用户访问 KeyId                                               | AKIDNYVCdoJQyGJ5brTf                                         |
| 9        | reservedFiled      | 保留字段                                                     | 保留字段，显示为`-`                                        |
| 10       | reqBytesSent       | 请求字节数（Bytes）                                          | 83886080                                                     |
| 11       | deltaDataSize      | 请求对存储量的改变（Bytes）                                  | 808                                                          |
| 12       | reqPath            | 请求的文件路径                                               | /folder/text.txt                                             |
| 13       | reqMethod          | 请求方法                                                     | put                                                          |
| 14       | userAgent          | 用户 UA                                                      | cos-go-sdk-v5.2.9                                            |
| 15       | resHttpCode        | HTTP 返回码                                                  | 404                                                          |
| 16       | resErrorCode       | 错误码                                                       | NoSuchKey                                                    |
| 17       | resErrorMsg        | 错误信息                                                     | The specified key does not exist.                            |
| 18       | resBytesSent       | 返回字节数（Bytes）                                          | 197                                                          |
| 19       | resTotalTime       | 请求总耗时（毫秒，等于响应末字节的时间-请求首字节的时间）    | 4295                                                         |
| 20       | logSourceType      | 日志源类型                                                   | USER（用户访问请求），CDN（CDN 回源请求）                    |
| 21       | storageClass       | 存储类型                                                     | STANDARD，STANDARD_IA，ARCHIVE                               |
| 22       | accountId          | 存储桶所有者ID                                               | 100000000001                                                 |
| 23       | resTurnAroundTime  | 请求服务端耗时（毫秒，等于响应首字节的时间-请求末字节的时间） | 4295                                                         |
| 24       | requester          | 访问者                                                       | 主账号 ID：子账号 ID，如果是匿名访问则显示`-`。              |
| 25       | requestId          | 请求 ID                                                      | NWQ1ZjY4MTBfMjZiMjU4NjRfOWI1N180NDBiYTY=                     |
| 26       | objectSize         | 对象大小（Bytes）                                            | 808，如果您使用分块上传，objectSize 字段只会在完成上传的时候显示，各个分块上传期间该字段显示`-` |
| 27       | versionId          | 对象版本 ID                                                  | 随机字符串                                                   |
| 28       | targetStorageClass | 目标存储类型，发起复制操作的请求会记录该字段                 | STANDARD，STANDARD_IA，ARCHIVE                               |
| 29       | referer            | 请求的 HTTP referer                                          | `*.example.com`或者111.111.111.1                             |
| 30       | requestUri         | 请求 URI                                                     | "GET /fdgfdgsf%20/%E6%B5%AE%E7%82%B9%E6%95%B0 HTTP/1.1"      |


## 场景示例

### 场景1：审计追溯

#### 需求场景

某个对象文件访问不了，定位原因。
![image-20210824201630965](https://main.qcloudimg.com/raw/27278487fb0dc287d8fd0c2893bea36a.png)

#### 解决方案

进入 COS 访问日志检索页面，输入对象名称作为关键词检索日志。
```
json-log2019-05-09_00645d9a-1118-4d69-8411-cfd57ede9ea1_000
```
![image-20210824203316458](https://main.qcloudimg.com/raw/23497a30f40395ade78356ede3d6e5aa.png)
通过时间柱状图，得知近1天有14条日志记录。针对14条日志记录下钻分析，点击左侧字段快速分析栏，查看 **resHttpCode** 信息。
![image-20210824203424637](https://main.qcloudimg.com/raw/a9aed31374180a80bb946a95b2bd62cd.jpg)
通过快速分析得知，6条非200的请求信息，其中5条 **resHttpCode** 为403的日志信息和一条 **resHttpCode** 为204日志信息，单击快速检索这两个 httpcode 的日志。
![image-20210824202954618](https://main.qcloudimg.com/raw/46fa533cbc164a9115e67d47996ea610.png)
由日志可以得知，5条错误码为 Access Deny 日志均为访问对象失败日志，通过 resHttpCode 为204的日志发现，用户`1000******`在8月24日20点16分，通过 COS 控制台执行了删除 object 操作，导致对象访问失败。

### 场景2：运营统计

#### 需求场景

- 统计当天访问量 Top10热门的 bucket
- 统计当天某个 bucket 的访问趋势
- 错误请求 Top10的访问者
- 失败操作的 bucket 分布
- 用户请求有效率趋势

#### 解决方案

- 统计当天访问量 Top10热门的 bucket
```
(reqMethod:"GET") | select bucketName, count(*) group by bucketName
```
![image-20210824203857045](https://main.qcloudimg.com/raw/1940741d830d1740d153aa8dd5846680.png)
- 统计当天某个 bucket 的访问趋势
```sql
* | select time_series(__TIMESTAMP__, '1m', '%Y-%m-%dT%H:%i:%s+08:00', '0') AS time, count(*) as pv, reqMethod group by time, reqMethod order by time limit 200
```
![image-20210824204151584](https://main.qcloudimg.com/raw/25dd0853f46113b934339606950e7c9c.png)
- 错误请求 Top10的访问者
```
resHttpCode:>200 | select remoteIp, count(*) group by remoteIp
```
![image-20210825171944260](https://main.qcloudimg.com/raw/c52f013b47511bd348d4734b517bf7ab.png)
- 失败操作的 bucket 分布
```
resHttpCode:>200 | select bucketName, count(*) group by bucketName
```
![image-20210825172054202](https://main.qcloudimg.com/raw/6cd6315f2fd3eea0765cbfe242998e48.png)
- 用户请求有效率趋势
```
* | select time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0')  as time,round(sum(case when resHttpCode=200 then 1.00 else 0.00 end) / cast(count(*) as double) * 100,1) as "请求有效率" group by time limit 1000
```
![image-20210825172428752](https://main.qcloudimg.com/raw/cf8d9b146e69e66b82dfd229e6f3bbe4.png)
- 用户请求来源分布
```
* | select ip_to_province(remoteIp) as province ,  count(*) as c group by province order by c desc limit 50
```
![image-20210826103822974](https://main.qcloudimg.com/raw/e5a25ac492765be8e41cfb8a9e938f95.png)



