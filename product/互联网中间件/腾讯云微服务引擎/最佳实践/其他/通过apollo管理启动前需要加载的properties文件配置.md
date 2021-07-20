## 操作场景

本文介绍如何通过 apollo 管理来管理启动前需要加载的 properties 文件，常见于数据源或者一些不怎么变更的文件 properties 配置，主要抽离文件配置的重复内容和屏蔽环境差异，一般用于容器环境, 通过ENV注入所需变量配置.

## 操作说明
- 约定应用加载的配置文件名称，放到公共 namespace 抽离公共配置，项目有需要特别修改的，直接关联公共 namespace 覆盖或增加响应配置。示例中使用 `config.properties`和`db-config.properties`，对应公共 namespace  `PLATFORM.config.properties`和`PLATFORM.db-config.properties`：
  - config.properties：不经常修改或者非数据源但启动前需要加载的配置项。
  - db-config.properties：数据源相关的配置。

- 确保需要托管文件在项目中存在，空文件也可。
- 选择 apollo 托管则全部以 apollo 上配置为准，文件内已有内容会被覆盖。
- 除了公共 properties 文件外，其他 properties 文件默认也会被扫到并从 apollo 拉取：
	- 如果不存在会报错退出，建立对应文件名的私有 namespace 即可。
	- 如果不想404直接退出,可以传入环境变量 `APOLLO_FORCE_PROPERTIES=false`。
