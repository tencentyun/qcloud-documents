signurl 命令用于获取某个对象的预签名 URL，可以通过此 URL 匿名访问对象。

## 命令格式

```plaintext
./coscli signurl cos://<bucketAlias>/<key> [flag]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

signurl 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -h        | --help        | 输出帮助信息                 |
| -c        | --config-path | 指定要使用的配置文件路径     |
| -t        | --time        | 设置 URL 过期时间（默认1000s） |

## 操作示例

### 获取 bucket1 桶内 pictrue.jpg 的预签名 URL

```plaintext
./coscli signurl cos://bucket1/pictrue.jpg
```

### 获取 bucket2 桶内 pictrue.jpg 的预签名 URL，并设置 URL 的过期时间为1314秒

```plaintext
./coscli signurl cos://bucket2/pictrue.jpg --time 1314
```

