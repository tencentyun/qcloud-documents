
cp 命令用于上传、下载或拷贝文件。

## 命令格式

```plaintext
./coscli cp <source_path> <destination_path> [flags]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

cp 命令包含以下可选 flag：

| flag 简写 | flag 全称       | flag 用途                            |
| --------- | --------------- | ------------------------------------ |
| -h        | --help          | 输出帮助信息                         |
| -c        | --config-path   | 指定要使用的配置文件路径             |
|   无       | --include       | 包含特定模式的文件                   |
|   无       | --exclude       | 排除特定模式的文件                   |
| -r        | --recursive     | 是否递归遍历文件夹下所有文件       |
|   无       | --srotage-class | 指定上传至文件的类型（默认 STANDARD） |
|   无       | --part-size     | 文件分块大小（默认32MB）     |
|   无       | --thread-num    | 并发线程数（默认并发5）      |
|   无       | --rate-limiting | 单链接速率限制（0.1~100MB/s）       |


>?
> - cp 命令在上传和下载大文件时会自动启用并发上传/下载。
> - 当文件大于 `--part-size` 时，COSCLI 会先将文件按 `--part-size` 进行切块，之后用 `--thread-num` 个线程并发地执行上传/下载任务。
> - 每个线程都会维护一个链接，对于每个链接，您可以使用 `--rate-limiting` 参数对单链接进行限速，当启用并发上传/下载时，总速率为 `--thread-num * --rate-limiting`。
> - 当以分块形式上传/下载文件时，会默认开启断点续传。
> - `--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```
./coscli cp ~/test/ cos://bucket1/example/ -r --include ".*.mp4"
```

## 操作示例

### 上传操作

#### 上传单文件

```plaintext
./coscli cp ~/example.txt cos://bucket1/example.txt
```

#### 将本地 test 文件夹下的所有文件上传至 bucket1 桶中的 example 文件夹下

```plaintext
./coscli cp ~/test/ cos://bucket1/example/ -r
```

#### 将本地 test 文件夹下的所有 .mp4 类型文件上传至 bucket1 桶中的 example 文件夹下

```plaintext
./coscli cp ~/test/ cos://bucket1/example/ -r --include .*.mp4
```

#### 将本地 test 文件夹下的所有非 .md 类型文件上传至 bucket1 桶中的 example 文件夹下

```plaintext
./coscli cp ~/test/ cos://bucket1/example/ -r --exclude .*.md
```

#### 将本地 dir 文件夹下有 dirA、dirB、dirC、dirD 四个文件夹，将 dir 文件夹下除 dirD 文件夹之外的所有内容上传

```plaintext
./coscli cp dir/ cos://bucket1/example/ -r --exclude dirD/.*
```

#### 将本地 test 文件夹下的所有文件上传至 bucket1 桶中的 example 文件夹下，并以归档类型文件存储

```plaintext
./coscli cp ~/test/ cos://bucket1/example/ -r --storage-class ARCHIVE
```

### 下载操作

#### 下载单文件

```plaintext
./coscli cp cos://bucket1/example.txt ~/example.txt
```

#### 将 bucket1 桶中的 example 文件夹下的所有文件下载到本地 test 文件夹下

```plaintext
./coscli cp cos://bucket1/example/ ~/test/ -r
```

#### 将 bucket1 桶中的 example 文件夹下所有 .mp4 类型文件下载至本地 test 文件夹下

```plaintext
./coscli cp cos://bucket1/example/ ~/test/ -r --include .*.mp4
```

#### 将 bucket1 桶中的 example 文件夹下所有非 .md 类型文件下载至本地 test 文件夹

```plaintext
./coscli cp cos://bucket1/example/ ~/test/ -r --exclude .*.md
```

### 拷贝操作

#### 桶内拷贝单文件

```plaintext
./coscli cp cos://bucket1/example.txt cos://bucket1/example_copy.txt
```

#### 跨桶拷贝单文件

```plaintext
./coscli cp cos://bucket1/example.txt cos://bucket2/example_copy.txt
```

#### 将 bucket1 桶中 example1 文件夹下的所有文件拷贝至 bucket2 桶中 example2 文件夹下

```plaintext
./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r
```

#### 将 bucket1 桶中 example1 文件夹下的所有 .mp4 类型文件拷贝至 bucket2 桶中 example2 文件夹下

```plaintext
./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r --include .*.mp4
```

#### 将 bucket1 桶中的 example1 文件夹下所有非 .md 类型文件拷贝至 bucket2 桶中 example2 文件夹下

```plaintext
./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r --exclude .*.md
```
