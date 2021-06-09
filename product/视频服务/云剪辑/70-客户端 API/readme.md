## 客户端 API 编辑方法

### Step 1：新增/编辑 API 文档
1. 在 core 目录下找到所要新增/编辑的文档。
2. 以 core/demo.md 为样板，进行新增/修改。

### Step 2：新增/编辑数据结构
1. 在 core-data-structure 目录下找到要新增/编辑的数据结构。
2. 以 core-data-structure/demo.md 为样板，进行新增/修改。

### Step 3：生成文档
1. 执行 `bash gen_client_api_from_core.sh`，会自动生成各个 API 文档，以及数据结构。
2. 将所有文件提交 github，并依照腾讯云官网相关流程，更新官网文档。