## 1. API Description
This API (ModifyClusterServiceImage ) is used to modify service images.
Domain name for API request: `ccs.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. For additional parameters, please see [Common Request Parameters](/doc/api/457/9463) page.

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------|
| clusterId | Cluster ID. Enter the "clusterId" returned when calling the API [Query Cluster List](/doc/api/457/9448) | String | Yes | 
| serviceName | Service name. Enter the "serviceName" returned when calling the API [Query Service List](/doc/api/457/9440) | String | Yes | 
| image | New image. If an instance in the service has only one container, this parameter can be specified. Either "image" or "containers" is required | String | No |
| containers.n | New image. If an instance in the service has multiple containers, this parameter is required to specify the "name" and "image" of the container to be modified. Either "image" or "containers" is required | Object Array | No | 
| namespace | Namespace, Enter the "namespace" returned when calling the API [Query Service List](/doc/api/457/9440). Default is "default" | String | No |

`containers` parameter details:

| Parameter | Description | Type | Required |  
|---------|---------|---------|---------
| containerName| Container name |String | Yes | 
| image | Container image | String | Yes | 

## 3. Output Parameters
 
| Parameter | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned | String |
| message | Module error message description depending on API | String |


## 4. Example
Input
```
  https://domain/v2/index.php?Action=ModifyClusterServiceImage&clusterId=clus-xxxxx
  &serviceName=test
  &containers.0.containerName=test1
  &containers.0.image=nginx:1.0
  &containers.1.containerName=test2
  &containers.1.image=watch:latest
  &other common parameters
```
or
```
  https://domain/v2/index.php?Action=ModifyServiceDescription&clusterId=clus-xxxxx
  &serviceName=test
  &image=nginx:1.0
  &other common parameters
```
Output
```
  {
      "code" : 0,
      "codeDesc": "Success",
      "message" : "ok"
  }

```

