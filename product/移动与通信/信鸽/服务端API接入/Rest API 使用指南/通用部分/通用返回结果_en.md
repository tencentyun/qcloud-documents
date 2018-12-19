
```
{
"ret_code":0,
"erroeMsg":"ok"
"result":{"status":0}
}
```

**The fields are defined as follows:**

| Parameter Name | Type | Required | Description |
|-|-|-|-|
| ret_code | Int | Yes | Error code |
| err_msg | String | No | Error message in case of request errors |
| result | Json | No | If the request is correct and some additional data need to be returned, the result is encapsulated in json of the field, and if no, this field may not exist. |
>**Note:** 
>1) Both parameters and values are case-sensitive. Except as otherwise noted, they are all in lowercase.
>2) All K and V must be urlencoded to prevent the resolving from being affected by characters like "&" or "=" in it. 

