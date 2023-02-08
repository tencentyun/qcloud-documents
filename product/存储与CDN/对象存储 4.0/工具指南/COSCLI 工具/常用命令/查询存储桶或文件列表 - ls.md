ls 命令用于查询所有存储桶列表、查询存储桶下的文件列表和文件夹下的文件列表。

## 命令格式
```plaintext
./coscli ls [cos://<bucket-name>[/prefix/]] [flag]
```

ls 命令包含以下参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
| cos://&lt;bucket-name&gt; | 可选参数。指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。  |使用桶别名访问：cos://example-alias<br>使用桶名称访问：cos://examplebucket-1250000000  |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |

ls 命令包含以下可选 flag：

| flag 简写 | flag 全称   | flag 用途                            |
| --------- | ----------- | ------------------------------------ |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --include   | 包含特定模式的文件                   |
|     无       | --exclude   | 排除特定模式的文件                   |
| -r        | --recursive | 是否递归地遍历文件夹，并列出所有文件 |
|     无      | --limit       | 指定列出的最大数量（0 - 1000） |

>? 
> - `--include` 和`--exclude`支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```plaintext
./coscli ls cos://bucket1 -r --include ".*.mp4"
```
> - 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例


### 列出当前账号下所有存储桶

```plaintext
./coscli ls
```

返回的信息包括：桶名称，地域，创建时间，存储桶总数。示例如下：

```plaintext
           BUCKET NAME          |     REGION      |     CREATE DATE
--------------------------------+-----------------+-----------------------
  examplebucket-1250000000      | ap-nanjing      | 2022-01-01T00:00:00Z
--------------------------------+-----------------+-----------------------
                                  TOTAL BUCKETS:  |          1
                                ------------------+-----------------------
```

### 列出文件

#### 列出 bucket1 存储桶中的所有文件

```plaintext
./coscli ls cos://bucket1
```

返回的信息包括：对象键（对象在存储桶中的唯一标识），存储类型，最近更新时间，对象大小，对象总数。示例如下：

```plaintext
        KEY      |   TYPE   |      LAST MODIFIED       |  SIZE
-----------------+----------+--------------------------+---------
        test.txt | STANDARD | 2022-01-01T00:00:00.000Z |   2  B
-----------------+----------+--------------------------+---------
                                   TOTAL OBJECTS:      |   1
                            ---------------------------+---------
```

#### 列出 bucket1 存储桶中 picture 文件夹下的所有文件和文件夹

```plaintext
./coscli ls cos://bucket1/picture/
```

普通列出仅返回查询路径所在层级的数据，不对子路径进行展开。示例如下：

```plaintext
        KEY        |   TYPE   |      LAST MODIFIED       |  SIZE
-------------------+----------+--------------------------+---------
 picture/subfolder |      DIR |                          |   
  picture/pic1.png | STANDARD | 2022-01-01T00:00:00.000Z | 162  B
-------------------+----------+--------------------------+---------
                                   TOTAL OBJECTS:        |   2
                            -----------------------------+---------
```


#### 递归列出 bucket1 存储桶中 picture 文件夹下的所有文件

```plaintext
./coscli ls cos://bucket1/picture/ -r
```

如果查询路径所在层级有子路径，递归列出会对所有子路径进行扫描，返回查询路径层级下的所有文件。示例如下：

```plaintext
             KEY            |   TYPE   |      LAST MODIFIED       |  SIZE
----------------------------+----------+--------------------------+---------
 picture/subfolder/pic2.png |      DIR |                          |   
          picture/subfolder |      DIR |                          |   
           picture/pic1.png | STANDARD | 2022-01-01T00:00:00.000Z | 162  B
----------------------------+----------+--------------------------+---------
                                            TOTAL OBJECTS:        |   2
                                     -----------------------------+---------
```

#### 递归列出 bucket1 存储桶中所有的 .mp4 类型文件

```plaintext
./coscli ls cos://bucket1 -r --include .*.mp4
```

#### 递归列出 bucket1 存储桶中的所有不是 .mp4 类型的文件

```plaintext
./coscli ls cos://bucket1 -r --exclude .*.mp4
```

#### 递归列出 bucket1 存储桶中 picture 文件夹下所有以 test 开头并且类型不是 .jpg 的文件

```plaintext
./coscli ls cos://bucket1/picture -r --include ^picture/test.* --exclude .*.jpg
```
