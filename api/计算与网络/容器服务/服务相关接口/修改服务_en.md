Parameter Name## 1. API Description
 
This API (ModifyClusterService) is used to modify service.

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).
**Note: The parameters for modifying service are the same with those for creating service, except for "strategy" and "minReadySeconds". You need to pass all service parameters when modifying the service, including the new service parameters that are identical with their original counterparts. If you only wish to adjust the number of replicas or the description of the service, use our APIs designed for such actions.** 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
| serviceName   | Yes | String       | Service name |
| serviceDesc   | No | String       | Service description |
| replicas      | Yes | Int          | Number of instance replicas |
| strategy      | Yes | String       | Service update strategy (Recreate or RollingUpdate). The Recreate method kills all containers under the service before service update, then recreate the containers based on the new parameters. The RollingUpdate method performs rolling update on the containers: First, kill some of the containers and create some new containers based on the new parameters. When the new containers are successfully launched, kill old containers and create new ones, until all new containers are successfully creates and all old containers are killed, achieving a gated launching process. |
| minReadySeconds | No | Int         | In second. This is the time to wait before launching the next new container when using RollingUpdate method. For example, if minReadySeconds is set to 10, the cluster will first launch a new container, and wait for 10 seconds before launching another new container, after the previous one is successfully launched. This is done until the number of new containers reaches the number of replicas. |
| accessType    | No | String | Service access type. <br>LoadBalancer: this creates a public network load balancer for the service. Traffic is forwarded to the service when you access the IP and port of this load balancer. <br>NodePort: this opens a port on every Node in the cluster. Traffic is forwarded to this service when you access the IPs and ports for any of these Nodes. <br>SvcLBTypeInner: this creates a private network load balancer and occupies an IP under the subnet (you need to specify subnetId). <br>ClusterIP: The service does not provide external access. Only the other services within the cluster can access the service. Default is ClusterIP |
| portMappings.n | No | Object Array | Port mapping information. This is required if the container needs network access | 
| volumes.n     | No | Object Array | Container volume definition | 
| labels.n      | No | Object Array | Service tag |
| containers.n  | Yes | Object Array | Container array. You need to define at least one container for a service, the defined containers are launched upon service creation |
| namespace      | No | String      | Namespace. Default is "default" |
| subnetId     | No | String      | Subnet ID. Enter the unSubnetId (unified subnet ID) returned when calling the API [Query Subnet List](https://www.qcloud.com/document/api/215/1371). This is mandatory if "accessType" is "SvcLBTypeInner" |

"portMappings" parameter details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| lbPort | Yes | Int | If accessType is LoadBalancer or SvcLBTypeInner, this is the listening port of the load balancer and the service.<br> If accessType is NodePort or ClusterIP, this is the listening port of the service |
| containerPort | Yes | Int | Container listening port |
| nodePort | No | Int | Port opened on the node when accessType is NodePort, LoadBalancer or SvcLBTypeInner. The system assigns a nodePort by default if this is left empty |
| protocol | Yes | String | Protocol (TCP or UDP) |

"volumes" parameter details. For more information, please see [Mounting Data Volumes](https://www.qcloud.com/document/product/457/9112).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|
| name   | Yes | String      | Container volume name |
| volumeType   | Yes | String      | Container volume type. Currently hostPath and cbsDisk are supported. **Note: For cbsDisk, the number of service instances must be 1, because cbs disk does not support mounting multiple nodes at the same time** |
| hostPath  | No | String   | This is required when volumeType is hostPath. Container volume directory on the host. This directory will be mapped to the container when the container launches. If this field is left empty, a temporary directory will be created on the Node for the container volume and deleted when the container is terminated. This directory and the data in it are retained if hostPath is specified |
| cbsDiskId | No | String | This is required when volumeType is cbsDisk. This is the ID of cbs network disk. This cbs disk is mounted to the host where the container resides and mapped to the container when the container launches, and unmounted from the host when the container is terminated. Enter the storageId (cloud disk ID) field returned when calling the API [Query Cloud Disk Information](https://www.qcloud.com/document/api/362/2519) |

"labels" parameter details

| Parameter Name | Type | Description       |
|------|------|-----------|
| key   | String | Tag key  |
| value | String | Tag value |

"containers" parameter details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------
| containerName | Yes | String | Container name |
| image  | Yes | String | Container image |
| envs.n | No | Object Array | Container environment variable array. For more information, please see the definition of envs |
| volumeMounts.n | No | Object Array | Container volume mount point. For more information, please see the definition of volumeMounts |
| healthCheck.n | No | Object Array | Container health check. For more information, please see the definition of healthCheck |
| cpu | No | Int | CPU resource required for the container. Unit: mU (0.001 core), minimum is 100 (0.1 core).<br>0 or empty value means no restriction<br>For more information, please see [Configuring Service Resource Limits](https://www.qcloud.com/document/product/457/9099) |
| cpuLimits  | No | Int | Maximum CPU resource available for the container. Unit: mU (0.001 core), minimum is 100 (0.1 core).<br>0 or empty value means no restriction, and a value greater than 0 must be no less than the value of "cpu"<br>For more information, please see [Configuring Service Resource Limits](https://www.qcloud.com/document/product/457/9099) |
| memory | No | Int |Maximum memory available for the container (in MiB). It is recommended to choose a value no less than 4 MiB.<br>0 or empty value means no restriction, and the required memory equals to maximum available memory by default<br>For more information, please see [Configuring Service Resource Limits](https://www.qcloud.com/document/product/457/9099) |
| command | No | String | Startup command for the container. <br>For more information, please see [Service Operation Commands and Parameter Configurations](https://www.qcloud.com/document/product/457/9100) |
| arguments.n | No | String Array | Startup parameter for the container. <br>For more information, please see [Service Operation Commands and Parameter Configurations](https://www.qcloud.com/document/product/457/9100) |

"envs" parameter details

| Parameter Name | Type | Description |
|---------|---------|---------|
| name | String | Environment variable name |
| value | String | Environment variable value |

"volumeMounts" parameter details. For more information, please see [Data Volume Mounting Instruction](https://www.qcloud.com/document/product/457/9112).

| Parameter Name | Type | Description |
|---------|---------|---------|
| volumeName | String | Volume name. This must be a name defined in the parameters in the "volumes" mentioned above |
| mountPath | String | Volume mount point in the container |
| mode | String | Indicates how container accesses the volume. ro: read only. rw: read and write |

"healthCheck" parameter details. For more information, please see [Service Health Check Settings](https://www.qcloud.com/document/product/457/9094).

| Parameter Name | Type | Description |
|---------|---------|---------|
| type         | String | Value is liveCheck or readyCheck. liveCheck is used to check if the container is alive. Container is restarted if the check fails. readyCheck is used to check if the container is ready, and request forwarding towards the container will be stopped if the check fails |
| healthNum    | Int    | Success threshold for the check. it means the container is considered to be alive if the check succeeds for this number of times consecutively. For example, if "type" is "liveCheck", "healthNum" is 3, then the container is considered alive if the check returns successful result for 3 times in a row  |
| unhealthNum  | Int    | Failure threshold for the check. it means the container is considered to be dead if the check fails for this number of times consecutively. For example, if "type" is "liveCheck", "unhealthNum" is 3, then the container is considered dead if the check returns failed result for 3 times in a row   |
| intervalTime | Int    | Interval time between health checks, that is, the time until the next health check (in second) |
| timeOut      | Int    | Operation timeout for health checks (in second) |
| delayTime    | Int    | After the container starts up, the time to wait before enabling health check (in second). Default is 0 (enable immediately). Note, if "type" is "readyCheck", the container is considered unready within the delayTime period after it launches, during which requests are not forwarded to this container when you access the corresponding service  |
| checkMethod  | String | Type of the check (methodTcp, methodHttp, methodCmd) | 
| port         | Int    | Port. This is valid when "checkMethod" is "methodTcp" or "methodHttp". If "checkType" is "methodTcp", connection probe will be performed towards this container port during check operation. The probe is considered successful if connection is successful, or considered as failed otherwise. If "checkType" is "methodHttp", an HTTP or HTTPS request will be sent to this container port, the probe is considered successful if the returned httpcode falls within 200-399, or considered as failed otherwise  |
| protocol     | String | Valid when "checkMethod" is "methodHttp". Protocol used when performing HTTP probe against the container. Only HTTP and HTTPS are supported  |
| path         | String | Valid when "checkMethod" is "methodHttp". When HTTP probe is performed on the container, a URL is created: protocol://containerIp:port/path, the probe is then executed by initiating a GET operation towards this URL. "protocol" and "port" are the parameters specified above  |
| cmd          | String | Valid when "checkMethod" is "methodCmd". The probe operation is performed by executing the command "cmd" against the container. The probe is then considered successful if the returned result is 0, or considered as failed otherwise.   | 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API |


## 4. Example

Input

```
  https://domain/v2/index.php?Action=ModifyClusterService
  &clusterId=cls-xxxxx
  &serviceName=my-web-service
  &replicas=5
  &accessType=LoadBalancer
  &portMappings.0.lbPort=80
  &portMappings.0.containerPort=80
  &portMappings.0.protocol=TCP
  &containers.0.name=nginx
  &containers.0.imag=docker.io/nginx
  &namespace=default
  &Other common parameters
```

Output

```
  {
    "code": 0,
    "message": "", 
}

```
