## 使用Go(TinyGo)进行智能合约开发

读者对象：本章节主要描述使用Go进行ChainMaker合约编写的方法，主要面向于使用Go进行ChainMaker的合约开发的开发者。为了最小化wasm文件尺寸，使用的是TinyGO编译器。

### 使用Docker镜像进行合约开发

ChainMaker官方已经将容器发布至 [docker hub](https://hub.docker.com/u/chainmakerofficial)

1. 首先拉取镜像

```
docker pull chainmakerofficial/chainmaker-go-contract:1.2.0
```

请指定你本机的工作目录$WORK_DIR，例如/data/workspace/contract，挂载到docker容器中以方便后续进行必要的一些文件拷贝

```
docker run -it --name chainmaker-go-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-go-contract:1.2.0 bash
# 或者先后台启动
docker run -d  --name chainmaker-go-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-go-contract:1.2.0 bash -c "while true; do echo hello world; sleep 5;done"
# 再进入容器
docker exec -it chainmaker-go-contract /bin/sh
```

2. 编译合约
```
cd /home/
# 解压缩合约SDK源码
tar xvf /data/contract_go_template.tar.gz
cd contract_tinygo
# 编译main.go合约
sh build.sh
```
生成合约的字节码文件在
```
/home/contract_tinygo/main.wasm
```

`main.wasm`文件可在[TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)上传并部署

3. 合约开发框架描述
解压缩contract_go_template.tar.gz后，文件描述如下：
```
/home/contract_tinygo# ls -l
total 64
-rw-rw-r-- 1 1000 1000    56 Jul  2 12:45 build.sh            	# 编译脚本
-rw-rw-r-- 1 1000 1000  4149 Jul  2 12:44 bulletproofs.go		# 合约SDK基于bulletproofs的范围证明接口实现
-rw-rw-r-- 1 1000 1000 18871 Jul  2 12:44 chainmaker.go			# 合约SDK主要接口及实现
-rw-rw-r-- 1 1000 1000  4221 Jul  2 12:44 chainmaker_rs.go		# 合约SDK sql接口实现
-rw-rw-r-- 1 1000 1000 11777 May 24 13:27 easycodec.go			# 序列化工具类
-rw-rw-r-- 1 1000 1000  3585 Jul  2 12:44 main.go				# 存证示例代码
-rwxr-xr-x 1 root root 65122 Jul  6 07:22 main.wasm				# 编译成功后的wasm文件
-rw-rw-r-- 1 1000 1000  1992 Jul  2 12:44 paillier.go 			# 合约SDK基于paillier的半同态运算接口实现
```

用户使用Go编写智能合约后，可以把源代码更新到`main.go`文件中并重新编译，可得到新的智能合约的字节码，并前往[TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)上传并部署。更多关于使用Rust进行开发长安连智能合约的详情，可参考长安连官网[使用Go(TinyGo)进行智能合约开发](https://docs.chainmaker.org.cn/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#go-tinygo)