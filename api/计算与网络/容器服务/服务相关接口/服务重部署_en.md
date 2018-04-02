## 1. API Description
This API (RedeployClusterService ) is used to redeploy service pods. When images in the image repository change, you can use this API to pull an image again.
Service update strategy when pods are redeployed:
* Service update strategy can be **Recreate** and **RollingUpdate**. For more information, please see the description of "strategy" in the table of input parameters in [Modifying Services](/doc/product/457/9434).
* When instances are redeployed, their update strategy is subject to the update strategy set for the service.
*The default update strategy for a new service is **RollingUpdate** when no changes are made.

Domain name for API request: `ccs.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. For additional parameters, please see [Common Request Parameters](/doc/api/457/9463) page.

| Parameter | Description | Type | Required |  
|---------|---------|---------|---------|
| clusterId | Cluster ID. Enter the "clusterId" returned when calling the API [Query Cluster List](/doc/api/457/9448) | String | Yes |
| serviceName | Service name. Enter the "serviceName" returned when calling the API [Query Service List](/doc/api/457/9440) | String | Yes |
| namespace | Namespace, Enter the "namespace" returned when calling the API [Query Service List](/doc/api/457/9440). Default is "default" | String | No |

## 3. Output Parameters
 
| Parameter | Description | Type |
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed | Int |
| codeDesc | Business error code. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned | String |
| message | Module error message description depending on API | String | 

## 4. Example
Input
```
  https://domain/v2/index.php?Action=RedeployClusterService
  &clusterId=clus-xxxxx
  &serviceName=test
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

