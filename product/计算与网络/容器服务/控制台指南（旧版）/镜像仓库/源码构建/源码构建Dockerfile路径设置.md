# 源码构建功能 Dockerfile 路径与构建目录问题指南

腾讯云容器服务提供了镜像自动构建能力，在源码构建配置中，可以指定 Dockerfile 路径与构建目录。

## 源码构建功能 Dockerfile 路径与构建目录该怎么填 ?

![][pic1]

答案: **填写以项目为根路径的相对路径**

如果没有填写，系统有默认值：

* Dockerfile 路径默认值： 代码仓库根目录下的 Dockerfile (`Dockerfile`)
* 构建目录默认值： 代码仓库根目录 (`./`)

## 源码构建功能使用 Dockerfile 路径和构建目录细节?

源码构建功能首先 clone 用户指定的仓库，切换到相应的分支(branch)或标签(tag)，然后在代码仓库根目录执行 `docker build -f $DOCKERFILE_PATH $WORKDIR` 构建出容器镜像。

## Dockerfile文件中的源路径应该怎么写 ?

对于 `COPY`，`ADD` 等涉及源路径的命令，源路径应该写成相对于构建目录的相对路径。

[pic1]:https://mc.qcloudimg.com/static/img/33d587e49512bbee6ebc19d2f1961f94/pic1.png
