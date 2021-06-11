使用腾讯云容器服务（Tencent Kubernetes Engine，TKE）部署 GooseFS 时，需要在 TKE 上按需预留作业所需的 CPU、MEM、SSD 等资源。当前您可以通过手动拉取镜像的模式进行部署。主要流程如下：
1. 创建 TKE 集群。
2. 拉取 GooseFS 镜像。
3. 部署及调试。

## 准备事项

在开始部署前，您需要先确保如下条件已经就绪：
1. TKE 集群使用的 Kubernetes 版本需要大于1.18版本。
2. 已获取 GooseFS 镜像或者 GooseFS-FUSE 镜像。
3. TKE 集群的各节点间网络互通。

## 操作步骤

使用手动模式在 TKE 上部署 GooseFS 的详细操作步骤如下：

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke)，并创建 TKE 集群。集群配置信息可以按照业务需要选择合适的资源，默认推荐配置如下。您也可以参考 [TKE 快速入门](https://cloud.tencent.com/document/product/457/54231) 指引创建一个标准集群。
 - SA2.45XLARGE464 机型、内网带宽 25Gb
 - Master 信息：32GB/高效云盘100G x 1块
 - Worker 信息：64GB/高效云盘100G x 5块（至少3块）
2. 拉取 GooseFS 镜像到集群上，您可以根据业务需要拉取 GooseFS 镜像或者 GooseFS-FUSE 镜像。
3. 创建容器。
4. 拉起 Master 进程：
```plaintext
$ cat start_master.sh 
docker run -d --rm \
--net=host \
--name=goosefs-master \
-v /root/goosefs_ufs:/opt/goosefs/underFSStorage \
-e GOOSEFS_JAVA_OPTS=" \
-Dgoosefs.master.hostname=goosefs-master \
-Dgoosefs.master.mount.table.root.ufs=/opt/goosefs/underFSStorage" \
goosefs-1.0.0 master
```
5. 拉起 Worker 进程：
```plaintext
$ cat start_worker.sh 

docker run -d --rm \
--net=host \
--name=goosefs-worker1 \
--shm-size=1G \
-v /root/docker_test/goosefs_ufs:/opt/goosefs/underFSStorage \
-e GOOSEFS_JAVA_OPTS=" \
-goosefs.worker.memory.size=1G \
-goosefs.master.hostname=goosefs-master" \
goosefs-1.0.0 worker
```
6. 拉起 FUSE 进程：
```plaintext
$ cat start_fuse.sh 

docker run -d \
--name=goosefs-fuse \
-u=0 \
--net=host \
-v /mnt/ramdisk:/opt/ramdisk \
-v /mnt:/mnt:rshared \
-v /etc/yum.repos.d:/etc/yum.repos.d \
--cap-add SYS_ADMIN \
--device /dev/fuse \
goosefs-fuse-1.0.0 fuse
```
7. 开始调试。
```plaintext
$ docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
311784081cfc goosefs-fuse-1.0.0 "/entrypoint.sh fuse" 8 minutes ago Up 8 minutes goosefs-fuse
ab1cb7ab313c goosefs-1.0.0 "/entrypoint.sh work…" 8 minutes ago Up 8 minutes goosefs-worker1
b08a53b7ed46 goosefs-1.0.0 "/entrypoint.sh mast…" 8 minutes ago Up 8 minutes
```
8. 获取容器 id 后，进入容器：
```plaintext
$ docker exec -it <CONTAINER_ID> /bin/bash
```
 如下图所示：
![](https://main.qcloudimg.com/raw/8f9aba2470f38836dbaff7e7a48a657d.png)
9. 查看容器标准输出：
```plaintext
$ docker logs <CONTAINER_ID>
```
 如下图所示：
![](https://main.qcloudimg.com/raw/a1bbe15a0d811f9d4af2117d010f2702.png)

