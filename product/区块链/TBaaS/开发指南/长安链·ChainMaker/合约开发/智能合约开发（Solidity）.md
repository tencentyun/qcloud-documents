


本章节主要描述使用 Solidity 进行 ChainMaker 合约编写的方法，主要面向于使用 Solidity 进行 ChainMaker 的合约开发的开发者。

### 使用 Docker 镜像进行合约开发

ChainMaker 官方已经将容器发布至 [docker hub](https://hub.docker.com/u/chainmakerofficial)。

#### 1. 拉取镜像
代码示例如下：
```
docker pull chainmakerofficial/chainmaker-solidity-contract:1.2.0
```

请指定你本机的工作目录 $WORK_DIR，例如 /data/workspace/contract，挂载到 docker 容器中以方便后续进行必要的一些文件拷贝。

```
docker run -it --name chainmaker-solidity-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-solidity-contract bash
# 或者先后台启动
docker run -d  --name chainmaker-solidity-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-solidity-contract bash -c "while true; do echo hello world; sleep 5;done"
# 再进入容器
docker exec -it chainmaker-solidity-contract /bin/sh
```

#### 2. 编译合约
代码示例如下：

```
cd /home/
# 解压缩合约SDK源码
tar xvf /data/contract_solidity_template.tar.gz
cd contract_solidity
# 编译token.sol合约
solc --abi --bin --hashes --overwrite -o . token.sol
```

生成合约的字节码文件路径如下：

```
/home/contract_solidity/Token.bin
```

`Token.bin` 文件可在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。

#### 3. 合约开发框架描述
解压缩 contract_solidity_template.tar.gz 后，文件描述如下：

```
/home/contract_solidity# ls -l
total 4
-rw-rw-r-- 1 1000 1000 2816 Apr 29  2021 token.sol              # token合约
```

用户使用 Solidity 编写智能合约后，可以把源代码更新到 `token.sol` 文件中并重新编译，可得到新的智能合约的字节码，并前往 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。更多关于使用 Solidity 开发长安链智能合约的详情，可参考长安链官网 [使用 Solidity 进行智能合约开发](https://docs.chainmaker.org.cn/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#solidity)。
