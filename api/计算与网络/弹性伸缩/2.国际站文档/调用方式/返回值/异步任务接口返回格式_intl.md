## 1. Format of Returned Results for Common Asynchronous Task APIs
You can only operate asynchronous task APIs for one resource in each request, for example, creating load balance or resetting host operating system, and so on.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code of the returned result. 0: Succeed; other values: Failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message of the returned result
</td><td> No
</td></tr>
<tr>
<td> requestId
</td><td> String
</td><td> Task ID
</td><td> Yes
</td></tr></tbody></table>

## 2. Format of Returned Results for Batch Asynchronous Task APIs
You can operate asynchronous task APIs for multiple resources in each request, for example, changing passwords, starting machines, stopping machines, and so on.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code of the returned result. 0: Succeed; other values: Failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message of the returned result
</td><td> No
</td></tr>
<tr>
<td> detail
</td><td> Array
</td><td> The code, message, and requestId of the operation performed on the resource ("key" is resource ID)
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
If all operations performed on the resource succeed, the outermost code will be 0
If all operations performed on the resource fail, the outermost code will be 5100
If part of operations performed on the resource fail, the outermost error code will be 5400
In the third case, the terminal can obtain the information about failed operations by using the detail field.
