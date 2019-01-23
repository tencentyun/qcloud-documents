## 设置节点Label
### 使用限制
1. \*kubernetes\* 和 \*qcloud\* 相关标签禁用编辑和删除
2. \*kubernetes\* 和 \*qcloud\*  标签为保留键， 不支持添加
3. 当前仅支持单个节点设置Label，不支持批量设置

### 操作指引
#### 控制台设置节点Label
1. 选择需要设置节点的集群，进入集群详情。
2. 进入节点列表页，选择需要设置Label的节点，选择更多操作，点击编辑Label。
3. 编辑Label。
![][1]

#### kubectl设置节点Label
1. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
2. 执行命令设置节点Label：
```shell
kubectl label nodes <node-name> <label-key>=<label-value>
```
3. 通过kubectl get nodes --show-labels查看节点标签
```shell
kubectl get nodes --show-labels
NAME           STATUS    ROLES     AGE       VERSION         LABELS
172.17.124.5   Ready     <none>    12d       v1.10.5-tke.3   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=QCLOUD,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/region=sh,failure-domain.beta.kubernetes.io/zone=200001,kubernetes.io/hostname=172.17.124.5
172.17.124.8   Ready     <none>    12d       v1.10.5-tke.3   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=QCLOUD,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/region=sh,failure-domain.beta.kubernetes.io/zone=200001,kubernetes.io/hostname=172.17.124.8
```

[1]:https://main.qcloudimg.com/raw/dc33fc478ae091fd681811821122feba.png
