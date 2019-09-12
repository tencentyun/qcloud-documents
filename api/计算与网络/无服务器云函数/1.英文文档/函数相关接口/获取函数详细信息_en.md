## 1. API Description
This API is used to acquire the details of a certain function, including its name, code, handling method, associated triggers, timeout and other fields.     

Domain name for API access: scf.api.qcloud.com
## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetFunction.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the function whose details are to be acquired. |
| code | No | Int | 0: The code field is not included in the returned details. 1: The code field is included in the returned details. Default is 0. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| data | String | JSON data which contains function information, such as trigger name, runtime memorySize, entry point function, function description, version number, code size, code and so on. |

Apart from certain fields such as function description upon creation, handler name and runtime memory size, the "data" field also contains the list of triggers that are associated with this function. Data structure for each trigger entry is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| modtime | String | The last time when the trigger was modified. |
| type | String | Trigger type. Two types are currently supported: cos and timer. |
| triggerDesc | String | Trigger parameter. For a timer trigger, this field is the cron expression; for a COS trigger, this field is the COS trigger event. |
| triggerName | String | Trigger name |
| addtime | String | The time when the trigger was bound to the function. |

## 4. Example

#### When Code is not returned

Input
```
https://scf.api.qcloud.com/v2/index.php?Action=GetFunction
&<Common request parameters>
&functionName=helljin89
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "modTime": "2017-05-18 16:38:38",
        "functionName": "helljin89",
        "triggers": [
            {
                "modTime": "2017-05-18 17:28:36",
                "type": "timer",
                "triggerDesc": {
                    "cron": "*/1 * * * *"
                },
                "triggerName": "abc",
                "addTime": "2017-05-18 17:28:36"
            }
        ],
        "handler": "lambda_function.lambda_function",
        "codeSize": 3225,
        "memorySize": 128,
        "version": "LATEST",
        "timeout": 300,
        "description": "abc\nefg"
    }
}

```
#### When Code is returned

Input
```
https://scf.api.qcloud.com/v2/index.php?Action=GetFunction
&<Common request parameters>
&functionName=helljin89
&code=1
```
Output:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "modTime": "2017-05-18 16:38:38",
        "codeError": "",
        "code": "import mymath.myadd as myadd\nimport mymath.mysub as mysub\nimport mymath.test.mymultiply as mymultiply\nimport json\nimport os\n\ndef lambda_function(event, context):\n    a = event['a']\n    b = event['b']\n    print \"+\", myadd.myadd(a, b)\n    print \"-\", mysub.mysub(a, b)\n    print \"*\", mymultiply.mymult(a, b)\n    return \"hello\"\n\n",
        "description": "abc\nefg",
        "triggers": [
            {
                "modTime": "2017-05-18 17:28:36",
                "type": "timer",
                "triggerDesc": {
                    "cron": "*/1 * * * *"
                },
                "triggerName": "abc",
                "addTime": "2017-05-18 17:28:36"
            }
        ],
        "handler": "lambda_function.lambda_function",
        "codeSize": 3225,
        "memorySize": 128,
        "timeout": 300,
        "version": "LATEST",
        "codeResult": "success",
        "functionName": "helljin89"
    }
}
```

