## 简介
本文提供了 GooseFS 集成 [MinIO](http://www.minio.org.cn/overview.shtml) 的步骤。由于 GooseFS、MinIO 和 COS 三者均支持 AWS S3 协议，因此 GooseFS 可以很方便地与 MinIO 集成，下面将详细介绍操作步骤。

## 前提条件

1. 安装 [golang1.17](https://go.dev/doc/install) 以上。
2. 确保 make 命令可用。
3. 安装 Java 8。
4. 安装 [SSH](https://www.ssh.com/ssh/)，确保能通过 SSH 连接到 LocalHost，并远程登录。
5. 安装 [Git](https://git-scm.com/downloads)。
6. COS 服务上创建一个存储桶用于远端存储，操作指引请参见 [控制台快速入门](https://cloud.tencent.com/document/product/436/38484)。

## 操作步骤

### 打通 MinIO 和 COS

如果在官网直接下载 MinIO 二进制包，并按照文档连接 COS，会发现非法 URI 的报错。这里的原因是 MinIO 会随机生成一个 BucketName，它不符合 COS 的 BucketName 规则（结尾是数字），因此 COS 无法正常响应。为了解决这个问题，有以下两个方法解决。

<dx-tabs>
::: 方法一：通过代理修改 minio 请求 path
本方法核心思想是通过代理修改 minio 请求 path，具体方法如下：

####  编译 MinIO Server
1. 从官方代码仓库拉取代码。
```
git clone https://github.com/minio/minio.git
```
2. 进入到 minio 所在目录，编译代码。
```
cd minio
make
```
编译成功后中 minio 目录下会出现 minio 可执行文件。

#### 启动 MinIO

1. 创建 proxy.py 文件，内容如下：
```python
import mitmproxy.http
from mitmproxy import flowfilter


class Interceptor:
    def __init__(self):
        self.filter = flowfilter.parse("~u http://cos.ap-\\w+.myqcloud.com")
        self.flag = True

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            if flow.request.path[-11:] == '/?location=' and self.flag:
                flow.request.path = flow.request.path[:-11] + "-0000" + flow.request.path[-11:]
                self.flag = False

    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass


addons = [
    Interceptor()
]
```
2. 依次执行如下命令：
```bash
# 安装依赖，如果没有pip3则先安装
pip3 install mitmproxy
# 启动COS适配插件
mitmweb --listen-port 8888 -s proxy.py --no-web-open-browser -q & echo $! > cmd.pid
# 启用HTTP代理
export http_proxy=http://127.0.0.1:8888
# 配置参数
export MINIO_ROOT_USER={AccessId}
export MINIO_ROOT_PASSWORD={SecretKey}
# 启动MINIO Sever，ap-guangzhou需要替换为实际的region。
minio gateway s3 http://cos.ap-guangzhou.myqcloud.com
```
这里的 ap-guangzhou 需要替换成正确的 Endpoint。
启动成功后如图所示，至此，MinIO 已经可以正常地操作 COS。      
![](https://qcloudimg.tencent-cloud.cn/raw/a8ad6f3a890ab745b0a375faf1246c59.png)
3. 记录如下三个值，用于配置 GooseFS。
 - API 对应 Endpoint。
 - RootUser 对应 SecretId。
 - RootPass 对应 SecretKey。
:::
::: 方法二：修改 MinIO 生成 BucketName 的逻辑
此方法的思路是修改 MinIO 生成 BucketName 的逻辑，使其生成符合规则的名称。

1. 从官方代码仓库拉取代码。
```
git clone https://github.com/minio/minio.git
```
2. 进入到 minio 所在目录，找到相应代码并修改。
```
cd minio
vim cmd/gateway/s3/gateway-s3.go
```
需要修改的函数是 randString，如下图所示。
修改部分已高亮显示，即在139行末尾添加了+"-000000"。
![](https://qcloudimg.tencent-cloud.cn/raw/03fd405bed2e6cc922f0ed75b2bf8eb5.png)
3. 修改完成后，确认保存。
4. 编译 MinIO。
```
make
```
编译成功后 minio 目录下会出现 minio 可执行文件。
4. 设置环境变量，使得 MinIO 可以操作 COS。
```
export MINIO_ROOT_USER=SecretId
export MINIO_ROOT_PASSWORD=SecrectKey
```
可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretId 和 SecretKey。
5. 启动 MinIO
```
./minio gateway s3 http://cos.ap-guangzhou.myqcloud.com
```
:::
</dx-tabs>


### 配置 GooseFS

1. 从官方仓库下载 GooseFS 安装包到本地。
官方仓库下载链接：[goosefs-1.2.0-bin.tar.gz](https://cos-data-lake-release-1253960454.cos.ap-guangzhou.myqcloud.com/goosefs/1.2.0/release/goosefs-1.2.0-bin.tar.gz)。
2. 下载对应版本的S3插件**goosefs-underfs-s3a-1.2.0.jar**，将其放在 ${GOOSEFS_HOME}/lib目录下。
3. 执行如下命令，对安装包进行解压。
```
tar -zxvf goosefs-1.2.0-bin.tar.gz
cd goosefs-1.2.0
```
解压后，得到 goosefs-1.2.0，即 GooseFS 的主目录。下文将以 ${GOOSEFS_HOME} 表示该目录的绝对路径。
4. 在 ${GOOSEFS_HOME}/conf 的目录下，创建 goosefs-site.properties 配置文件。内容如下：
```
goosefs.master.mount.table.root.ufs=s3://{BucketName}/{DirectoryName}
goosefs.underfs.s3.endpoint={Endpoint}
goosefs.underfs.s3.disable.dns.buckets=true
goosefs.underfs.s3.inherit.acl=false
aws.accessKeyId={SecretId}
aws.secretKey={SecretKey}
```
5. 启用 GooseFS 前，执行如下命令，检查系统环境，确保 GooseFS 可以在本地环境中正确运行。
```
./bin/goosefs validateEnv local
```
6. 执行如下命令，对 GooseFS 进行格式化。该命令将清除 GooseFS 的日志和 worker 存储目录下的内容。
```
./bin/goosefs format
```
7. 启动 GooseFS。
```
./bin/goosefs-start.sh local
```
该命令执行完毕后，可以访问 `http://localhost:9201` 和 `http://localhost:9204`，分别查看 Master 和 Worker 的运行状态，并且可以检查参数是否生效。如下图所示：  
![](https://qcloudimg.tencent-cloud.cn/raw/5203d442c2fb1573e7b27295a5cd28e6.png)
启动成功后，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/13cde13c592cdd2bac17db9dce1de033.png)
        
### 测试

我们通过`goosefs fs`命令对其进行简单的读写测试。

1. 查看当前根目录下有以下三个文件：
![](https://qcloudimg.tencent-cloud.cn/raw/4dcc8ca6daa8d9ef1b287d46bda350a3.png)
在 MinIO 中查看：
![](https://qcloudimg.tencent-cloud.cn/raw/cc5c2ede929605f81992057ffdc9473b.png)
通过 COS 控制台查看：
![](https://qcloudimg.tencent-cloud.cn/raw/9b7c5c59906ada5ea638804d4fa0b2bd.png)
可以看到它们是一致的。
2. 测试通过 goosefs fs 命令上传一个文件，并分别在 goosefs fs、MinIO 和 COS 控制台中验证结果。
![](https://qcloudimg.tencent-cloud.cn/raw/9883bac9c451269234e2f9d2e2ce3c0e.png)
如上图所示，首先创建了一个名为 test123 的文件，内容是 hello world。
3. 通过 goosefs 将其上传，并利用 ls 和 cat 命令验证。
在 MinIO 和 COS 控制台中可以看到这个文件，可以证明它们已经连通。
 - COS 控制台
![](https://qcloudimg.tencent-cloud.cn/raw/4a225f90ca5e6e219767239e35ec1f9b.png)
 - MinIO 控制台
![](https://qcloudimg.tencent-cloud.cn/raw/2a5668c2553cbc45abe46535c7c8a663.png)
