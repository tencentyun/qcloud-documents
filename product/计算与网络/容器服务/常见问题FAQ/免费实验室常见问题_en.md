## 免费实验室常见问题

### 1. 通过示例集群创建自定义应用报错
#### 1.1 (-241007)示例集群不支持的参数 PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster service namespace must be u*********]
说明： 示例集群通过namespaces进行用户隔离，创建自定义应用必须在您的namespaces下创建，你可以通过错误获取您的namespaces。
解决方法： 修改Namespace 为您的namespaces即可。

#### 1.2 (-241007)示例集群不支持的参数 PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster pod's cpu limits cannot be zero]

说明： 示例集群下创建的资源必须设置实例的CPU和内存Request和Limit限制
解决方法：在模板内容的containers字段下的resources字段补充完整request和limit的限制，如下：
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
