

虚拟机部署 Demo: [tsf_python_vm_demo >>](https://main.qcloudimg.com/raw/cfc64e09c79e05581275ad6baaa1b20c/tsf_python_vm_demo-1108.zip) 

容器部署 Demo: [tsf_python_docker_demo >>](https://main.qcloudimg.com/raw/e94cd237b6e49b0cb3f34a024926544a/tsf_python_docker_demo.zip)

Demo 提供了 3 个 Python 应用，对应的服务名分别是：

- user
- shop
- promotion

3 个应用之间的调用关系是：`user => shop => promotion`。



## 工程目录

以 tsf_python_vm_demo 中的 userService 为例说明虚拟机应用工程目录。

- **userService.py 和 common.py**：python 应用程序
- **start.sh**: 启动脚本。
- **stop.sh**: 停止脚本。
- **cmdline**: 检查进程是否存活的文件。
- **spec.yml**: 服务描述文件，具体解释参考 Mesh 开始使用指引。
- **apis 目录**：存放 API 定义的目录， 具体解释参考 Mesh 开始使用指引。



> **程序包格式说明**
>
> 如果程序包是 Java 应用且文件后缀是 `.jar` ，在部署应用时，TSF 会执行 `java -jar xxx.jar` 命令启动应用；如果程序包的后缀名不是 `.jar` （如 Python 应用），在部署应用时，需要将 Python 文件、启停脚本、健康检查脚本压缩成 `zip` 或 `tar.gz` 格式的压缩包进行部署。



以 tsf_python_docker_demo 中的 demo-mesh-user 为例说明容器应用工程目录。

- Dockerfile：使用 userService 目录中 start.sh 脚本来启动 python 应用。
- userService目录：基本结构和 tsf_python_vm_demo中 userService 目录类似，除了没有 stop.sh 和 cmdline 文件。

