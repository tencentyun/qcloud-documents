## 接口描述
 
本接口（EmrDescribeClusterNode）用于查询单个集群的节点信息。

接口请求域名：`emr.api.qcloud.com`

## 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 EmrDescribeClusterNode。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| ClusterId | 是 | string | EMR 集群 ID，emr-xxxx 格式 |
| NodeFlag | 是 | string | 节点名称，取值为：master，core，task，common，all |
| PageNo | 否 | int | 第几页，首页从1开始 |
| PageSize | 否 | int | 每页记录数，默认20 |

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.totalCnt | int | 查询的集群总个数。|
| data.n.appId | int | 应用 ID |
| data.n.ip | string | IP 地址 |
| data.n.wanIp | string | 外网 IP 地址 |
| data.n.spec | string | CVM 规格 |
| data.n.regionId | int | 地区 ID |
| data.n.zoneId | int | 可用区 ID |
| data.n.diskSize | int | 数据盘容量，单位 G |
| data.n.nameTag | string | 节点 tag |
| data.n.services | string | 节点上部署的服务 |
| data.n.nodeFlag | string | 节点类型 |
| data.n.cvmId | string | CVM 实例 ID |
| data.n.cpu | int | CPU 核数 |
| data.n.memSize | int | 内存容量，单位 G |
| data.n.applyTime | string | 节点申请时间 |
| data.n.freeTime | string | 节点销毁时间 |

## 示例
 
输入
<pre>
  https://emr.api.qcloud.com/v2/index.php?Action=EmrDescribeClusterNode
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &ClusterId=emr-jov423ny
  &NodeFlag=all

</pre>

输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCnt": 3,
        "nodeList": [
            {
                "appId": 1253534036,
                "ip": "10.0.0.219",
                "wanIp": "192.168.27.199",
                "spec": "CVM.S1",
                "regionId": 1,
                "zoneId": 100002,
                "diskSize": 100,
                "nameTag": "master.1",
                "services": "NameNode,ResourceManager,Zookeeper,Hive,Hmaster,Ganglia",
                "nodeFlag": "master",
                "cvmId": "ins-as8q4gma",
                "cpu": 8,
                "memSize": 16,
                "applyTime": "2017-05-10 16:10:04",
                "freeTime": "0000-00-00 00:00:00"
            },
            {
                "appId": 1253534036,
                "ip": "10.0.0.230",
                "wanIp": "",
                "spec": "CVM.S1",
                "regionId": 1,
                "zoneId": 100002,
                "diskSize": 500,
                "nameTag": "core.1",
                "services": "DataNode,NodeManager,RegionServer",
                "nodeFlag": "core",
                "cvmId": "ins-jv9s80qs",
                "cpu": 8,
                "memSize": 16,
                "applyTime": "2017-05-10 16:10:07",
                "freeTime": "0000-00-00 00:00:00"
            },
            {
                "appId": 1253534036,
                "ip": "10.0.0.163",
                "wanIp": "",
                "spec": "CVM.S1",
                "regionId": 1,
                "zoneId": 100002,
                "diskSize": 500,
                "nameTag": "core.2",
                "services": "DataNode,NodeManager,RegionServer",
                "nodeFlag": "core",
                "cvmId": "ins-r0cpzgxa",
                "cpu": 8,
                "memSize": 16,
                "applyTime": "2017-05-10 16:10:10",
                "freeTime": "0000-00-00 00:00:00"
            }
        ]
    }
}
```
