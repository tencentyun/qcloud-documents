 

## 概述

GooseFSx-CLI 是腾讯云数据加速器 GooseFSx 的客户端命令行工具。您可通过命令行指令，自动化、脚本化管理 GooseFSx 中的数据。


## 部署

将 GooseFSx-CLI 程序包拷贝到 GooseFSx 客户端，便可直接运行。



## 配置参数

首次使用需要配置参数 AK、SK 和 token，配置参数有以下方式：

### 方式一：直接执行配置命令

执行如下命令：

```
./goosefsx-cli
```

请按照指引，依次输入 AK、SK 和 token：

```
2023/02/16 19:55:44 Welcome to goosefsx-cli!
When you use goosefsx-cli for the first time, you need to input some necessary information to generate the default configuration file of goosefsx-cli.
The path of the configuration file: /root/.goosefsx.yaml
Input Your Secret ID: 
xxx
Input Your Secret Key: 
yyy
Input Your Session Token: 
test-token123
```


### 方式二：直接编辑配置文件 `/root/.goosefsx.yaml`

```
# cat /root/.goosefsx.yaml
goosefsx:
  base:
     secretid: xxx
     secretkey: yyy
     sessiontoken: test-token123
     scheme: https
     endpoint: goosefs.internal.tencentcloudapi.com
```




## 数据流动任务命令

data_flow 用于数据流动任务。

### 前提条件

在使用数据流动任务命令之前，请先创建数据流动/关联存储桶，详情请参见 [管理 GooseFSx 数据流动和关联存储桶](https://cloud.tencent.com/document/product/1424/77959)。


### 创建数据流动任务并异步返回结果

创建数据流动任务，立即返回下发任务是否成功；随着数据量不同，数据流动任务执行时间也不同，可通过以下查询命令来查询数据流动任务执行结果。



#### 命令格式

```
./goosefsx-cli data_flow create [flags]
```

create 命令包含以下 flag：

| flag 全称       | flag 简写 | flag 用途                                                    |
| --------------- | --------- | ------------------------------------------------------------ |
| --task-type     | 无        | 数据流动任务类型，FS_TO_COS（文件系统到 COS Bucket）或者 COS_TO_FS（COS Bucket 到文件系统） |
| --bucket        | 无        | COS 存储桶名                                                 |
| --region        | 无        | 存储桶所属地域                                               |
| --filesystem-id | 无        | 文件系统 ID                                                  |
| --task-path     | 无        | 对于 FS_TO_COS，TaskPath 是 Bucket 映射目录的相对路径，对于 COS_TO_FS 是 COS 上的路径。如果置为空, 则表示全部数据 |
| --task-name     | 无        | 任务名称                                                     |

#### 输出参数

| 参数名称        | 类型   | 描述                                                         |
| --------------- | ------ | ------------------------------------------------------------ |
| Task ID         | string | 任务 ID                                                      |
| Task Request ID | string | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |


#### 操作示例

**创建数据流动任务**

```
./goosefsx-cli data_flow create --task-type=COS_TO_FS --bucket=bucket_test-1252246555 --region=ap-shanghai --filesystem-id=xxx --task-path=test/ --task-name=test
```

**返回值**

```
Create data repository task successfully!
=======================
  Task ID: x_task_1676551831746
  Task Request ID: f90a8741-f59b-465c-b44c-4758e7ed68a0

```

数据流动任务的结果，通过查询命令来查看。



### 获取数据流动任务的执行结果

查询数据流动任务的执行结果，执行中、已完成、失败。



#### 命令格式

```
./goosefsx-cli data_flow taskstatus [flags]
```


taskstatus 命令包含以下 flag：

| flag 全称       | flag 简写 | flag 用途      |
| --------------- | --------- | -------------- |
| --region        | 无        | 存储桶所属地域 |
| --task-id       | 无        | 任务 ID        |
| --filesystem-id | 无        | 文件系统 ID    |

#### 输出参数

| 参数名称                        | 类型   | 描述                                                         |
| ------------------------------- | ------ | ------------------------------------------------------------ |
| Query data flow task ID         | string | 任务 ID                                                      |
| Query data flow task status     | string | 获取数据流动任务状态，其中包含的数字 0(初始化)、 2(已完成)、3(任务失败) |
| Query data flow task Request ID | string | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |

 

#### 操作示例

**获取数据流动实时任务状态**

```
./goosefsx-cli data_flow taskstatus --region=ap-shanghai --task-id=xxx --filesystem-id=xxx 
```


**返回值**

```
Query data flow task successfully!
=======================
  Query data flow task ID: x_task_1676551831746
  Query data flow task Request ID: fad14898-b975-423e-9588-7c5be84ad4e9
  Query data flow task status: 数据流动任务状态为 2, 已完成

```

>!task-id 为创建数据流动任务的返回值。



### 创建数据流动任务并实时返回结果

创建数据流动任务并返回执行结果，已完成或失败。



#### 命令格式

```
./goosefsx-cli data_flow createAndWaitFinish [flags]
```

createAndWaitFinish 命令包含以下 flag：

| flag 全称       | flag 简写 | flag 用途                                                    |
| --------------- | --------- | ------------------------------------------------------------ |
| --task-type     | 无        | 数据流动任务类型，FS_TO_COS（文件系统到 COS Bucket）或者 COS_TO_FS（COS Bucket 到文件系统） |
| --bucket        | 无        | COS 存储桶名                                                 |
| --region        | 无        | 存储桶所属地域                                               |
| --filesystem-id | 无        | 文件系统 ID                                                  |
| --task-path     | 无        | 对于 FS_TO_COS, TaskPath 是 Bucket 映射目录的相对路径, 对于 COS_TO_FS 是 COS 上的路径。如果置为空, 则表示全部数据 |
| --task-name     | 无        | 任务名称                                                     |

#### 输出参数

| 参数名称                        | 类型   | 描述                                                         |
| ------------------------------- | ------ | ------------------------------------------------------------ |
| Task ID                         | string | 创建数据流动任务 ID                                          |
| Task Request ID                 | string | 创建数据流动任务唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |
| Query data flow task ID         | string | 获取数据流动任务 ID                                          |
| Query data flow task Request ID | string | 获取数据流动任务唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |
| Query data flow task status     | string | 获取数据流动任务状态，其中包含的数字 0(初始化)、2(已完成)、3(任务失败) |



#### 操作示例

**创建数据流动任务**

```
./goosefsx-cli data_flow createAndWaitFinish --task-type=COS_TO_FS --bucket=bucket_test-xxxx --region=ap-shanghai --filesystem-id=xxx --task-path=test/ --task-name=test
```

 

**返回值**


```
Create data repository task successfully!
=======================
  Task ID: x_task_1676553288519
  Task Request ID: 2902f31e-4bfc-4709-828f-999072c92478
Query data flow task successfully!
=======================
  Query data flow task ID: x_task_1676553288519
  Query data flow task Request ID: ee9d0646-9c9b-4589-b661-f492631147af
  Query data flow task status: 数据流通任务状态为 2, 已完成

```



