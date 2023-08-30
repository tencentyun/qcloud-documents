本文档将为您介绍在 [告警设置 ](https://console.cloud.tencent.com/cwp/setting) > **机器人通知**设置接收 JSON 格式告警数据后，用户将收到的各类告警的传输字段及说明。

>?
>- 目前机器人通知处于灰度状态，仅对明确有该需求的客户开放，若您希望实时接收主机安全 webhook 机器人告警，请 [联系我们](https://cloud.tencent.com/online-service) 申请使用。
>-  [告警设置 ](https://console.cloud.tencent.com/cwp/setting)  > **机器人通知**与消息中心的机器人相互独立，没有关联。

## 公共字段
#### 示例
```
{
    "uin": "",
    "nickname": "",
    "server": "",
    "instance_id": "",
    "region": "",
    "time": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| uin         | 用户 uin           |
| nickname    | 用户昵称           |
| server      | 机器 ip [机器别名] |
| instance_id | 机器实例 id        |
| region      | 机器所在区域       |
| time        | 事件时间           |


## 异常登录
#### 示例
```
{
    "event_type": "异常登录",
    "src_ip": "",
    "area": "",
    "level": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| src_ip         | 来源 ip     |
| area    | 来源地           |
| level      |危胁等级|

## 密码破解
#### 示例
```
{
    "event_type": "密码破解",
    "src_ip": "",
    "area": "",
    "count": "",
    "banned": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| src_ip         | 来源 ip     |
| area    | 来源地           |
|count     |尝试次数|
|banned      |阻断状态|


## 文件查杀
### 恶意文件
#### 示例
```
{
    "event_type": "恶意文件",
    "file_type": "",
    "path": "",
    "level": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| file_type         | 文件类型     |
|path      |文件路径|
|level      |威胁等级|


### 异常进程
#### 示例
```
{
    "event_type": "异常进程",
    "pid": "",
    "path": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| pid         | 进程 id     |
|path      |进程路径|

## 恶意请求
#### 示例
```
{
    "event_type": "恶意请求",
    "url": "",
    "count": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| url         | 恶意域名    |
|count      |请求次数|

## 高危命令
#### 示例
```
{
    "event_type": "高危命令",
    "cmd": "",
    "level": "",
    "status": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| cmd         | 命令内容    |
|level      |威胁等级|
|status      |处理状态|

## 本地提权
#### 示例
```
{
    "event_type": "本地提权",
    "user": "",
    "process": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| user         | 提权用户    |
|process      |提权进程|

## 反弹 Shell
#### 示例
```
{
    "event_type": "反弹Shell",
    "process": "",
    "dst_ip": "",
    "dst_port": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
| process         | 进程名称    |
|dst_ip      |目标主机|
|dst_port|目标端口|

## java 内存马
#### 示例
```
{
    "event_type": "java内存马",
    "type": "",
    "pid": "",
    "argv": "",
    "class_name": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|type|内存马类型|
|pid|进程 id|
|argv|进程参数|
|class_name|内存马 class 名称|

## 核心文件监控
#### 示例
```
{
    "event_type": "核心文件",
    "rule_name": "",
    "exe_path": "",
    "file_path": "",
    "count": "",
    "level": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|rule_name|命中规则名称|
|exe_path|进程路径|
|file_path|文件路径|
|count|事件数量|
|level|威胁等级|

## 网络攻击
#### 示例
```
{
    "event_type": "网络攻击",
    "src_ip": "",
    "city": "",
    "vul_name": "",
    "dst_port": "",
    "status": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|src_ip|来源 ip|
|city|来源城市|
|vul_name|漏洞名称|
|dst_port|目标端口|
|status|攻击状态|

## 客户端离线
#### 示例
```
{
    "event_type": "客户端离线",
    "offline_hour": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|offline_hour|客户端离线时长|

## 客户端卸载
```
{
    "event_type": "客户端卸载"
}
```

## 漏洞通知
#### 示例
```
{
    "event_type": "漏洞",
    "category": "",
    "vul_name": "",
    "level": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|category|漏洞分类|
|vul_name|漏洞名称|
|level|威胁等级|

## 基线通知
#### 示例
```
{
    "event_type": "基线",
    "category": "",
    "rule_name": "",
    "level": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|category|基线分类|
|rule_name|规则名称|
|level|威胁等级|

## 勒索防御
#### 示例
```
{
    "event_type": "勒索防御",
    "file_path": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|file_path|文件目录|


## 网页防篡改
### 篡改成功
#### 示例
```

{
    "event_type": "网页防篡改（篡改成功）",
    "protect_name": "",
    "protect_path": "",
    "recover_type": "",
    "recovered_status": "",
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|protect_name|防护名称|
|protect_path|防护目录|
|recover_type|事件类型|
|recovered_status|事件状态|

### 恢复失败
#### 示例
```
{
    "event_type": "网页防篡改（恢复失败）",
    "protect_name": "",
    "protect_path": "",
    "exception": ""
}
```
#### 字段说明
| 字段名称    | 说明               |
| ----------- | ------------------ |
|protect_name|防护名称|
|protect_path|防护目录|
|exception|失败原因|
