腾讯云提供的块存储设备根据类型的不同拥有不同的性能和价格，具体内容可以参考[云硬盘的分类](/doc/product/362/2353)，需要注意的是，由于不同应用程序的工作负载不同，若未提供足够的 I/O 请求来充分利用云硬盘时，可能无法达到云硬盘的最大性能。

云硬盘的性能如何衡量？一般使用以下几个指标对存储设备的性能进行描述：

- IOPS：每秒读/写次数，单位为次（计数）。存储设备的底层驱动类型决定了不同的 IOPS。
- 吞吐量：每秒的读写数据量，单位为MB/s。
- 时延：IO操作的发送时间到接收确认所经过的时间，单位为秒。


FIO是测试磁盘性能的一个非常好的工具，用来对硬件进行压力测试和验证。建议使用libaio的I/O引擎进行测试，请用户自行安装FIO和Libaio。

不同场景的测试公式基本一致，只有3个参数（读写模式，iodepth，blocksize）的区别。下面举例说明使用block size为4k，iodepth为1来测试顺序读性能的命令。

命令如下：

```
fio --bs=4k --ioengine=libaio --iodepth=1 --direct=1 --rw=read --time_based --runtime=600  --refill_buffers --norandommap --randrepeat=0 --group_reporting --name=fio-read --size=100G --filename=/dev/sdb
```
每个工作负载适合的最佳iodepth不同，具体取决于您的特定应用程序对于 IOPS 和延迟的敏感程度。



参数说明：
![](//mccdn.qcloud.com/static/img/44b8577054f94a8920d57f23945b3289/image.jpg)

常见用例如下：
- block=4k iodepth=1 随机读测试，能反映磁盘的时延性能；
- block=128K iodepth=32 能反映峰值吞吐性能 ; 
- block=4k iodepth=32 能反映峰值IOPS性能。

下图为SSD云硬盘的测试性能截图：
![](//mccdn.qcloud.com/static/img/1609e6314d25fe8c60d2b41fb680d93a/image.png)
![](//mccdn.qcloud.com/static/img/ead7220181d8491752899b195e8bc15c/image.png)
![](//mccdn.qcloud.com/static/img/9a9621f1eaec3f630fbad75f8d3820ee/image.png)