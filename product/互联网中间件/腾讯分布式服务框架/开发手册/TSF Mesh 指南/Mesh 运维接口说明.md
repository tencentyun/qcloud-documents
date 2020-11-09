Service Mesh 微服务架构的核心是在用户的服务侧同机（虚拟机）或同 Pod（容器）部署一个网络代理来让用户实现无侵入的接入微服务。因为代理是以本地额外的服务实现的，本地应用无感知，为了快速定位出现的问题，代理侧提供了大量的 HTTP 运维接口。

## 代理的组件
本地代理分为以下三个组件：
- **pilot-agent**
管理整个代理侧环境，如 iptables 规则的更新、本地应用和服务的配置管理，同时负责 mesh-dns 和 envoy 组件的生命周期管理。
- **Mesh-DNS**
托管本地的 DNS 请求，将 Mesh 结构内的流量导入本地代理。
- **Envoy**
负责服务发现和路由，HTTP 请求的负载均衡等，负责处理流入本地服务和从本地服务流出的所有流量。

##  iptables 规则
为了将流入和流出的流量导入到本地代理中，TSF Mesh 使用了 iptables 作流量转发，一般规则如下（虚拟机环境在本地，容器环境在 sidecar 容器中）：
 
**iptables -t nat -L -n**
```plaintext
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
ISTIO_INBOUND  tcp  --  0.0.0.0/0            0.0.0.0/0           

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ISTIO_OUTPUT  all  --  0.0.0.0/0            0.0.0.0/0           
DNS_OUTPUT  all  --  0.0.0.0/0            0.0.0.0/0           

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         

Chain DNS_OUTPUT (1 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0            owner UID match 1000
DNAT       udp  --  0.0.0.0/0            0.0.0.0/0            udp dpt:53 to:127.0.0.1:55354
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:53 to:127.0.0.1:55354

Chain ISTIO_INBOUND (1 references)
target     prot opt source               destination         
ISTIO_REDIRECT  tcp  --  0.0.0.0/0            9.77.7.28            tcp dpt:8089

Chain ISTIO_OUTPUT (1 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0            owner UID match 1000
DNAT       tcp  --  0.0.0.0/0            {特定 IP}        to:9.77.7.28:15001

Chain ISTIO_REDIRECT (1 references)
target     prot opt source               destination         
REDIRECT   tcp  --  0.0.0.0/0            0.0.0.0/0            redir ports 15001
```

**DNS_OUTPUT**
- 托管本地的 DNS 请求到 mesh-dns 进程。
- 第一条 RETURN 规则非常重要，不再托管从 mesh-dns 转发出来的 DNS 请求。
- 后面两条是托管本地的53端口（即 DNS 原生请求端口）的流量。

**ISTIO_INBOUND**
- 托管访问本地服务的流量。
- 可以看到托管的流量非常细粒度，只托管注册到 Mesh 框架的`9.77.7.28:8089`的流量。

**ISTIO_OUTPUT**
- 托管从本地流出的流量。
- 第一条 RETURN 规则非常重要，不再托管从代理转发出来的请求。
- 第二条是将访问{特定 IP} - 从 DNS 中获得的流量导入到本地的代理中（即引用的 ISTIO_REDIRECT 规则）。


## 本地接口
如果在本地调用`netstat -lntp | grep 127.0.0.1`，会出现以下三个 listen 服务，分别是各个本地组件提供的运维接口的 IP 和 port。
```plaintext
tcp        0      0 127.0.0.1:15020         0.0.0.0:*               LISTEN      5168/pilot-agent    
tcp        0      0 127.0.0.1:15021         0.0.0.0:*               LISTEN      5261/mesh-dns       
tcp        0      0 127.0.0.1:15000         0.0.0.0:*               LISTEN      5266/envoy
```


### pilot-agent 运维接口
**curl 127.0.0.1:15020/help**
```plaintext
admin commands are:
	GET /health: print out the health info for data-plane
	GET /config_dump/{component}: print out the configuration of the component, component can be pilot-agent/envoy/mesh-dns
	GET /help: print out list of admin commands
	GET /config/agent: print out the pilot-agent configuration
	GET /config/services: print out the services info
	GET /config/global: print out the global mesh configuration
	GET /config/envoy: print out the envoy startup configuration
	GET /version: print out the pilot-agent version
	GET /version/{component}: print out the version of the component, component can be pilot-agent/envoy/mesh-dns
	GET /latest_error: print out the latest error info
	GET /status: print out the status, result could be <INIT>, <CONFIG_READY>, <FLOW_TAKEOVER>, <SERVICE_REGISTERED>
	GET /epoch/{component}: print out the component restart epoch, component can be envoy/mesh-dns
	POST /hot_restart/{component}: hot restart the component process, component can be envoy/mesh-dns
	PUT /update: update the component
	PUT /logging/{scope}/{level}: dynamic change logging level, scope can be healthz/admin/ads/default/model, level can be debug/info/warn/error/none
```
其中主要的接口如下：
- /status：查看本地各个组件的状态。
- /health：查看本地各个组件的健康信息。
- /version：查看本地代理服务的版本。

###  Mesh-DNS 运维接口
**curl 127.0.0.1:15021/help**
```plaintext
admin commands are:
	GET /health: print out the health info for mesh-dns
	GET /config_dump: print out all of the mesh-dns runtime configs
	GET /latest_error: print out the latest error info
	GET /help: print out list of admin commands
	GET /version: print out version info
	GET /status: print out status info
	PUT /logging/{scope}/{level}: dynamic change logging level, scope can be admin/default/healthz/model, level can be error/none/debug/info/warn
```
其中主要的接口如下：
 /config_dump：查看本地托管的 DNS 信息。

###  Envoy 运维接口
**curl 127.0.0.1:15000/help**
```plaintext
admin commands are:
  /: Admin home page
  /certs: print certs on machine
  /clusters: upstream cluster status
  /config_dump: dump current Envoy configs (experimental)
  /cpuprofiler: enable/disable the CPU profiler
  /healthcheck/fail: cause the server to fail health checks
  /healthcheck/ok: cause the server to pass health checks
  /help: print out list of admin commands
  /hot_restart_version: print the hot restart compatibility version
  /listeners: print listener addresses
  /logging: query/change logging levels
  /quitquitquit: exit the server
  /reset_counters: reset all counters to zero
  /runtime: print runtime values
  /runtime_modify: modify runtime values
  /server_info: print server version/status information
  /stats: print server stats
  /stats/prometheus: print server stats in prometheus format
```
其中主要的接口如下：
- /clusters：查看各个部署组下的实例信息和健康信息，例如查看本地服务节点的健康信息`curl -s 127.0.0.1:15000/clusters | grep "in#"`。
- /config_dump：将服务路由信息打印出来，一般调用`curl -s 127.0.0.1:15000/config_dump -o 1.json`，打开1.json即可查看路由信息。
