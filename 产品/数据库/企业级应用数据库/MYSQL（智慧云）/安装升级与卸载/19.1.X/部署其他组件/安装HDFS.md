## 安装HDFSHDFS
步骤1：登录计划安装HDFS的设备，使用lsblk查看磁盘信息。
步骤2：使用mkfs工具将目标磁盘格式化为xfs文件系统。若已经格式化为xfs文件系统，请跳过此步骤。示例如下：
```
# mkfs.xfs -f /dev/sdg
# mkfs.xfs -f /dev/sdh
# mkfs.xfs -f /dev/sdi
```
步骤3：创建目录文件并挂载。
```
# mkdir -p /data{2..4}
```
步骤4：修改/etc/fstab文件，设置自动挂载到指定路径。
```
# vim /etc/fstab
/dev/sdg                /data2                  xfs     defaults,noatime        0 0
/dev/sdh                /data3                  xfs     defaults,noatime        0 0
/dev/sdi                /data4                  xfs     defaults,noatime        0 0
```
步骤5：挂载磁盘
```
# mount -a
```
步骤6：使用df -hT命令查阅是否挂载成功。
步骤7：再次回到主控机，找到tdsql_host文件，确认hdfs的IP、数量是否正确，示例如下：
>!hdfs初始数量只能为1或3，如果只有1台HDFS，请只保留tdsql_hdfs1这一行。另外，如果HDFS基于高可用部署了3台，则zookeeper服务器也必须是3台或更多。

```
[tdsql_hdfs] 
tdsql_hdfs1 ansible_ssh_host=172.xxx.xxx.19
tdsql_hdfs2 ansible_ssh_host=172.xxx.xxx.135
tdsql_hdfs3 ansible_ssh_host=172.xxx.xxx.121

```
>!如果HDFS服务器是新加入的服务器，需要将IP补充到[tdsql_allmacforcheck]。并执行以下命令，添加新加服务与原有服务的免密登录：

```
# cd tdsql_install/scripts
# vim ip_passwd_list	#执行完成后，请删除此文件中的内容
	192.xxx.xxx.xxx  password
# sh nokey.sh

```
步骤8：修改group_vars/all文件下列参数，示例如下：
```
# vim group_vars/all
tdsql_hdfs_ssh: 36000				#hdfs机器间ssh通信端口
hdfs_datadir: /data2/hdfs/data,/data3/hdfs/data,/data4/hdfs/data		#hdfs的存放数据文件的路径（一个磁盘一个路径，逗号分隔）
```
步骤9：安装HDFS，执行以下命令，最终显示failed任务数为0即安装成功。
```
# ansible-playbook -i tdsql_hosts playbooks/tdsql_hdfs.yml
```

## 验证HDFS是否安装成功
步骤1：在HDFS服务器集群下查看/tdsqlbackup路径是否被创建。
```
# su - tdsql
#查看/tdsqlbackup目录是否已经被自动创建，权限是否如下
$ hadoop fs -ls / 
drwxr-xr-x   - tdsql supergroup          0 2019-01-02 17:52 /tdsqlbackup
#如果目录不在或者权限不对，用下面命令修改：
$ hadoop fs -mkdir /tdsqlbackup
$ hadoop fs -chown tdsql.supergroup /tdsqlbackup
```
步骤2：用tdsql用户执行以下命令，查看所有namenode和datanode节点状态。
```
$ hdfs haadmin -getAllServiceState  #高可用部署时，执行
$ hdfs dfsadmin -report
```
步骤3（可选）：如果基于高可用（3节点）的HDFS，在不同服务器上用tdsql用户执行jps命令，看到的结果不同。
- hdfs1和hdfs2机器上应该看到NameNode、JournalNode、DataNode、DFSZKFailoverController
- hdfs3机器上应该看到DataNode、JournalNode

## 配置HDFS监控
步骤1：进入赤兔前台，在左侧菜单点击【集群管理】>点击对应集群名称，进入【集群详情】，找到HDFS服务器列表信息。若没有配置，点击【修改配置】在HDFS集群列表中添加HDFS的IP:port. 一个IP:PORT一行（不要使用逗号、分号、句号等分格或结尾）.
>?高可用部署（3节点）的HDFS的namenode节点默认为hdfs1、hdfs2两台服务器，默认使用的50070端口。单节点架构的hdfs的默认端口号是9870。
