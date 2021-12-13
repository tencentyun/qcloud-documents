## 功能介绍

Golang Get 可以借助代码管理工具通过远程拉取或更新代码包及其依赖包，并自动完成编译和安装，使得整个过程就像安装应用程式一样简单。目前 CODING 代码仓库已支持在多仓库中使用 **go get** 功能，以下是快速上手指南。

## 快速开始

假如用户拥有 A 仓库，其代码仓库的 Git HTTPS 地址是：`https://e.coding.net/{team}/{project}/{repo}.git`（花括号中是变量，以实际情况为准），以该仓库 `https://e.coding.net/baulk/jackson/mux.git` 为例：

用户可以通过以下命令设置好模块名。

```shell
go mod init e.coding.net/baulk/jackson/mux
```

如果要通过 go get 获得模块，可以运行如下命令：

```shell
go get e.coding.net/baulk/jackson/mux
```

另外多仓库也支持获取子仓库的模块：

```shell
go get e.coding.net/baulk/jackson/mux/dev
```

有一些存储库的 Git HTTPS 克隆地址是: `https://e.coding.net/{team}/{project}.git`，用户可以通过如下命令设置好模块名：

```shell
go mod init e.coding.net/team/project
```

如果要通过 go get 获得模块，可以运行如下命令：

```shell
go get e.coding.net/team/project
```

>!此类存储库不完全支持直接获取子模块，您应该使用 `e.coding.net/team/project/project` 作为模块名、获得模块及其子模块。
