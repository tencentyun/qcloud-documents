### sig 生成算法
双方维护同一份私钥，在发起请求的时候发起方（合作方）将当前的请求参数数组，按照 key 值进行排序，然后 'key=value' 拼接到加密串后，进行 md5 的编码，接收方（H5 轻应用统计）以同样的处理方式，对 ts 小于或等于 30 分钟的请求进行处理，sig 一致则合法，否则失败。如下为 php 的对应的 sig 生成算法举例：

```
$secret_key = '3023IU&^_W(5#@';
ksort($params);
foreach ($params as $key => $value) {
$secret_key.= $key.'='.$value;
}
$sign = md5($secret_key);
return $sign;
```

| 字段 | 含义 | 
|---------|---------|
| $params | 所有请求的参数数组 |
| key | 参数名 |
| value | 值 |
| secret_key | 注册成功后每个 App 对应返回的 secret_key |


### 返回参数说明

| 字段 | 含义 | 
|---------|---------|
| code | 返回码 | 
| v2 | 表示当前 API 的版本号 | 
| class | 提供的接口类别 | 

### 返回码示例

**成功**

```
{
    code:0,
    info:"success",
  -data:{
          -20160921:{
                  pv:"100492539",
                  uv:"8227032",
                  vv:"67535349",
                  iv:"9826284"
          }
      }
}
```
**失败**

```
{
    code:60002,
    info:"wrong sign",
    data:[]
}
```
