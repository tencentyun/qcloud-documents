
## 步骤1：编写基础应用（使用 spring boot 框架）

1. 首先我们创建一个 Spring Boot 应用。使用 curl 和 unzip 命令新建一个空 Web 项目：
<dx-codeblock>
:::  plaintext
curl https://start.spring.io/starter.zip \
    -d dependencies=web \
    -d javaVersion=1.8 \
    -d bootVersion=2.3.3.RELEASE \
    -d name=helloworld \
    -d artifactId=helloworld \
    -d baseDir=helloworld \
    -o helloworld.zip
unzip helloworld.zip
cd helloworld
:::
</dx-codeblock>
上述命令将创建一个 Spring Boot 项目。
<dx-alert infotype="explain" title="">
如需在 Windows 系统上使用上述 curl 命令，您需要以下命令行之一：
<ul style = "margin-bottom: 0px;"><li><a href = "https://docs.microsoft.com/en-us/windows/wsl/install-win10">WSL（推荐）</a></li>
<li><a href = "https://cygwin.com/install.html">cygwin</a></li></ul>
或者选择性地使用 <a href = "https://start.spring.io/#!type=maven-project&language=java&platformVersion=2.3.3.RELEASE&packaging=jar&jvmVersion=1.8&groupId=com.example&artifactId=helloworld&name=helloworld&description=&packageName=com.example.helloworld&dependencies=web">Spring Initializr（预加载配置）</a>生成项目。
</dx-alert>
2. 将 `src/main/java/com/example/helloworld/HelloworldApplication.java` 内容更新如下：
<dx-codeblock>
:::  java
package com.example.helloworld;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class HelloworldApplication {

  @RestController
  class HelloworldController {

    @GetMapping("/")
    String hello() {
      return "Hello World!";
    }
  }

  public static void main(String[] args) {
    SpringApplication.run(HelloworldApplication.class, args);
  }
}
:::
</dx-codeblock>
3. 在 `src/main/resources/application.properties` 中，将服务器端口设置成 `80`：
<dx-codeblock>
:::  URL
server.port=80
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
以上代码会创建一个基本的 Web 服务器，并监听 `80` 端口。
</dx-alert>



## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
# 选择构建用基础镜像。如需更换，请到[dockerhub官方仓库](https://hub.docker.com/_/java?tab=tags)自行选择后替换。
FROM maven:3.6.0-jdk-8-slim as build

# 指定构建过程中的工作目录
WORKDIR /app

# 将src目录下所有文件，拷贝到工作目录中src目录下（.gitignore/.dockerignore中文件除外）
COPY src /app/src

# 将pom.xml文件，拷贝到工作目录下
COPY settings.xml pom.xml /app/

# 执行代码编译命令
# 自定义settings.xml, 选用国内镜像源以提高下载速度
RUN mvn -s /app/settings.xml -f /app/pom.xml clean package

# 选择运行时基础镜像
FROM alpine:3.13

# 容器默认时区为UTC，如需使用上海时间请启用以下时区设置命令
# RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone

# 安装依赖包，如需其他依赖包，请到alpine依赖包管理(https://pkgs.alpinelinux.org/packages?name=php8*imagick*&branch=v3.13)查找。
# 选用国内镜像源以提高下载速度
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tencent.com/g' /etc/apk/repositories \
    && apk add --update --no-cache openjdk8-jre-base \
    && rm -f /var/cache/apk/*

# 指定运行时的工作目录
WORKDIR /app

# 将构建产物jar包拷贝到运行时目录中
COPY --from=build /app/target/*.jar .

# 暴露端口
# 此处端口必须与部署时填写的端口一致，否则会部署失败。
EXPOSE 80

# 执行启动命令.
# 写多行独立的CMD命令是错误写法！只有最后一行CMD命令会被执行，之前的都会被忽略，导致业务报错。
# 请参考[Docker官方文档之CMD命令](https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["java", "-jar", "/app/springboot-1.0.jar"]
:::
</dx-codeblock>
2. 添加一个 `.dockerignore` 文件，以从容器映像中排除文件：
<dx-codeblock>
:::  sh
Dockerfile
.dockerignore
target/
:::
</dx-codeblock>

## 步骤3（可选）：本地构建镜像

1. 如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：
<dx-codeblock>
:::  sh
docker build -t helloworld-java
:::
</dx-codeblock>
2. 构建成功后，运行 `docker images`，可以看到构建出的镜像，随后您可以将此镜像上传至您的镜像仓库。
<dx-codeblock>
:::  sh
REPOSITORY        TAG       IMAGE ID         CREATED            SIZE
helloworld-java   latest    c994813b495b     8 seconds ago      271MB
:::
</dx-codeblock>


## 步骤4：部署到云托管

详情请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
