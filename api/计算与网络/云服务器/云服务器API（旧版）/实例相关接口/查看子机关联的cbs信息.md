>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
域名:cvm.api.qcloud.com
接口名:DescribeInstanceCbsInfo

查看子机关联的cbs信息

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| uInstanceIds.n (uInstanceIds 为列表，此处入参需要填写列表元素 ) | 是 | String | 子机ID列表|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 描述（待补充） |
| data.cbsList | Array | 描述（待补充）| 
| data.cbsList.cbsId | Int | 描述（待补充）| 
| data.cbsList.appId | Int | 描述（待补充）| 
| data.cbsList.projectId | Int | 描述（待补充）| 
| data.cbsList.dealId | Int | 描述（待补充）| 
| data.cbsList.dealName | String | 描述（待补充）| 
| data.cbsList.tranId | String | 描述（待补充）| 
| data.cbsList.payMode | String | 描述（待补充）| 
| data.cbsList.lifeState | String | 描述（待补充）| 
| data.cbsList.cbsType | String | 描述（待补充）| 
| data.cbsList.deadline | String | 描述（待补充）| 
| data.cbsList.portable | Int | 描述（待补充）| 
| data.cbsList.assigned | Int | 描述（待补充）| 
| data.cbsList.autoRenewFlag | Int | 描述（待补充）| 
| data.cbsList.attached | Int | 描述（待补充）| 
| data.cbsList.diskType | String | 描述（待补充）| 
| data.cbsList.zone | Int | 描述（待补充）| 
| data.cbsList.qcloudZone | Int | 描述（待补充）| 
| data.cbsList.diskSize | Int | 描述（待补充）| 
| data.cbsList.realDiskSize | Int | 描述（待补充）| 
| data.cbsList.cbsUuid | String | 描述（待补充）| 
| data.cbsList.deviceId | Int | 描述（待补充）| 
| data.cbsList.dom0Ip | String | 描述（待补充）| 
| data.cbsList.target | String | 描述（待补充）| 
| data.cbsList.alias | String | 描述（待补充）| 
| data.cbsList.status | Int | 描述（待补充）| 
| data.cbsList.addTimeStamp | String | 描述（待补充）| 
| data.cbsList.cbsSnap | Int | 描述（待补充）| 
| data.cbsList.modTimeStamp | String | 描述（待补充）| 
| data.cbsList.cbsInstanceId | String | 描述（待补充）| 
| data.cbsList.fsType | String | 描述（待补充）| 
| data.cbsList.path | String | 描述（待补充）| 
| data.cbsList.volumeType | String | 描述（待补充）| 
| data.cbsList.hostBlockSize | Int | 描述（待补充）| 
| data.cbsList.vmBlockSize | Int | 描述（待补充）| 
| data.cbsList.deviceLanIp | String | 描述（待补充）| 
| data.cbsList.cvmAlias | String | 描述（待补充）| 
| data.cbsList.zoneId | Int | 描述（待补充）| 
| data.cbsList.zoneName | String | 描述（待补充）| 
| data.cbsList.uInstanceId | String | 描述（待补充）| 


## 4. 示例
输入
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceCbsInfo
&uInstanceIds.0=ins-1nr7zocq
&uInstanceIds.1.ins-bviuv6oc=
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":[
        {
            "uInstanceId":"ins-1nr7zocq",
            "cbsList":[
                {
                    "cbsId":"87655566",
                    "appId":"1351000042",
                    "projectId":"0",
                    "dealId":"453092",
                    "dealName":"20160510110001",
                    "tranId":"",
                    "payMode":"prepay",
                    "lifeState":"normal",
                    "cbsType":"tssd",
                    "deadline":"0000-00-00 00:00:00",
                    "portable":"0",
                    "assigned":"1",
                    "autoRenewFlag":"0",
                    "attached":"1",
                    "diskType":"root",
                    "zone":"254",
                    "qcloudZone":"100002",
                    "diskSize":"50",
                    "realDiskSize":"0",
                    "cbsUuid":"426147840405689",
                    "deviceId":"4812371",
                    "dom0Ip":"10.112.100.81",
                    "target":"xvda",
                    "alias":"未命名",
                    "status":"2",
                    "addTimeStamp":"2016-05-10 11:51:28",
                    "cbsSnap":"0",
                    "modTimeStamp":"2016-05-10 11:51:29",
                    "cbsInstanceId":"disk-968y2s8a",
                    "fsType":"",
                    "path":"",
                    "volumeType":"cbs",
                    "hostBlockSize":"512",
                    "vmBlockSize":"512",
                    "deviceLanIp":"10.104.62.87",
                    "cvmAlias":"miao",
                    "zoneId":"100002",
                    "zoneName":"广州二区",
                    "uInstanceId":"ins-1nr7zocq"
                }
            ]
        }
    ]
}
```

