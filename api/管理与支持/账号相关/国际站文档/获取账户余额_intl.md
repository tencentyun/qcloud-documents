## 1. API Description
This API (DescribeAccountBalance) is used to obtain cloud account information.

Domain Name: trade.api.qcloud.com

 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> null
<td> --
<td> --
<td> --
</tbody></table>

 

## 3. Output Parameters 
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0: Successful; other values: Failed. 
<tr>
<td> message
<td> String
<td> Error message 
<tr>
<td> balanceInfo
<td> Int 
<td> The "Show available balance" field in the cloud account information (in cent) 
</tbody></table>

 

## 4. Example 
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeAccountBalance
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>
</pre>


Output
```
  {
      "code":0,
      "message": "success",
      "balanceInfo":12345
  }
```

