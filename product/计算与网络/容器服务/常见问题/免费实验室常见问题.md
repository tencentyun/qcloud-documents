### 通过示例集群创建自定义应用报错

#### (-241007)示例集群不支持的参数 PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster service namespace must be u*********]

**说明**： 示例集群通过 namespaces 进行用户隔离，创建自定义应用必须在您的 namespaces下创建，您可以通过错误码返回，或从Namespace列表页面获取您的 namespaces。
**解决方法**： 修改 Namespace 为您的 namespaces 即可。

#### (-241007)示例集群不支持的参数 PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster pod's cpu limits cannot be zero]

**说明**： 示例集群下创建的资源必须设置实例的 CPU 和内存 Request 和 Limit 限制。
**解决方法**：在模板内容的 containers 字段下的 resources 字段补充完整 request 和 limit 的限制，如下：
```yaml
......
containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: ng
        resources:
          requests:
            requests:
            cpu: 200m
            memory: 128M
          limits:
            cpu: 200m
            memory: 128M
        securityContext:    
          privileged: false
......
```
