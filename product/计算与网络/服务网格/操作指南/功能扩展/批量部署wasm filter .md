TCM提供了2个工具来帮助用户快速部署wasm filter。工具支持二进制和镜像两种格式的wasm filter，可按照Label筛选部署范围。

### 前提条件

TCM >= 1.8
K8s >= 1.16

### 实现原理

目前业界主要的实现，都是通过挂载hostPath，将wasm文件挂载到容器内，这样的实现存在2个不足之处：

- 存量的Pod无法做到文件挂载，必须重启Pod加上路径挂载。
- 通过文件挂载的方式需要机器上存在对应的文件，否则EnvoyFilter创建之后可能导致envoy异常，此处存在潜在时序问题。

TCM基于envoy原生支持的remoteSource，可以在Pod启动之后拉取wasm，这样就可以不重启Pod同时支持wasm。其次，我们简化了架构，每个节点不再需要一个damonset的pod, 一定程度上节省了节点资源。TCM定义了一个名为`AutoWasm`的CRD，支持用户从镜像仓库或者其余数据源拉取wasm扩展文件。我们实现的controller会进行该自定义资源的List/Watch，并且生成最终的EnvoyFilter，同时会拉取并缓存wasm文件，该controller可以支持水平扩展。

![wasm.png](https://qcloudimg.tencent-cloud.cn/raw/e9db35e68b28da16216311da84b0c3dc.png)



### 组件获取

wasmc：与docker类似，该工具可以实现将.wasm上传到OCI标准的镜像仓库。
wasmer: 一个服务端程序，用于实现wasm的快速部署。

### 组件部署

wasmc:

[点击下载](https://mesh-1251707795.cos.ap-guangzhou.myqcloud.com/wasmc)

wasmer：

```shell
helm repo add servicemesh-tcm https://servicemesh.tencentcloudcr.com/chartrepo/tcm
helm install servicemesh-tcm/wasmer --generate-name
```



### 使用示例

##### 将wasm推到镜像仓库

```shell
# 将准备好的exaple.wasm文件push到OCI标准的镜像仓库，支持二进制或镜像格式
wasmc push ccr.ccs.tencentyun.com/xxx/wasm-add-header:v0.3 -f ./example.wasm

Pushed ccr.ccs.tencentyun.com/xxx/wasm-add-header:v0.3
Digest: sha256:xxxx

# 从仓库将文件pull到本地
wasmc pull ccr.ccs.tencentyun.com/xxx/wasm-add-header-wadecai:v0.3

Pulled ccr.ccs.tencentyun.com/xxx/wasm-add-header-wadecai:v0.3
Sha256: xxx
Location: xxx/filter.wasm
```


以下是一个使用示例，实现wasm的扩展部署

##### 从镜像仓库获取wasm扩展并部署

wasm部署文件aw.yaml

```yaml
apiVersion: wasm.tcm.io/v1alpha1
kind: AutoWasm
metadata:
  name: test
  namespace: default
spec:
  filter:
    applyPorts:
      - 9080
    rootID: test
    source:
      registry:
        image: ccr.ccs.tencentyun.com/xxx/wasm-add-header:v0.3
    vmID: test
  secret: test # 镜像仓库secret
  selector:
    matchLabels:
      app: details
```



> spec.filter.applyPorts: 需要生效的端口（该字段选填，默认所有端口）
> spec.filter.rootID: 唯一ID用于共享wasm的RootContext and Contexts（选填）
> spec.filter.vmID: wasm虚机ID（选填，不填会自动生成）
> spec.filter.sourc: wasm文件来源，支持registry和object，代表镜像仓库和对象存储
> spec.selector.matchLabels: 用于匹配需要生效的Pod
> spec.secret：镜像仓库密码，公开镜像可以不填写secret

其中，source.registry部分表示从镜像仓库获取wasm扩展。

##### 从cos获取wasm扩展并部署

```yaml
apiVersion: wasm.tcm.io/v1alpha1
kind: AutoWasm
metadata:
  name: test
  namespace: default
spec:
  filter:
    applyPorts:
      - 9080
    rootID: test
	    source:
      object:
        url: https://aaaa.com/bbb
    vmID: test
  selector:
    matchLabels:
      app: details
```



> 当前只支持获取Public对象存储。

##### 创建并查看效果

```shell
kubectl apply -f aw.yaml
```



> aw. yaml文件内容如上文所述，wasm文件从镜像仓库获取

- 检查aw CR已经EnvoyFilter

```shell
kubectl get aw
NAME   SECRET   MATCH               SOURCE                                                                     APPLYPORTS   TIME                   PHASE
test   test     {"app":"details"}   {"registry":{"image":"ccr.ccs.tencentyun.com/xxx/wasm-add-header:v0.3"}}   [9080]       2021-10-27T10:00:36Z   Synced

kubectl get envoyfilter test -o yaml

apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  creationTimestamp: "2021-10-28T08:25:24Z"
  name: test
  namespace: default
spec:
  configPatches:
  - applyTo: HTTP_FILTER
    match:
      context: SIDECAR_INBOUND
      listener:
        filterChain:
          filter:
            name: envoy.filters.network.http_connection_manager
            subFilter:
              name: envoy.filters.http.router
        portNumber: 9080
    patch:
      operation: INSERT_BEFORE
      value:
        name: envoy.filters.http.wasm
        typedConfig:
          '@type': type.googleapis.com/udpa.type.v1.TypedStruct
          typeUrl: type.googleapis.com/envoy.extensions.filters.http.wasm.v3.Wasm
          value:
            config:
              name: test
              rootId: test
              vmConfig:
                code:
                  remote:
                    httpUri:
                      cluster: outbound|8081||wasmer.istio-system.svc.cluster.local
                      timeout: 600s
                      uri: wasmer.istio-system:8081/wasm/750d63889653e7117fcbc0831f10f0e1d3f7ec0c82fe5787b71d08a783e3393f
                    sha256: 750d63889653e7117fcbc0831f10f0e1d3f7ec0c82fe5787b71d08a783e3393f
                runtime: envoy.wasm.runtime.v8
                vmId: test
  workloadSelector:
    labels:
      app: details
```



- 校验效果

```shell
kubectl get pod -o wide

NAME                              READY   STATUS    RESTARTS      AGE   IP             NODE      NOMINATED NODE   READINESS GATES
details-v1-79f774bdb9-2vhjx       2/2     Running   0             4m   172.16.0.10     cwd-dev   <none>           <none>

curl -s 172.16.0.10:9080 -vvv

* About to connect() to 10.244.0.157 port 9080 (#0)
*   Trying 10.244.0.157...
* Connected to 10.244.0.157 (10.244.0.157) port 9080 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.29.0
> Host: 172.16.0.10:9080
> Accept: */*
>
< HTTP/1.1 404 Not Found
< content-type: text/html; charset=ISO-8859-1
< server: istio-envoy
< date: Thu, 28 Oct 2021 06:16:22 GMT
< content-length: 273
< x-envoy-upstream-service-time: 1
< hello: world
< x-envoy-decorator-operation: details.default.svc.cluster.local:9080/*
<
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
  <HEAD><TITLE>Not Found</TITLE></HEAD>
  <BODY>
    <H1>Not Found</H1>
    `/' not found.
    <HR>
    <ADDRESS>
     WEBrick/1.6.0 (Ruby/2.7.1/2020-03-31) at
     172.16.0.10:9080
    </ADDRESS>
  </BODY>
</HTML>
```

可以看到`hello: world`已经添加成功