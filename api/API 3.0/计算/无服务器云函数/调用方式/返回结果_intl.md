## **Returned Result for Success**

Take viewing the instance status list (DescribeInstancesStatus) version 2017-03-12 through the Cloud Virtual Machine interface as an example. If the call succeeds, the possible returned result is as follows:

    {
        "Response": {
            "TotalCount": 0,
            "InstanceStatusSet": [],
            "RequestId": "b5b41468-520d-4192-b42f-595cc34b6c1c"
        }
    }

* `Response` and its internal `RequestId` are fixed fields and will be returned as long as processed by the API no matter whether the request succeeds.
* `RequestId` is used to uniquely identify an API request. If the API is abnormal, you can contact us and provide the ID for troubleshooting.
* Except for the fixed fields, all the fields are defined by the specific API. For the fields returned by different APIs, see the definitions in the API documentation. In this example, TotalCount and InstanceStatusSet are the fields defined by the DescribeInstancesStatus API. As the user who calls the request does not have a Cloud Virtual Machine instance yet, TotalCount returns a value of 0 in this case and the InstanceStatusSet list is empty.

## **Returned Result for Error**

If the call fails, the returned result may look like the example below:

    {
        "Response": {
            "Error": {
                "Code": "AuthFailure.SignatureFailure",
                "Message": "The provided credentials could not be validated. Please check your signature is correct."
            },
            "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
        }
    }

* The presence of the Error field indicates that the request call failed. The Error field and its internal Code and Message fields, must be returned when the call fails.
* Code indicates the error code of the specific error. When the request goes wrong, you can use this error code to locate the cause and solution in the common error code list and the error code list corresponding to the current API.
* Message shows the specific cause of this error. The message text is subject to change or update as the business develops or the experience gets optimized, so you should not rely on this return value.
* RequestId is used to uniquely identify an API request. If the API is abnormal, you can contact us and provide the ID for troubleshooting.


## **Common Error Codes**


If there is an Error field in the returned result, it means that the API call failed. The Code field in Error indicates the error code. The error codes that may appear for all Tencent Cloud services are common error codes, which are listed below:


| Error code | Error description |
|----------|----------|
| InvalidParameter | Wrong parameter (including errors with parameter format, type, etc.) |
| InvalidParameterValue | Wrong parameter value |
| MissingParameter | Missing parameter; a required parameter is missing |
| UnknownParameter | Unknown parameter; an undefined parameter passed in by the user will cause this error |
| AuthFailure | Error with CAM signature/authentication |
| InternalError | Internal error |
| InvalidAction | API does not exist |
| UnauthorizedOperation | Unauthorized operation |
| RequestLimitExceeded | The number of requests exceeds the frequency limit |
| NoSuchVersion | API version does not exist |
| UnsupportedRegion | API does not support the passing region |
| UnsupportedOperation | Unsupported operation |
| ResourceNotFound | Resource does not exist |
| LimitExceeded | Quota limit is exceeded |
| ResourceUnavailable | Resource not available |
| ResourceInsufficient | Insufficient resource |
| FailedOperation | Operation failed |
| ResourceInUse | Resource is in use |
| DryRunOperation | DryRun operation, which means the request will succeed, but an unnecessary DryRun parameter is passed in |
