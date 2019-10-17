### 创建 Integrator
流连接能够与腾讯云上已有的产品通过配置打通数据传输。 对于作为流计算结果输出作用的 Topic，配置其 Integrator 可实现数据自动输出到 TencentDB。
1. 在 Topic 列表中单击【新建Integrator】。
![](https://main.qcloudimg.com/raw/b534bff3b0539e031bb08d23c9b29d99.png)
2. 在弹出的页面中填写 Integrator 信息。 
类型固定选择【CDB For MySQL】，输入目的 TencentDB 数据库的用户名和密码之后，单击【验证】，将会使用该用户名、密码连接 TencentDB 数据库，验证通过后会有提示信息。
![](https://main.qcloudimg.com/raw/b6fe5b6ca6eea6ca593361b693e21bdf.png)
接着在【验证】下方将出现 TencentDB 数据库的库、表选择。
![](https://main.qcloudimg.com/raw/f0bf19a4e2a6a20d1df0664af4002c8f.png)	
3. 选择库、表后，单击【创建】完成 Integrator。	

### 启动和停止 Integrator
只有启动了 Integrator 之后，CDP 才会在后端执行将数据向 TencentDB 导出的任务。所以在创建了 Integrator 之后，请确认启动。
![](https://main.qcloudimg.com/raw/5e6f9ba80017bdeb6ae1192fa59fe8fb.png)
### 删除 Integrator
Integrator 需停止后才能删除。
![](https://main.qcloudimg.com/raw/72a25c390d613f1577f9de85c5204145.png)
