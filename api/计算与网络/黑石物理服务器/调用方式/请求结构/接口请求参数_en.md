API request parameters are specific to each API. This means that different APIs support different API request parameters. The first letter of each API request parameter is in lowercase so that the parameters can be differentiated from common request parameters.
Take the [Bind EIP to CPM](/document/product/386/6673) as an example. It supports the following API request parameters:

| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | No | String | EIP instance ID |
| instanceId | No | String | CPM instance ID, which can be obtained from the "unInstanceId" in the returned fields of API [Query CPM](/doc/api/386/6728) |

Here are the descriptions of each field:

| Field | Description |
|---|---|
| Parameter Name | Name of request parameter supported by the API. The user can use this name as an API request parameter when using this API. Name of request parameter supported by the API. The user can use this name as an API request parameter when using this API. |
| Required | Indicates whether this parameter is mandatory. "Yes" means the parameter is mandatory for the API, while "No" means the parameter is not mandatory. |
| Type | Data type of the API parameter. |
| Description | A brief description of the API request parameter. |


If a user wants to bind EIP to CPM, the request link may be as follows:

```
  https://eip.api.qcloud.com/v2/index.php?
  &<Common request parameters>
  &instanceId=cpm-xxxxxx&eipId=eip-vvvvvvv
```

A complete request needs two types of request parameters: common request parameters and API request parameters. Only API request parameters are listed above. For information on common request parameters, please see [Common Request Parameters](/document/product/386/6718) section.
