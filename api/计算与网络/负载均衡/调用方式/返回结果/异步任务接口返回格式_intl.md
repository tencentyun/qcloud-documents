## Format of Returned Results for Common Asynchronous Task APIs
With such asynchronous task APIs, only one resource can be operated for each request, for example, creating load balancer or resetting OS for server.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code on the result. 0: Successful; other values: Failed.
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message on the result.
</td></tr>
<tr>
<td> requestId
</td><td> String
</td><td> Task ID
</td></tr></tbody></table>

## Format of Returned Results for Batch Asynchronous Task APIs
With such asynchronous task APIs, multiple resources can be operated for each request, for example, changing passwords, starting or shutting down servers.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code on the result. 0: Successful; other values: Failed.
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message on the result.
</td></tr>
<tr>
<td> detail
</td><td> Array
</td><td> The code, message, and requestId returned for an operation performed on the resource with the resource ID as key.
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
>**Note:**
If the operations are successful for all resources, the outermost code is 0.
If the operations fail for all resources, the outermost code returns 5100.
If the operations fail for some resources, the outermost code returns 5400.
In the third case, the terminal can obtain the information about the failed operations via "detail" field.

