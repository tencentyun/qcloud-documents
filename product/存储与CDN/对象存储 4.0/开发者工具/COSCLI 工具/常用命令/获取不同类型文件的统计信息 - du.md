
du 命令用于列出某存储桶或某文件夹下，每一种存储类型文件的统计信息。统计信息包括不同存储类型的文件总数、每种类型文件的总大小。

## 命令格式

```plaintext
./coscli du cos://<bucketAlias>[/prefix/] [flag]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

ls 命令包含以下可选参数：

| 参数格式 | 参数用途       | 示例                 |
| -------- | -------------- | -------------------- |
| /prefix/ | 指定某一文件夹 | cos://bucket1/picture/ |

du 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h        | --help        | 输出帮助信息             |
| -c        | --config-path | 指定要使用的配置文件路径 |
|    无       | --include     | 包含特定模式的文件       |
|      无       | --exclude     | 排除特定模式的文件       |

>? 
>- `--include` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
>- 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```plaintext
./coscli du cos://bucket1/picture/ --include ".*.mp4"
```

## 操作示例

### 列出 bucket1 存储桶内文件的统计信息

```plaintext
./coscli du cos://bucket1
```

### 列出 bucket1 存储桶 picture 文件夹下文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/
```

### 列出 bucket1 存储桶 picture 文件夹下所有 .mp4 类型文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/ --include .*.mp4
```

### 列出 bucket1 存储桶 picture 文件夹下所有非 .md 类型文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/ --exclude .*.md
```
