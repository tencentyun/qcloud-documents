
## 详细描述

CPU 使用率高如何优化

## 原因分析

一般都是由加密算法造成的，在低端芯片上更为明显。
云存和P2P视频传输默认都开启加密功能，云存和 P2P 视频传输目前采用的加密算法分别为 AES-CBC-128 和 AES-CTR-128。
下面给出部分加密算法在不同平台的跑分测试结果
![](https://qcloudimg.tencent-cloud.cn/raw/1481dbff81f8e119d7ee26c3594eb270.png)
可以看到 AES-CBC-256 在 Hi3516E 系列的 CPU 上加密性能约为9600KB/s（AES-CBC-128 性能略高于 AES-CBC-256），假设云存视频的码率为 2mbps，即每秒的数据量大约为 256KB，计算可得CPU使用率约为3%，实际使用过程中受其他业务影响CPU使用率可能高于估算值。
P2P 视频传输采用的 AES-CTR-128 性能和 AES-CBC-128 性能相近，假设有多个用户同时向设备端拉流观看，CPU 的使用率会成倍增长，给设备端带来较大压力。
SDK 使用的 mbedtls 版本为2.16.9，用户可以自行下载对应版本并编译进行跑分测试，方法如下：
设置环境变量并编译
export CC="XXXXX"
export CFLAGS="-std=c99"
make
./programs/test/benchmark即为性能测试程序，在设备上运行该程序查看跑分结果并估算 CPU 使用率

## 解决方法

- 用户自行适配 mbedtls 的硬件加速相关接口，并替换SDK内默认的 mbdetls 库
- 关闭加密功能（不推荐）
