## 1 功能说明 
1. APP管理员可以通过该接口获取APP中所有群组的ID。
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：

私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群全部支持使用本REST API获取群组ID。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/get_appid_group_list?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```
### 2.3 请求参数 

URL中各参数的含义以及填写方式参见[REST API简介](/doc/product/269/REST API简介)。 

### 2.4 最高调用频率 

100次/秒。如需提升调用频率，请根据[工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请处理。 

### 2.5 HTTP请求方式 

POST 

### 2.6 HTTP请求包体格式 

JSON 

### 2.7 请求包示例

#### 2.7.1 基础形式

如果APP中的总群数量超过10000个，最多只会返回10000个群组ID（如果需要完整获取，必须使用分页拉取的形式）。 
```
{}
```

#### 2.7.2 分页拉取

可以使用Limit和Next两个值用于控制分页拉取：
1. Limit限制回包中GroupIdList中群组的个数，不得超过10000； 
1. Next控制分页。对于分页请求，第一次填0，后面的请求填上一次返回的Next字段，当返回的Next为0，代表所有的群都拉取到了；
1. 例如：假设需要分页拉取，每页展示20个，则第一页的请求参数应当为`{“Limit” : 20, “Next” : 0}`，第二页的请求参数应当为`{“Limit” : 20, “Next” : 上次返回的Next字段}`，依此类推；
1. Limit或者Next的取值不会对应答包体中的TotalCount造成影响。 

```
{
    "Limit": 1000,  
    "Next": 0
}
```

#### 2.7.3 指定群组形态

可以指定拉取的群组所属的群组形态，如Public，Private，ChatRoom、AVChatRoom和BChatRoom。
```
{
    "GroupType" : "Public" // 拉取哪种群组形态，不填为拉取所有
}
```

#### 2.7.4 ALL IN ONE

```
{
    "Limit": 1000,  
    "Next": 0,   
    "GroupType" : "Public" // 拉取哪种群组形态，不填为拉取所有
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 |属性 |说明 |
|---------|---------|---------|---------|
| Limit | Integer | 选填| 本次获取的群组ID数量的上限，不得超过10000。如果不填，默认为最大值10000。 |
| Next | Integer | 选填 | 群太多时分页拉取标志，第一次填0，以后填上一次返回的值，返回的Next为0代表拉完了。 |
| GroupType | String | 选填 |如果仅需要返回特定群组形态的群组，可以通过GroupType进行过滤，但此时返回的TotalCount的含义就变成了APP中属于该群组形态的群组总数。不填为获取所有类型的群组。[群组形态](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)包括Public（公开群），Private（私密群），ChatRoom（聊天室），AVChatRoom（互动直播聊天室）和BChatRoom（在线成员广播大群）。|

### 2.9 应答包体示例

```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    "TotalCount": 2, 
    "GroupIdList": [
        {
            "GroupId": "@TGS#2J4SZEAEL"
        },
        {
            "GroupId": "@TGS#2C5SZEAEF"
        }
    ]，
    "Next": 4454685361
}
```
### 2.10 应答包字段说明 

| 字段 | 类型| 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。  |
| ErrorInfo | String | 错误信息。  |
| TotalCount | Integer | APP当前的群组总数。如果仅需要返回特定群组形态的群组，可以通过GroupType进行过滤，但此时返回的TotalCount的含义就变成了APP中该群组形态的群组总数。<br/>例如：假设APP旗下总共50000个群组，其中有20000个为公开群组，如果将请求包体中的GroupType设置为Public，那么不论Limit和Offset怎样设置，应答包体中的TotalCount都为20000，且GroupIdList中的群组全部为公开群组。  |
| GroupIdList | Array | 获取到的群组ID的集合。 |
| Next | Integer | 分页拉取的标志。 |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 |含义说明 | 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。 | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。 | 
| 10018 | 应答包长度超限。因为请求的内容过多，导致应答包超过了最大包长（1MB），请尝试减少单次请求的数据量。 | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](http://avc.qcloud.com/wiki2.0/im/APITester/APITester.html#v4/group_open_http_svc/get_appid_group_list)调试本接口。 

Server调试工具 

可以通过[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中的调试工具进行简单的REST API调试，命令如下： 
```
# 获取APP中所有群组信息(默认获取50个)
./TimRestApiGear.php group_open_http_svc get_appid_group_list 
```
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。 

## 4 API集成 

### 4.1 PHP集成 

在云通信[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK#3-timrestapigear.php.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E)中，可以通过TimRestInterface的如下成员函数快速集成该API： 
```
// 获取app中所有群组, 最多只会返回10000个(如果需要获取完整必须使用高级接口)
abstract function group_get_appid_group_list();

// 获取app中所有群组(高级接口)
abstract function group_get_appid_group_list2($limit, $offset, $group_type);
```

## 5 可能触发的回调 

无。 

## 6 参考 

无。 
