## 1. API Description
This API (ModifyClusterService) is used to modify service.
Domain name for API request: `ccs.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. For additional parameters, please see [Common Request Parameters](/doc/api/457/9463).
>**Note:**
> The parameters for modifying service are the same with those for creating service, except for `strategy` and `minReadySeconds`.
> You need to pass all service parameters when modifying the service, including the new service parameters that are identical with their original counterparts.
> If you only want to adjust the number of replicas or the description of the service, use our APIs designed for such actions.

| Parameter| Description | Type | Required | 
|---------|---------|---------|---------
| clusterId | Cluster ID, which needs to be entered The field clusterId returned via the API [Query Cluster List](/doc/api/457/9448) | String | Yes |
| serviceName | Service name, which is composed of lowercase letters, numbers and "-" with a length no more than 63 characters. It starts with a lowercase letter and ends with a lowercase letter or a number. | String | Yes |
| serviceDesc | Service description | String | No |
| replicas | Number of pod replicas | Int | Yes | 
| strategy | Service update policy (Recreate or RollingUpdate)<br>The Recreate method kills all the containers under the service before service update, and then recreates the containers based on new parameters.<br>The RollingUpdate method performs rolling update on the containers: First, kill some of the containers and create some new containers based on the new parameters. When the new containers are successfully launched, kill old containers and create new ones, until all new containers are successfully created and all old containers are killed, achieving a process of gated launch. | String | Yes |
| minReadySeconds | This is the time (in sec) to wait before launching the next new container when using RollingUpdate method. For example, if minReadySeconds is set to 10, the cluster first launches a new container, and wait for 10 seconds before launching another new container after the previous one is successfully launched. This is done until the number of new containers reaches the number of replicas. | Int | No | 
| accessType | Service access method. If it is not specified, default is ClusterIP.<br>LoadBalancer: This creates a public network load balancer for the service. Traffic is forwarded to the service when you access the IP and port of this load balancer.<br>SvcLBTypeInner: This creates a private network load balancer and occupies an IP under the subnet (you need to specify subnetId).<br>ClusterIP: The service cannot be accessed from outside the cluster. Only the other services within the cluster can access the service. Default is ClusterIP.<br>None: Network access is not available. The parameter portMappings.n is not required in this case. | String | No |
| portMappings.n | Port mapping information. When accessType is None, network access is not provided | Object Array | No |
| volumes.n | Container volume definition. If this is not specified, the field volumeMounts.n in the container object is not required either. | Object Array | No | 
| containers.n | Container array. You need to define at least one container for a service. The defined containers are launched upon service creation. | Object Array | Yes | 
| namespace | Namespace. Enter the field namespace returned via the API [Query Service List](/doc/api/457/9440). Default is "default". | String | No | 
| subnetId | Subnet ID. Enter the field unSubnetId (unified subnet ID) returned via the API [Query Subnet List](/doc/api/215/1371). This is requied if "accessType" is "SvcLBTypeInner". | String | No |
| nodeAffinity | Node affinity. Clusters of version 1.4.6 are not supported. The scheduling for node affinity uses nodeAffinity hard scheduling (requiredDuringSchedulingIgnoredDuringExecution) of Kubernetes. When Pod found that no node that meets the conditions is available for scheduling, scheduling may fail. | Object Array | No |
| podAffinity | Pod affinity. Clusters of version 1.4.6 are not supported. The pod under the service is specified to rely on the deployment of other pods. The scheduling for pod affinity uses podAffinity hard scheduling (requiredDuringSchedulingIgnoredDuringExecution) of Kubernetes. When Pod found that no node that meets the conditions is available for scheduling, scheduling may fail. | Object Array | No |

"portMappings" is described as followed: 

| Field | Description | Type | Required |  
|---------|---------|---------|---------|
| lbPort | If accessType is LoadBalancer or SvcLBTypeInner, this is the listening port of the load balancer and the service.<br>If accessType is ClusterIP, this is the listening port of the service. | Int | Yes | 
| containerPort | The listening port of container | Int | Yes |
| nodePort | Port opened on the node when accessType is LoadBalancer and SvcLBTypeInner. The system assigns a nodePort by default if this is left empty. | Int | No |
| protocol | Protocol (TCP or UDP) | String | Yes |

"volumes" is described as follows. For more information, please see [How to Mount Data Volume](/doc/product/457/9112).

| Field | Description | Type | Required | 
|---------|---------|---------|---------|
| name | Container volume name | String | Yes |
| volumeType | Container volume type. "hostPath", "cbsDisk", "configMap" and "nfsDisk" are supported. **Note: For cbsDisk, the number of service pods must be 1, because multiple nodes cannot be mounted to a CBS disk at a time.** | String | Yes | 
| hostPath | When volumeType is hostPath, container volume directory on the host is mapped to the container when the container launches. If this field is left empty, a temporary directory is created on the Node for the container volume and deleted when the container is terminated. This directory and the data in it are retained if hostPath is specified. | String | No |
| cbsDiskId | When volumeType is cbsDisk, this field is required. This is the ID of CBS network disk. This cbs disk is mounted to the host in which the container resides and mapped to the container when the container launches. It is unmounted from the host when the container is terminated. Enter the field storageId (cloud disk ID) returned via the API [Query Cloud Disk Information](/doc/api/362/2519). | String | No |
| nfsPath | When volumeType is nfsDisk, this field is required. This is the path where NFS disk is mounted, for example, `127.0.0.1:/exports`. | String | No |
| configId | When volumeType is configMap, this field is required. This is the ID of the configuration item to be mounted. | String | No | 
| configVersion | When volumeType is configMap, this field is required. This is the version of the configuration item to be mounted. | String | No |
| configKeys.n | When volumeType is configMap, this field is required. This is the array of the key for the configuration item to be mounted. | Object Array | No |

"Containers" is described as follows:

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| containerName | Container name, which cannot exceed 63 characters | String | Yes | 
| image | Container image | String | Yes | 
| envs.n | Container environment variable array. Variable name can only contain uppercase and lowercase letters, numbers and underscores, and cannot start with a number. | Object Array | No |
| volumeMounts.n | Container volume mount point | Object Array | No | 
| healthCheck.n | Container health check | Object Array | No | 
| cpu | CPU resource required for the container. Unit: mU (0.001 core). Minimum is 100 (0.1 core).<br>0 or empty value means no restriction.<br>For more information, please see [Configure Service Resource Limits](/doc/product/457/9099). | Int | No | 
| cpuLimits | Maximum CPU resource available for the container. Unit: mU (0.001 core). Minimum is 100 (0.1 core).<br>0 or empty value means no restriction, and a value greater than 0 must be no less than the value of "cpu".<br>For more information, please see [Configure Service Resource Limits](/doc/product/457/9099). | Int | No |
| memory | Memory required for the container (in MiB). It is recommended to choose a value no less than 4 MiB.<br>0 or empty value means no restriction, and a value greater than 0 must be no less than the value of "memory". If `memoryLimits` is not specified, the required memory equals to maximum available memory by default.<br>For more information, please see [Configure Service Resource Limits](/doc/product/457/9099). | Int | No |
| memoryLimits | Maximum memory available for the container (in MiB). It is recommended to choose a value no less than 4 MiB.<br>0 or empty value means no restriction.<br>For more information, please see [Configure Service Resource Limits](/doc/product/457/9099). | Int | No |
| command | Startup command for the container.<br>For more information, please see [Service Operation Commands and Parameter Configurations](/doc/product/457/9100). | String | No |
| arguments.n | Startup parameter for the container.<br>For more information, please see [Service Operation Commands and Parameter Configurations](/doc/product/457/9100). | String Array | No |
| privileged | Startup parameter for the container (case-sensitive). "true" means to enable, and "false" means to disable.<br>For more information, please see [Service Operation Commands and Parameter Configurations](/doc/product/457/9100). | Bool | No | 
| workingDir | Startup parameter for the container.<br>For more information, please see [Service Operation Commands and Parameter Configurations](/doc/product/457/9100). | String | No |

"envs" is described as follows:

| Field | Description | Type |
|---------|---------|---------|
| name | Environment variable name | String |
| value | Environment variable value | String |

"volumeMounts" is described as follows. For more information, please see [How to Mount Data Volume](/doc/product/457/9112).

| Field | Description | Type |
|---------|---------|---------|
| volumeName | Volume name | String | 
| mountPath | Volume mount point in the container | String |
| mode | Indicate how container accesses the volume. ro: read only. rw: read and write. | String |

For more information on the definition of `healthCheck`, please see [Service Health Check Settings](/doc/product/457/9094).

| Field | Description | Type |
|---------|---------|---------|
| type | Available value: liveCheck or readyCheck. "liveCheck" is used to check whether the container is alive. Container is restarted if the check fails. "readyCheck" is used to check whether the container is ready, and request forwarding towards the container is stopped if the check fails. | String |
| healthNum | Threshold for success check. Value range: 1-10. It means the container is considered to be alive if the check succeeds for this number of times consecutively. For example, if "type" is "liveCheck" and `healthNum" is 1, then the container is considered alive if the check returns successful result for 1 time in a row. | Int |
| unhealthNum | Threshold for failure check. Value range: 1-10. It means the container is considered to be dead if the check fails for this number of times consecutively. For example, if "type" is "liveCheck" and "unhealthNum" is 3, then the container is considered dead if the check returns failed result for 3 times in a row. | Int |
| intervalTime | Interval time between health checks (in sec), that is, the time until the next health check. Value range: 2-300. | Int |
| timeOut | Operation timeout for health checks (in sec). Value range: 2-60 seconds. | Int |
| delayTime | After the container starts up, the time to wait before health check is enabled (in sec). Default is 0 (enable immediately). Value range: 0-60 seconds. Note, if "type" is "readyCheck", the container is considered unready within the delayTime period after it launches, during which requests are not forwarded to this container when you access the corresponding service. |Int |
| checkMethod | Type of check (methodTcp, methodHttp, methodCmd) | String |
| port | Port. Value range: 1-65535. It is valid when checkMethod is methodTcp or methodHttp. If checkType is methodTcp, connection probe is performed towards this container port during the check process. The probe is considered successful if connection is successful, otherwise it is considered as failed. If "checkType" is `methodHttp`, an HTTP or HTTPS request is sent to this container port. The probe is considered successful if the returned httpcode falls within 200-399, otherwise it is considered as failed. | Int |
| protocol | The protocol used when HTTP probe is performed on the container, which is valid when checkMethod is methodHttp. Only HTTP and HTTPS are supported. |String |
| path | This is valid when checkMethod is methodHttp. When HTTP probe is performed on the container, a URL is created:` protocol://containerIp:port/path`, the probe is then executed by initiating a GET operation towards this URL. | String |
| cmd | This is valid when checkMethod is methodCmd. The command "cmd" is executed on the container when probe is performed. The probe is considered successful if the returned result is 0, otherwise it is considered as failed. | String |

