## 1. 作业相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 提交作业 | [SubmitJob](/document/api/599/12683) | 用于提交一个待执行的作业 |
| 查看作业列表| [DescribeJobs](/document/product/599/12686) | 用于查看一个或者多个作业的概览信息 |
| 查看作业信息 | [DescribeJob](/document/product/599/12685) | 用于查看一个作业的详细信息，包括内部任务（Task）和依赖（Dependence）信息 |
| 查看任务信息 | [DescribeTask](/document/product/599/12684) | 用于查看一个任务详细信息，包括任务实例（TaskInstance）信息 |
| 查看作业的提交信息 | [DescribeJobSubmitInfo](/document/product/599/12687) | 用于查看一个作业的提交信息，相当于查看作业对应的 SubmitJob 的参数 |
| 终止任务实例 | [TerminateTaskInstance](/document/product/599/12688) | 用于终止一个任务实例
| 终止作业 | [TerminateJob](/document/product/599/12689) | 用于终止一个作业，相当于对作业所包括的所有任务实例执行 TerminateTaskInstance 操作 |
| 删除作业 | [DeleteJob](/document/product/599/12682) | 用于删除一个处于完结状态（成功或者失败）的作业记录 |

## 2. 计算环境相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 创建计算环境 | [CreateComputeEnv](/document/api/599/12691) | 用于创建一个计算环境，包含一个或者多个 CVM 实例 |
| 修改计算环境 | [ModifyComputeEnv](/document/api/599/13637) | 用于修改计算环境的期望节点数量 |
| 删除计算环境 | [DeleteComputeEnv](/document/api/599/12692) | 用于删除一个计算环境 |
| 查看计算环境列表 | [DescribeComputeEnvs](/document/api/599/12695) | 用于查看一个或者多个计算环境的概览信息 |
| 查看计算环境信息 | [DescribeComputeEnv](/document/api/599/12694) | 查看计算环境详情 |
| 查看计算环境活动信息 | [DescribeComputeEnvActivities](/document/api/599/13638) | 用于查询计算环境的活动信息 |
| 查看计算环境的创建信息 | [DescribeComputeEnvCreateInfo](/document/product/599/14604) | 用于查看一个计算环境的创建信息，相当于查看计算环境对应的 CreateComputeEnv 的参数 |


## 3. 查看配置类接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查看CVM可用机型配置信息 | [DescribeAvailableCvmInstanceTypes](/document/product/599/12701) | 查看批量计算可用的 CVM 机型配置信息 |

## 4. 任务模板相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 创建任务模板 | [CreateTaskTemplate](/document/product/599/12698) | 用于创建一个任务模板 |
| 修改任务模板 | [ModifyTaskTemplate](/document/product/599/12697) | 用于修改一个任务模板 |
| 查看任务模板 | [DescribeTaskTemplates](/document/product/599/12700) | 用于查看一个或者多个任务模板 |
| 删除任务模板 | [DeleteTaskTemplates](/document/product/599/12699) | 用于删除一个或者多个任务模板 |
