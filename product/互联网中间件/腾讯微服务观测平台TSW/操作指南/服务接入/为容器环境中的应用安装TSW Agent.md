## 操作场景

本文档主要引导通过容器部署应用的用户，使用 TSW Agent。

用户以容器方式部署应用时，如果想要通过 TSW 的 Agent 采集调用链数据，需要以下 Dockerfile 将应用、Agent 一起打包成镜像。

## 操作步骤
1. 下载 zip 包（[下载地址](https://tsw-agent-1300555551.cos.ap-guangzhou.myqcloud.com/tsw-client-package.zip)）。
>!您需要将应用程序 JAR 包和 tsw-client-package.zip 放在同级目录下，并在该目录下编写 Dockerfile。

2. 编写 Dockerfile。
<dx-codeblock>
::: shayuyan
FROM centos:7
RUN yum update -y &amp;&amp; yum install -y java-1.8.0-openjdk
# 设置时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
ENV workdir /app/

# 下面的 jar 包需要替换为您的 jar 包，注意这个 jar 包要和您的 dockerfile 位于同一级目录
ENV jar test-registry-0.0.1-SNAPSHOT.jar

# Agent 运行必要参数，服务名需要替换为具体服务（应用）名，在 TSW 的同一环境/地域（命名空间）中，将以 servicename 隔离服务数据
# servicename 需要与 jar 包主体名称保持一致。此外，您在控制台接入服务时输入的服务名需要与 servicename 保持一致
 ENV servicename test-registry


# Agent 运行必要参数：数据上报 IP、端口（port），如果没有特殊情况 IP、port 不变
ENV etlip 169.254.0.143
ENV etlport 9550

# 需要替换成自己的token
ENV token tsw_site@xxxxxxxx
COPY ${jar} ${workdir}
WORKDIR ${workdir}

# 下载工具
RUN yum update &amp;&amp; yum -y install unzip
ADD tsw-client-package.zip ${workdir}

# 解压替换变量
RUN cd ${workdir} &amp;&amp; unzip tsw-client-package.zip &amp;&amp; \
    rm tsw-client-package.zip &amp;&amp; cd tsw-client-package &amp;&amp; \
    chmod +x bin/setup.sh; bin/setup.sh ${servicename} ${etlip} ${etlport} ${token}
CMD ["sh", "-ec", "exec java -javaagent:${workdir}tsw-client-package/tsw-agent.jar  -jar ${jar}"]
:::
</dx-codeblock>

3. 将应用 jar 包、tsw-client-package.zip、Dockerfile 放在统一路径。
4.  同级目录执行 `docker build . -t 镜像名称` 构建镜像。
