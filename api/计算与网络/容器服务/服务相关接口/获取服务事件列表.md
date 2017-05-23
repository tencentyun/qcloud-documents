## 1. 接口描述
 
本接口 (DescribeServiceEvent) 用于查询服务最近一小时的事件列表。

接口请求域名：<font style="color:red">ccs.api.qcloud.com</font>



## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/document/api/457/9463)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| clusterId   | 是    | String |集群ID，可通过查询集群接口反回字段中的 clusterId获取。 |
| serviceName   | 是    | String | 服务名 |
|namespace| 否 | String      |命名空间,默认为default|


## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败|
| message | String | 模块错误信息描述，与接口相关|
| eventList | Object Array |事件列表，详细信息如下|

eventList 参数详细说明


| 字段 | 类型 | 描述 |
|---------|---------|---------|
| firstSeen | String | 事件首次出现时间(相同事件会被去重，只返回一条) |
| lastSeen | String| 事件最后出现时间 |
| count| Int| 事件总共出现的次数 |
| level | String| 事件等级，分两种: 正常事件为Normal，异常事件为Warning |
| objType | String | 事件对应的kubernetes资源类型，例如Pod, ReplicationController, Service, Node, Deployment, Daemonset, ReplicaSet, Job, Secret, Configmap. 关于kubernetes资源，详见[kubernetes资源] (https://github.com/kubernetes/kubernetes/blob/b392910bc7de425372fe6bf03a2c2c92fe1bae12/docs/devel/api-conventions.md#types-kinds) |
| objName | String | 事件对应的kubernetes资源名称 |
| reason | String | 事件原因 |
| message | String | 事件详细内容 |


## 4. 示例
输入

```
  https://domain/v2/index.php?Action=DescribeServiceEvent
  &clusterId=cls-xxxxx
  &serviceName=test-web-service
  &namespace=default
  &其它公共参数
```
输出

```
 {
    "code" : 0,
    "message":"",
	"data":{
	    "eventList": [
	    {
        "firstSeen": "2016-11-08 16:15:15",
        "lastSeen": "2016-11-09 16:59:56",
        "count": 6530,
        "level": "Warning",
        "objType": "Pod",
        "objName": "frontend-542052039-h2yj8",
        "reason": "pod启动失败",
        "message": "Error syncing pod, skipping: failed to \"StartContainer\" for \"php-redis\" with ImagePullBackOff: \"Back-off pulling image \\\"gcr.io/google-samples/gb-frontend:v5\\\"\"\n"
       },
       {
        "firstSeen": "2016-11-08 16:15:15",
        "lastSeen": "2016-11-09 16:59:56",
        "count": 6530,
        "level": "Normal",
        "objType": "Pod",
        "objName": "frontend-542052039-h2yj8",
        "reason": "操作重试",
        "message": "Back-off pulling image \"gcr.io/google-samples/gb-frontend:v5\""
       } 
	]
	} 
}

```