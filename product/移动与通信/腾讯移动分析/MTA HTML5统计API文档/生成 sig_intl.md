### Algorithm for Generating sig
Both sides maintain the same private key. When initiating requests, the initiator (partner) sorts the parameter arrays of current requests based on the key value, and join 'key=value' at the end of the encrypted string for MD5 encoding. The receiver (H5 Light App Tracking) processes requests with ts equal to or less than 30 minutes using the same method. It is valid when sig is consistent, otherwise it fails. The following shows an example of algorithm for generating sig of php:

```
$secret_key = '3023IU&^_W(5#@';
ksort($params);
foreach ($params as $key => $value) {
$secret_key.= $key.'='.$value;
}
$sign = md5($secret_key);
return $sign;
```

| Field | Meaning | 
|---------|---------|
| $params | Parameter array of all requests |
| key | Parameter name |
| value | Value |
| secret_key | The secret_key returned for each App when it is registered successfully |


### Response Parameters

| Field | Meaning | 
|---------|---------|
| code | Returned code | 
| v2 | The current version number of API | 
| class | API class | 

### Example of Returned Code

**Successful**

```
{
    code:0,
    info:"success",
  -data:{
          -20160921:{
                  pv:"100492539",
                  uv:"8227032",
                  vv:"67535349",
                  iv:"9826284"
          }
      }
}
```
**Failed**

```
{
    code:60002,
    info:"wrong sign",
    data:[]
}
```

