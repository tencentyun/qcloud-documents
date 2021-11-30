## 操作场景

当您的 Java 业务容器化至 Kubernetes 后，可通过本文了解如何使用 Skywalking Agent 上报调用链到 TSW 来观测 Java 应用。这种方式的好处在于不需要修改原来的基础镜像，也不用重新构建新的服务镜像，而是以 sidecar 模式，通过共享 volume 的方式将 agent 所需的相关文件挂载到已经存在的服务镜像中。

## 操作步骤

### 编写 Java 应用

用户使用待部署的 Java 应用。本文例子使用 Spring boot 编写Java应用，具体代码省略，可参考GitHub 上 [tsw-demo](https://github.com/tencentyun/tsw-demo) 中 spring-boot-hello 模块。

### 打包镜像

1. 准备 dockerfile 文件，本文以  spring-boot-hello 为例。
   ```dockerfile
   FROM centos:7
   RUN echo "ip_resolve=4" >> /etc/yum.conf
   RUN yum update -y && yum install -y java-1.8.0-openjdk
   # 设置时区。
   RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
   RUN echo "Asia/Shanghai" > /etc/timezone
   ENV workdir /app/
   # 下面的 jar 包可替换为您的应用 jar包，注意这个 jar 包要和您的 dockerfile 位于同一级目录
   ENV jar spring-boot-hello-1.0.jar
   COPY target/${jar} ${workdir}
   WORKDIR ${workdir}
   # JAVA_OPTS 环境变量的值为部署组的 JVM 启动参数，在运行时 bash 替换。使用 exec 以使 Java 程序可以接收 SIGTERM 信号。
   CMD ["sh", "-ec", "exec java ${JAVA_OPTS} -jar ${jar}"]
   ```

2. 将 dockerfile 和 jar 包置于同一目录，执行以下命令，编译镜像。
   ```shell
   docker build -t tsw_demo/tsw_demo_hello:v1.0 . 
   ```

3. 将镜像按照 TKE 镜像仓库指引推送到仓库，本文示例如下：
   ```
   sudo docker login --username=[uin] ccr.ccs.tencentyun.com
   sudo docker tag [ImageId] ccr.ccs.tencentyun.com/tsw_demo/tsw_demo_hello:[tag]
   sudo docker push ccr.ccs.tencentyun.com/tsw_demo/tsw_demo_hello:[tag]
   ```


### 部署应用

部署应用至 Kubernetes 时，需修改以下几项:

1. 增加 Skywalking Agent 的 initContainers，以 sidecar 模式挂载 agent。**qcloud-tsw/tsw-dist-of-apache-skywalking** 镜像已发布到TKE公共镜像，镜像版本前三位对应 Skywalking 的版本，如示例中 v8.3.0.1 对应 Skywalking 的 v8.3.0 版本。

2. **JAVA_OPTS** 环境变量添加 agent 启动目录。

3. 添加 Skywalking Agent 配置的环境变量，取值可以从 [TSW 接入指引页面](https://console.cloud.tencent.com/tsw/service) 获取。

   - **SW_AGENT_COLLECTOR_BACKEND_SERVICES** = {collector.backend_service} 后端上报地址
   - **SW_AGENT_AUTHENTICATION** = {agent.authentication} 数据上报鉴权凭证
   - **SW_AGENT_NAME** = {agent.service_name} 服务名

	 ![](https://main.qcloudimg.com/raw/ed15c15d1897a17e0108bf60d5412d13.png)

示例如下：
<dx-codeblock>
:::  yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-demo
  template:
    metadata:
      labels:
        app: hello-demo
    spec:
      initContainers:
      - name: sw-agent-sidecar
        image: ccr.ccs.tencentyun.com/qcloud-tsw/tsw-dist-of-apache-skywalking:v8.3.0.1
        imagePullPolicy: IfNotPresent
        command: ['sh']
        args: ['-c','mkdir -p /skywalking/agent && cp -r /usr/skywalking/agent/* /skywalking/agent']
        volumeMounts:
        - mountPath: /skywalking/agent
          name: sw-agent
      containers:
      - name: hello-demo
        image: ccr.ccs.tencentyun.com/tsw_demo/tsw_demo_hello:v1.0
        volumeMounts:
        - mountPath: /usr/skywalking/agent
          name: sw-agent
        env:
        - name: JAVA_OPTS
          value: "-javaagent:/usr/skywalking/agent/skywalking-agent.jar"
        - name: SW_AGENT_COLLECTOR_BACKEND_SERVICES
          value: "ap-guangzhou.tencentservicewatcher.com:11800"
        - name: SW_AGENT_NAME
          value: "tke-hello-demo"
        - name: SW_AGENT_AUTHENTICATION
          value: "tsw_site@example"
      volumes:
      - name: sw-agent
        emptyDir: {}
        
------
apiVersion: v1
kind: Service
metadata:
  name: hello-demo
  labels:
    app: hello-demo
spec:
  type: ClusterIP
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: hello-demo
:::
</dx-codeblock>


### 验证

多次访问 Java 应用后，可以在 [TSW 分布式依赖拓扑](https://console.cloud.tencent.com/tsw/topology)、[调用链查询](https://console.cloud.tencent.com/tsw/trace) 等页面确认数据是否上报，若没有数据，可在 Skywalking Agent 路径查看日志查找原因，本文示例挂载目录是`/usr/skywalking/agent`。
>?初次上报，数据存在1分钟左右延迟，请稍加等待。若等待时长较长，请通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 与我们取得联系。

```
curl {ip:port}/echo/123
```
分布式依赖拓扑：
![](https://main.qcloudimg.com/raw/909241c1d7283fe2b8917d47dd2f5cff.png)

调用链查询：
![](https://main.qcloudimg.com/raw/f363d444fa744a7e82c440476d000664.png)


