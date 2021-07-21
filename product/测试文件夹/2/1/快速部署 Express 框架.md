## 简介

域名重定向，是指当用户通过浏览器访问某个 URL 时，Web 服务器被设置自动跳转到另外一个 URL。

## 应用场景

- 网站支持 HTTP 和 HTTPS，例如：http://tencent.com 和 https://tencent.com 需要访问到同一个 Web 服务
- 网站更换过域名，例如：https://tengxun.com 换成 https://tencent.com，两个域名访问到同一个 Web 服务
- 网站部分内容做过调整，原始 URL 已经无法访问，可以重定向到一个新的提供服务的 URL 上

>!
> 1. 当用户使用了重定向后，会多一条下面的注解，这条注解表明Ingress 的转发规则由 TKE 管理，后期不能被删除和修改，否者会和 CLB 侧设置的重定向规则冲突。`ingress.cloud.tencent.com/rewrite-support: "true"`
> 2. 假设用字母表示域名地址。若 A 已经重定向至 B，则 A 不能再重定向至 C（除非先删除老的重定向关系，再建立新的重定向关系）；B 不能重定向至任何其它地址；A 也不能重定向到 A。


两种使用方式：
- **自动重定向说明**：用户需要先创建出一个 HTTPS:443 监听器，并在其下创建转发规则。通过调用本接口，系统会自动创建出一个 HTTP:80 监听器（如果之前不存在），并在其下创建转发规则，与 HTTPS:443 监听器下的域名等各种配置对应。
- **手动重定向说明**：用户手动配置原访问地址和重定向地址，系统自动将原访问地址的请求重定向至对应路径的目的地址。同一域名下可以配置多条路径作为重定向策略，实现 HTTP 和 HTTPS 之间请求的自动跳转。




## 操作步骤


Ingress 支持通过控制台和 YAML 两种方式进行重定向，具体步骤如下：

<dx-tabs>
::: 控制台方式
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【集群】。
2. 在“集群管理”页面，选择需修改 Ingress 的集群 ID。
3. 在集群详情页，选择左侧【服务与路由】>【Ingress】。如下图所示：
   ![](https://main.qcloudimg.com/raw/69e9c55ea644144ea5848c98b9d0462a.png)
4. 单击【新建】，在“新建 Ingress”页面中，注意“重定向”的选择：
   - **无**：不使用重定向规则。
   - **手动**：会在“转发配置”下面出现一栏“重定向转发配置”。
     - “转发配置”里面填写的方式和普通 Ingress 的转发配置一样，后端是某个服务。
     - “重定向转发配置”里面填写的方式和普通 Ingress 的转发配置一样，但后端是某个“转发配置”里的某条路径。
       ![](https://main.qcloudimg.com/raw/7f045376ed79348b2cc67e9042c23f98.png)
   - **自动**：仅对“转发配置”里的协议为“HTTPS”的路径生效，都将自动生成一个“HTTP”的路径，路径完全一样，只有协议不一样。“HTTP”的路径的转发规则自动重定向到“HTTPS”的路径。
     ![](https://main.qcloudimg.com/raw/372ed3c7e0d63f07fb54decf943cf3bd.png)
:::
::: YAML\s方式
#### 自动重定向：HTTP 重定向到 HTTPS

注意：仅对 HTTPS 协议的转发规则生效
Ingress YAML 中配置注解：`ingress.cloud.tencent.com/auto-rewrite: true`
配置该注解之后，转发路径种的所有 HTTPS 监听器中存在的七层转发规则都将被对应到 HTTP 监听器中作为重定向规则。域名与路径路径都保持一致。

#### 手动重定向

需要增加一个annotation ，修改一个annotation：

- 增加的 annotation：`ingress.cloud.tencent.com/rewrite-support: "true"`    # 表示允许重定向
- 修改的 annotation：
  ```yaml
  # 原注解 格式：
  {
   "host": "<domain>",
   "path": "<path>",
   "backend": {
     "serviceName": "<service name>",
     "servicePort": "<service port>"
   }
  }
  
	
  # 新注解格式：
  {
    "host": "<domain>",
    "path": "<path>",
    "backend": {
      "serviceName": "<service name>",
      "servicePort": "<service port>"
    },
    "rewrite": {
      "port": "<rewrite-port>",
      "host": "<rewrite-domain>",
      "path": "<rewrite-path>"
    }
  }
  ```

  ### 举例

  需求：某服务之前是通过 `121.4.25.44/path2` 进行访问，后来发布了一个新版本，想通过`121.4.25.44/v2/path2` 访问。

  - 增加一条 annotation：`ingress.cloud.tencent.com/rewrite-support: "true"`    # 允许重定向
  - 修改原 annotation：`kubernetes.io/ingress.http-rules: '[{"path":"/path1","backend":{"serviceName":"path1","servicePort":"80"}},{"path":"/path2","backend":{"serviceName":"path2","servicePort":"80"}},{"path":"/v1/path1","rewrite":{"port":80,"path":"/path1"}},{"path":"/v2/path2","rewrite":{"port":80,"path":"/path2"}}]'   # 把 /v1/path1 替换为 /path1  80端口；把 /v2/path2 替换为 /path2 80端口。注意：host可以省略`

  修改后的 YAML：

  ```yaml
  apiVersion: extensions/v1beta1
  kind: Ingress
  metadata:
    annotations:
      description: test
      ingress.cloud.tencent.com/rewrite-support: "true"
      kubernetes.io/ingress.class: qcloud
      kubernetes.io/ingress.http-rules: '[{"path":"/path1","backend":{"serviceName":"path1","servicePort":"80"}},{"path":"/path2","backend":{"serviceName":"path2","servicePort":"80"}},{"path":"/v1/path1","rewrite":{"port":80,"path":"/path1"}},{"path":"/v2/path2","rewrite":{"port":80,"path":"/path2"}}]'
      kubernetes.io/ingress.https-rules: "null"
      kubernetes.io/ingress.rule-mix: "true"
    name: test
    namespace: default
  spec:
    rules:
    - http:
        paths:
        - backend:
            serviceName: path1
            servicePort: 80
          path: /path1
          pathType: ImplementationSpecific
    - http:
        paths:
        - backend:
            serviceName: path2
            servicePort: 80
          path: /path2
          pathType: ImplementationSpecific
  status:
    loadBalancer:
      ingress:
      - ip: 121.4.25.44
  ```
完整 Ingress Annotation 说明请[参考](https://cloud.tencent.com/document/product/457/56112)
:::
</dx-tabs>




