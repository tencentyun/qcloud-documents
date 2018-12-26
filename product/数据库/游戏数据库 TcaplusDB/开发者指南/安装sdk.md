## 操作场景
本文档指导您在 Linux 系统环境下如何安装和使用 TcaplusDB Pb。
## 运行环境
Linux 2.6、Suse 32 位 / 64 位。

## 前提条件
### Protobuf 安装
在安装和使用 TcaplusDB Pb 前需安装 Protobuf，若已安装可忽略此节。
Protobuf 是 Google 推出的一种混合语言数据标准，是一种轻便的结构化数据存储格式。TcaplusDB 系统支持使用 Protobuf 格式定义文件（.proto）定义数据表。在使用 TcaplusDB Pb API 之前，需要在 GameSvr 服务器上安装 Protobuf。在此推荐使用源代码进行 Protobuf 安装，安装方法如下：
1. 准备 GameSvr 环境。
首先需要准备安装了 CentOS6- x86_64 或 CentOS7-x86_64 版本操作系统的 GameSvr。为了编译构建 Protobuf，需要安装以下软件，安装方法请自行查询：
 - autoconf
 - automake
 - libtool
 - curl (used to download gmock)
 - make
 - g++
 - unzip

2. 下载 Protobuf（syntax=”proto2”）源码安装包。
单击 [下载源码安装包](https://github.com/google/protobuf/releases/tag/v2.6.1)。
3. 解压源码安装包，并进入源码根目录下，以下为命令行操作。
```
tar -xzvf protobuf-2.6.1.tar.gz
cd ./protobuf-2.6.1
```
4. Configure 并指定安装路径前缀，推荐安装到路径 /usr/local/protobuf 下，以下为命令行操作。
```
./configure --prefix=/usr/local/protobuf
```
5. 编译并安装，以下为命令行操作。
```
make
make check
make install
```
6. 测试，使用 protoc 命令查看是否安装成功，以下为命令行操作。
```
protoc -version
```
如下图所示，安装成功。
![](https://mc.qcloudimg.com/static/img/0c9e3f1f45df121b214f07b8961c1c09/1.jpg)

## 操作步骤
### SDK 下载
单击[ SDK 下载](https://mc.qcloudimg.com/static/archive/5455997ec0076386ac96536d71f0a1ce/TcaplusPbApi3.18.0.152096.x86_64_release_20170712.tar.gz)。

### SDK 安装
``` tar –xzf<安装包路径> -C <安装目录> ```

### 校验
安装完成后，根目录结构如下表所示：

| 目录及文件 | 说明 |
|---------|---------|
| include/tcaplus_service/ | TCAPLUS 服务化 API 头文件 |
| lib/libtcaplusserviceapi.a | TCAPLUS 服务化 API 库文件 |
| include/tcaplus_service/protobuf/ | Protobuf API 头文件|
| lib/libtcaplusprotobufapi.a | TCAPLUS Protobuf API 库文件 |
| examples/tcaplus/ProtoBuf | TCAPLUS Protobuf API 应用示例 |

### 运行 example 访问 TcaplusDB
GameSvr 游戏服务器中对应数据访问逻辑的开发，可以参考 example 中的各接口实例。

1. 解压 TcaplusDB Pb API 发布包。
```
tar -xzvf TcaplusPbApi3.18.0.152096.x86_64_release_20170712.tar.gz
```
2. 配置 TcaplusDB 系统连接信息。
	1. 在命令行输入如下代码进入目录：   
```
cd TcaplusPbApi3.18.0.152096.x86_64_release_20170712/release/x86_64/examples/tcaplus/C++_common_for_pb2
```

	2. 在命令行输入 vi common.h 修改 common.h 头文件，根据业务情况修改如下图片内容。
	**DIR_URL_ARRAY：**tcapdir 地址和端口号。
	**DIR_URL_COUNT：**tcapdir 个数。
	**TABLE_NAME：**需要访问的目标表。
	**APP_ID：**需要访问的 AppId。
	**ZONE_ID：**部署单元 ZoneId。
	**SIGNATURE：**业务 AppKey。

	![](https://mc.qcloudimg.com/static/img/4eddaa926243031049ab2e019d8686ab/image.png)
3. 修改环境配置设置文件。
在 TcaplusPbApi3.18.0.152096.x86_64_release_20170712/release/x86_64/examples/tcaplus 目录下有分别通过异步方式以及协程方式调用API的例子，现在以协程方式调用 Set 接口设置数据为例：
在命令行输入如下代码进入目录：
```
cd TcaplusPbApi3.18.0.152096.x86_64_release_20170712/release/x86_64/examples/tcaplus/C++_pb2_coroutine_simpletable/SingleOperation/set
```
协程方式 Set 例子的所有代码都在该目录中。修改 envcfg.env 文件，将 PROTOBUF_HOME 环境变量设置为本机 protobuf 的安装路径（--prefix指定），并将 TCAPLUS_HOME 环境变量设置为 Tcaplus Pb API 包下 release/x86_64 目录的绝对路径，如下图：
![](https://mc.qcloudimg.com/static/img/093250c857a6c77847fd14bd037dc7e9/image.png)
4. 设置环境变量。
在代码目录下执行：
```
source envcfg.env
bash conv.sh
```
5. 编译二进制程序。
执行`make`命令编译 example 二进制，编译成功生成 mytest 可执行文件。
![](https://mc.qcloudimg.com/static/img/9b4dd73cf2d3b93721d9782a76804d7f/mytest.png)
6. 执行二进制程序。
命令行输入`./mytest` ，执行二进制程序。执行结果将在命令行标准输出中显示，若遇到错误，请查看代码目录下的 tcaplus_pb.log 日志文件。
