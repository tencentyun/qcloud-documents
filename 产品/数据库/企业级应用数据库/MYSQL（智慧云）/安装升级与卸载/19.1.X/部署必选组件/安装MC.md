## 概述
该模块用于提供分布式事务实时强一致性读所需的GTS（全局时钟）。该模块必须在tdsql_part1_site.yml和tdsql_part2_site.yml完全安装成功后再安装。MC模块对分布式事务实时强一致性读来说是必选模块，如有可能建议采用高可用架构部署。MC服务器必须配置为1台或者3台。
>?如果不需要分布式事务实时强一致性读能力，可以无需安装该模块。

## 安装MC
步骤1：返回主控机，检查或修改tdsql_hosts文件的MC模块IP。示例如下：
```
# vim tdsql_install/tdsql_hosts
[tdsql_mc]  #生产环境建议使用独立机器高可用架构部署，测试环境可以和zk、proxy混布
tdsql_mc1 ansible_ssh_host=172.16.16.47   # 如果是单节点部署，仅保留该行保留tdsql_mc1
tdsql_mc2 ansible_ssh_host=172.16.16.39      
tdsql_mc3 ansible_ssh_host=172.16.16.46     
```
步骤2：修改group_vars/all文件
```
# vim group_vars/all
tdsql_mc_netif: eth0  #mc机器节点（ifconfig查看）网卡的名称
```
步骤3：执行部署
```
# cd tdsql_install/
# ansible-playbook -i tdsql_hosts playbooks/tdsql_mc.yml
```
步骤4：验证 MC 集群是否正常启动，登录已安装MC的所有节点，通过 ps 命令查看是否存在mc进程。并通过集群中任一节点调用获取 GTS 的 HTTP API 来验证，如：
```
# ps -ef | grep mc
# curl -XGET http://IP:12379/meta-cluster/api/get-ts/1/10
或者：# curl -XGET http://host:12379/meta-cluster/api/get-ts/1/10
## 如host为mc-host-1。 可以通过cat /etc/hosts查看
## 若能正常返回txn_ts的结果，则说明集群启动成功。
```
>?截止到本章节，安装尚未完成，请继续阅读。
