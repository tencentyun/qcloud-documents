## COSBench 简介

COSBench 是一款由 Intel 开源，用于对象存储的压测工具。腾讯云 COS 作为兼容 S3 协议的对象存储系统，可使用该工具进行读写性能压测。


## 系统环境

工具推荐运行在 CentOS 7.0 及其以上版本，ubuntu 环境可能存在预期外的问题。


## 影响性能的因素

- **机器核心数**：机器核心数较少，开启的 worker 数目较多，容易在上下文切换上产生大量的开销，建议采用32或64核进行压测。
- **机器网卡**：机器流出的流量受网卡限制，大文件的流量压力测试，建议采用万兆以上的网卡。
- **请求网络链路**：外网链路质量不一，同时外网下载会产生外网下行流量费用，建议同地域使用内网访问。
- **测试时间**：性能测试时，建议测试时间适当延长，获取一个较为稳定的数值。
- **测试环境**：程序运行的 JDK 版本，同样也会影响性能。例如测试 HTTPS，低版本客户端的加密算法存在 [GCM BUG](https://bugs.openjdk.java.net/browse/JDK-8201633)，随机数发生器可能存在锁等问题。




## COSBench 实践步骤

1. 从 [COSBench GitHub](https://github.com/intel-cloud/cosbench/releases) 网站下载 COSBench 0.4.2.c4.zip 压缩包，并在服务器上进行解压。
2. 安装 COSBench 的依赖库，执行如下命令。
 - 对于 centos 系统，执行如下命令安装依赖：
```
sudo yum install nmap-ncat java curl java-1.8.0-openjdk-devel -y
```
 - 对于 ubuntu 系统，执行如下命令安装依赖
```
sudo apt install nmap openjdk-8-jdk 
```
3. 编辑 s3-config-sample.xml 文件并添加任务配置信息，任务配置主要包含如下五个阶段：
   1. init 阶段：创建存储桶。
   2. prepare 阶段：worker 线程，PUT 上传指定大小的对象，用于 main 阶段读取。
   3. main 阶段：worker 线程混合读写对象，运行指定时长。
   4. cleanup 阶段，删除生成的对象。
   5. dispose 阶段：删除存储桶。

示例配置如下：

```shell
<?xml version="1.0" encoding="UTF-8" ?>
<workload name="s3-50M-sample" description="sample benchmark for s3">

  <storage type="s3" config="accesskey=AKIDHZRLB9Ibhdp7Y7gyQq6BOk1997xxxxxx;secretkey=YaWIuQmCSZ5ZMniUM6hiaLxHnxxxxxx;endpoint=http://cos.ap-beijing.myqcloud.com" />

  <workflow>

    <workstage name="init">
      <work type="init" workers="10" config="cprefix=examplebucket;csuffix=-1250000000;containers=r(1,10)" />
    </workstage>

    <workstage name="prepare">
      <work type="prepare" workers="100" config="cprefix=examplebucket;csuffix=-1250000000;containers=r(1,10);objects=r(1,1000);sizes=c(50)MB" />
    </workstage>

    <workstage name="main">
      <work name="main" workers="100" runtime="300">
        <operation type="read" ratio="50" config="cprefix=examplebucket;csuffix=-1250000000;containers=u(1,10);objects=u(1,1000)" />
        <operation type="write" ratio="50" config="cprefix=examplebucket;csuffix=-1250000000;containers=u(1,10);objects=u(1000,2000);sizes=c(50)MB" />
      </work>
    </workstage>

    <workstage name="cleanup">
      <work type="cleanup" workers="10" config="cprefix=examplebucket;csuffix=-1250000000;containers=r(1,10);objects=r(1,2000)" />
    </workstage>

    <workstage name="dispose">
      <work type="dispose" workers="10" config="cprefix=examplebucket;csuffix=-1250000000;containers=r(1,10)" />
    </workstage>

  </workflow>

</workload>
```

**参数说明**

| 参数                 | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| accesskey、secretkey | 密钥信息，分别替换为用户的 SecretId  和 SecretKey            |
| cprefix              | 存储桶名称前缀，例如 examplebucket                           |
| containers           | 为存储桶名称数值区间，最后的存储桶名称由 cprefix 和 containers 组成，例如：examplebucket1，examplebucket2 |
| csuffix              | 用户的 APPID，需注意 APPID 前面带上符号`-`，例如 -1250000000 |
| runtime              | 压测运行时间                                                 |
| ratio                | 读和写的比例                                                 |
| workers              | 压测线程数                                                   |

4. 编辑 cosbench-start.sh 文件，在 Java 启动行添加如下参数，关闭 s3 的 md5 校验功能：
```plaintext
-Dcom.amazonaws.services.s3.disableGetObjectMD5Validation=true
```
5. 启动 cosbench 服务。
 - 对于 centos 系统，执行以下命令：
```plaintext
sudo bash start-all.sh
```
 - 对于 ubuntu 系统，执行以下命令：
```plaintext
sudo bash start-driver.sh &
sudo bash start-controller.sh &
```
6. 执行以下命令提交任务。
```plaintext
sudo bash cli.sh submit conf/s3-config-sample.xml
```
并通过该网址`http://ip:19088/controller/index.html`（ip 替换为用户的压测机器 IP）查看执行状态：
![](https://main.qcloudimg.com/raw/77f1631fa15141332d123fb472bab7ac.png)
此时可以看到五个执行阶段，如下图所示：
![](https://main.qcloudimg.com/raw/3ccb5a60253ceb20c6da9292582c4355.png)
7. 下面展示的是所属地域为北京地域、32核、内网带宽为17Gbps的 CVM 进行上传和下载性能测试，包括以下2个阶段：
    1. prepare 阶段：100个 worker 线程，上传1000个50MB对象。
    2. main 阶段：100个 worker 线程混合读写对象，运行300秒。

经过以上阶段1和阶段2的性能压测，结果如下：
![](https://main.qcloudimg.com/raw/e3ac34b6f8340c5cbc834d4f98ba9341.png)

8. 执行以下命令，停止测试服务。
```plaintext
sudo bash stop-all.sh
```
