## Response for a Successful Request

Take the CVM API "View Instance Status List" (DescribeInstancesStatus) (version 2017-03-12) as an example. If it is successfully called, the possible returned result is as follows:

    {
        "Response": {
            "TotalCount": 0,
            "InstanceStatusSet": [],
            "RequestId": "b5b41468-520d-4192-b42f-595cc34b6c1c"
        }
    }

* The Response and its RequestId are fixed fields, which are always returned as long as the request is processed by the API, regardless of whether it is successful or not.
* RequestId is used to uniquely identify an API request. If an API exception occurs, you can contact us and provide this ID to solve the problem.
* Other fields than the fixed ones are defined for specific APIs. Fields returned by each API can be found in relevant API documentation. In this example, TotalCount and InstanceStatusSet are defined for the API DescribeInstancesStatus. Since there is no CVM instance when the request is initiated, the returned value for TotalCount is 0 and the InstanceStatusSet list is empty.

## Response for a Failed Request

If the call fails, the returned values are as follows:

    {
        "Response": {
            "Error": {
                "Code": "AuthFailure.SignatureFailure",
                "Message": "The provided credentials could not be validated. Please check your signature is correct."
            },
            "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
        }
    }

* Error indicates a failed call. The Error field along with its Code and Message fields are returned if the call fails.
* Code indicates the specific error code. When an error occurs with the request, you can find the cause and solution in the common error codes and the error code list for the current API based on this error code.
* Message indicates the reason for the error, which may be changed or updated from time to time as the business grows or experience improves. Therefore, you should not rely on this returned value.
* RequestId is used to uniquely identify an API request. If an API exception occurs, you can contact us and provide this ID to solve the problem.


## Common Error Codes


If the Error field exists in the returned result, it means the call to the API failed. The Code field in the Error indicates the error code. Common error codes are error codes that may appear in all businesses, as shown below.


| Error Code | Description |
|----------|----------|
| InvalidParameter | Invalid parameter (including incorrect parameter format, type, etc.) |
| InvalidParameterValue | Incorrect parameter value |
| MissingParameter | A required parameter is missing |
| UnknownParameter | Unknown parameter. This error occurs when a user passes an undefined parameter. |
| AuthFailure | CAM signature/authentication failure |
| InternalError | Internal error |
| InvalidAction | API does not exist |
| UnauthorizedOperation | Unauthorized operation |
| RequestLimitExceeded | The number of requests exceeds the frequency limit |
| NoSuchVersion | The API version does not exist |
| UnsupportedRegion | The API does not support the region passed |
| UnsupportedOperation | Operation is not supported |
| ResourceNotFound | Resource does not exist |
| LimitExceeded | Quota exceeded |
| ResourceUnavailable | Unavailable resource |
| ResourceInsufficient | Insufficient resources |
| FailedOperation | Operation failed |
| ResourceInUse | Resource is occupied |
| DryRunOperation | DryRun operation. It means that the request will be successful, but multiple DryRun parameters are passed. |

