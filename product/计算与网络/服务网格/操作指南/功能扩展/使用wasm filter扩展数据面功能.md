Wasm 是 WebAssembly 的缩写，可以编写二进制形式的指令加载到 envoy filter chain 中，实现网格数据面能力扩展。这种形式使得 envoy 和扩展组件的解耦，用户不再需要通过修改 envoy 代码、编译特殊的 envoy 版本来实现能力扩展，并且还具备动态加载和安全隔离等优势。

从 Istio 1.6 版本开始，Proxy-Wasm 沙盒 API 取代了 Mixer 作为 Istio 主要的扩展实现方案，用于实现 envoy 和 wasm 虚拟机之间的交互，因此通过 wasm filter 来扩展 envoy 需要使用 [Proxy-WASM SDK](https://github.com/proxy-wasm/spec)。

通常编写 wasm 文件扩展网格数据面能力主要分为以下几步：

1. 编写 wasm filter，可请参见 [示例](https://github.com/envoyproxy/envoy-wasm/tree/19b9fd9a22e27fcadf61a06bf6aac03b735418e6/examples/wasm)。
2. 将 wasm filter 注入到 configmap 中，通过 configmap 将 wasm filter 挂载到任意工作负载，避免将 wasm filter 拷贝到多个 node 上。
   ```bash
   kubectl create cm -n foo example-filter --from-file=example-filter.wasm
   ```
3. 将 wasm filter 挂载到业务工作负载，可利用 [Istio 的 annotation 机制](https://istio.io/latest/docs/reference/config/annotations/)，在创建工作负载的时候自动挂载相应的文件：
   ```yaml
   sidecar.istio.io/userVolume: '[{"name":"wasmfilters-dir","configMap": {"name": "example-filter"}}]'
   sidecar.istio.io/userVolumeMount: '[{"mountPath":"/var/local/lib/wasm-filters","name":"wasmfilters-dir"}]'
   ```
   将 annotation 应用到对应的工作负载之上：
   ```bash
   
   kubectl patch deployment -n foo frontpage-v1 -p '{"spec":{"template":{"metadata":{"annotations":{"sidecar.istio.io/userVolume":"[{\"name\":\"wasmfilters-dir\",\"configMap\": {\"name\": \"example-filter\"}}]","sidecar.istio.io/userVolumeMount":"[{\"mountPath\":\"/var/local/lib/wasm-filters\",\"name\":\"wasmfilters-dir\"}]"}}}}}'
   ```
4. 创建 envoyfilter，将 wasm filter 添加到对应工作负载的 envoy filter chain 中，使其生效。
   ```yaml
   apiVersion: networking.istio.io/v1alpha3
   kind: EnvoyFilter
   metadata:
     name: frontpage-v1-examplefilter
     namespace: foo
   spec:
     configPatches:
     - applyTo: HTTP_FILTER
       match:
         context: SIDECAR_INBOUND
         listener:
           filterChain:
             filter:
               name: envoy.http_connection_manager
               subFilter:
                 name: envoy.router
       patch:
         operation: INSERT_BEFORE
         value:
           config:
             config:
               name: example-filter
               rootId: my_root_id
               vmConfig:
                 code:
                   local:
                     filename: /var/local/lib/wasm-filters/example-filter.wasm
                 runtime: envoy.wasm.runtime.v8
                 vmId: example-filter
                 allow_precompiled: true
           name: envoy.filters.http.wasm
     workloadSelector:
       labels:
         app: frontpage
         version: v1
   EOF
   ```



至此，wasm filter 部署完成，另一种 wasm filter 的使用形式是镜像，请参见 [制作 wasm filter 镜像](https://docs.solo.io/web-assembly-hub/latest/tutorial_code/getting_started/)，利用 WASME 工具部署，请参见 [使用 wasme 部署 wasm filter](https://docs.solo.io/web-assembly-hub/latest/tutorial_code/deploy_tutorials/deploying_with_istio/)。

可以看出，wasm filter 的部署较为繁琐，尤其是需要大规模部署的时候，没有工具将难以进行批量部署和管理，TCM 提供了便捷的部署工具，可以利用工具将二进制或者镜像形式的 wasm filter 批量部署到业务中，详情见 [使用 TCM 工具批量部署 wasm filter](https://cloud.tencent.com/document/product/1261/65362)。

