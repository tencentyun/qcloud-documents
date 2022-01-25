## 操作场景

本文通过一个 demo 进行应用通过 Nginx 接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 本地编译构建打包机器环境已安装了 C/C++ 编译所需的工具（make, gcc, g++）等。
- 根据您自身的业务，已准备好业务部署的资源，`虚拟机部署`、`容器化部署`选择其中一种方式即可。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。
  - **容器化部署**已创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

1. 编译 Nginx。
 1. 下载 [nginx](http://nginx.org/en/download.html)，推荐使用稳定版本 nginx-1.20.2，下载后并解压，解压后的目录名为 nginx-1.20.2。
    - 对于 centos5.4 系统的用户：
       1. 直接获取nginx-polaris的预编译包：[nginx-polaris-1.0.0-centos5-x86_64.tar.gz](https://github.com/polarismesh/nginx-polaris/releases/download/v1.0.0/nginx-polaris-1.0.0-centos5-x86_64.tar.gz)。
       - 将预编译包放进 nginx-1.20.2 目录中，并进行解压。
    - 对于其他版本操作系统的用户：
         1. 下载 [polaris-cpp](https://github.com/polarismesh/polaris-cpp/releases) 最新版本源码，并进行解压
         - 执行 make package 编译 polaris-cpp 源码，编译后获得 polaris_cpp_sdk.tar.gz。
         - 将 polaris_cpp_sdk.tar.gz 放到 nginx-1.20.2 目录中，并进行解压，获得 polaris_cpp_sdk 目录。
         - 下载 [nginx-polaris](https://github.com/polarismesh/nginx-polaris/releases) 最新版本源码，并进行解压，获得 nginx-polaris-${version} 目录。
         - 拷贝 nginx-polaris-${version}/config 到 nginx-1.20.2/polaris_cpp_sdk 目录中。
         - 拷贝 nginx-polaris-${version}/nginx_polaris_module 和 nginx-polaris-${version}/nginx_polaris_limit_module 到 nginx-1.20.2 目录中。
 - 操作后，nginx-1.20.2 目录内容如下：
<dx-codeblock>
:::  sh
    |-- nginx-1.19.2
    |   |-- CHANGES
    |   |-- CHANGES.ru
    |   |-- LICENSE
    |   |-- Makefile
    |   |-- README
    |   |-- auto
    |   |-- build
    |   |-- build.sh
    |   |-- conf
    |   |-- configure
    |   |-- contrib
    |   |-- html
    |   |-- man
    |   |-- objs
    |   |-- polaris_client
    |   `-- src
    |-- nginx_polaris_limit_module
    |   |-- config
    |   |-- ngx_http_polaris_limit_module.cpp
    |   `-- ngx_http_polaris_limit_module.h
    |-- nginx_polaris_module
    |   |-- config
    |   |-- ngx_http_upstream_polaris_module.cpp
    |   |-- ngx_http_upstream_polaris_module.h
    |   |-- ngx_http_upstream_polaris_wrapper.cpp
    |   `-- ngx_stream_upstream_polaris_module.cpp
    `-- polaris_cpp_sdk
        |-- config
        |-- dlib
        |-- include
        `-- slib
:::
</dx-codeblock>
 - 进入 nginx-1.20.2 目录，执行以下命令进行配置以及构建：
<dx-codeblock>
:::  sh
    ./configure \
            --add-module=nginx_polaris_limit_module \
            --add-module=nginx_polaris_module \
            --add-module=polaris_cpp_sdk \
        --with-stream
    make install     
:::
</dx-codeblock>
  - 构建后，ngnix 整体会安装到 /usr/local/nginx 下面，需要将 nginx-1.20.2/polaris.yaml 配置文件拷贝到 /usr/local/nginx/sbin 下面，完成整个编译过程。
  - 修改 /usr/local/nginx/nginx.conf 文件，指定使用 polarismesh 进行反向转发。示例只展示关键修改点：
<dx-codeblock>
:::  c
    http {
      server {
         location / {
            proxy_set_header Host $host;
            proxy_pass http://host_upstream;
         }
      }
      upstream host_upstream {
          polaris service_namespace=default service_name=$host timeout=1.5;
           server 127.0.0.1:6000;
       }      
    }
:::
</dx-codeblock>
2. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
3. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
4. 单击目标引擎的“ID”，进入基本信息页面。
5. 查看访问地址，nginx-polaris 访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
6. 修改 /usr/local/nginx/sbin/polaris.yaml 中的注册中心地址。
<dx-codeblock>
:::  c
global:
    serverConnector:
    addresses:
    - 10.0.4.6:8091
:::
</dx-codeblock>
7. 注册被调端服务：
在容器环境下，用户开发完被调端的服务后，可以通过 [关联 K8s 集群](https://cloud.tencent.com/document/product/1364/65869?from=copy) 的方式，将通过容器部署的服务，自动注册到北极星上（默认会使用default命名空间进行注册），注册后如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/c41f8224309f7996713593ceb9887309.png)
<dx-alert infotype="notice" title="">
被调端服务的服务名必须为小写，才能支持被 Nginx 调用到。
</dx-alert>
8. 部署主调端应用。虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。
   1. **虚拟机部署**部署 Nginx 应用。
     - 上传 /usr/local/nginx 目录至 CVM 实例。
     - 执行启动命令进行启动：
<dx-codeblock>
:::  sh
./nginx -c /usr/local/nginx/conf/nginx.conf
:::
</dx-codeblock>
   2. **容器化部署**部署 Nginx 应用。
     - 编写 dockerfile，将 /usr/local/nginx 打入容器镜像中。
     - 通过 TKE 部署并运行镜像。
9. 确认部署结果。
    进入部署主调端应用的 CVM 或者容器中，通过 `curl -H'Host:$被调服务名'  127.0.0.1:$NGINX 监听端口/path`的方式向 Nginx 发起 HTTP 调用，能获取到被调方结果，证明部署成功。例如，被调方服务使用上面部署 echo-server 服务：
<dx-codeblock>
:::  url
curl -H'Host:echo-server' 127.0.0.1:80/echo?value=hello-polaris
:::
</dx-codeblock>
  预期返回值：`echo: hello-polaris`
