### setFrameRate 修改帧率
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|setFrameRatePara|SetFrameRatePara|修改帧率参数|
|callback|```ReqCallback<lagame.SetFrameRateRsp>```|修改帧率回调|

SetFrameRatePara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|frameRate|number|帧率，取值 5 ~ 30|

lagame.SetFrameRateRsp 暂未定义任何字段。

调用结果将在 callback 中异步返回。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const setFrameRatePara = {
	frameRate: 15,
};

let seq = room.setFrameRate(setFrameRatePara, event => console.log(event));
```


