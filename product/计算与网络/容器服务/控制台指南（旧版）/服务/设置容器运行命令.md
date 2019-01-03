## 概述
创建服务时，我们通常都是通过镜像来指定实例中容器所运行的进程。在默认的情况下，镜像会运行默认的命令，如果我们想运行一个特定的命令或重写镜像的默认值，这里需要使用到以下三个设置：

- 工作目录（ workingDir）：指定当前的工作目录。
- 运行命令（ command ）：控制镜像运行的实际命令。
- 命令参数（ args ）：传递给运行命令的参数。

## 工作目录说明
指定当前的工作目录，若不存在则自动创建，如果没有指定，则使用容器运行时的默认值。若镜像里面如果没指定 workdir，且在控制台未指定，workdir 默认为 " / "。

## 容器如何执行命令和参数
如何将 docker run 命令适配到腾讯云容器服务，单击查看 [详情](/doc/product/457/9883)。
 
Docker 的镜像拥有存储镜像信息的相关元数据，如果不提供运行命令和参数，容器运行会运行镜像制作时提供的默认的命令和参数，Docker 原生定义这两个字段为 “ Entrypoint ” 和 " CMD "。详情可查看 Docker 的 [Entrypoint 说明](https://docs.docker.com/engine/reference/builder/#/entrypoint)，[CMD 说明](https://docs.docker.com/engine/reference/builder/#/cmd)。
如果在创建服务时填写了容器的运行命令和参数，将会覆盖镜像构建时的默认命令 " Entrypoint "、" CMD "，规则如下：

| 镜像 Entrypoint |镜像 CMD|容器的运行命令|容器的运行参数| 最终执行|
| :-------- | :--------| :------ | :-------- | :------ |
| [ls]   | [/home]|  未设置  |未设置    |[ls / home]  |
| [ls]   | [/home]|  [cd]  |未设置    |	[cd]        |
| [ls]   | [/home]|  未设置  |[/data] |[ls / data]  |
| [ls]   | [/home]|  [cd]  |[/data] |[cd / data]  |

>**注意:**
>Docker entrypoint 对应容器服务控制台上的运行命令，Docker run 的 CMD 参数对应容器服务控制台上的运行参数，当有多个运行参数时，在容器服务的运行参数中输入参数，每个参数单独一行。
