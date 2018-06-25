## 1. API Description
 
This API (DescribeAllClass) is used to acquire all category class relationships of the current user.

Domain:  vod.api.qcloud.com

 

## 2. Input Parameters
 

None

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0:  Succeeded, other values:  Failed
<tr>
<td> message <td> String <td> Error message
<tr>
<td> data 	<td> Array <td> List of category class relationships of the current user
<tr>
<td> data.info <td> Array <td> Information of the first level category  
<tr>
<td> data.subclass <td> Array <td> Information of sub-categories under the first level category
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=DescribeAllClass
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": [
        {
            "info": {
                "id": 149,
                "parent_id": -1,
                "name": "Test",
                "level": 0,
                "file_num": 0
            },
            "subclass": [
                {
                    "info": {
                        "id": 213,
                        "parent_id": 149,
                        "name": "New second level category",
                        "level": 1,
                        "file_num": 0
                    },
                    "subclass": []
                },
                {
                    "info": {
                        "id": 215,
                        "parent_id": 149,
                        "name": "New second level category (1)",
                        "level": 1,
                        "file_num": 0
                    },
                    "subclass": []
                }
            ]
        },
    ]
}

```


