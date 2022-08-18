

本章节主要描述使用 Go 进行 ChainMaker 合约编写的方法，主要面向于使用 Go 进行 ChainMaker 的合约开发的开发者。Docker-go 合约运行在独立的 Docker VM 容器中，与长安链节点程序通过 UNIX Domain Socket 或者 TCP 通信。Docker-go 合约需在 Linux 环境下进行编译。
<dx-alert infotype="notice" title="">
安装 DockerGo 合约时，合约名称必须跟编译合约时使用的合约名保持一致。
</dx-alert>


## 使用 Docker 镜像进行合约开发

ChainMaker 官方已经将容器发布至 [docker hub](https://hub.docker.com/u/chainmakerofficial)。

1. 拉取镜像
```
docker pull chainmakerofficial/chainmaker-docker-go-contract:v2.2.1
```
请指定您本机的工作目录 $WORK_DIR，例如 /data/workspace/contract，挂载到 docker 容器中以方便后续进行必要的一些文件拷贝。
```
docker run -it --name chainmaker-docker-go-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-docker-go-contract:v2.2.1 bash
```

2. 编译合约，压缩合约
```
$ cd /home
$ tar xvf /data/contract_docker_go_template.tar.gz
$ cd contract_docker_go
$ ./build.sh
please input contract name, contract name should be same as name in tx: 
<contract_name> #此处contract_name必须和交易中的合约名一致
please input zip file: 
<zip_file_name> #建议与contract_name保持一致（不包含文件后缀）
```
编译、压缩好的文件位置如下：
```
/home/contract_docker_go/<contract_name>.7z
```
`<contract_name>.7z` 文件可在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。

用户使用 Go（DockerGo） 编写智能合约后，可以把源代码更新到 `main.go` 文件中并重新编译，可得到新的智能合约的压缩文件，并前往 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。更多关于使用 Go（DockerGo） 开发长安链智能合约的详情，可参考长安链官网 [使用 Go（DockerGo）进行智能合约开发](https://docs.chainmaker.org.cn/v2.2.1/html/operation/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#docker-go)。
