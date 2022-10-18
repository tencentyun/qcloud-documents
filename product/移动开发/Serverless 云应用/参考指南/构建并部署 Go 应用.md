
## 步骤1：编写基础应用

1. 创建名为 `helloworld` 的新目录，并转到此目录中：
<dx-codeblock>
:::  sh
mkdir helloworld
cd helloworld
:::
</dx-codeblock>
2. 创建一个包含以下内容的 `go.mod` 文件：
<dx-codeblock>
:::  go
module helloworld
go 1.13
:::
</dx-codeblock>
3. 在同一目录中，创建一个 `main.go` 文件，并将以下代码行复制到其中：
<dx-codeblock>
:::  go
package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", handler)
    port := "80"
    if err := http.ListenAndServe(":"+port, nil); err != nil {
        log.Fatal(err)
    }
}

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello World!\n")
}
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
此代码会创建一个基本的 Web 服务器，侦听 `80` 端口。
</dx-alert>



## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
# 选择构建用基础镜像（选择原则：在包含所有用到的依赖前提下尽可能体积小）。如需更换，请到[dockerhub官方仓库](https://hub.docker.com/_/golang?tab=tags)自行选择后替换。
FROM golang:1.17.1-alpine3.14 as builder

# 指定构建过程中的工作目录
WORKDIR /app

# 将当前目录（dockerfile所在目录）下所有文件都拷贝到工作目录下（.dockerignore中文件除外）
COPY . /app/

# 执行代码编译命令。操作系统参数为linux，编译后的二进制产物命名为main，并存放在当前目录下。
RUN GOOS=linux go build -o main .

# 选用运行时所用基础镜像（GO语言选择原则：尽量体积小、包含基础linux内容的基础镜像）
FROM alpine:3.13

# 容器默认时区为UTC，如需使用上海时间请启用以下时区设置命令
# RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone

# 指定运行时的工作目录
WORKDIR /app

# 将构建产物/app/main拷贝到运行时的工作目录中
COPY --from=builder /app/main /app/index.html /app/

# 执行启动命令
# 写多行独立的CMD命令是错误写法！只有最后一行CMD命令会被执行，之前的都会被忽略，导致业务报错。
# 请参考[Docker官方文档之CMD命令](https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["/app/main"]
:::
</dx-codeblock>
2. 添加一个 `.dockerignore` 文件，以从容器映像中排除文件：
<dx-codeblock>
:::  go
vendor/
.dockerignore
.gcloudignore
.gitignore
:::
</dx-codeblock>

## 步骤3（可选）：本地构建镜像

1. 如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：
<dx-codeblock>
:::  sh
docker build -t helloworld .
:::
</dx-codeblock>
2. 构建成功后，运行 `docker images`，可以看到构建出的镜像，随后您可以将此镜像上传至您的镜像仓库。
<dx-codeblock>
:::  sh
REPOSITORY     TAG       IMAGE ID         CREATED          SIZE
helloworld   latest    6948f1ebee94     8 seconds ago      82.7MB
:::
</dx-codeblock>


## 步骤4：部署到云托管

详情请参见  [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。



