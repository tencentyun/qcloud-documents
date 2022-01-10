Hadoop 工具依赖 Hadoop-2.7.2 及以上版本，实现了以腾讯云 COS 作为底层存储文件系统运行上层计算任务的功能。启动 Hadoop 集群主要有单机、伪分布式和完全分布式等三种模式，本文主要以 Hadoop-2.7.4 版本为例进行 Hadoop 完全分布式环境搭建及 wordcount 简单测试介绍。

## 准备环境
1. 准备若干台机器。
2. 安装配置系统：[CentOS-7-x86_64-DVD-1611.iso](http://isoredirect.centos.org/centos/7/isos/x86_64/)。
3. 安装 Java 环境，具体操作请参见 [Java 安装与配置](/doc/product/436/10865)。
4. 安装 Hadoop 可用包：[Apache Hadoop Releases Download](http://hadoop.apache.org/releases.html#16+April%2C+2018%3A+Release+2.7.6+available)。 

#### 网络配置
使用`ifconfig -a`查看各台机器的 IP，相互使用 ping 命令检查 ，看是否可以 ping 通，同时记录每台机器的 IP。

## 配置 CentOS
#### 配置 hosts
```
vi /etc/hosts
```
编辑内容：
```
202.xxx.xxx.xxx master
202.xxx.xxx.xxx slave1
202.xxx.xxx.xxx slave2
202.xxx.xxx.xxx slave3
//IP 地址替换为真实 IP
```
#### 关闭防火墙
```
systemctl status firewalld.service  //检查防火墙状态
systemctl stop firewalld.service  //关闭防火墙
systemctl disable firewalld.service  //禁止开机启动防火墙
```
#### 时间同步
```
yum install -y ntp  //安装 ntp 服务
ntpdate cn.pool.ntp.org  //同步网络时间
```
#### 安装配置 JDK
上传 JDK 安装包（如jdk-8u144-linux-x64.tar.gz）到`root`根目录。
```
mkdir /usr/java
tar -zxvf jdk-8u144-linux-x64.tar.gz -C /usr/java/
rm -rf jdk-8u144-linux-x64.tar.gz
```
#### 各个主机之间复制 JDK
```
scp -r /usr/java slave1:/usr
scp -r /usr/java slave2:/usr
scp -r /usr/java slave3:/usr
.......
```
#### 配置各个主机 JDK 环境变量
```
vi /etc/profile
```
编辑内容：
```
export JAVA_HOME=/usr/java/jdk1.8.0_144
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
source/etc/profile    //使配置文件生效
java -version       //查看 java 版本
```
#### 配置 SSH 无密钥访问
分别在各个主机上检查 SSH 服务状态：
```
systemctl status sshd.service  //检查 SSH 服务状态
yum install openssh-server openssh-clients  //安装 SSH 服务，如果已安装，则不用执行该步骤
systemctl start sshd.service  //启动 SSH 服务，如果已安装，则不用执行该步骤
```
分别在各个主机上生成密钥：
```
ssh-keygen -t rsa  //生成密钥
```
在 slave1 上：
```
cp ~/.ssh/id_rsa.pub ~/.ssh/slave1.id_rsa.pub
scp ~/.ssh/slave1.id_rsa.pub master:~/.ssh
```
在 slave2 上：
```
cp ~/.ssh/id_rsa.pub ~/.ssh/slave2.id_rsa.pub
scp ~/.ssh/slave2.id_rsa.pub master:~/.ssh
```
依此类推...
在 master 上：
```
cd ~/.ssh
cat id_rsa.pub >> authorized_keys
cat slave1.id_rsa.pub >>authorized_keys
cat slave2.id_rsa.pub >>authorized_keys
scp authorized_keys slave1:~/.ssh
scp authorized_keys slave2:~/.ssh
scp authorized_keys slave3:~/.ssh
```
## 安装配置 Hadoop
### 安装 Hadoop
上传 hadoop 安装包（如hadoop-2.7.4.tar.gz）到`root`根目录。
```
tar -zxvf hadoop-2.7.4.tar.gz -C /usr
rm -rf hadoop-2.7.4.tar.gz
mkdir /usr/hadoop-2.7.4/tmp
mkdir /usr/hadoop-2.7.4/logs
mkdir /usr/hadoop-2.7.4/hdf
mkdir /usr/hadoop-2.7.4/hdf/data
mkdir /usr/hadoop-2.7.4/hdf/name
```
进入`hadoop-2.7.4/etc/hadoop`目录下，进行下一步操作。
### 配置 Hadoop
#### 1. 修改`hadoop-env.sh`文件，增加如下内容：
```
export JAVA_HOME=/usr/java/jdk1.8.0_144 
```
若 SSH 端口不是默认的22，可在`hadoop-env.sh`文件里修改：
```
export HADOOP_SSH_OPTS="-p 1234"
```
#### 2. 修改 `yarn-env.sh`
```
export JAVA_HOME=/usr/java/jdk1.8.0_144
```
#### 3. 修改`slaves`
配置内容：
```
删除：
localhost
添加：
slave1
slave2
slave3
```
#### 4. 修改`core-site.xml`
```
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://master:9000</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>file:/usr/hadoop-2.7.4/tmp</value>
  </property>
</configuration>
```
#### 5. 修改`hdfs-site.xml`
```
<configuration>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/usr/hadoop-2.7.4/hdf/data</value>
    <final>true</final>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/usr/hadoop-2.7.4/hdf/name</value>
    <final>true</final>
  </property>
</configuration>
```
#### 6. 修改`mapred-site.xml`
```
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.jobhistory.address</name>
    <value>master:10020</value>
  </property>
  <property>
    <name>mapreduce.jobhistory.webapp.address</name>
    <value>master:19888</value>
  </property>
</configuration>
```
#### 7. 修改`yarn-site.xml`
```
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.mapred.ShuffleHandler</value>
  </property>
  <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>master:8032</value>
  </property>
  <property>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>master:8030</value>
  </property>
  <property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>master:8031</value>
  </property>
  <property>
    <name>yarn.resourcemanager.admin.address</name>
    <value>master:8033</value>
  </property>
  <property>
    <name>yarn.resourcemanager.webapp.address</name>
    <value>master:8088</value>
  </property>
</configuration>
```
#### 8. 各个主机之间复制 Hadoop
```
scp -r /usr/ hadoop-2.7.4 slave1:/usr
scp -r /usr/ hadoop-2.7.4 slave2:/usr
scp -r /usr/ hadoop-2.7.4 slave3:/usr
```
#### 9. 各个主机配置 Hadoop 环境变量
打开配置文件：
```
vi /etc/profile
```
编辑内容：
```
export HADOOP_HOME=/usr/hadoop-2.7.4
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
export HADOOP_LOG_DIR=/usr/hadoop-2.7.4/logs
export YARN_LOG_DIR=$HADOOP_LOG_DIR
```
使配置文件生效：
```
source /etc/profile
```
### 启动 Hadoop
#### 1. 格式化 namenode
```
cd /usr/hadoop-2.7.4/sbin
hdfs namenode -format
```
#### 2. 启动
```
cd /usr/hadoop-2.7.4/sbin
start-all.sh
```
#### 3. 检查进程
master 主机包含 ResourceManager、SecondaryNameNode、NameNode 等，则表示启动成功，例如：
```
2212 ResourceManager
2484 Jps
1917 NameNode
2078 SecondaryNameNode
```
各个 slave 主机包含 DataNode、NodeManager 等，则表示启用成功，例如：
```
17153 DataNode
17334 Jps
17241 NodeManager
```
## 运行 wordcount
由于 Hadoop 自带 wordcount 例程，所以可以直接调用。在启动 Hadoop 之后，我们可以通过以下命令来对 HDFS 中的文件进行操作：
```
hadoop fs -mkdir input
hadoop fs -put input.txt /input
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.4.jar wordcount /input /output/
```
![6762940-439379efda5b4ad6_副本](//mc.qcloudimg.com/static/img/50a03d9e0504301d54d12631cc8da075/image.jpg)
出现如上图结果就说明 Hadoop 安装已经成功了。

#### 查看输出目录
```
hadoop fs -ls /output
```

#### 查看输出结果
```
hadoop fs -cat /output/part-r-00000
```
![6762940-623e7b1c1b81cb4c_副本](//mc.qcloudimg.com/static/img/6d777bc87c16b0fb10713bbecda1636d/image.jpg)

>?单机模式与伪分布式模式的操作方法的详细过程，请参见官网文档 [Hadoop入门](https://hadoop.apache.org/docs/r1.0.4/cn/quickstart.html)。
