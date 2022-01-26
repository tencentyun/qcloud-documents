## 漏洞描述
-----
近日，腾讯云关注到 Apache Log4j2远程代码执行漏洞被公开，Log4j2中存在 JNDI 注入漏洞，当程序将用户输入的数据进行日志记录时，既可触发此漏洞，利用此漏洞可以在目标服务器上执行任意代码。具体漏洞信息请参见 [Apache Log4j2远程代码执行漏洞风险紧急告警](https://s.tencent.com/research/report/144)。

## 漏洞影响
-----
在弹性 MapReduce 服务中 flink、hive、ranger、 presto、 oozie 、knox 、 storm 、druid 等组件有受此漏洞影响。请受影响的用户可参照以下方案进行修复。

## 解决方案
-----

替换 log4j2的包为安全版本
受影响版本：Apache log4j2 2.0 ~ 2.15.0-rc1
安全版本：Apache log4j-2.17.1正式版

## 修复命令
-----
1. 标准 EMR 目录修复命令
<table>
<thead>
<tr>
<th>wget https://image-repo-gz-1259353343.cos.ap-guangzhou.myqcloud.com/user-patches/common/fix-log4j2.sh -O fix-log4j2.sh && bash -x fix-log4j2.sh /usr/local/service
</th>
</tr>
</thead>
</table >

2. 运行任务时缓存目录中 jar 修复
1) 确保提交的任务里面没有问题 jar，否则下次提交的任务还会缓存。
2) 直接删除目录下的问题 jar。
<table>
<thead>
<tr>
<th>/data/emr/yarn/local/filecache/<br>
   /data/emr/yarn/local/usercache/<br>
   /data1/emr/yarn/local/filecache/<br>
   /data1/emr/yarn/local/usercache/<br>
   /data2/emr/yarn/local/filecache/<br>
   /data2/emr/yarn/local/usercache/</th>
</tr>
</thead>
</table >
上述只列出了3块数据盘的情况，其中/data 后面跟的数字为数据盘索引，需要把全部数据盘的/data 目录下对应文件进行清理。

3. 非标准目录(非/usr/local/service 目录)修复，执行命令
 <table>
<thead>
<tr>
<th>EXTRA_DISRUPTOR_DIR=/path/to/other bash fix-log4j2.sh /path/to/other</th>
</tr>
</thead>
</table >

4. 其他场景修复
升级该漏洞相关的6个 jar 包：log4j-api,log4j-core,log4j-jul,log4j-slf4j-impl,log4j-web，disruptor。如果没有上面的某个包，则无需替换。

## 重启服务与灰度修复

-----
1. 对集群的某台机器执行修复。
- 重启这个节点上的服务 flink、spark、hive、ranger 、 presto 、oozie、storm、impala、knox、druid。
- 重启各个常驻任务，flink任务，storm任务，spark任务。

2. 此节点重启服务验证没问题后，再执行其他节点的修复。

## 修复原理

-----
1. 将修复后的6个 jar 放在执行目录的 fix-log4j 目录下。 
2. 查找待修复目录，修复6个 jar 包，发现则替换，未发现不会替换，会同时替换 tar.gz 以及 war 包中的对应问题 jar，以及 hdfs 上/user/hadoop/share 路径下的缓存包。
- 替换其中的 log4j-api,log4j-core,log4j-jul,log4j-slf4j-impl,log4j-web 2.0～2.17.1为2.17.1版本。
- 替换其中的 disruptor-3.4.2.jar 以下的版本为3.4.2版本，注意 disruptor 仅对部分组件替换。

## 服务有问题回滚步骤
-----
需要将问题 jar 包拷贝回去，并删除添加的最新 jar 包。
1. 解压备份文件。
<table>
<thead>
<tr>
<th>cd fix-log4j2<br>tar zxvf rm_if_no_need_to_rollback.tar.gz.1639576622
</th>
</tr>
</thead>
</table >
其中1639576622为临时生成的时间戳，需找到对应文件进行解压。

2. 将备份文件拷贝回去。
<table>
<thead>
<tr>
<th> cp -r ./root/fix-log4j2/emr_fix_log4j_bak_10812_1639576622/usr/local/service/* /usr/local/service/</th>
</tr>
</thead>
</table >
其中10812_1639576622 为执行时临时生成的数字，需找到对应文件进行复制。

3. 删除添加的 log4j 系列最新 jar 包。
<table>
<thead>
<tr>
<th> find /usr/local/service/ -name log4j-api-2.17.1.jar | xargs -n1 -I{} rm -f {}<br>
  find /usr/local/service/ -name log4j-web-2.17.1.jar | xargs -n1 -I{} rm -f {}<br>
      find /usr/local/service/ -name log4j-jul-2.17.1.jar | xargs -n1 -I{} rm -f {}<br>
 find /usr/local/service/ -name log4j-slf4j-impl-2.17.1.jar | xargs -n1 -I{} rm -f {}<br>
   find /usr/local/service/ -name log4j-core-2.17.1.jar | xargs -n1 -I{} rm -f {}</th>
</tr>
</thead>
</table >

4. 如果是其他目录/path/to/other 的回滚，则将/usr/local/service/替换为/path/to/other。

