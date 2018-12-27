虚拟机部署 Demo：[tsf_python_vm_demo](https://main.qcloudimg.com/raw/18374feb774a9be209d47bd5d3ab9914/tsf_python_vm_demo-1225.tar.gz) 
容器部署 Demo：[tsf_python_docker_demo](https://main.qcloudimg.com/raw/69a7f9a875481662871efd2345ac4ff0/tsf_python_docker_demo-1225.tar.gz)

Demo 提供了 3 个 Python 应用，对应的服务名分别是：
- user
- shop
- promotion

默认的监听端口为**80**，如果需要更改应用监听端口，将**start.sh**和**spec.yaml**中对应的80端口改掉即可(**注意：两个文件都要修改**)
3 个应用之间的调用关系是：`user -> shop -> promotion`。


## 工程目录
### 虚拟机工程目录
以 tsf_python_vm_demo 中的 userService 为例说明虚拟机应用工程目录。
- **userService.py 和 common.py**：Python 应用程序
- **start.sh**：启动脚本。
- **stop.sh**：停止脚本。
- **cmdline**：检查进程是否存活的文件。
- **spec.yaml**：服务描述文件，具体解释请参考 [Mesh 开发使用指引](https://cloud.tencent.com/document/product/649/19049)。
- **apis 目录**：存放 API 定义的目录， 具体解释请参考 [Mesh 开发使用指引](https://cloud.tencent.com/document/product/649/19049)。

其中 star.sh、stop.sh、cmdline 的编写方法请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)。


### 容器应用工程目录
以 tsf_python_docker_demo 中的 demo-mesh-user 为例说明容器应用工程目录。
- **Dockerfile**：使用 userService 目录中 start.sh 脚本来启动 Python 应用。
- **userService**目录：基本结构和 tsf_python_vm_demo中 userService 目录类似，除了没有 stop.sh 和 cmdline 文件。
- **start.sh**：应用的启动脚本，user demo的启动脚本如下
```shell
#! /bin/bash
cp /root/app/userService/spec.yaml /opt/tsf/app_config/ 
cp -r /root/app/userService/apis /opt/tsf/app_config/
cd /root/app/userService/
python ./userService.py 80 1>./logs/user.log 2>&1
```
脚本说明：
1) 应用工作目录为`/root/app/userService/`，应用日志目录为`/root/app/userService/logs/user.log`
2) 第2行：创建 `/opt/tsf/app_config/apis` 目录
3) 第3行：将`spec.yaml`文件拷贝到`/opt/tsf/app_config/` 中。
4) 第4行：将`apis`目录拷贝到`/opt/tsf/app_config/` 中。
5) 第5行：启动user应用

> **注意：** 您需要在容器启动后通过用户程序的启动脚本拷贝目录，不可以在 Dockerfile 中提前拷贝。

