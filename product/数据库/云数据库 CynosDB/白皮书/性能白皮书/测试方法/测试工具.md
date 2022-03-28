本文为您介绍 TDSQL-C MySQL 版性能测试工具 sysbench，以及如何在云服务器 CVM 实例上安装 sysbench。

## sysbench 工具介绍
sysbench 是一个跨平台且支持多线程的模块化基准测试工具，用于评估系统在运行高负载的数据库时相关核心参数的性能表现。可绕过复杂的数据库基准设置，甚至在没有安装数据库的前提下，快速了解数据库系统的性能。

## sysbench 参数说明
| 参数 | 说明 | 
|---------|---------|
| db-driver | 数据库引擎  | 
| mysql-host | TDSQL-C MySQL 版实例连接地址  |
| mysql-port | TDSQL-C MySQL 版实例连接端口  |
| mysql-user | TDSQL-C MySQL 版实例帐号  |
| mysql-password | TDSQL-C MySQL 版实例帐号对应的密码  |
| mysql-db | 	TDSQL-C MySQL 版实例数据库名 |
| table_size| 测试表大小  |
|tables | 测试表数量 |
| events | 测试请求数量 |
| time | 测试时间 |
| threads | 测试线程数 |
| percentile | 需要统计的百分比，默认值为95%，即请求在95%的情况下的执行时间 |
| report-interval | 表示 N 秒输出一次测试进度报告，0表示关闭测试进度报告输出，仅输出最终的报告结果 |
| skip-trx | 是否跳过事务<br>1：跳过<br>0：不跳过 |

## 安装方法
本压测使用 sysbench 1.0.20 (using bundled LuaJIT 2.1.0-beta2)版本。更多信息，请参见 [sysbench 官方文档](https://github.com/akopytov/sysbench?spm=a2c4g.11186623.2.12.36061072oZL2qS)。
>!1台客户端1000个并发，超过1000并发后增加1个客户端，以此类推。

1. 在云服务器 CVM 实例执行如下命令安装 sysbench。
```
yum install gcc gcc-c++ autoconf automake make libtool bzr mysql-devel git mysql
git clone https://github.com/akopytov/sysbench.git
##从 Git 中下载 sysbench
cd sysbench
##打开 sysbench 目录
git checkout 1.0.20
##切换到 sysbench 1.0.20 版本
./autogen.sh
##运行 autogen.sh
./configure --prefix=/usr --mandir=/usr/share/man
make
##编译
make install
```
2. 执行如下命令配置客户端，使内核可以使用所有的 CPU 处理数据包，同时减少 CPU 之间的上下文切换。
```
sudo sh -c 'for x in /sys/class/net/eth0/queues/rx-*; do echo ffffffff>$x/rps_cpus; done'
sudo sh -c "echo 32768 > /proc/sys/net/core/rps_sock_flow_entries"
sudo sh -c "echo 4096 > /sys/class/net/eth0/queues/rx-0/rps_flow_cnt"
sudo sh -c "echo 4096 > /sys/class/net/eth0/queues/rx-1/rps_flow_cnt"
```
>?ffffffff 表示使用32个 CPU（1个 f 表示4个 CPU）。


