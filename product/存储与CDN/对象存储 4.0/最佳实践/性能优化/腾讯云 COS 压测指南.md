## COSBench 简介

COSBench 是一款由 Intel 开源的，用于对象存储的压测工具。腾讯云 COS 作为兼容 S3 协议的对象存储系统，可使用该工具进行读写性能压测。


## 系统环境

工具需运行在 CentOS 7.0 及其以上版本。


## 影响性能的因素

- **机器核心数**：机器核心数较少，开启的 worker 数目较多，容易在上下文切换上产生大量的开销，建议采用32或64核进行压测。
- **机器网卡**：机器流出的流量受网卡限制，大文件的流量压力测试，建议采用万兆以上的网卡。
- **请求网络链路**：外网链路质量不一，同时外网下载会产生外网下行流量费用，建议同地域使用内网访问。
- **测试时间**：性能测试时，建议测试时间适当延长，获取一个较为稳定的数值。
- **测试环境**：程序运行的 JDK 版本，同样也会影响性能。例如测试 HTTPS，低版本客户端的加密算法存在 [GCM BUG](https://bugs.openjdk.java.net/browse/JDK-8201633)，随机数发生器可能存在锁等问题。


## 测试结果

下面以所属地域为北京地域、32核、内网17Gbps 带宽的 CVM 为例，按照以下 COSBench 配置和方法，进行上传和下载性能测试：
1. prepare 阶段：100个 worker 线程，PUT 上传1000个50MB对象。
2. main 阶段：100个 worker 线程混合读写对象，运行300秒。
 - HTTP 测试的结果如下：
   ![](https://main.qcloudimg.com/raw/f1172a0b4fee2344cb1bebbcee8bf75c.png)
 - HTTPS 测试的结果如下：
   ![](https://main.qcloudimg.com/raw/9cbe05dfd23d69048abb5199bc515979.png)


## COSBench 实践步骤

1. 从 [github](https://github.com/intel-cloud/cosbench/releases) 网站下载 cosbench 0.4.2.c4 压缩包，并在服务器上进行解压。
2. 执行命令`yum install nmap-ncat java curl java-1.8.0-openjdk-devel -y`安装 COSBench 的依赖库。
3. 编辑 s3-config-sample.xml 文件并添加任务配置信息，任务配置主要包含如下五个阶段：
 1.   init 阶段：创建存储桶。
 1.   prepare 阶段：worker 线程，PUT 上传指定大小的对象，用于 main 阶段读取。
 1.   main 阶段：worker 线程混合读写对象，运行指定时长。
 1.   cleanup 阶段，删除生成的对象。
 1.   dispose 阶段：删除存储桶。

示例配置如下：
```shell
<?xml version="1.0" encoding="UTF-8" ?>
<workload name="s3-50M-sample" description="sample benchmark for s3">

  <storage type="s3" config="accesskey=AKIDHZRLB9Ibhdp7Y7gyQq6BOk1997xxxxxx;secretkey=YaWIuQmCSZ5ZMniUM6hiaLxHnxxxxxx;endpoint=http://cos.ap-beijing.myqcloud.com" />

  <workflow>

    <workstage name="init">
      <work type="init" workers="10" config="cprefix=s3testqwer;csuffix=-1251668577;containers=r(1,10)" />
    </workstage>

    <workstage name="prepare">
      <work type="prepare" workers="100" config="cprefix=s3testqwer;csuffix=-1251668577;containers=r(1,10);objects=r(1,1000);sizes=c(50)MB" />
    </workstage>

    <workstage name="main">
      <work name="main" workers="100" runtime="300">
        <operation type="read" ratio="50" config="cprefix=s3testqwer;csuffix=-1251668577;containers=u(1,10);objects=u(1,1000)" />
        <operation type="write" ratio="50" config="cprefix=s3testqwer;csuffix=-1251668577;containers=u(1,10);objects=u(1000,2000);sizes=c(50)MB" />
      </work>
    </workstage>

    <workstage name="cleanup">
      <work type="cleanup" workers="10" config="cprefix=s3testqwer;csuffix=-1251668577;containers=r(1,10);objects=r(1,2000)" />
    </workstage>

    <workstage name="dispose">
      <work type="dispose" workers="10" config="cprefix=s3testqwer;csuffix=-1251668577;containers=r(1,10)" />
    </workstage>

  </workflow>

</workload>
```
4. 编辑 cosbench-start.sh 文件，在 Java 启动行添加参数，关闭 s3 的 md5 校验功能：
```
-Dcom.amazonaws.services.s3.disableGetObjectMD5Validation=true
```
5. 执行以下命令提交任务。
```
sh cli.sh submit conf/s3-config-sample.xml
```
并通过该网址`http://ip:19088/controller/index.html`查看执行状态：
![](https://main.qcloudimg.com/raw/77f1631fa15141332d123fb472bab7ac.png)
此时可以看到五个执行阶段，如下图所示：
![](https://main.qcloudimg.com/raw/3ccb5a60253ceb20c6da9292582c4355.png)
测试结果如下：
![](https://main.qcloudimg.com/raw/cbbb6199d89d1749424b7e3ba89be96d.png)
6. 执行以下命令，停止测试服务。
```
sh stop-all.sh
```
