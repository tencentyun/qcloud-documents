## 1. 接口描述
本接口(DescribeUserGw)用于查询对端网关。
接口请求域名：<font style='color:red'>vpc.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为DescribeUserGw。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| userGwId | 否 | String | 对端网关ID或者统一ID，建议使用统一ID，例如：cgw-1tb1k34n。 |
| userGwName | 否 | String | 对端网关名称。|
| offset | 否 | Int | 初始行的偏移量，默认为0。|
| limit | 否 | Int | 每页行数，默认为10。|
| orderField | 否 | String | 按某个字段排序，目前支持userGwName和默认按createTime排序，默认按createTime排序。|
| orderDirection | 否 | String | 升序（asc）还是降序（desc）,默认：asc。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| totalCount | Int | 返回结果中对端网关总数量。|
| data.n | Array | 返回的数组。|
| data.userGwName | String | 对端网关名称。| 
| data.userGwId | Int | 系统分配的对端网关ID，例如：400。| 
| data.unUserGwId | String | 系统分配的新的对端网关ID，推荐使用新的对端网关ID，例如：cgw-1tb1k34n。| 
| data.userGwAddr | String | 对端网关公网IP。| 
| data.vpnConnNum | Int | 已链接的通道数量。| 
| data.createTime | String | 创建时间：2016-06-23 11:11:49。| 


 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidUserGw.NotFound | 无效的对端网关。对端网关资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%af%b9%e7%ab%af%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeUserGw">DescribeUserGw</a>接口查询对端网关。 |

## 5. 示例
输入
```
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeUserGw
 &<公共请求参数>
```
输出
```
{
    "code":"0",
    "message":"",
    "totalCount":"20",
    "data":[
        {
            "userGwName":"183.60.249.12",
            "userGwId":"404",
            "unUserGwId":"cgw-1tb1k34n",
            "userGwAddr":"183.60.249.12",
            "vpnConnNum":"1",
            "createTime":"2016-06-23 11:11:49"
        },
        {
            "userGwName":"183.60.249.138",
            "userGwId":"403",
            "unUserGwId":"cgw-mzmzjzf9",
            "userGwAddr":"183.60.249.138",
            "vpnConnNum":"1",
            "createTime":"2016-06-22 21:20:54"
        },
        {
            "userGwName":"SH",
            "userGwId":"402",
            "unUserGwId":"cgw-2530cjg1",
            "userGwAddr":"222.92.194.28",
            "vpnConnNum":"1",
            "createTime":"2016-04-28 14:15:41"
        },
        {
            "userGwName":"183.60.249.126",
            "userGwId":"401",
            "unUserGwId":"cgw-j8pcwzu9",
            "userGwAddr":"183.60.249.126",
            "vpnConnNum":"1",
            "createTime":"2016-04-22 12:18:05"
        },
        {
            "userGwName":"183.60.249.129",
            "userGwId":"400",
            "unUserGwId":"cgw-blr1nrwb",
            "userGwAddr":"183.60.249.129",
            "vpnConnNum":"1",
            "createTime":"2016-04-21 20:47:47"
        },
        {
            "userGwName":"183.60.249.121",
            "userGwId":"399",
            "unUserGwId":"cgw-ov9j6csd",
            "userGwAddr":"183.60.249.121",
            "vpnConnNum":"0",
            "createTime":"2016-04-21 20:47:14"
        },
        {
            "userGwName":"183.60.249.95",
            "userGwId":"397",
            "unUserGwId":"cgw-g013kis9",
            "userGwAddr":"183.60.249.95",
            "vpnConnNum":"0",
            "createTime":"2016-01-23 13:41:35"
        },
        {
            "userGwName":"183.60.249.33",
            "userGwId":"396",
            "unUserGwId":"cgw-c5p3f6fr",
            "userGwAddr":"183.60.249.33",
            "vpnConnNum":"0",
            "createTime":"2016-01-18 17:08:09"
        },
        {
            "userGwName":"115.159.143.150",
            "userGwId":"344",
            "unUserGwId":"cgw-oe7vq0uz",
            "userGwAddr":"115.159.143.150",
            "vpnConnNum":"0",
            "createTime":"2015-11-26 02:30:02"
        },
        {
            "userGwName":"9101",
            "userGwId":"315",
            "unUserGwId":"cgw-e098slul",
            "userGwAddr":"183.60.249.39",
            "vpnConnNum":"0",
            "createTime":"2015-11-06 11:18:53"
        }
    ],
    "codeDesc":"Success"
}
```

