## 1. API Description
 
This API (DescribeClusterServiceInfo) is used to query the details of a single service.

Domain for API request: ccs.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| serviceName   | Yes    | String | Service name |
| namespace      | No | String      | Namespace. Default is "default" |

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API |
| service | Object Array | Service list. Details are shown below |

``service`` parameter details

| Parameter Name | Type | Description |
|---------|---------|---------|
| serviceName | String | Service name |
| serviceDesc | String | Service description |
| externalIp | String | Public access IP for the service. If the service access type is specified as load balancer upon service creation, a load balancer will be created for the service in which case this IP is the load balancer IP |
| accessType | String | Service access type. <br>LoadBalancer: this creates a public network load balancer for the service. Traffic is forwarded to the service when you access the IP and port of this load balancer. <br>NodePort: this opens a port on every Node in the cluster. Traffic is forwarded to this service when you access the IPs and ports for any of these Nodes. <br>SvcLBTypeInner: this creates a private network load balancer and occupies an IP under the subnet (you need to specify subnetId). <br>Empty: The service does not provide external access by default. Only other services within the cluster can access the service |
| createdAt | String | Creation time of service |
| currentReplicas | Int | Number of running pod replicas |
| desiredReplicas | Int | Number of pod replicas that are expected to run. This is specified when creating the service |
| lbId | String | Corresponding public Lb ID of the service. This is only created if the service is specified to access the Internet upon creation |
| lbStatus | String | Public network load balancer status. Possible values are: None (the service has no Internet load balancer), Creating (load balancer is being created) and Running (load balancer is running) |
| portMappings | Object Array | Port related information. See the following table for details about the fields in the object |
| status | String | Service status. See the table below for detailed description |
| reasonMap | map[string]int | A set containing the reasons for why the service is in the current status. The map key is reason, while the map value is the number of containers with the same reason. Suppose a pair of key and value: {"Failed to download image":2}, this means two containers failed to download image |
| labels | Map | Service tag list |
| volumes | Object Array | Service volume. See the volume definition below for detailed definitions |
| containers | Object | Service container list |
| serviceIp | String | VIP used to access the service within the cluster |
| namespace | String | Namespace |


``status`` details

| Status Type | Description |
|---------|---------|
| Normal | Running |
| Abnormal | Service exception, such as container failed to launch |
| Waiting | Service waiting, such as container is currently downloading image |
| Paused | Update paused. This status occurs if the user pauses update operation in the middle of service update |
| Updating | Service updating |
| RollingBack | Service rolling back |

``portMappings`` parameter details

| Parameter Name | Type | Description |
|---------|---------|---------|
| nodePort | Int | Port opened on the node |
| lbPort | Int | If accessType is LoadBalancer or SvcLBTypeInner, this is the listening port of the load balancer and the service.<br> If accessType is NodePort or ClusterIP, this is the listening port of the service |
| containerPort | Int | Container listening port |
| protocol | String | Protocol (TCP or UDP) |

