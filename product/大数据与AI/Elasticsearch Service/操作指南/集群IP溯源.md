本文介绍如何在腾讯云 Elasticsearch Service 上，开启 IP 溯源日志，进行请求来源的 IP 溯源。以帮助用户解决无法确定有哪些客户端在使用的情况。

## 使用限制
IP 溯源日志功能为腾讯云开发的ES内核能力，仅在腾讯云 Elasticsearch Service 的 PaaS 模式支持。当前支持的版本号为：6.8.2 / 7.10.1 / 7.14.2。

>? 2023年6月1日后创建的集群可直接使用该能力。在此之前创建的集群需要在控制台滚动重启集群，以将内核更新至最新才可使用。

## 设置 IP 溯源日志开启
### 集群维度动态配置开关
```
# req/rsp均支持独立开启、关闭
"http.tracer.request.enable"
"http.tracer.response.enable"

# 支持使用uri前缀过滤
"http.tracer.include"
"http.tracer.exclude"

# 支持ip过滤
"http.tracer.remote_ip.include"
"http.tracer.remote_ip.exclude"

# body打印支持独立开启、关闭
"http.tracer.request.body.enable"
"http.tracer.response.body.enable"
```
>?
> - 强烈建议您尽可能多的设置过滤条件，避免日志打印过多，影响集群性能，甚至引发磁盘写满风险。
> - 避免长期打开此开关，随用随开，用完及时关闭。

### 关闭示例
```
PUT _cluster/settings
{
  "transient": {
    "http.tracer.request.enable": false,
    "http.tracer.response.enable": false,
    "http.tracer.include": null,
	"http.tracer.exclude": null,
	"http.tracer.remote_ip.include": null,
    "http.tracer.remote_ip.exclude": null,
	"http.tracer.request.body.enable": false,
    "http.tracer.response.body.enable": false
  }
}

———关闭ip溯源日志———
不打印
```

### 开启示例
```
PUT _cluster/settings
{
  "transient": {
    "http.tracer.request.enable": true,
    "http.tracer.response.enable": true,
    "http.tracer.include": [
      "/.kibana/_search"
    ]
  }
}

———日志，打印req，rsp———
[2023-04-17T15:39:26,952][INFO ][o.e.h.HttpTracer         ] [1681467780000360532] [29940][null][GET][/.kibana/_search] received request from [Netty4HttpChannel{localAddress=/9.10.64.164:9200, remoteAddress=/9.2.1.38:41696}]
[2023-04-17T15:39:26,959][INFO ][o.e.h.HttpTracer         ] [1681467780000360532] [29940][null][OK][application/json; charset=UTF-8][2600808] sent response to [Netty4HttpChannel{localAddress=/9.10.64.164:9200, remoteAddress=/9.2.1.38:41696}] success [true]
---公网访问情况---
[2023-04-25T11:36:13,197][INFO ][o.e.h.HttpTracer         ] [1681703897000800432] [74][null][GET][/.kibana/_search] received request from [Netty4HttpChannel{localAddress=/9.10.66.6:9200, remoteAddress=/9.10.65.111:53349}], body [], x-forwarded-for [113.108.77.60]
[2023-04-25T11:36:13,238][INFO ][o.e.h.HttpTracer         ] [1681703897000800432] [74][null][OK][application/json; charset=UTF-8][2607129] sent response to [Netty4HttpChannel{localAddress=/9.10.66.6:9200, remoteAddress=/9.10.65.111:53349}] success [true]
```

```
PUT _cluster/settings
{
  "transient": {
    "http.tracer.request.enable": true,
    "http.tracer.response.enable": false,
    "http.tracer.request.body.enable": true,
    "http.tracer.include": [
      "/.kibana/_search"
    ]
  }
}

———日志，打印body，不打印rsp———
[2023-04-25T10:36:08,090][INFO ][o.e.h.HttpTracer         ] [1681703897000800432] [148][null][GET][/.kibana/_search] received request from [Netty4HttpChannel{localAddress=/9.10.66.6:9200, remoteAddress=/9.2.1.38:53310}], body [{"query":{"query_string":{"query":"*"}}}]
```

```
PUT _cluster/settings
{
  "transient": {
    "http.tracer.request.enable": true,
    "http.tracer.response.enable": false,
    "http.tracer.request.body.enable": true,
    "http.tracer.remote_ip.exclude": "9.2.1.38",
    "http.tracer.include": [
      "/.kibana/_search"
    ]
  }
}

———日志，过滤指定ip———
不打印
```
**注意事项**：
1. 公网访问溯源
	1. 内网访问情况，remoteAddress 就是真实 IP；公网访问情况，remoteAddress 是负载均衡的网关 IP。
	2. 取 header 中的 x-forwarded-for 可以拿到真实的公网访问 IP，req 日志会输出。
2. IP 过滤
	1. 不填写则不过滤，可数组形式填写多个 IP 过滤。
	2. 不支持通过公网 IP 过滤（x-forwarded-for）。

## 在腾讯云控制台查看 IP 溯源日志
1. 登录腾讯云[ Elasticsearch 控制台](https://console.cloud.tencent.com/es)，单击**集群名称**访问目标集群，跳转至**日志**页面。
2. 输入关键字查找IP溯源日志，6.8.2版本输入"o.e.h.n.Netty4HttpTracer"查找，7.10.1/7.14.2版本输入"o.e.h.HttpTracer"查找
![](https://qcloudimg.tencent-cloud.cn/raw/ce2672b2da348e8b3d7b7f669ff6945b.png)
