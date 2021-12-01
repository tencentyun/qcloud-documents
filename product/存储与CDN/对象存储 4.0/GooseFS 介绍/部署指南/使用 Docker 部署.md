本文主要介绍如何使用 Docker 部署 GooseFS。

## 准备事项

1. 安装 Docker 19.03.14 及以上。
2. CentOS 7及以上。
3. 已获取 GooseFS docker 镜像，例如 goosefs:v1.0.0。

## 安装步骤

1. 创建 ufs 目录，将本机目录挂载到 GooseFS 根目录：
```shell
mkdir /tmp/goosefs_ufs 
```
2. 启动 master 进程：
```shell
docker run -d  --rm \
--net=host \
--name=goosefs-master \
-v /tmp/goosefs_ufs:/opt/data \
-e GOOSEFS_JAVA_OPTS=" \
-Dgoosefs.master.hostname=localhost \
-Dgoosefs.master.mount.table.root.ufs=/opt/data" \
goosefs:v1.0.0 master
```
 <dx-alert infotype="explain" title="说明">
- -Dgoosefs.master.hostname：设置 master 地址。
- -Dgoosefs.master.mount.table.root.ufs：设置 GooseFS 根目录挂载点。
- -v /tmp/goosefs_ufs:/opt/data：将本地目录映射到 docker 容器内。
- --net=host：docker 采用 host 网络。
</dx-alert>
3. 启动 worker 进程：
```shell
docker run -d --rm \
--net=host \
--name=goosefs-worker1 \
--shm-size=1G \
-e GOOSEFS_JAVA_OPTS=" \
-Dgoosefs.worker.memory.size=1G \
-Dgoosefs.master.hostname=localhost" \
goosefs:v1.0.0 worker
```

## 操作演示

1. 查看容器：
```shell
[root@VM-0-7-centos ~]# docker ps | grep goosefs
0bda1cac76f4        goosefs:v1.0.0      "/entrypoint.sh mast…"   32 minutes ago      Up 32 minutes                           goosefs-master
b6260f9a0134        goosefs:v1.0.0     "/entrypoint.sh work…"   About an hour ago   Up About an hour                        goosefs-worker1
```
2. 进入容器：
``` shell
docker exec -it 0bda1cac76f4 /bin/bash
```
3. 挂载 COS 目录：
```shell
goosefs fs mount --option fs.cosn.userinfo.secretId={secretId} \
    --option fs.cosn.userinfo.secretKey={secretKey} \
    --option fs.cosn.bucket.region=ap-beijing \
    --option fs.cosn.impl=org.apache.hadoop.fs.CosFileSystem \
    --option fs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.CosN \
    /cosn {cos桶}
```
4. 查看目录：
```shell
[goosefs@VM-0-7-centos goosefs-1.0.0-SNAPSHOT-noUI-noHelm]$ goosefs fs ls /
drwxrwxrwx  goosefs        goosefs                      1       PERSISTED 01-01-1970 08:00:00:000  DIR /cosn
drwxr-xr-x  root           root                         0       PERSISTED 06-25-2021 11:01:24:000  DIR /my 
```
5. 查看 worker 节点：
```shell

 [goosefs@VM-0-7-centos goosefs-1.0.0-SNAPSHOT-noUI-noHelm]$ goosefs fsadmin report capacity
 Capacity information for all workers: 
    Total Capacity: 1024.00MB
        Tier: MEM  Size: 1024.00MB
    Used Capacity: 0B
        Tier: MEM  Size: 0B
    Used Percentage: 0%
    Free Percentage: 100%

 Worker Name      Last Heartbeat   Storage       MEM
 172.31.0.7       0                capacity      1024.00MB
                                  used          0B (0%)
```
