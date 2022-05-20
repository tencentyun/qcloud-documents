本文介绍如何在自建 Kubernetes 集群上安装 LogListener 组件，从而将日志收集到日志服务（Cloud Log Service，CLS）。
在自建 Kubernetes 集群上安装 LogListener 组件的过程中，系统自动完成以下操作：
1. 创建 CLS-logconfigs CRD。
2. 部署工作负载 cls-provisioner。
3. 以 DaemonSet 模式安装 LogListener。


## 操作步骤

1. 登录 Kubernetes 集群。
2.	依次执行如下命令，安装 cls-provisioner Helm。
```
wget https://mirrors.tencent.com/install/cls/k8s/tencentcloud-cls-k8s-install.sh
```
```
chmod 744 tencentcloud-cls-k8s-install.sh
```
```
./tencentcloud-cls-k8s-install.sh --region xxx --secretid xxx --secretkey xxx 
```
安装完成后，CLS 会自动创建名为 `cls-k8s-随机 ID` 的默认机器组。
>! 安装 cls-provisioner Helm 前，请确保已在 Kubernetes 集群中安装 Helm 命令，详情请参见 [安装 Helm](https://docs.helm.sh/docs/intro/install/) 文档。
>

## 参数说明

-	--secretid：腾讯云账户访问密钥 ID。
-	--secretkey：腾讯云账户访问密钥 Key。
-	--region：CLS 服务地域。
-	--docker_root：集群 Docker 的根目录，默认是 /var/lib/docker。
>? 
> - 建议不同的集群使用不同的 cluster_id。
> - 不同的集群数据可以投递到相同的 topic。
> - 默认 ID 生成规则为：cls-k8s-8位随机 ID。
>   
-	--network：网络使用类型，内网（intra）或者外网（internet），默认使用内网。
-	--api_network：云 API 的网络使用类型，内网（intra）或者外网（internet），默认使用外网（internet）。
- --api_region：云 API 的地域，地域详情请参见 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。
- region 和 api_region 地区保持一致，可分别参考 [域名-loglistener](https://cloud.tencent.com/document/product/614/18940#LogListener) ，[地域-日志服务 API3.0](https://cloud.tencent.com/document/product/614/18940#API3) 文档检验网络。

#### 示例

北京组件组件部署：
```
./tencentcloud-cls-k8s-install.sh --secretid xxx --secretkey xx --region ap-beijing  --network internet --api_region ap-beijing
```


