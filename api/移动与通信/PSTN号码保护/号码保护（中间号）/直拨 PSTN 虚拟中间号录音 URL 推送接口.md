## 1. 接口描述

功能： 直拨 PSTN 虚拟中间号录音 URL 推送接口   
接口地址： 直拨双方号码请求时设置  
请求方式：POST  

## 2. 参数说明 
| 参数名 | 要求 | 备注 | 
|---------|---------|------------|
| appId | 必选 | xxx | 
| callId | 必选 | 通话唯一标识 callId，由推送方生成保证全局唯一 | 
| requestId | 可选 | App 操作 session buffer 原样返回 | 
| bindId | 必选 | 双方号码 + 中间号绑定 ID，该 ID 全局唯一 | 
| src | 必选 | 主叫号码 | 
| dst | 必选 | 被叫号码 | 
| dstVirtualNum | 必选 | 主叫通讯录直拨虚拟保护号码 | 
| recordUrl | 必选 | 录音下载 URL | 

**确认响应包必填字段**  
```
HTTP/1.1 200 OK
Content-Type: text/plain;charset=utf-8
Content-Length: 0
```