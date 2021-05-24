## 1. 接口描述

功能： 回拨录音 URL 推送    
接口地址： 在回拨呼叫请求的接口参数`recordUrl`带上对应的回调地址或者线下配置默认地址
请求方式：POST  

## 2. 参数说明 
| 参数名 | 要求 | 备注 | 
|---------|---------|------------|
| appId | 必选 | 线下对接分配的唯一标识码 | 
| callId | 必选 | 回拨请求响应中返回的 callId | 
| requestId | 必选 | 回拨请求时请求携带的 requestId，原样返回 | 
| src | 必选 | 主叫号码 | 
| dst | 必选 | 被叫号码 | 
| recordUrl | 必选 | 录音下载 URL | 
| callType | 可选 | 通话类型（1: VOIP 2:IP TO PSTN 3: PSTN TO PSTN）,如果话单中没有该字段，默认值为回拨3（PSTN TO PSTN） | 
| ringRecoResult | 可选 | 未接通铃声识别结果（请求 ringRecognition 值为1） 0：未知（未识别出铃声或铃声误别服务异常） 1：关机 2：空号 3：通话中 4：无法接通 5：欠费停机 6：呼转异常 7：被叫拒接 8：主叫挂断 9：运营商落地限制 10：其它异常 | 

**确认响应包必填字段**  
```
HTTP/1.1 200 OK
Content-Type: text/plain;charset=utf-8
Content-Length: 0
```
