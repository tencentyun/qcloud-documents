代码示例：[Java](https://github.com/TencentCloudBase/cloudbase-examples/tree/master/cloudbaserun/java)

可单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-examples&workDir=cloudbaserun%2Fjava&appName=java-hello-world" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div>


## 第 1 步：编写基础应用

首先我们创建一个 Spring Boot 应用。

使用 curl 和 unzip 命令新建一个空 Web 项目：

```plaintext
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
```

上述命令将创建一个 Spring Boot 项目。

>? 
> 如需在 Windows 系统上使用上述 curl 命令，您需要以下命令行之一：
> 
> - [WSL（推荐）](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
> - [cygwin](https://cygwin.com/install.html)
> 
> 或者选择性地使用 [Spring Initializr（预加载配置）](https://start.spring.io/#!type=maven-project&language=java&platformVersion=2.3.3.RELEASE&packaging=jar&jvmVersion=1.8&groupId=com.example&artifactId=helloworld&name=helloworld&description=&packageName=com.example.helloworld&dependencies=web) 生成项目：
> 

将 `src/main/java/com/example/helloworld/HelloworldApplication.java` 内容更新如下：

```java
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

```

在 `src/main/resources/application.properties` 中，将服务器端口设置成 `8080`：

```
server.port=8080
```

以上代码会创建一个基本的 Web 服务器，并监听 `8080` 端口。

## 第 2 步：将应用容器化

在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：

```docker
# 使用官方 maven/Java 8 镜像作为构建环境
# https://hub.docker.com/_/maven
FROM maven:3.6-jdk-11 as builder

# 将代码复制到容器内
WORKDIR /app
COPY pom.xml .
COPY src ./src

# 构建项目
RUN mvn package -DskipTests

# 使用 AdoptOpenJDK 作为基础镜像
# https://hub.docker.com/r/adoptopenjdk/openjdk8
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM adoptopenjdk/openjdk11:alpine-slim

# 将 jar 放入容器内
COPY --from=builder /app/target/helloworld-*.jar /helloworld.jar

# 启动服务
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/helloworld.jar"]
```

添加一个 `.dockerignore` 文件，以从容器映像中排除文件：

```
Dockerfile
.dockerignore
target/
```

## 第 3 步（可选）：本地构建镜像

如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：

```sh
docker build -t helloworld-java .
```

构建成功后，运行 `docker images`，可以看到构建出的镜像：

```
REPOSITORY        TAG       IMAGE ID         CREATED            SIZE
helloworld-java   latest    c994813b495b     8 seconds ago      271MB
```

随后您可以将此镜像上传至您的镜像仓库。

## 第 4 步：部署到 CloudBase 云托管

请参考 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
