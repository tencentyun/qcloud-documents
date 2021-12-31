


代码示例：[Go](https://github.com/TencentCloudBase/cloudbase-examples/tree/master/cloudbaserun/go)

可单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-examples&workDir=cloudbaserun%2Fgo&appName=go-hello-world" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div>



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
    port := "8080"
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
此代码会创建一个基本的 Web 服务器，侦听 `8080` 端口。
</dx-alert>



## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
# 使用官方 Golang 镜像作为构建环境
FROM golang:1.15-buster as builder

WORKDIR /app

# 安装依赖
COPY go.* ./
RUN go mod download

# 将代码文件写入镜像
COPY . ./

# 构建二进制文件
RUN go build -mod=readonly -v -o server

# 使用裁剪后的官方 Debian 镜像作为基础镜像
# https://hub.docker.com/_/debian
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM debian:buster-slim
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 将构建好的二进制文件拷贝进镜像
COPY --from=builder /app/server /app/server

# 启动 Web 服务
CMD ["/app/server"]
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


## 步骤4：部署到 CloudBase 云托管

详情请参见  [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。


