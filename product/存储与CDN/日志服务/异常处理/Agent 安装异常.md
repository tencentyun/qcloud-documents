> 如何安装使用日志服务 Loglistener，详情请参阅 [ LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414) 文档，并了解 [ Loglistener 机制](https://cloud.tencent.com/document/product/614/17415)。

## 可能原因

以下原因可能会导致无法正确安装 Loglistener：
1. 内核版本仅支持64位。
2. 安装方式出错。
3. 最新特性功能依赖较高版本 Loglistener。


## 处理步骤

1. 确认内核版本。
Loglistener 安装目录下的 bin 目录中的可执行文件只支持 Linux 64位内核，执行命令 **uname -a**， 确认内核版本是否为 x86_64。
2. 确认安装执行命令。
Tools 目录中的脚本文件为 bash 脚本，不支持 `sh install.sh` 的执行方式，推荐使用 `./install.sh` 或 `bash install.sh` 的方式，请务必按照 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414) 文档进行操作。
3. 确认 Loglistener 版本。
日志服务最新特性可能依赖新版 Loglistener，若确认是使用新特性异常，请下载 [Loglistener 最新版本](https://main.qcloudimg.com/raw/8656fcadd12ab9689674df09b510b52b/loglistener.2.2.2.tar.gz)。
4. 验证 Loglistener 成功安装。
请查看确认 LogListener 进程是否正常运行，进入安装目录查看命令如下：
```shell
cd loglistener/tools && ./p.sh
```
正常情况下，输出如下：
 ![](https://main.qcloudimg.com/raw/e256cf61689ead123251a8f9f3a753c9.png)
进入安装目录执行如下命令，验证配置项是否配置正确、网络状况是否良好。
```shell
cd loglistener/bin && ./check
```
正常情况下，输出如下：
 ![](https://main.qcloudimg.com/raw/e7e85f139feb14b1aaa3353b2bafd5e1.png)
 以上命令执行无误后，即可表明 Loglistener 被成功安装。
