Pod 安全组将腾讯云 CVM 安全组与 Kubernetes Pod 集成。您可以使用腾讯云 CVM 安全组来定义规则，以允许进出您部署在多种 TKE 节点类型（目前只支持超级节点，后续会支持普通节点等）上运行的 Pod 的入站和出站网络流量。

## 限制条件

在为 Pod 使用安全组之前，请考虑以下限制条件：
- Pod 必须运行在 TKE 1.20 或更高版本的集群中。
- Pod 的安全组目前仅支持超级节点，其他类型节点后续上线。
- Pod 的安全组不能与双栈集群一起使用。
- 超级节点仅支持部分地域，请参考 [超级节点支持地域](https://cloud.tencent.com/document/product/457/58172)。

## 为 Pod 启用安全组能力

### 安装扩展组件

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 为集群安装 SecurityGroupPolicy（安全组策略）组件。
  - 如果您还没有创建集群，可以在创建集群的时候安装 SecurityGroupPolicy 组件。详情见 [通过集群创建页安装](https://cloud.tencent.com/document/product/457/49442#.E9.80.9A.E8.BF.87.E9.9B.86.E7.BE.A4.E5.88.9B.E5.BB.BA.E9.A1.B5.E5.AE.89.E8.A3.85)。
  - 如果您需要给已创建好的集群中的 Pod 开启安全组能力，请在组件管理中安装 SecurityGroupPolicy 组件。详情见 [通过组件管理页安装](https://cloud.tencent.com/document/product/457/49442#.E9.80.9A.E8.BF.87.E7.BB.84.E4.BB.B6.E7.AE.A1.E7.90.86.E9.A1.B5.E5.AE.89.E8.A3.85)。
![](https://qcloudimg.tencent-cloud.cn/raw/d88d3679c74b40bbf5c163eb73cf8f77.png)
3. 在组件管理页面查看组件状态。如组件状态为“成功”，代表组件部署完成。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3c7adc90b704ad0b800cf988c0c9f16b.png)
4. 在超级节点页面，确认您的 TKE 标准集群已包含超级节点，目前仅支持调度到超级节点上的 Pod 开启安全组能力。
![](https://qcloudimg.tencent-cloud.cn/raw/b28c0b8e9d71082ba63aea0872c29126.png)

## 部署示例应用程序

要对 Pod 使用安全组，您必须将 [SecurityGroupPolicy](#sgp) 部署到您的集群。以下步骤向您展示了如何使用 [CloudShell](https://cloud.tencent.com/document/product/1278/60734) 为 Pod 使用安全组策略。除非另有说明，否则请从同一终端完成所有步骤，因为在以下步骤中使用的变量不会跨终端持续存在。

### 使用安全组部署示例 Pod

1.  创建一个安全组以与您的 Pod 一起使用。以下步骤可帮助您创建一个简单的安全组，仅用于说明目的。在生产集群中，您的规则可能会有所不同。
    a. 检索集群的 VPC 和集群安全组的 ID。您在使用时可替换`my-cluster`。
    ```shell
    my_cluster_name=my-cluster
    my_cluster_vpc_id=$(tccli tke DescribeClusters --cli-unfold-argument --ClusterIds $my_cluster_name --filter Clusters[0].ClusterNetworkSettings.VpcId | sed 's/\"//g')
    my_cluster_security_group_id=$(tccli vpc DescribeSecurityGroups --cli-unfold-argument --Filters.0.Name security-group-name --Filters.0.Values tke-worker-security-for-$my_cluster_name --filter SecurityGroupSet[0].SecurityGroupId | sed 's/\"//g')
    ```
    b. 为您的 Pod 创建安全组。您在使用时可替换`my-pod-security-group`。记下运行命令后输出中返回的安全组 ID，您将在后面的步骤中使用它。
    ```shell
    my_pod_security_group_name=my-pod-security-group
    tccli vpc CreateSecurityGroup --GroupName "my-pod-security-group" --GroupDescription "My pod security group"
    my_pod_security_group_id=$(tccli vpc DescribeSecurityGroups --cli-unfold-argument --Filters.0.Name security-group-name --Filters.0.Values my-pod-security-group --filter SecurityGroupSet[0].SecurityGroupId | sed 's/\"//g')
    echo $my_pod_security_group_id
    ```
    c. 允许您上一步中创建的 Pod 安全组到集群安全组的 TCP 和 UDP 端口53流量，以允许部署示例中 Pod 可以通过域名访问应用程序。
    ```shell
    tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_cluster_security_group_id --SecurityGroupPolicySet.Ingress.0.Protocol UDP --SecurityGroupPolicySet.Ingress.0.Port 53 --SecurityGroupPolicySet.Ingress.0.SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Action ACCEPT
    tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_cluster_security_group_id --SecurityGroupPolicySet.Ingress.0.Protocol TCP --SecurityGroupPolicySet.Ingress.0.Port 53 --SecurityGroupPolicySet.Ingress.0.SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Action ACCEPT
    ```
    d. 需要允许任何协议和端口从安全组关联的 Pod 到任意安全组关联的 Pod 的入站流量。并且允许安全组关联的 Pod 的任何协议和端口的出站流量。
    ```shell
    tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Protocol ALL --SecurityGroupPolicySet.Ingress.0.Port ALL --SecurityGroupPolicySet.Ingress.0.SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Action ACCEPT
    tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Egress.0.Protocol ALL --SecurityGroupPolicySet.Egress.0.Port ALL --SecurityGroupPolicySet.Egress.0.Action ACCEPT
    ```

2.  创建一个 Kubernetes 命名空间来部署资源。
  ```shell
  kubectl create namespace my-namespace
  ```
[](id:sgp)
3. 将 SecurityGroupPolicy 部署到您的集群。
    a. 将以下示例安全策略保存为`my-security-group-policy.yaml`。如果您更愿意根据服务帐户标签选择 Pod，则可以替换 podSelector 为 serviceAccountSelector，您必须指定一个或另一个选择器。如果指定多个安全组，则所有安全组中的所有规则都会对选定的 Pod 有效。将`$my_pod_security_group_id`替换为您在上一步中为 Pod 创建安全组时记下的安全组 ID 。
    ```yaml
    apiVersion: vpcresources.tke.cloud.tencent.com/v1beta1
    kind: SecurityGroupPolicy
    metadata:
      name: my-security-group-policy
      namespace: my-namespace
    spec:
      podSelector: 
        matchLabels:
          app: my-app
      securityGroups:
        groupIds:
          - $my_pod_security_group_id
    ```
<dx-alert infotype="notice" title="">
您为 Pod 指定的一个或多个安全组必须满足以下条件：
- 它们必须存在。
- 它们必须允许来自集群安全组（for kubelet）的入站请求，允许给 Pod 配置的健康检查可以工作。
- 您的 CoreDNS pod 的安全组必须允许 Pod 安全组的入站 TCP 和 UDP 端口53流量。
- 它们必须具有必要的入站和出站规则才能与其他 Pod 进行通信。


**安全组策略仅适用于新调度的 Pod。它们不会影响正在运行的 Pod。如需存量 Pod 生效，则需要您确认存量 Pod 满足上述条件后手动重建。**
</dx-alert>
    b. 部署策略。
    ```shell
    kubectl apply -f my-security-group-policy.yaml
    ```
4. 部署示例应用程序使用您在上一步中 podSelector 指定的 my-app 匹配标签。
    a. 将以下内容保存到名为`sample-application.yaml`。
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
      namespace: my-namespace
      labels:
        app: my-app
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          terminationGracePeriodSeconds: 120
          containers:
          - name: nginx
            image: nginx:latest
            ports:
            - containerPort: 80
          nodeSelector:
            node.kubernetes.io/instance-type: eklet
          tolerations: 
          - effect: NoSchedule
            key: eks.tke.cloud.tencent.com/eklet
            operator: Exists
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: my-app
      namespace: my-namespace
      labels:
        app: my-app
    spec:
      selector:
        app: my-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ```

    b. 使用以下命令部署应用程序。当您部署应用程序时，Pod 会优先调度到超级节点上，并且将应用您在上一步中指定的安全组到 Pod 上。
    ```shell
    kubectl apply -f sample-application.yaml
    ```
>! 如果您没有使用 nodeSelector 优先调度到超级节点，当 Pod 调度到其他节点的时候，安全组是不生效的并且 `kubectl describe pod` 会输出 `security groups is only support super node, node 10.0.0.1 is not super node`。
>
5.  查看使用示例应用程序部署的 Pod。截止现在为止此终端称为 `TerminalA`。
  ```shell
  kubectl get pods -n my-namespace -o wide
  ```
  示例输出如下：
  ```shell
  NAME                             READY   STATUS    RESTARTS   AGE   IP           NODE                             NOMINATED NODE   READINESS GATES
  my-deployment-866ffd8886-9zfrp   1/1     Running   0          85s   10.0.64.10   eklet-subnet-q21rasu6-8bpgyx9r   <none>           <none>
  my-deployment-866ffd8886-b7gzb   1/1     Running   0          85s   10.0.64.3    eklet-subnet-q21rasu6-8bpgyx9r   <none>           <none>
  ```

6.  在另一个终端中进入任意 Pod，此终端称为 `TerminalB`。替换为上一步输出中返回的 Pod ID。
  ```shell
  kubectl exec -it -n my-namespace my-deployment-866ffd8886-9zfrp -- /bin/bash
  ```

7.  在终端 `TerminalB` 中确认示例应用程序工作正常。
  ```shell
  curl my-app
  ```
  示例输出如下：
  ```html
  <!DOCTYPE html>
  <html>
  <head>
  <title>Welcome to nginx!</title>
  ...
  ```
  您收到了响应是因为运行应用程序的所有 Pod 都与您创建的安全组关联。该安全组包含规则有：
	1. 允许与安全组关联的所有 Pod 之间的所有流量。
	2. 允许 DNS 流量从该安全组出站到您的节点关联的集群安全组，这些节点正在运行 CoreDNS Pod，您的 Pod 会对 `my-app` 进行域名查找。

8.  从 `TerminalA` 中，从集群安全组中删除允许 DNS 通信的安全组规则。
  ```shell
  tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_cluster_security_group_id --SecurityGroupPolicySet.Ingress.0.Protocol UDP --SecurityGroupPolicySet.Ingress.0.Port 53 --SecurityGroupPolicySet.Ingress.0.SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Action ACCEPT
  tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument --SecurityGroupId $my_cluster_security_group_id --SecurityGroupPolicySet.Ingress.0.Protocol TCP --SecurityGroupPolicySet.Ingress.0.Port 53 --SecurityGroupPolicySet.Ingress.0.SecurityGroupId $my_pod_security_group_id --SecurityGroupPolicySet.Ingress.0.Action ACCEPT
  ```

9.  从 `TerminalB`，尝试再次访问应用程序。
  ```shell
  curl my-app
  ```
  尝试失败，因为 Pod 不能访问 CoreDNS Pod，集群安全组不再允许从与您安全组关联的 Pod 中进行 DNS 通信。
  如果您尝试使用 IP 地址访问应用程序，您仍然会收到响应，因为所有端口都允许在具有与其关联的安全组的 pod 之间进行，并且不需要域名查找。

10. 完成试验后，您可以使用以下命令删除创建的示例安全组策略、应用程序和安全组。
  ```
  kubectl delete namespace my-namespace
  tccli vpc DeleteSecurityGroup --cli-unfold-argument --SecurityGroupId $my_pod_security_group_id
  ```
