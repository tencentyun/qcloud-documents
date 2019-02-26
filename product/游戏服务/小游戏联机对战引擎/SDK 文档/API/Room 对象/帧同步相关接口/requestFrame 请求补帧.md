### requestFrame 请求补帧
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|requestFramePara|RequestFramePara|请求补帧参数|
|callback|```ReqCallback<lagame.FrameInputRsp>```|请求补帧回调|

RequestFramePara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|beginFrameId|number|起始帧号|
|endFrameId|number|结束帧号|

lagame.FrameInputRsp 暂未定义任何字段。

调用结果将在 callback 中异步返回。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const requestFramePara = {
	beginFrameId: 100,
	endFrameId: 120,
};

let seq = room.requestFrame(requestFramePara, event => console.log(event));
```

