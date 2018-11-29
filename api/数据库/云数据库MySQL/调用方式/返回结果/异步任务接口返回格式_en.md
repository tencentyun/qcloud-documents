## 1. Return format for ordinary asynchronous task APIs
For such asynchronous task APIs, one request operates only one resource, for example creating load balance, resetting the host operating system.
<table class="t">
<tbody><tr>
<th> <b>Name </b>
</th><th><b> Type </b>
</th><th><b> Description </b>
</th><th><b> Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code, 0 for succeeded, other values for failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message returned
</td><td> No
</td></tr>
<tr>
<td> requestId
</td><td> String
</td><td> Task No.
</td><td> Yes
</td></tr></tbody></table>

## 2. Return Format of Batch Asynchronous Task APIs
For such asynchronous task APIs, one request operates multiple resources, for example changing passwords, starting machines, stopping machines.
<table class="t">
<tbody><tr>
<th> <b>Name </b>
</th><th><b> Type </b>
</th><th><b> Description </b>
</th><th><b> Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code, 0 for succeeded, other values for failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message returned
</td><td> No
</td></tr>
<tr>
<td> detail
</td><td> Array
</td><td> The resource ID is used as the key and the code, message, requestId for the resource operation is returned. 
</td><td> Yes
</td></tr></tbody></table>

For example:

```
{
        "code":0,
        "message": "success",
        "detail":
        {
             "qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0":
            {
             "code":0,
             "message":"",
             "requestId":"1231231231231":,
            }
              "qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0":
            {
              "code":0,
              "message":"",
              "requestId":"1231231231232":,
            }
        }
}
```
>Note:
If all resource operations succeeded, the outermost code is 0
If all resource operations failed, the outermost code will be 5100
If some resource operations failed, the outermost code will be 5400
In the third case, the terminal can get information about the failed operations via details.