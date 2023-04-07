本文介绍如何在自建 Kubernetes 集群上安装 LogListener 组件，从而将日志收集到日志服务（Cloud Log Service，CLS）。

在自建 Kubernetes 集群上安装 LogListener 组件的过程中，可以按步骤参考以下操作：
1. 依赖
 - 标准的 kubernetes 集群，不支持 microk8s 或者 k3s 等非标准部署的 Kubernetes 集群。
 - 需要 helm 版本为3.1以上版本。

2. 安装 Helm
安装详情可参考 [安装 Helm](https://docs.helm.sh/docs/intro/install/) 。

3. 安装 LogListener
```
wget https://mirrors.tencent.com/install/cls/k8s/tencentcloud-cls-k8s-install.sh
```
```
bash +x tencentcloud-cls-k8s-install.sh
```
```
./tencentcloud-cls-k8s-install.sh --region ap-guangzhou --secretid xxx --secretkey xxx
```

4. 参数说明
<table>
	<tr>
		<th>参数名</th>
		<th>类型描述</th>
	</tr>
		<tr>
			<td>secretid</td>
			<td>腾讯云账户访问 ID</td>
		</tr>
		<tr>
			<td>secretkey</td>
			<td>腾讯云账户访问密钥</td>
		</tr>
		<tr>
			<td>region</td>
			<td>CLS 服务地域</td>
		</tr>
		<tr>
			<td>docker_root</td>
			<td>集群 Docker 的根目录，默认是/var/lib/docker，如果集群不是这个默认目录，需要指定具体的 Docker 的根目录。</td>
		</tr>
		<tr>
			<td>cluster_id</td>
			<td>集群 ID，如果不指定，在安装期间会生成一个默认 ID（最好指定一个集群 ID，默认生成的 ID 的可读性较差）。</td>
		</tr>
		<tr>
			<td>network</td>
			<td>使用内网还是外网，默认使用外网。</td>
		</tr>
		<tr>
			<td>api_network</td>
			<td>云 API 使用内网还是外网，默认使用外网（internet）。</td>
		</tr>
		<tr>
			<td>api_region</td>
			<td>云 API 的地域，地域详情请参见<a href="https://cloud.tencent.com/document/product/614/18940"> 可用地域</a> 文档。</td>
		</tr>
</table>

	示例：
  广州组件部署
  ```
  ./tencentcloud-cls-k8s-install.sh --secretid xxx --secretkey xx --region ap-guangzhou  --network internet --api_region ap-guangzhou
  ```

5. 查看 
  1. 查看安装 Helm 包
  安装成功后，查看 Helm 安装 tencent-cloud-cls-log。
  ```
  helm list -n kube-system
  ```

  2. 查看组件
  ```
  kubectl get pods -o wide -n kube-system | grep tke-log-agent
  ```
  ```
  kubectl get pods -o wide -n kube-system | grep cls-provisioner
  ```

  使用上述命令查看组件是否都启动正常，正常情况下，每台宿主机上都会启动一个 tke-log-agent 的采集 pod 和一个 cls-provisioner 的 pod。

6. 配置LogListener

  1. 执行以下kubectl命令修改tke-log-agent环境变量

     ```
     kubectl edit ds tke-log-agent -n kube-system
     ```

  2. 通过编辑环境变量定义LogListener采集配置![img](https://tapd.woa.com/tfl/captures/2023-01/tapd_20422236_base64_1673580199_31.png)

  3. 参数说明

     <table>
     	<tr>
     		<th>变量名</th>
     		<th>变量描述</th>
     	</tr>
     		<tr>
     			<td>MAX_CONNECTION</td>
     			<td>最大连接数，默认10</td>
     		</tr>
     		<tr>
     			<td>CHECKPOINT_WINDOW_SIZE</td>
     			<td>单个文件的checkpoint 环长度，默认1024</td>
     		</tr>
     		<tr>
     			<td>MAX_FILE_BREAKPOINTS</td>
     			<td>位点文件大小，N*2k，N默认8k</td>
     		</tr>
     		<tr>
     			<td>MAX_SENDRATE</td>
     			<td>最大发送速率，Bytes/s，默认不限制</td>
     		</tr>
     		<tr>
     			<td>MAX_FILE</td>
     			<td>最大监控文件数量，默认15000</td>
     		</tr>
     		<tr>
     			<td>MAX_DIR</td>
     			<td>最大监控目录数量，默认5000</td>
     		</tr>
     		<tr>
     			<td>MAX_HTTPS_CONNECTION</td>
     			<td>https最大连接数，默认100</td>
     		</tr>
     		<tr>
     			<td>CONCURRENCY_TASKS</td>
     			<td>loglistener任务池，默认256 （3.x以上支持）</td>
     		</tr>
       	<tr>
     			<td>PROCESS_TASKS_EVERY_LOOP</td>
     			<td>单次循环处理任务数，默认4</td>
     		</tr>
       	<tr>
     			<td>CPU_USAGE_THRES</td>
     			<td>loglistener使用内存阈值，默认不限制</td>
     		</tr>
     </table>

7. 升级

  1. Kubernetes 版本是1.13以上的版本：
  ```
  wget http://mirrors.tencent.com/install/cls/k8s/upgrade/upgrade.sh
  ```

    ```
  chmod +x upgrade.sh
    ```

    ```
  ./upgrade.sh
  ```

  2. Kubernetes 版本是1.13以下的版本：
  ```
  wget http://mirrors.tencent.com/install/cls/k8s/upgrade/upgrade-1.13.sh
  ```

    ```
  chmod +x upgrade-1.13.sh
  ```

    ```
  ./upgrade-1.13.sh
  ```

8. 卸载
  使用下面命令可以卸载已经安装的 tencent-cloud-cls-log helm 包。
  ```
  helm uninstall tencent-cloud-cls-log -n kube-system
  ```
>! 如果想要完全删除 tencent-cloud-cls-log 包，无论之前安装的时候 –cluster_id 参数指定错误需要删除重新部署还是不再部署，都需要执行下面命令，将 cls-k8s 的 secret 删除，因为这里面保存着 –cluster_id 参数。
```
kubectl delete secret -n kube-system cls-k8s
```

8. 异常排查
可参考 [自建 K8S 日志采集排查指南](https://cloud.tencent.com/document/product/614/84182) 文档。
