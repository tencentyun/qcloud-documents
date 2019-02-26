### cancelMatch 取消匹配
**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|cancelMatchPara|CancelMatchPara|取消匹配参数|
|callback|```ReqCallback<lagame.CancelMatchRsp>```|获取房间列表回调|

CancelMatchPara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|matchType|lagame.MatchType|匹配类型，参考“枚举类型”一节|

lagame.CancelMatchRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|

调用结果将在 callback 中异步返回。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const cancelMatchPara = {
	matchType: MBS.ENUM.MatchType.ONLINEMATCH,
};

const seq = mbs.cancelMatch(cancelMatchPara, event => console.log(event));
```