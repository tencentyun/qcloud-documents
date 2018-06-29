Unless otherwise specified, the returned values of each request contain the following fields:

<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th width="50"> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td>Int
</td><td> Error code on the result. 0: Successful; other values: Failed. For more information, please see<a href="https://cloud.tencent.com/document/api/377/4173" title=" the ">Error Codes </a> page.
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Request result
</td></tr></tbody></table>

For example:
Example requests that use common parameters:

```
 https://domain/v2/index.php?Action=DescribeInstances&SecretId=xxxxxxx&Region=gz
 &Timestamp=1402992826&Nonce=345122&Signature=mysignature&instanceId=101
```


 Possible returned result is as follows:

```
{
    "code":0,
    "message": "success",
    "instanceSet":
   [{
        "instanceId":"qcvm1234",
        "cpu":1,
        "mem":2,
        "disk":20,
        "bandwidth":65535,
        "os":"centos_62_64",
        "lanIp":"10.207.248.186",
        "wanIp":null,
        "status":0
   }]
}
```
