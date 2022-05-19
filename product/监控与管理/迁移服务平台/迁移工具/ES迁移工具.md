  

## ES迁移工具

### 概述
ES迁移过程中，需要对源集群进行快照、数据传输、目标肌群快照恢复等多步操作，在数据量大、迁移时间窗口短的情况下操作繁琐并且易出错。ES迁移工具基于快照和对象存储，能够快速完成全流程的操作，提高迁移效率和安全性。

### 使用环境
系统环境
Windows、Linux 和 macOS 系统。

#### 步骤1：获取工具
前往[控制台工具集](https://console.cloud.tencent.com/msp)下载ES迁移工具。

#### 步骤2：解压工具包
解压工具包，正确解压后的工具目录结构如下所示：

> migration-kit
> 	| - linux
> 	| - mac
> 	| - windows
> 	| — config.yaml      # 迁移工具配置文件

#### 步骤3：执行命令
> ./migration-kit es --help
> ./migration-kit es all -c config.yaml