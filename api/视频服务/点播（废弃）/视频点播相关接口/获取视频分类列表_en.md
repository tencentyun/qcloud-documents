## 1. API Description
 
This API (DescribeClass) is used to acquire global category list, including the relationship between ID and category description (not relevant to specific files).

Domain: vod.api.qcloud.com
 

## 2. Input Parameters
 
None

 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=DescribeClass&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
    "data": [
            {
              "id": "0",
              "name": "Others",
              "create_time": "2014-11-27 10:22:37",
              "update_time": "2014-11-27 17:52:13"
            },
            {
              "id": "98",
              "name": "Movie",
              "create_time": "2015-04-08 09:52:20",
              "update_time": "2015-04-08 09:52:20"
            }
   ]
}


```


