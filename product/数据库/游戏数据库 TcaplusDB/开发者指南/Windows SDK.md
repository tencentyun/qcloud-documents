
## 操作场景
本文档为 Tcaplus Protobuf API Windows(x64) 用户手册。
## 运行环境

操作系统 - Microsoft Windows x86\_64
编译环境 - Microsoft Visual Studio 2015 (VC14.0)

## 操作步骤
### 下载软件包

1. 下载依赖包和 Tcaplus Protobuf API 软件包： [SDK 下载]()。
2. 解压缩，以下是软件包的结构。
```
Tcaplus_PbAPI_3.32.0.171987_Win64Vc14MT_Release_20180413
|-- cfg                                                 # 配置目录
|-- docs                                                # 文档目录
|   `-- tcaplus
|-- include                                             # 依赖头文件目录
|   `-- tcaplus_pb_api
|-- lib                                                 # 库目录
|    |-- Debug
|    `-- Release
|-- examples                                            # 示例目录
   `-- tcaplus
       |-- C++_common_for_pb2                           # 示例公共头文件目录
       |-- C++_pb2_asyncmode_simpletable                # 异步模式的pb简单表示例
       |-- C++_pb2_coroutine_simpletable                # 协程模式的pb简单表示例
```



### 准备

1. 请确保已经在 [腾讯云 TcaplusDB](https://cloud.tencent.com/product/tcaplus) 开通了游戏业务并且已经获取到对应的 App 信息（例如 AppId，ZoneId，AppKey）。
2. 解压缩 `TSF4G_BASE-2.7.28.164975_Win64Vc14Mt_Release.zip` 并安装。
  * 假设安装的根路径是 `D:\Tencent\tsf4gMT`, 相关文件将会被安装到 `D:\Tencent\tsf4gMT\win64vc14MT`路径下
3. 编译并安装`Porotbuf-3.5.1`。
  * 源码地址 https://github.com/google/protobuf/releases/
  * 编译安装指南 https://github.com/google/protobuf/tree/master/cmake
  * 假设安装路径为 `D:\protobuf-3.5.1`
4. 编译并安装`OpenSSL-1.1.0f`。
  * 源代码地址 https://www.openssl.org/source/
  * 编译安装指南 https://wiki.openssl.org/index.php/Compilation_and_Installation
  * 假设安装路径为 `D:\openssl-1.1.0f`
5. 设置环境变量。。
  * `TSF4G_HOME="D:\Tencent\tsf4gMT"`
  * `PROTOBUF_HOME="D:\protobuf-3.5.1"`
  * `OPENSSL_HOME="D:\openssl-1.1.0f"`

### 构建

1. 解压缩 Tcaplus Pb API 安装包。
2. 在 `examples/tcaplus/C++_common_for_pb2/common.h` 文件中设置 App 信息。
  * Tcapdir 接入点地址列表 - `DIR_URL_ARRAY`
  * Tcapdir 接入点地址个数 - `DIR_URL_COUNT`
  * 用户表名，使用之前用户需要预先使用示例目录中的 table_test.xml 文件创建表 - `TABLE_NAME`
  * 用户业务ID - `APP_ID`
  * 用户业务区服ID - `ZONE_ID`
  * 用户业务密码 - `SIGNATURE`

  ```C
  //examples/tcaplus/C++_common_for_pb2/common.h

  /******************用户自定义****************************/
  // Tcapdir 接入点地址列表
  static const char DIR_URL_ARRAY[][TCAPLUS_MAX_STRING_LENGTH] =
  {
  	"tcp://10.125.32.21:9999"
  };
  // Tcapdir 接入点地址个数
  static const int32_t DIR_URL_COUNT = 1;
  // 用户表名
  static const char * TABLE_NAME = "tb_online";
  // 用户业务ID
  static const int32_t APP_ID = 4;
  // 用户业务区服ID
  static const int32_t ZONE_ID = 1;
  // 用户业务密码
  static const char * SIGNATURE = "8e24269ba91f433ca7e89b1cbb77368e";
  /******************用户自定义******************************/
  ```

3. 以 `examples\tcaplus\C++_pb2_coroutine_simpletable\SingleOperation\set`为例。
```
set/
|-- main.cpp                              # 示例主函数代码
|-- readme.txt
|-- table_test.proto                        # T表定义proto文件,表需要预先创建
|-- pb_co_set.sln                           # 项目VisualSudio解决方案文件
|-- pb_co_set.vcxproj                       # 项目VisualSudio工程文件
|-- proto_generate.cmd                      # 编译proto文件脚本
`-- tlogconf.xml
```
  * 首先，确认已经使用`table_test.proto`在目标 App 中创建表成功。
  * 执行`proto_generate.cmd`脚本，在当前路径下生成依赖文件。
    * `table_test.pb.cc`
    * `table_test.pb.h`
  * 在Microsoft Visual Studio 2015中打开项目文件`pb_co_set.sln`。
  * 生成解决方案。
  * 如果没有错误产生，在`examples\tcaplus\C++_pb2_coroutine_simpletable\SingleOperation\set/x64`路径下将会生成可执行文件`pb_co_set.exe`。


### 测试

1. 拷贝 `pb_co_set.exe`, `tlogconf.xml` 两个文件到同一目录下。
2. 切换`administrator`身份并使用 cmd.exe 或 powershell.exe 运行可执行文件`pb_co_set.exe`。
3. 检查输出。
4. 如果需要了解运行详细信息，请查看日志文件`tcaplus_pb.log`。
5. 如果需要运行`*_crypto`示例, 请确保`libcrypto-1_1-x64.dll`文件在系统Path路径下,这个文件能够在 openssl 的编译目录下找到。

  ![Output](https://main.qcloudimg.com/raw/40627a3a2dff8a4a4aeea57cda2bb8bb.png)


## Tcaplus Pb API 命令列表

Tcaplus Pb API 支持多种类型操作，支持异步和协程模式，用户可以在示例中找到对应的用法。以下是 Tcaplus Pb API 命令列表：

|命令                          | 描述  |
| ------------------------------- | ------------ |
|SET           |通过指定一条记录所有主键设置一条记录。如果记录存在执行覆盖操作，否则执行插入操作。 |
|GET          |从一个 Tcaplus pb 表中通过指定一条记录所有主键查询一条记录，如果数据记录不存在，将会返回错误。|
|ADD           |通过指定一条记录所有主键插入一条记录。如果记录存在返回错误。|
|DELETE         |通过指定一条记录的所有主键删除此记录，如果数据不存在则返回错误。|
|BATCHGET              |从一个 Tcaplus pb 表中通过指定多组主键查询多条记录。|
|TRAVERSE           |遍历一个 Tcaplus pb 表，将返回多条记录。|
|FIELDGET        |从一个 Tcaplus pb 表中通过指定一条记录所有主键查询一条记录。本操作只查询和传输用户指定的字段的值，减少网络传输流量。如果数据记录不存在，将会返回错误。|
|FIELDSET   |通过指定一条记录的所有主键修改指定字段，只传输指定字段的值。减轻网络流量。如果数据记录存在，将执行更新操作，否则将会返回错误。|
|FIELDINC      |通过指定一条记录的所有主键对指定的字段进行自增操作，此命令字仅支持 int32，int64，uint32 和 uint64 类型字段。特性与 FIELDSET 类似。|
|GETBYPARTKEY  |通过指定部分主键，查询符合条件的多条数据，主键集合必须在建表的时候创建了索引，否则会返回错误。|










