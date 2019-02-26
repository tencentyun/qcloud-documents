## 1. API Description 
Domain: vpc.api.qcloud.com<br>
API name: DescribeVpcLimit<br>

This API is used to query VPC service limits.

## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> type.n <td> Yes <td> String <td> VPC type
</tbody></table>


## 3. Output Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code. 0: Succeeded; other values: Failed
<tr>
<td> message <td> String <td> Error message
<tr>
<td> data <td> Array <td> Returned array
</tbody></table>

**Data Array Structure**

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.limit <td> Array <td> Restriction information
</tbody></table>

## 4. Example 
Input

<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcLimit
&type.0=1
&type.1=2
&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>


Output

```
{
    "code": 0,
    "message": "",
    "data": {
        "limit": {
            "1": 10,
            "2": 10
        }
    }
}
```
