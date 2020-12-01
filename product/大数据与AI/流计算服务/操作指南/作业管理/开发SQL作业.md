登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，创建 SQL 作业后，在【作业管理】中单击要进行开发的作业名称，然后单击【分析开发】即可在作业草稿中进行作业开发。

## 编写和调试 SQL
开发 SQL 作业需在 SQL 编辑器中输入 SQL 分析语句并在下方进行作业参数设置。单击【分析模板】可以快速在编辑器中插入常用的 Ckafka 或 JDBC 等数据流的定义语句。单击【保存】可以将 SQL 语句和作业参数信息同时保存。具体的参数含义详见 [参数设置](https://cloud.tencent.com/document/product/849/48287#.E5.8F.82.E6.95.B0.E8.AE.BE.E7.BD.AE)。

SQL 语句的编写请参考 [SQL 开发指南](https://cloud.tencent.com/document/product/849/18030)。
![](https://main.qcloudimg.com/raw/70a41b4315b2582486bb1f6b89be4403.png)

### 语法检查
编写并保存 SQL 语句后，可进行语法检查，以避免因语法错误而导致运行失败。单击 SQL 编辑器右上角【语法检查】，可对已保存 SQL 语句进行语法检查。若语法无误，则在 SQL 编辑器上方提示“语法检查成功”；若有语法错误，将提示相应语法错误，请按照提示进行修改，直至语法检查通过。
![](https://main.qcloudimg.com/raw/62a89ca61d1b6f0cdcf981b49c809105.png)

### 调试
在 SQL 语句的语法检查通过，并且已在参数设置中选择了所需的内置 Connector 和引用程序包后，可以对 SQL 作业进行调试，即用样例数据作为输入，查看输出结果和调试日志，确认作业可以正常运行且输出数据符合预期。

单击 SQL 编辑器右上方的【调试】，即可进入调试界面。在【上传调试数据】中上传本地的调试数据，单击【上传】打开本地文件选择框，选择并上传该数据源对应的文件。若有多个数据源，则需要分别进行选择和上传。调试文件需注意满足以下条件：
- 默认使用逗号区分。
2. 调试文件仅支持 UTF-8 格式。
3. 调试文件最大支持1MB或1千条记录。
4. 数值类型仅支持普通格式，不支持科学计数法。

![](https://main.qcloudimg.com/raw/6f1ba9e50c467f57b40b35f0eee77ae3.png)
上传调试数据后，单击【开始调试】即开始试运行作业，并将在1 - 2分钟内返回调试结果，同时在调试结果下方展示调试日志。若结果符合预期，则可以继续进行作业发布；若不符合预期，请检查数据源、SQL 语句、内置 Connector 和引用程序包设置等环节是否存在问题，调整后再重新进行调试。单击【结束调试】即可回到分析发开发页面。
![](https://main.qcloudimg.com/raw/febeeb6316717724bb1c719035c3fd5e.png)

## 参数设置
### Checkpoint
即作业快照，开启 checkpoint 之后作业会按照设置的时间间隔自动保存作业快照，用于遇到故障时作业的恢复。可设置 checkpoint 的时间间隔，设置范围在30至3600秒。

### 内置 Connector
由系统提供可让用户选择的 connector，例如在 SQL 语句中使用了来自 Ckafka 的数据流，则必须要在此处选择 Ckafka 相应的 connector。关于上下游的 SQL DDL 写法与内置 Connector 的使用说明请参考 [上下游开发指南](https://cloud.tencent.com/document/product/849/48263)。

### 引用程序包
若 SQL 开发指南中提供的内置函数不满足需求，用户可以自行开发自定义函数，并以 JAR 包的形式在【程序包管理】中上传后，方可在此添加引用程序包，并选择版本。

若前述的内置 Connector 无法满足需求，用户也可以自行开发自定义 Connector，以同样的方式上传并在此添加引用。自定义 Connector 的开发请参考 [自定义 Connector](https://cloud.tencent.com/document/product/849/48330)。

程序包的上传和版本管理方式请参考 [程序包管理](https://cloud.tencent.com/document/product/849/48295)。

### 算子默认并行度
用户指定的整个作业的算子默认并行度。1个并行度将占用1 CU 计算资源。

### 日志状态
显示当前地域的运行日志的开启状态，若要进行调整则需要到【诊断日志】>【运行日志】>【日志投递设置】中进行操作。详情可参考 [查看作业日志信息](https://cloud.tencent.com/document/product/849/48288) 中的开启运行日志。
