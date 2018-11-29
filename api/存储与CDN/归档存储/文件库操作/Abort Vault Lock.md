## 功能描述

要实现锁定文件库，需进行以下步骤：

1. 初始化文件库锁定策略。成功后返回锁定 ID，同时文件库进入InProgress状态。此时文件库表现形如文件库已锁定，可用以测试效果
2. 进入 InProgress 状态之后24 小时内，利用锁定ID调用Complete Vault Lock以完成锁定。文件库在锁定之后无法进行解锁使用，也无法发起中止锁定

说明：

- 进入InProgress状态之后，若测试不及预期，用户可调用Abort Vault Lock以中止锁定，并重新发起初始化。
- 如果进入InProgress状态之后24 小时内，未完成锁定，则文件库会退出 InProgress 状态，并删除文件库锁定策略。

Delete Vault Lock实现删除文件库锁定策略，中止在`InProgress`状态的文件库锁定。如果文件库锁定处于 `Locked` 状态，则返回 `AccessDeniedException` 

## 请求

### 请求语法

```http
DELETE /<UID>/vaults/<VaultName>/lock-policy HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容

