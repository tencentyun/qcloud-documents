#漏洞公告 | Apache Log4j2 远程代码执行漏洞公告

****
##漏洞描述
近日，腾讯云关注到Apache Log4j2远程代码执行漏洞被公开，Log4j2中存在JNDI注入漏洞，当程序将用户输入的数据进行日志记录时，既可触发此漏洞，利用此漏洞可以在目标服务器上执行任意代码。具体漏洞信息请参见 https://s.tencent.com/research/report/144

##漏洞影响
在弹性MapReduce服务中 flink、hive、ranger、 presto、 oozie 、knox 、 storm 、druid 等组件有受此漏洞影响。

## 解决方案

替换log4j2的包为安全版本
受影响版本：Apache log4j2 2.0 ~ 2.15.0-rc1
安全版本：Apache log4j-2.17.0正式版


## 修复命令

1. 标准EMR目录修复命令

	wget https://image-repo-gz-1259353343.cos.ap-guangzhou.myqcloud.com/user-patches/common/fix-log4j2.sh -O fix-log4j2.sh && bash -x fix-log4j2.sh /usr/local/service

2. 运行任务时缓存目录中jar修复

1) 确保提交的任务里面没有问题jar，否则下次提交的任务还会缓存。

2) 直接删除目录下的问题jar	。

	/data/emr/yarn/local/filecache/
	/data/emr/yarn/local/usercache/
	/data1/emr/yarn/local/filecache/
	/data1/emr/yarn/local/usercache/
	/data2/emr/yarn/local/filecache/
	/data2/emr/yarn/local/usercache/
上述只列出了3块数据盘的情况，其中/data后面跟的数字为数据盘索引，需要把全部数据盘的/data目录下对应文件进行清理。

3. 非标准目录(非/usr/local/service目录)修复，执行命令

	EXTRA_DISRUPTOR_DIR=/path/to/other bash fix-log4j2.sh /path/to/other

4. 其他场景修复
升级该漏洞相关的6个jar包：log4j-api,log4j-core,log4j-jul,log4j-slf4j-impl,log4j-web，disruptor。如果没有上面的某个包，则无需替换。

## 重启服务与灰度修复
1. 对集群的某台机器执行修复，重启这个节点上的服务
flink、spark、hive、ranger 、 presto 、oozie、storm、impala、knox、druid
重启各个常驻任务，flink任务，storm任务，spark任务。

2. 此节点重启服务验证没问题后，再执行其他节点的修复。

## 修复原理
1. 将修复后的6个jar放在执行目录的fix-log4j目录下。
2. 查找待修复目录，修复6个jar包，发现则替换，未发现不会替换，会同时替换tar.gz以及war包中的对应问题jar，以及hdfs上/user/hadoop/share路径下的缓存包
替换其中的 log4j-api,log4j-core,log4j-jul,log4j-slf4j-impl,log4j-web 2.0～2.17.0为2.17.0版本
替换其中的 disruptor-3.4.2.jar以下的版本为3.4.2版本，注意disruptor仅对了部分组件替换。



## 服务有问题回滚步骤
需要将问题jar包拷贝回去，并删除添加的最新jar包。

1. 解压备份文件

	cd fix-log4j2
	tar zxvf rm_if_no_need_to_rollback.tar.gz.1639576622 

其中1639576622为临时生成的时间戳，需找到对应文件进行解压。

2. 将备份文件拷贝回去

	cp -r ./root/fix-log4j2/emr_fix_log4j_bak_10812_1639576622/usr/local/service/* /usr/local/service/

其中10812_1639576622 为执行时临时生成的数字，需找到对应文件进行复制。

3. 删除添加的log4j系列最新jar包

	find /usr/local/service/ -name log4j-api-2.17.0.jar | xargs -n1 -I{} rm -f {}
	find /usr/local/service/ -name log4j-web-2.17.0.jar | xargs -n1 -I{} rm -f {}
	find /usr/local/service/ -name log4j-jul-2.17.0.jar | xargs -n1 -I{} rm -f {}
	find /usr/local/service/ -name log4j-slf4j-impl-2.17.0.jar | xargs -n1 -I{} rm -f {}
	find /usr/local/service/ -name log4j-core-2.17.0.jar | xargs -n1 -I{} rm -f {}

4. 如果是其他目录/path/to/other的回滚，则将/usr/local/service/替换为/path/to/other

