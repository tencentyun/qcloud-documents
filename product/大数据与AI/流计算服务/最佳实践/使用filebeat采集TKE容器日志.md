## 背景

当业务使用腾讯云容器服务 TKE 进行部署时，可以通过 filebeat 来采集 TKE 中各个 pod 的日志，写入到下游的 Elasticsearch 集群中，然后在 kibana 上进行日志的查询与分析。本文介绍如何使用 filebeat daemonset 的方式采集容器中的日志。

## 实战过程

下面以采用运行 containerd 的 TKE 容器集群，以采集 nginx 日志为例，介绍使用 filebeat 采集 nginx pod 上的日志并写入到 es。

### 部署nginx daemonset

首先使用了一个 Docker Hub 中的 nginx 镜像，部署了一个名为 nginx 的 DaemonSet。
![](https://main.qcloudimg.com/raw/c0ef710a9beec9ee43946e8e13936256.png)

### 部署 filebeat daemonset

1. 创建 ConfigMap

filebeat 以 filebeat.yml 文件为主配置文件，首先创建一个 filebeat.yml 配置的 ConfigMap。
![](https://main.qcloudimg.com/raw/9e64ca39db10bb6472799a30329b09d3.png)
新建的 ConfigMap 中的变量名为 filebeat.yml, 内容为具体的配置信息，以下是一个最简单的 filebeat.yml 配置。
```
		filebeat.inputs:
		- type: log 
			symlinks: true
			paths:
				- /var/log/containers/*.log

		output.elasticsearch:
			hosts: ['x.x.x.x:9200']
			username: "elastic"
			password: "x.x.x.x"
```
2. 使用公有镜像库中的 filebeat 镜像，部署 filebeat daemonset
![](https://main.qcloudimg.com/raw/be802b4541c5daba9d595cb2b4202154.png)

3. 配置数据卷
![](https://main.qcloudimg.com/raw/cbb196c74e2d5fd134b29e78017938eb.png)

4. 配置运行参数
![](https://main.qcloudimg.com/raw/2b720df3576016140f83b9cf7140ffa0.png)
 
5. 配置挂载点
![](https://main.qcloudimg.com/raw/c9bc9b8836ab4cb329b10e3aa9296ea9.png)

>? 数据卷和挂载点说明：
>1. 使用 ConfigMap 数据卷，使得 filebeat pod 可以读取到自定义的 filebeat.yml 配置。
>2. 使用主机路径`/var/log/containers`, 使得 filebeat pod 可以读取到其它pod的日志，因为其它 pod 的日志都会打印在宿主机的`/var/log/containers` 路径下。
>3. 因为主机路径`/var/log/containers` 下的 pod 日志，都是使用软链接，链接到`/var/log/pods` 目录下的各个 pod 的日志文件，因为也需要把主机路径`/var/log/containers` 挂载到 filebeat pod 上，这也是为什么在 filebeat.yml 中要定义 symlinks: true 的原因，因为默认情况下，filebeat 不对读取链接文件。

6. 在 kibana 中查看日志
进入到 filebeat.yml 中定义的 es 集群对应的 kibana 中，查看对应索引是否生成，是否可以正常查看 nginx 日志。
![](https://main.qcloudimg.com/raw/120591c2dcad63559108562724ddb06d.png)
通过以上步骤，可以看到，nginx 的日志可以正常被采集到。但是上述配置采集的是宿主机上所有 pod 的日志，有时需要只采集固定的某几个 pod 的日志，该怎么实现呢？

### 通过YML配置部署一个可以获取到Pod元信息的filebeat demonset

在实际的业务场景中，通常需要通过 filebeat 采集部署在相同 host 上的多个 pod 的日志，往往也需要获取到采集到的 pod 的元信息，比如命令空间、pod 名称、标签等信息，以方便进行过滤或者检索。获取到 pod 的元信息需要调用 k8s 的 API, filebeat 内部也实现了这个功能，因此可以直接使用 filebeat 的[container input](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-container.html)以及[add\_kubernetes\_metadata](https://www.elastic.co/guide/en/beats/filebeat/7.10/add-kubernetes-metadata.html) processors 来实现。

在 TKE 控制台上，单击 **YML 创建资源**按钮，直接使用如下 yml 配置创建 filebeat demonset。
```
---
		apiVersion: v1
		kind: ConfigMap
		metadata:
			name: filebeat-config
			namespace: default
			labels:
				k8s-app: filebeat
		data:
			filebeat.yml: |-
				filebeat.inputs:
				- type: container
					paths:
						- /var/log/containers/*.log
					processors:
						- add_kubernetes_metadata:
								host: ${NODE_NAME}
								matchers:
								- logs_path:
										logs_path: "/var/log/containers/"

				processors:
					- add_cloud_metadata:
					- add_host_metadata:
				output.elasticsearch:
					hosts: ['${ELASTICSEARCH_HOST:elasticsearch}:${ELASTICSEARCH_PORT:9200}']
					username: ${ELASTICSEARCH_USERNAME}
					password: ${ELASTICSEARCH_PASSWORD}
		---
		apiVersion: apps/v1
		kind: DaemonSet
		metadata:
			name: filebeat
			namespace: default
			labels:
				k8s-app: filebeat
		spec:
			selector:
				matchLabels:
					k8s-app: filebeat
			template:
				metadata:
					labels:
						k8s-app: filebeat
				spec:
					serviceAccountName: filebeat
					terminationGracePeriodSeconds: 30
					containers:
					- name: filebeat
						image: ccr.ccs.tencentyun.com/tke-market/filebeat:7.10.1
						args: [
							"-c", "/etc/filebeat.yml",
							"-e",
						]
						env:
						- name: ELASTICSEARCH_HOST
							value: x.x.x.x
						- name: ELASTICSEARCH_PORT
							value: "9200"
						- name: ELASTICSEARCH_USERNAME
							value: elastic
						- name: ELASTICSEARCH_PASSWORD
							value: Elastic123
						- name: NODE_NAME
							valueFrom:
								fieldRef:
									fieldPath: spec.nodeName
						securityContext:
							runAsUser: 0
							# If using Red Hat OpenShift uncomment this:
							#privileged: true
						resources:
							limits:
								memory: 200Mi
							requests:
								cpu: 100m
								memory: 100Mi
						volumeMounts:
						- name: config
							mountPath: /etc/filebeat.yml
							readOnly: true
							subPath: filebeat.yml
						- name: varlibdockercontainers
							mountPath: /var/lib/docker/containers
							readOnly: true
						- name: varlog
							mountPath: /var/log
							readOnly: true
						- name: varpods
							mountPath: /var/log/pods
							readOnly: true
					volumes:
					- name: config
						configMap:
							defaultMode: 0640
							name: filebeat-config
					- name: varlibdockercontainers
						hostPath:
							path: /var/lib/docker/containers
					- name: varlog
						hostPath:
							path: /var/log
					- name: varpods
						hostPath:
							path: /var/log/pods
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: ClusterRoleBinding
		metadata:
			name: filebeat
		subjects:
		- kind: ServiceAccount
			name: filebeat
			namespace: default
		roleRef:
			kind: ClusterRole
			name: filebeat
			apiGroup: rbac.authorization.k8s.io
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: RoleBinding
		metadata:
			name: filebeat
			namespace: default
		subjects:
			- kind: ServiceAccount
				name: filebeat
				namespace: default
		roleRef:
			kind: Role
			name: filebeat
			apiGroup: rbac.authorization.k8s.io
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: RoleBinding
		metadata:
			name: filebeat-kubeadm-config
			namespace: default
		subjects:
			- kind: ServiceAccount
				name: filebeat
				namespace: default
		roleRef:
			kind: Role
			name: filebeat-kubeadm-config
			apiGroup: rbac.authorization.k8s.io
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: ClusterRole
		metadata:
			name: filebeat
			labels:
				k8s-app: filebeat
		rules:
		- apiGroups: [""] # "" indicates the core API group
			resources:
			- namespaces
			- pods
			- nodes
			verbs:
			- get
			- watch
			- list
		- apiGroups: ["apps"]
			resources:
				- replicasets
			verbs: ["get", "list", "watch"]
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: Role
		metadata:
			name: filebeat
			# should be the namespace where filebeat is running
			namespace: default
			labels:
				k8s-app: filebeat
		rules:
			- apiGroups:
					- coordination.k8s.io
				resources:
					- leases
				verbs: ["get", "create", "update"]
		---
		apiVersion: rbac.authorization.k8s.io/v1
		kind: Role
		metadata:
			name: filebeat-kubeadm-config
			namespace: default
			labels:
				k8s-app: filebeat
		rules:
			- apiGroups: [""]
				resources:
					- configmaps
				resourceNames:
					- kubeadm-config
				verbs: ["get"]
		---
		apiVersion: v1
		kind: ServiceAccount
		metadata:
			name: filebeat
			namespace: default
			labels:
				k8s-app: filebeat
---
```

>? 配置说明：
>1. 命令空间为 default，根据需要也可以直接替换。
>2. 创建了名为 filebeat 的服务账号，并且授予获取 pods 列表、获取 pod 详情等接口的权限，filebeat 会使用该账号获取到 pods 的元信息。
>3. 通过 container input 采集`/var/log/containers/`目录下的日志， container input 可采集容器的 stdout 和 stderr。

在 kibana 中查看日志, 可以看到每条日志中都包含有 kubernetes 字段。
![](https://main.qcloudimg.com/raw/e3a067a58599b22f48aed63b8c10ea79.png)

上述配置通过 container input 直接采集到了 filebeat pod 所在的 node 上的所有 pod 的日志，当然，也包括了 filebeat 自身的日志，在真实的业务场景中，往往只需要采集业务关心的 pod 的日志即可，此时一种方式是通过在 filebeat.yml 中定义[processor](https://www.elastic.co/guide/en/beats/filebeat/current/defining-processors.html#condition-equals), 对采集到的所有日志 event 进行过滤，过滤掉不关心的日志 event 即可（比如通过 drop event processor 过滤掉某些不关心的 namespace 和 pod 的日志）；另外一种解决办法是通过 Autodiscover 定义新的 filebeat.yml 配置文件，通过定义模板只采集固定 pod 的日志，下面是一个简单的 Autodiscover 配置，该配置只采集容器名称为nginx的pod的日志：
```
	filebeat.autodiscover:
				providers:
					- type: kubernetes
						templates:
							- condition:
									equals:
										kubernetes.container.name: nginx
								config:
									 - type: container
										 paths:
											- /var/log/containers/${data.kubernetes.pod.name}_*.log

	processors:
				- add_cloud_metadata:
				- add_host_metadata:
	output.elasticsearch:
				hosts: ['${ELASTICSEARCH_HOST:elasticsearch}:${ELASTICSEARCH_PORT:9200}']
				username: ${ELASTICSEARCH_USERNAME}
				password: ${ELASTICSEARCH_PASSWORD}

```

通过修改名为 filebeat-config 的 ConfigMap, 并重新部署 pod，使得新配置生效，在 kibana 中查看日志，可以看到只有 nginx pod 的日志被采集到了。
![](https://main.qcloudimg.com/raw/1abec60b358e3e803696ec01d3e554d9.png)