`nodeAffinity` is described as follows:

| Field | Description | Type |
|---------|---------|---------|
| key | The key of the Label used to specify node affinity | String | 
| operator | Affinity operator, including In, NotIn, Exists, DoesNotExist, Gt, Lt | String | 
| values | The value of the Label used to specify node affinity | String Array |

>For example, the label of Node1 is: NodeType = S1.SMALL1, the label of Node2 is NodeType = S1.SMALL2, and the label of Node 3 is NodeType =  S1.MEDIUM2. If the parameter nodeAffinity is specified as NodeType In S1.SMALL1 when you create a service, the container of the service is scheduled under Node1.

`podAffinity` is described as follows:

| Field | Description | Type |
|---------|---------|---------|
| key | The key of the Label used to specify Pod affinity | String | 
| operator | Affinity operator, including In, NotIn, Exists, DoesNotExist | String | 
| values | The value of the Label used to specify Pod affinity | String Array |

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input
```
  https://domain/v2/index.php?Action=ModifyClusterService
  ------------Basic Parameters----------
  &clusterId=cls-xxxxx
  &serviceName=my-web-service
  &replicas=1
  &strategy=Recreate
  &minReadySeconds=1
  ------------Port Mapping------------
  &accessType=LoadBalancer
  &portMappings.0.protocol=TCP
  &portMappings.0.containerPort=80
  &portMappings.0.lbPort=80
  &portMappings.0.nodePort=0
  ------------Data Volume------------
  &volumes.0.name=vol
  &volumes.0.hostPath=
  &volumes.0.volumeType=hostPath
  ------------Container-related------------
  &containers.0.containerName=test
  &containers.0.image=nginx
  ------------Resource Limit------------
  &containers.0.cpu=200
  &containers.0.cpuLimits=300
  &containers.0.memory=128
  ------------Environment Variable------------
  &containers.0.envs.0.name=envkey1
  &containers.0.envs.0.value=envval1
  ------------Mount Point------------
  &containers.0.volumeMounts.0.volumeName=vol
  &containers.0.volumeMounts.0.mountPath=/data
  &containers.0.volumeMounts.0.mode=rw
  ------------Health Check------------
  &containers.0.healthCheck.0.type=liveCheck
  &containers.0.healthCheck.0.checkMethod=methodHttp
  &containers.0.healthCheck.0.port=80
  &containers.0.healthCheck.0.protocol=HTTP
  &containers.0.healthCheck.0.path=/
  &containers.0.healthCheck.0.cmd=
  &containers.0.healthCheck.0.delayTime=0
  &containers.0.healthCheck.0.timeOut=2
  &containers.0.healthCheck.0.intervalTime=3
  &containers.0.healthCheck.0.healthNum=1
  &containers.0.healthCheck.0.unhealthNum=3
  ------------nodeAffinity------------
  &nodeAffinity.0.key=qcloud
  &nodeAffinity.0.operator=In
  &nodeAffinity.0.values.0=my-app
  ------------podAffinity------------
  &podAffinity.0.key=qcloud
  &podAffinity.0.operator=In
  &podAffinity.0.values.0=my-app
  &Other Common Parameters
```
Output
```
  {
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```

