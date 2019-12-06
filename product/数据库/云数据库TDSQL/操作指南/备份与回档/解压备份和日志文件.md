出于压缩性能和压缩比的综合考虑，MariaDB 的备份文件和日志文件（binlog 文件）采用 LZ4（Extremely Fast Compression algorithm）工具进行压缩，您可以选用 LZ4 工具进行解压。由于常见的解压工具不支持该格式，本文特别给出解压工具和操作指引。


## Windows
### 下载工具
[工具下载地址](https://wiki-jjb-1254408587.cos.ap-chengdu.myqcloud.com/lz4_win64_v1_9_2.zip)

### 安装工具
双击 zip 文档，解压后得到 LZ4installv1.4.exe ，双击运行，按指引完成安装。
如果只是解压我们的文件，最后一步的复选框可以忽略。

### 解压文件
右键单击需要解压的 lz4 文件，选择 **Decode with LZ4** 项即可完成解压。

## Linux
### 安装工具
腾讯云云服务器的 yum 库中有 LZ4 组件，登录云服务器执行如下命令即可安装。
`$ yum install lz4`
直接执行 **lz4** 返回类似如下图所示，表示安装正确。
![](https://main.qcloudimg.com/raw/820a98757f5a5ccb84180f2289c88ddf.png)

### 解压文件
执行如下命令即可完成解压。
`$ lz4 -d xxx.lz4`
