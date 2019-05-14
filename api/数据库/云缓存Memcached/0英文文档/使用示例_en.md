This section provides an example about how to query the cloud Memcached instance list.
## Query CMEM Instance List
Related parameters are as follows:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> limit <td> No <td> Int <td> Page size. Its default value is 20 and the maximum 100.
<tr>
<td> offset <td> No <td> Int <td> Offset. The default is 0.
<tr>
<td> vpcId <td> No <td> Int <td> VPC network ID. Its optional values are -1, 0 and normal vpcId, where -1 indicates all networks and 0 indicates basic network.
<tr>
<td> subnetId <td> No <td> Int <td> VPC subnet ID. The default value is -1, which means that this parameter is ignored.
</tbody></table>

By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://cmem.api.qcloud.com/v2/index.php?
offset=0
&limit=2
&Action=DescribeCmem
&Region=gz
&SecretId=AKIDFdc8BcVIW3iE1Z40dQXABoyFzx1jikES
&Nonce=57667
&Timestamp=1467277471
&RequestClient=SDK_PHP_1.1
&Signature=SAM%2FX6QOCR4RD4H28%2BvyGkwtR8A%3D
```
The result of the above request is as follows, including two CMEM instances.

```
{
    "code": 0,
    "message": "",
    "totalCount": 8,
    "data": [
        {
            "cmemId": 104017777,
            "cmemName": "1111",
            "expire": 1,
            "status": 1,
            "autoRenew": 0,
            "wanIp": "10.66.107.102",
            "port": 9101,
            "projectId": 0
        },
        {
            "cmemId": 104017815,
            "cmemName": "cmem119199",
            "expire": 0,
            "status": 1,
            "autoRenew": 0,
            "wanIp": "10.66.150.210",
            "port": 9101,
            "projectId": 0
        }
    ]
}
```
