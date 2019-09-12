## 接口描述

**GetHostInfoById** 查询域名的详细配置信息。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>


>!
- 支持一次查询多个域名的详细信息
- 调用频率限制为1000次/分钟
- 接口已支持子账号调用，权限配置可参考权限 [配置示例](https://cloud.tencent.com/document/product/228/14867)

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetHostInfoById。

| 参数名称 | 是否必选 | 类型 | 描述                             |
| -------- | -------- | ---- | -------------------------------- |
| ids.n    | 是       | Int  | 查询的域名 ID，支持查询一个或多个 |

### 详细说明 

支持查询一个或多个 域名，查询多个域名时，参数传入方式可参考：

```
ids.0=123&ids.1=1234
```


## 出参说明

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array  | 结果数据，详细说明见下文<br/>详见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) |

### 详细说明

#### data 

| 参数名称 | 类型  | 描述                     |
| -------- | ----- | ------------------------ |
| hosts    | Array | 域名详细配置信息，见下文 |
| total    | Int   | 域名总数                 |

#### hosts

##### 基本配置

| 参数名称          | 类型   | 描述                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| id                | Int    | 域名接入 CDN 后的的标识 ID                                   |
| app_id            | Int    | 域名所属账号的 APPID                                         |
| owner_uin         | Int    | 域名所属账号                                                 |
| project_id        | Int    | 域名所属项目 ID                                              |
| host              | String | 域名                                                         |
| cname             | String | CDN 分配的 .cdn.dnsv1.com 后缀加速域名                       |
| host_type         | String | 接入方式<br/>"cos"：表示域名接入时使用的托管源为 COS 源<br/>"cname"：表示域名接入时使用的是自有源站<br/>"ftp"：表示该域名接入时使用了 CDN 提供的 FTP 托管源 |
| service_type      | String | 域名业务类型<br/>"web"：静态内容加速<br/>"download"：文件下载加速<br/>"media"：流媒体点播加速<br/>"live"：流媒体直播加速 |
| origin            | String | 域名源站配置                                                 |
| fwd_host_type     | String | 回源设置类型<br/>"default"：表示接入的域名即回源地址<br/>"custom"：该域名使用了自定义的回源 host |
| fwd_host          | String | 回源 host                                                     |
| bucket_name       | String | COS 源时，对应的 bucket 名称                                 |
| cache             | Object | 缓存规则设置，详细说明见下文                                 |
| status            | Int    | 域名加速状态<br/>1：域名审核中<br/>2：域名审核未通过<br/>3：域名审核通过处于部署中<br/>4：域名部署中<br/>5：域名已启动<br/>6：域名已关闭 |
| disabled          | Int    | 域名封禁状态<br/> 0：表示域名未被封禁，其他均为已封禁        |
| message           | String | 域名状态信息<br/> "已关闭"、"已启动"、"部署中"               |
| create_time       | String | 域名接入时间                                                 |
| update_time       | String | 更新时间                                                     |
| deleted           | String | 是否删除<br/>"no"：表示域名未删除<br/>"yes"：表示域名已删除  |
| middle_resource   | Int    | 中间源开关<br/>-1：表示该域名关闭了中间源服务<br/>0：表示该域名开启了中间源服务 |
| refer             | Object | 防盗链设置，详细说明见下文                                   |
| cache_mode        | String | 缓存规则类型<br/>"simple"：表示缓存完全依赖控制台设置<br/>"custom"：则表示缓存依赖控制台设置的缓存时间和源站吐出的 max-age 的最小值 |
| furl_cache        | String | 过滤参数<br/>"on"：开启全路径缓存，关闭过滤参数<br/>"off"：关闭全路径缓存，开启过滤参数 |
| http2             | Int    | 是否开启HTTP2.0<br/>"1"：表示已开启http2.0                   |
| ssl_type          | Int    | 是否开通HTTPS<br/>"0"：未开通HTTPS配置<br/>若为其他，则表示已开通HTTPS配置 |
| ssl_deploy_time   | String | SSL 部署时间                                                  |
| ssl_expire_time   | String | SSL 过期时间                                                  |
| ssl_cert_name     | String | 证书备注名                                                   |
| ssl_cert_id       | String | 托管证书 ID                                                   |
| seo               | String | 是否开启 SEO 优化<br/>"off"：表示未开启<br/>"on"：表示开启     |
| status_code_cache | Object | 状态码缓存设置<br/>"404"：404状态码缓存过期时间，单位为秒，设置为0表示不缓存 |
| safety_chain      | Object | 时间戳鉴权设置<br/>"switch"：开关，on-开启，off-关闭<br/>"key"：鉴权key<br/>"time_format"：时间戳格式，10-十进制，16-16进制<br/>"ttl_time"：过期时间<br/>更多配置说明可查看[鉴权配置](https://cloud.tencent.com/document/product/228/13677) |
| capping           | Object | 带宽上限设置<br/>"bandwidth"：设置的带宽封顶阈值<br/>"uint"：设置带宽封顶阈值的单位<br/>"hy"：yes 表示设置为请求回源<br/>"active"：yes 表示开启带宽封顶 |
| host_config       | Object | 其他高级配置项，具体见下文                                   |

##### host_config 更多配置

| 参数名称         | 类型   | 描述                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| backup_origin    | String | 备用源站设置                                                 |
| https_switch     | String | https 强制跳转设置<br/>"on"：表示开启 https 强制跳转，默认跳转方式为302<br/>"off"：表示未开启 |
| follow302_switch | String | 302跟随配置<br/>"on"：表示开启302跳转跟随<br/>"off"：表示关闭302跳转跟随 |
| ip_cc            | Object | IP 黑白名单配置<br/>"type"：2 表示白名单，1 表示黑名单<br/>"list"：具体的 IP/IP 段清单 |
| ip_freq_limit    | Object | IP 访问限频配置<br/> "type"：1 表示开启，0 表示关闭<br/>"limit_count"：设置的 QPS 阈值 |
| rsp_header       | Object | response-header 配置                                         |
| video_switch     | String | 视频拖拽配置<br/>"on"：开启视频拖拽<br/>"off"：关闭视频拖拽  |
| chunkFd_switch   | String | 分片回源配置<br/>"on"：开启分片回源<br/>"off"：关闭分片回源  |

##### cache

| 参数名称 | 类型   | 描述                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| type     | Int    | 缓存配置类型<br/>"0"：所有文件<br/>"1"：文件类型<br/>"2"：文件夹类型<br/>"3"：全路径文件 |
| rule     | String | 匹配规则，与上述 type 相对应                                 |
| time     | Int    | 缓存时间，单位为 秒                                          |
| unit     | String | 设置缓存时间时所用单位<br/>"d"：表示天<br/>"h"：表示小时<br/>"m"：表示分钟<br/>"s"：表示秒 |

##### refer

| 参数名称  | 类型  | 描述                                                         |
| --------- | ----- | ------------------------------------------------------------ |
| type      | Int   | 防盗链类型<br/>"0"：未配置防盗链<br/>"1"：黑名单<br/>"2"：白名单 |
| null_flag | Int   | 防盗链是否为空，若为1，则表示防盗链为空                      |
| list      | Array | 配置的防盗链名单                                             |

>! 未在上述文档中说明的字段为**无效字段**或**内部标识字段**，可直接忽略。



## 调用案例

### 示例参数

```
ids.0:1234
```

### GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetHostInfoById
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462434613
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXX
&ids.0=1234
```

### POST 请求

POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetHostInfoById',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'ids.0' => 1234
)
```

### 结果示例

```json
{
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"hosts": [{
			"id": 1234,
			"app_id": 12345678,
			"owner_uin": 87654321,
			"project_id": 0,
			"host": "www.test.com",
			"host_type": "cname",
			"service_type": "web",
			"origin": "2.2.2.2",
			"cache": [{
					"type": 0,
					"rule": "all",
					"time": 2592000,
					"unit": "d"
				},
				{
					"type": 1,
					"rule": ".php;.jsp;.asp;.aspx",
					"time": 0,
					"unit": "s"
				}
			],
			"status": 4,
			"disabled": 0,
			"message": "部署中",
			......
}
```





