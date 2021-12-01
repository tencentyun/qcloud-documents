> Wasm是WebAssembly的缩写，可以编写二进制形式的指令加载到envoy filter chain中，实现网格数据面能力扩展。这种形式使得envoy和扩展组件的解耦，用户不再需要通过修改envoy代码、编译特殊的envoy版本来实现能力扩展，并且还具备动态加载和安全隔离等优势。

从Istio 1.6版本开始，Proxy-Wasm 沙盒 API 取代了 Mixer 作为 Istio 主要的扩展实现方案，用于实现envoy和wasm虚拟机之间的交互，因此通过wasm filter来扩展envoy需要使用[Proxy-WASM SDK](https://github.com/proxy-wasm/spec)。

通常编写wasm文件扩展网格数据面能力主要分为以下几步：

1. 编写wasm filter，可参考[样例](https://github.com/envoyproxy/envoy-wasm/tree/19b9fd9a22e27fcadf61a06bf6aac03b735418e6/examples/wasm)。

2. 将wasm filter注入到configmap中，通过configmap将wasm filter挂载到任意工作负载，避免将wasm filter拷贝到多个node上。

   ```bash
   kubectl create cm -n foo example-filter --from-file=example-filter.wasm
   ```

3. 将wasm filter挂载到业务工作负载，可利用[Istio的annotation机制](https://istio.io/latest/docs/reference/config/annotations/)，在创建工作负载的时候自动挂载相应的文件：

   ```yaml
   sidecar.istio.io/userVolume: '[{"name":"wasmfilters-dir","configMap": {"name": "example-filter"}}]'
   sidecar.istio.io/userVolumeMount: '[{"mountPath":"/var/local/lib/wasm-filters","name":"wasmfilters-dir"}]'
   ```

   将annotation应用到对应的工作负载之上：

   ```bash
   
   kubectl patch deployment -n foo frontpage-v1 -p '{"spec":{"template":{"metadata":{"annotations":{"sidecar.istio.io/userVolume":"[{\"name\":\"wasmfilters-dir\",\"configMap\": {\"name\": \"example-filter\"}}]","sidecar.istio.io/userVolumeMount":"[{\"mountPath\":\"/var/local/lib/wasm-filters\",\"name\":\"wasmfilters-dir\"}]"}}}}}'
   ```

4. 创建envoyfilter，将wasm filter添加到对应工作负载的envoy filter chain中，使其生效。

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



至此，wasm filter部署完成，另一种wasm filter的使用形式是镜像，参考[制作wasm filter镜像](https://docs.solo.io/web-assembly-hub/latest/tutorial_code/getting_started/)，利用WASME工具部署，参考[使用wasme部署wasm filter](https://docs.solo.io/web-assembly-hub/latest/tutorial_code/deploy_tutorials/deploying_with_istio/)。

可以看出，wasm filter的部署还是比较繁琐的，尤其是需要大规模部署的时候，没有工具将难以进行批量部署和管理，TCM提供了便捷的部署工具，可以利用工具将二进制或者镜像形式的wasm filter批量部署到业务中，请见下一篇[使用TCM工具批量部署wasm filter](./批量部署wasm filter)。

