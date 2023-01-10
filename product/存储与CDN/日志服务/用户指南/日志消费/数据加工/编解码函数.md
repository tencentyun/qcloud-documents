## decode_url 函数

### 函数定义

将编码 URL 进行解码。

### 语法描述

```sql
decode_url(值)
```

### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
| url | URL 值 | string |是|-|-|

### 示例

原始日志：
```
{"url":"https%3A%2F%2Fcloud.tencent.com%2F"}
```
加工规则：
```
fields_set("result",decode_url(v("url")))
```
加工结果：
```
{"result":"https://cloud.tencent.com/","url":"https%3A%2F%2Fcloud.tencent.com%2F"}
```

## md5_encoding 函数
### 函数定义
计算并返回 MD5 值。

### 语法描述
```
md5_encoding(值)
```

### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|值|	待计算 MD5 值的数据|	String|	是|	-|	-|

### 示例
原始日志：
```
{"field": "haha"}
```
加工规则：
```
fields_set("field", md5_encoding(v("field")))
```
加工结果：
```
{"field":"4e4d6c332b6fe62a63afe56171fd3725"}
```



## uuid 函数
### 函数定义
生成 universally unique identifier (UUID) ，即唯一识别码。

### 语法描述
```
uuid() 
```

### 参数说明
无入参

### 示例
原始日志：

```
{"key":"value"}
```

加工规则：
```
fields_set("field",uuid())
```
加工结果：
```
{"field":"8c2db704-45c0-4ea1-9e2c-cf9c966e35cd","key":"value"}
```
