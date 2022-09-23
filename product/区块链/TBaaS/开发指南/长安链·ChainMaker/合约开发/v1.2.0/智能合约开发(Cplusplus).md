
本章节主要描述使用 C++ 进行 ChainMaker 合约编写的方法，主要面向于使用 C++ 进行 ChainMaker 的合约开发的开发者。

## 使用 Docker 镜像进行合约开发

ChainMaker 官方已经将容器发布至 [docker hub](https://hub.docker.com/u/chainmakerofficial)。

1. 拉取镜像
```
docker pull chainmakerofficial/chainmaker-cpp-contract:1.2.0
```
请指定您本机的工作目录 $WORK_DIR，例如 /data/workspace/contract，挂载到 docker 容器中以方便后续进行必要的一些文件拷贝。
```
docker run -it --name chainmaker-cpp-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-cpp-contract:1.2.0 bash
# 或者先后台启动
docker run -d --name chainmaker-cpp-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-cpp-contract:1.2.0 bash -c "while true; do echo hello world; sleep 5;done"
# 再进入容器
docker exec -it chainmaker-cpp-contract /bin/sh
```

2. 编译合约
```
cd /home/
tar xvf /data/contract_cpp_template.tar.gz
cd contract_cpp
make clean
emmake make
```
生成的合约字节码文件位置如下：
```
/home/contract_cpp/main.wasm
```
`main.wasm` 文件可在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。

3. 合约开发框架描述
解压缩 contract_cpp_template.tar.gz 后，文件描述如下：
	- **chainmaker**
		- **basic_iterator.cc**：迭代器实现
		- **basic_iterator.h**：迭代器头文件声明
		- **chainmaker.h**：sdk 主要接口头文件声明，详情见 SDK API 描述
		- **context_impl.cc**：与链交互接口实现
		- **context_impl.h**：与链交互头文件声明
		- **contract.cc**：合约基础工具类
		- **error.h**：异常处理类
		- **exports.js**：编译合约导出函数
		- **safemath.h**：assert 异常处理
		- **syscall.cc**：与链交互入口
		- **syscall.h**：与链交互头文件声明
	- **pb**
		- **contract.pb.cc**：与链交互数据协议
		- **contract.pb.h**：与链交互数据协议头文件声明
	- **main.cc**：用户写合约入口
	- **Makefile**：常用 build 命令

用户使用 C++ 编写智能合约后，可以把源代码更新到 `main.cc` 文件中并重新编译，可得到新的智能合约的压缩文件，并前往 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。更多关于使用 C++ 开发长安链智能合约的详情，可参考长安链官网 [使用 C++ 进行智能合约开发](https://docs.chainmaker.org.cn/v1.2.0/html/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#c)。
