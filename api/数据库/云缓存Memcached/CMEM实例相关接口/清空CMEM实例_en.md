## 1. API Description

This API (ClearCmem) is used to clear the CMEM instance.
It can be called from regions of Guangzhou, Shanghai and North America. A single instance can be cleared at maximum 5 times per day.

Domain name: cmem.api.qcloud.com

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> cmemName <td> Yes <td> String <td> Instance name
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: Succeeded, other values: Failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://cmem.api.qcloud.com/v2/index.php?Action=ClearCmem
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &cmemName=9003_TE

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


