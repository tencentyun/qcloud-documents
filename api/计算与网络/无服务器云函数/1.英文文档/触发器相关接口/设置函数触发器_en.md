## 1. API Description
This API is used to create or modify function trigger. Two trigger types are currently supported: cos and timer. Each function can have a maximum of 2 timer triggers and 2 COS triggers.

Domain name for API access: scf.api.qcloud.com

## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is SetTrigger.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the function to which the newly created trigger is bound. |
| triggerName | Yes | String | Name of the created trigger. For a timer trigger, the name can contain letters, numbers, en dashes (-) and underscores, up to 100 characters. For a COS trigger, the name must be in the format of `<bucketName>-<UID>.<Region>.myqcloud.com |
| type | Yes | String | Trigger type. Two types are currently supported: cos and timer. |
| triggerDesc | Yes | String | Trigger parameter. For a timer trigger, this is Linux cron expression; for a COS trigger, this is JSON data `{"event": "cos:ObjectCreated:*"}`. |
| newTriggerName | No | String | This parameter is used when you update the name of a timer trigger. The new name may contain letters, numbers, en dashes (-) and underscores, up to 100 characters. |

**Note**:

- An account can have at most 20 functions in a region, and each function can have up to 2 timer triggers and 2 COS triggers.
- A bucket can only be bound with triggers in the same region. You cannot bind bucket with triggers in different regions.
- When using a COS trigger, if you need to save function execution result to the bucket, it is recommended that you configure two different buckets, one for trigger source, one for the output result, in order to prevent function from running continuously due to circular dependency.
- Update is not supported for COS triggers.
- Name format for COS triggers should always be: `<bucketName>-<UID>.<Region>.myqcloud.com`.
- For COS triggers, you need to pass JSON data containing the following contents for triggerDesc:
```
{
    "event": "cos:ObjectCreated:*"
}
```

Currently supported event values are listed in the table below. There are certain restrictions when you bind COS event to a specific trigger:

1. If you bind the `cos:ObjectCreated:\*` event first, all subsequent operations to bind events that start with `cos:ObjectCreated` will fail.
2. If you bind an event that starts with `cos:ObjectCreated` (except `cos:ObjectCreated:\*`), subsequent operations to bind the `cos:ObjectCreated:\*` event will fail.
3. If you bind the `cos:ObjectRemove:\*` event first, all subsequent operations to bind events that start with `cos:ObjectRemove` will fail.
4. If you bind an event that starts with `cos:ObjectRemove` (except `cos:ObjectRemove:\*`), subsequent operations to bind the `cos:ObjectRemove:\*` event will fail.
5. If COS is already bound, operations to create COS triggers will fail.
6. You cannot update the names for COS triggers.


| Event | Description |
|--------|-------|
| cos:ObjectCreated:Put | Use the Put Object API to create file. |
| cos:ObjectCreated:Post | Use the Post Object API to create file. |
| cos:ObjectCreated:Copy | Use the Put Object - Copy API to create file. |
| cos:ObjectCreated:Append | Use the Append Object API to create file. |
| cos:ObjectCreated:CompleteMultipartUpload | Use the CompleteMultipartUploadt API to create file. |
| cos:ObjectCreated:* | Use "ObjectCreated" APIs mentioned above to create file. |
| cos:ObjectRemove:Delete | Use the Delete Object API to delete Object under a Bucket that doesn't have version management enabled, or use versionid to delete Object of specified version. |
| cos:ObjectRemove:DeleteMarkerCreated | Use the Delete Object API to delete Object under a Bucket that has version management enabled or paused. |
| cos:ObjectRemove:* |Use "ObjectRemove" APIs mentioned above to delete file. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
## 4. Example
#### Configure Timer Trigger

Input
```
https://scf.api.qcloud.com/v2/index.php?Action=SetTrigger
&<Common request parameters>
&functionName=hell
&triggerName=test1
&type=timer
&triggerDesc=*/2 * * * *
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

#### Configure COS Trigger

Input
```
https://scf.api.qcloud.com/v2/index.php?Action=SetTrigger
&<Common request parameters>
&functionName=hell
&triggerName=lambdatest3-1251664966.cn-south.myqcloud.com
&type=cos
&triggerDesc={"event": "cos:ObjectCreated:Put"}
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

