## Cluster Autoscaler

## 1. Overview
Cluster Autoscaler (CA) is an independent program that dynamically adjusts the number of nodes in a cluster to meet your needs. When the pods in the cluster cannot be scheduled due to insufficient resources, scaling up is automatically triggered to reduce the labor costs. When conditions such as idle nodes are met, scaling down is automatically triggered to save your resource costs.

## 2. How to Use It
### 2.1 Enable CA

Create an auto scaling group before using auto scaling. You can specify the minimum/maximum number and label.

 - Minimum/Maximum number - Limit the number of nodes in the scaling group.
 - Label - Nodes automatically scaled up are configured with a label that is set for the scaling group to implement a flexible scheduling policy for the service.

>**Notes:**
1. You need to configure `request` of the container under the service: Auto scaling up is triggered when some pods in the cluster cannot be scheduled due to insufficient resources, and the pod request is the basis for determining whether the resources are sufficient or not.
2. Do not directly modify the nodes belonging to the scaling group.
3. All nodes in the same scaling group should have the same configuration (model, label, etc.).
4. You can use PodDisruptionBudget (UI support will be available soon) to prevent pods from being deleted during scaling down.
5. Before specifying the minimum/maximum number of nodes in a scaling group, check whether the quota for the available zone where these nodes reside in is large enough.
6. It is not recommended to enable node auto scaling based on monitoring metrics.
7. Deleting a scaling group will terminate the CVMs in the scaling group. Please proceed with caution.

### 2.2 Triggering Conditions for Scaling Up/Down
#### Scaling Up
When pods in the cluster cannot be scheduled due to a lack of available resources, the auto scaling up policy is triggered to scale up the node to run these pods.
When the Kubernetes scheduler cannot find a place to run a pod, it sets the pod's PodCondition to false and the reason to "Unschedulable". The CA program performs scaling up by scanning whether there are unschedulable pods at regular intervals. If so, it will scale up the node to run these pods.

#### Scaling Down
When the proportion of both CPU and memory requests of all the pods on a node is less than 50%, the node is used as an alternative for scaling down. If the following conditions for scaling down are met, the node can be scaled down only when all the pods on it can be scheduled to other nodes.
The node containing the following types of pods cannot be scaled down:

- Pods with a strict PodDisruptionBudget. The node cannot be scaled down when PDB is not met
- Kube-system pods
- Pods that are not created by such controllers as deployment, replica set, job, and stateful set.
- Pods with local storage
- Pods that cannot be scheduled to other nodes

## 3. FAQ
### 3.1. What is the difference between Cluster Autoscaler and the node auto scaling based on monitoring metrics?

Cluster Autoscaler ensures that all the pods in the cluster can be scheduled, regardless of load. It also makes sure that the cluster contains no unnecessary nodes.
Node auto scaling based on monitoring metrics pays no attention to the pods during auto scaling. It may add a node with no pods, or delete a node with some system-critical pods, such as kube-dns. This auto scaling mechanism is not recommended by Kubernetes. Do not enable them at the same time because they conflict with each other.

### 3.2. What is the relationship between CA and scaling group?
A CA-enabled cluster will create a launch configuration and a scaling group that is bound with this launch configuration based on the selected node configuration. It will then perform scaling up/down in this bound scaling group. CVMs scaled up are automatically added to the cluster. Nodes that are automatically scaled up/down are billed on a postpaid basis. For more information on scaling group, please see [Auto Scaling](https://cloud.tencent.com/document/product/377).

### 3.3. Will CA scale down the nodes that I added manually on the TKE console?
No. CA only scales down the nodes within the scaling group. Nodes that are added on the [TKE console](https://console.cloud.tencent.com/ccs) are not added to the scaling group.

### 3.4. Can I add or remove CVMs on the AS console?
Yes but NOT RECOMMENDED. ed making any modifications on the [AS console](https://console.cloud.tencent.com/autoscaling).

### 3.5. Which configuration of the selected node will be inherited?
When creating a scaling group, you need to select a node in the cluster as a reference to create a [launch configuration](https://cloud.tencent.com/document/product/377/8543). The node configuration for reference includes:

 - vCPU
 - Memory
 - System disk size
 - Data disk size
 - Disk type
 - Bandwidth
 - Bandwidth billing method
 - Whether to assign public IP
 - Security group
 - VPC
 - Subnet

### 3.6. How to use multiple scaling groups?
According to the level and type of the service, you can create multiple scaling groups and set different labels for them to specify the label for the nodes scaled up in scaling groups, so as to classify the service.
 
### 3.7. Is the maximum number limited?
Each Tencent Cloud user is provided with a quota of 30 postpaid CVMs in each availability zone. Submit a ticket to apply for more CVMs for your scaling group.
For more information, please see [here](https://console.cloud.tencent.com/cvm/overview). Besides, the maximum number is limited to 200 for auto scaling. Submit a ticket to apply for more quota.

### 3.8. Will the availability of cluster be affected during scaling down? 
Since pods are rescheduled when a node is scaled down, the service must tolerate the rescheduling and short-term interruption before re-enabling scaling down. It is recommended that you set [PDB](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) for your service. PDB specifies the minimum number or percentage of replicas of a collection of pods that must be up at any time. With PodDisruptionBudget, an application deployer can ensure that cluster operations that voluntarily evict pods will never take down so many simultaneously as to cause data loss, an outage, or an unacceptable service degradation.

### 3.9. What types of pods will not trigger scaling down of a node?

 - Pods with a strict PodDisruptionBudget. The node cannot be scaled down when PDB is not met
 - Kube-system pods
 - Pods on the node are created by such controller as non-deployment, replica set, job, statefulset, etc.
 - Pods with local storage
 - Pods that cannot be scheduled to other nodes

### 3.10. How long before a node is scaled down when the condition for scaling down is met?
10 minutes

### 3.11. How long before a node is scaled down when it is marked as Not Ready?
20 minutes

### 3.12. How often a node is scanned for scaling?
10 seconds

### 3.13. How long will it take to complete the scaling up of CVMs?
It generally takes less than 10 minutes. For more information, please see [Auto Scaling](https://cloud.tencent.com/document/product/377).


### 3.14. Why is a node with unschedulable pods not scaled up?
The reasons may include the requested resource of a pod is too large, a node selector is set, the maximum number of nodes in the scaling group is reached, account balance is sufficient (AS cannot trigger scaling up if the account balance is insufficient), quota is insufficient. See [here](https://cloud.tencent.com/document/product/377/7862).


### 3.15. How to prevent Cluster Autoscaler from scaling down a specific node?

``` sh
# You can set the following information in the annotations of the node:
kubectl annotate node <nodename> cluster-autoscaler.kubernetes.io/scale-down-disabled=true
```

 
### 3.16. How to provide feedback on the scaling events to users? 

You can query the scaling events of a scaling group and view K8S events on the AS console. Events can be found on the following three resources:
1. kube-system/cluster-autoscaler-status
2. pod
3. node

* kube-system/cluster-autoscaler-status config map:
    * **ScaledUpGroup** - CA triggers scaling up.
    * **ScaleDownEmpty** - CA deletes a node with no pod running on it.
    * **ScaleDown** - CA triggers scaling down.
* node:
    * **ScaleDown** - CA triggers scaling down.
    * **ScaleDownFailed** - CA triggers scaling down but failed.
* pod:
    * **TriggeredScaleUp** - CA triggers scaling up because of this pod.
    * **NotTriggerScaleUp** - CA cannot find a scalable scaling group to schedule this pod.
    * **ScaleDown** - CA tries to evict this pod to scale down the node.




