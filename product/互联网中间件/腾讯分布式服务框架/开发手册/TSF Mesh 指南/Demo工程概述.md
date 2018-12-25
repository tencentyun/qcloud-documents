虚拟机部署 Demo：[tsf_python_vm_demo](https://main.qcloudimg.com/raw/cfc64e09c79e05581275ad6baaa1b20c/tsf_python_vm_demo-1108.zip) 
容器部署 Demo：[tsf_python_docker_demo](https://main.qcloudimg.com/raw/449b92688fabd8903e1486f1d00577be/tsf_python_docker_demo-1115.zip)

Demo 提供了 3 个 Python 应用，对应的服务名分别是：
- user
- shop
- promotion

3 个应用之间的调用关系是：`user => shop => promotion`。


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
- **start.sh**：在启动脚本中创建 `/opt/tsf/app_config/` 目录，然后将 spec.yaml 文件和 apis 目录拷贝到 `/opt/tsf/app_config/` 中。
**您需要在容器启动后通过用户程序的启动脚本拷贝目录，不可以在 Dockerfile 中提前拷贝**。
```
#! /bin/bash
mkdir -p /opt/tsf/app_config/apis 
cp /root/app/userService/spec.yaml /opt/tsf/app_config/
cp -r /root/app/userService/apis /opt/tsf/app_config/
cd /root/app/userService/
python ./userService.py 80 1>./logs/user.log 2>&1
```
