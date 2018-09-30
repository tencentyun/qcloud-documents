You can write an SCF to implement Web backend services and provide these services externally through the API gateway. The API gateway passes the content of the API request as parameters to the SCF, and sends the returned result from the function back to requester as the API response.

The API gateway trigger has the following features:

- **Push model**: When the API gateway receives an API request, the SCF will be triggered if it is configured on the backend of the API gateway. Meanwhile, the API gateway encapsulates the API request's information (such as the specific service receiving the request and API rules, the actual path of the request, the request method, the path, header and query of the request) as the request input parameters, and send it to the triggered function in the form of input parameter event.
- **Synchronous call**: The API gateway synchronously calls the function, and waits for the response of the function until the timeout set in the API gateway occurs. For more information about call types, please see [Call Types](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Configuration of the API Gateway Trigger

The API gateway trigger is configured in the API gateway **instead of the SCF**. When you configure API rules in the API gateway, select Cloud Function for the backend configuration, and then you can select the SCF that shares the same region with the API service.

When the SCF is configured in the API gateway, the timeout is also configured. The request timeout in the API gateway and the SCF execution timeout take effect respectively, as described below:
* API gateway timeout > SCF timeout: SCF timeout takes effect first. A response of 200 HTTP code is returned with an error code indicating that the SCF has timed out.
* API gateway timeout < SCF timeout: API gateway timeout takes effect first. A response of 5xx HTTP code is returned, indicating that the request has timed out.

## Binding Limits on API Gateway Trigger
 
In the API gateway, an API rule can only be bound to an SCF, but an SCF can be bound with multiple API rules as the backend. Besides, the API gateway trigger can only be bound to SCFs in the same region, i.e., those created in the Guangzhou region. These SCFs can only be bound to and triggered by the rules of the API services created in the Guangzhou region. To trigger an SCF with API gateway configuration in the specified region, you can create a function in this region.

## Event Message Structure of API Gateway Trigger

When receiving a request, the API gateway sends the following event data in JSON format to the bound SCF.

```
{
  "requestContext": {
    "serviceName": "testsvc",
    "path": "/test/{path}",
    "httpMethod": "POST",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  "headers": {
    "Accept-Language": "en-US,en,cn",
    "Accept": "text/html,application/xml,application/json",
    "Host": "service-3ei3tii4-251000691.ap-guangzhou.apigateway.myqloud.com",
    "User-Agent": "User Agent String"
  },
  "body": "{\"test\":\"body\"}",
  "pathParameters": {
    "path": "value"
  },
  "queryStringParameters": {
    "foo": "bar"
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  "stageVariables": {
    "stage": "test"
  },
  "path": "/test/value",
  "query": "foo=bar&bob=alice",
  "httpMethod": "POST"
}
```


The data structure is described as follows:

| Name | Content |
| ---------- | --- |
| requestContext | The configuration information of the API gateway sending the request, request ID, verification information and source information. serviceName, path and httpMethod represent the API gateway service, the request path and method of the API, respectively. stage represents the environment where the request source API is located. requestId represents the unique ID of the current request. identity represents user's verification method and the information to be verified. sourceIp represents the request source IP. |
| path       | Records the full path for the actual request |
| httpMethod | Records the HTTP method for the actual request |
| query | Records the full Query for the actual request |
| body | Records the full Body for the actual request |
| headers | Records the full Header for the actual request |
| pathParameters | Records the parameter path configured in the API gateway and its actual value |
| queryStringParameters | Records the parameter Query configured in the API gateway and its actual value |
| headerParameters | Records the parameter Header configured in the API gateway and its actual value |

```
Note:
1. As the API gateway iterates, more parameters will be added to requestContext. Parameters in the data structure will be increased only rather than being deleted to avoid data corruption.
2. Parameters in the actual request may appear in multiple locations and can be selected based on business needs.
```

## How Does the API Gateway Trigger Process the Response of SCF

Since the SCF is called synchronously, the API gateway triggers the SCF until it is successfully executed, and then sends the returned result from SCF to the API request initiator as the API response. Therefore, the SCF can be used to implement API backend services. It processes the API request and returns the result which will then be sent to the API requester.

