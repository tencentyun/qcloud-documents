lsparts 命令列出分块上传中产生的文件碎片。

## 命令格式

```plaintext
./coscli lsparts cos://<bucketAlias>[/prefix/] [flag]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

lsparts 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -h        | --help        | 输出帮助信息                 |
| -c        | --config-path | 指定要使用的配置文件路径     |
|     无      | --include     | 包含特定模式的文件           |
|     无      | --exclude     | 排除特定模式的文件           |
|     无      | --limit       | 指定列出的最大数量（0 - 1000） |

## 操作示例

### 列出 bucket1 桶内的所有文件碎片

```plaintext
./coscli lsparts cos://bucket1
```

### 列出 bucket1 桶内 pictrue 文件夹下的所有碎片

```plaintext
./coscli lsparts cos://bucket1/pictrue/
```
