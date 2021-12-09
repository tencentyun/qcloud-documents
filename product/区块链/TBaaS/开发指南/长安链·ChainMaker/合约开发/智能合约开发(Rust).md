## 使用 Rust 进行智能合约开发

读者对象：本章节主要描述使用 Rust 进行 ChainMaker 合约编写的方法，主要面向于使用 Rust 进行 ChainMaker 的合约开发的开发者。

Rust 安装及教程请参考: [Rust 官网](https://www.rust-lang.org/)

### 使用 Docker 镜像进行合约开发

ChainMaker 官方已经将容器发布至 [docker hub](https://hub.docker.com/u/chainmakerofficial)

1. 首先拉取镜像
```
docker pull chainmakerofficial/chainmaker-rust-contract:1.2.0
```
请指定你本机的工作目录 $WORK_DIR，例如 /data/workspace/contract，挂载到 docker 容器中以方便后续进行必要的一些文件拷贝
```
docker run -it --name chainmaker-rust-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-rust-contract:1.2.0 bash
# 或者先后台启动
docker run -d  --name chainmaker-rust-contract -v $WORK_DIR:/home chainmakerofficial/chainmaker-rust-contract:1.2.0 bash -c "while true; do echo hello world; sleep 5;done"
# 再进入容器
docker exec -it chainmaker-rust-contract /bin/sh
```

2. 编译合约
```
cd /home/
tar xvf /data/contract_rust_template.tar.gz
cd contract_rust
wasm-pack build
```
生成的合约字节码文件位于：
```
/home/contract_rust/target/wasm32-unknown-unknown/release/chainmaker_contract.wasm
```
`chainmaker_contract.wasm` 文件可在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。

3. 合约开发框架描述
解压缩 contract_rust_template.tar.gz 后，文件描述如下：
```
chainmaker-contract-sdk-rust$ tree -I target
.
├── Cargo.lock # 依赖版本信息
├── Cargo.toml # 项目配置及依赖，参考：https://rustwasm.github.io/wasm-pack/book/cargo-toml-configuration.html
├── Makefile   # build一个wasm文件
├── README.md  # 编译环境说明
├── src
│   ├── contract_fact.rs			# 存证示例代码
│   ├── easycodec.rs                # 序列化工具类
│   ├── lib.rs                      # 程序入口
│   ├── sim_context.rs              # 合约SDK主要接口及实现
│   ├── sim_context_bulletproofs.rs # 合约SDK基于bulletproofs的范围证明接口实现
│   ├── sim_context_paillier.rs     # 合约SDK基于paillier的半同态运算接口实现
│   ├── sim_context_rs.rs           # 合约SDK sql接口实现
│   └── vec_box.rs                  # 内存管理类
```
用户使用 Rust 编写智能合约后，可以把源代码更新到 `src/contract_fact.rs` 文件中并重新编译，得到新的智能合约的字节码，并前往 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上传并部署。更多关于使用 Rust 进行开发长安链智能合约的详情，可参考长安链官网 [使用 Rust 进行智能合约开发](https://docs.chainmaker.org.cn/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#rust)