For detailed definition of volumes, please see [Mounting Data Volumes](https://cloud.tencent.com/document/product/457/9112)

| Parameter Name | Type | Description |
|---------|---------|---------|
| name   | String      | Container volume name |
| hostPath  | String | Container volume directory on the Node. This directory will be mounted to the container when the container launches. If this field is left empty, a temporary directory will be created on the Node for the container volume and deleted when the container is terminated. This directory and the data in it are retained if hostPath is specified |

Container information

| Parameter Name | Type | Description |
|---------|---------|---------|
| containerName | String | Container name which is usually the same with service name |
| image | String | Container image |
| envs | Object Array | Container environment variable. For more information, please see the table below |
| volumeMounts | Object Array | Container volume. For more information, please see the table below |
| cpu | Int | CPU resource required for the container. Unit: mU (0.001 core) |
| cpuLimits  |  Int | Maximum CPU resource available for the container. Unit: mU (0.001 core) |
| memory | Int | Maximum memory available for the container. Unit: MiB |
| command | String | Startup command for the container. <br>For more information, please see [Service Operation Commands and Parameter Configurations](https://cloud.tencent.com/document/product/457/9100) |
| arguments | String Array | Startup parameters for the container. <br>For more information, please see [Service Operation Commands and Parameter Configurations](https://cloud.tencent.com/document/product/457/9100) |
| liveProbe | Object | Container liveness check information. For more information, please see the table below |
| readyProbe | Object | Container readiness check information. Definition is the same with liveProbe, see the table below |

``envs`` parameter details

| Parameter Name | Type | Description |
|---------|---------|---------|
| name | String | Environment variable name |
| value | String | Environment variable value |

``volumeMounts`` parameter details. For more information, please see [Data Volume Mounting Instruction](https://cloud.tencent.com/document/product/457/9112).

| Parameter Name | Type | Description |
|---------|---------|---------|
| volumeName | String | Volume name |
| mountPath | String | Path to which the volume is to be mounted in the container |
| mode | String | Indicates how container accesses the volume. ro: read only. rw: read and write |

Details of ``liveProbe`` and ``readyProbe`` parameters. For more information, please see [Service Health Check Configurations](https://cloud.tencent.com/document/product/457/9094)

| Parameter Name       | Type   |Description                                                                                                                                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| checkMethod    | String  | Type of the check (methodTcp, methodHttp, methodCmd) |
| healthNum    | Int     | Success threshold for the check, default is 3. it means the container is considered to be alive if the check succeeds for this number of times consecutively. For example, if ``type`` is ``liveCheck``, ``healthNum`` is 3, then the container is considered alive if the check returns successful result for 3 times in a row   |
| unhealthNum  | Int    | Failure threshold for the check, default is 3. It means the container is considered to be dead if the check fails for this number of times consecutively. For example, if ``type`` is ``liveCheck``, ``unhealthNum`` is 3, then the container is considered dead if the check returns failed result for 3 times in a row |
| intervalTime | Int    | Interval time between health checks, that is, the time until the next health check. Unit: second |
| timeOut      | Int    | Operation timeout for health checks. Unit: second  |
| delayTime    | Int    | After the container starts up, the time to wait before enabling health check (in second). Default is 0 (enable immediately). Note: If ``type`` is ``readyCheck``, the container is considered unready within the delayTime period after it launches, during which requests are not forwarded to this container when you access the corresponding service  |
| methodTcp      | Object  | Valid when ``checkMethod`` is ``methodTcp``. For more information, please see the table below |
| methodHttp     | Object  | Valid when ``checkMethod`` is ``methodHttp``. For more information, please see the table below |
| methodCmd     | Object  | Valid when ``checkMethod`` is ``methodCmd``. For more information, please see the table below |

``methodTcp`` parameter details

| Parameter Name        | Type   |Description                                                                                                                                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port    | Int  | Connection probe will be performed towards this container port during check operation. The probe is considered successful if connection is successful, or considered as failed otherwise.  |

``methodHttp`` parameter details

| Parameter Name       | Type   |Description                                                                                                                                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port         | Int     | HTTP service port of the container. When sending HTTP or HTTPS requests to this port, the probe is considered successful if the returned httpcode falls within 200-399, or considered as failed otherwise |
| protocol     | String | Protocol used when performing HTTP probe against the container. Only HTTP and HTTPS are supported |
| path         | String | A URL is created when performing HTTP probe against the container: protocol://containerIp:port/path, the probe is then executed by initiating a GET operation towards this URL. ``protocol`` and ``port` are the parameters specified above |

``methodCmd`` parameter details

| Parameter Name        | Type   |Description                                                                                                                                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cmd          | String | Valid when ``checkMethod`` is ``methodCmd``. The probe operation is performed by executing the command ``cmd`` against the container. The probe is then considered successful if the returned result is 0, or considered as failed otherwise.    |


## 4. Example

Input

```
  https://domain/v2/index.php?Action=DescribeClusterServiceInfo
  &clusterName=test-cluster
  &serviceName="simon"
  &Other common parameters
```

Output

```
{
    "returnCode": 0,
    "returnMsg": "ok",
    "data": {
        "service": {
            "serviceName": "xxx",
            "serviceDesc": "des",
            "status": "Waiting",
            "reasonMap": { 
                   "Failed to download image" : 1
             },
            "reason": "ImagePullBackOff",
            "regionId": 1,
            "desiredReplicas": 1,
            "currentReplicas": 0,
            "lbId": "",
			"lbStatus":"None",
            "createdAt": "2016-12-08 12:44:21",
            "accessType": "LoadBalancer",
            "serviceIp": "100.71.0.60",
            "externalIp": "",
			"namespace": "default",
            "portMappings": [
                {
                    "containerPort": 100,
                    "lbPort": 900,
                    "nodePort": 32191,
                    "protocol": "TCP"
                }
            ],
            "containers": [
                {
                    "name": "",
                    "image": "nginx",
                    "envs": null,
                    "volumeMounts": null,
                    "liveProbe": null,
                    "readyProbe": null,
                    "cpu": 0,
                    "memory": 0,
                    "command": "",
                    "arguments": null
                }
            ],
            "selector": {
                "qcloud-app": "xxx"
            },
            "labels": {
                "qcloud-app": "xxx"
            }
        }
    }
}

```
