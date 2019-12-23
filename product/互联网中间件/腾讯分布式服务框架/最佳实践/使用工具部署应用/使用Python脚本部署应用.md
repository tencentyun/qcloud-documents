TSF 应用可以使用 Python 脚本来部署。

## 前提条件

在开始持续集成之前，需要完成下述的准备工作。

1. 机器上保证安装的 Python 版本不低于 `2.7.14` 版本，并已安装 PIP 等 Python 包管理工具。

2. 获取腾讯云的访问密钥 [SecretId 和 SecretKey](https://cloud.tencent.com/document/product/598/37140) 。

3. 在 TSF 平台创建了[虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524)或[容器应用部署组](https://cloud.tencent.com/document/product/649/15525)。

4. 了解 Python 脚本使用。

## 虚拟机应用部署准备

1. 机器上保证安装的 Python 版本不低于 `2.7.14` 版本，并已安装 PIP 等 Python 包管理工具。
2. 从 [GitHub仓库](https://github.com/tencentyun/tsf-snippet/blob/master/upload_virtual_machine_deploy.py) 下载虚拟机部署 Python 脚本。
3. 修改脚本中的secret_id 、secret_key 为腾讯云访问密钥, region 为 TSF 服务所在地域。

   ```Python
   secret_id = "改为您的 SecretId"
   secret_key = "改为您的 SecretKey。"
   region = "改为您的服务所在地域，如 ap-guangzhou"
   ```

4. 安装脚本依赖包。

   ```Shell
   pip install requests cos-python-sdk-v5
   ```

5. 准备脚本参数，要严格保证参数顺序  
   - `path` : 本地文件路径，可以是针对脚本的相对路径,支持 `.tar.gz`,`.jar`,`.war`,`.zip` 结尾的文件。  
   - `applicationId` : 应用 ID。在 TSF 控制台左侧导航栏【应用管理】，选择目标应用第一列的应用 ID（如`application-qab76pxv`)。
   - `pkg_version` : 程序包版本，最长32个字符，支持 a-z，A-Z，0-9，横杠(-)、下划线(_)。  
   - `appId` : 用户 APPID。在腾讯云控制台账号中心>账号信息中获取 APPID（如`1300555551`)。
   - `group_id` : 部署组ID。在 TSF 控制台，单击目标应用ID，进入详情页，在【部署组】标签页中获取部署组的ID（如`group-gvk5pbdv`)。
   - `startup_params` : 启动参数。用户视情况可以自定义。

   ```Shell
   -Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m
   ```
    >**注意**：执行的脚本参数中如果版本号不变时，脚本会选择 TSF 平台已有的 jar 包进行再次部署。
6. 将以上参数按照顺序整理待用，格式形如下

   ```shell
   python2.7.14 upload_virtual_machine_deploy.py ./consumer-demo/target/consumer-demo-1.10.0-RELEASE.jar application-qab76pxv v001 1300555551 group-gvk5pbdv '-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m'
   ```

## 容器应用部署准备

1. 保证机器上能够构建、上传镜像（镜像及Dockerfile编写参考 [制作容器镜像](https://cloud.tencent.com/document/product/649/17007)，仓库使用请参考 [镜像仓库](https://cloud.tencent.com/document/product/649/16695)）。保证  Python 版本不低于 2.7.14 版本，并已安装 PIP 等 Python 包管理工具。
2. 从 [GitHub仓库](https://github.com/tencentyun/tsf-snippet/blob/master/upload_container_deploy.py) 下载容器部署Python脚本。
3. 修改脚本中的secret_id 、secret_key 为腾讯云访问密钥, region 为 TSF 服务所在地域。修改脚本中的 docker_build_command、docker_push_command 为 实际的 docker build 和 push 命令。

   ```Python
   secret_id = "改为Access Key ID"
   secret_key = "改为Access Key Secret。"
   docker_build_command = "改为 docker build 命令"
   docker_push_command = "改为 docker push 命令"
   region = "改为您的服务所在地域，如 ap-guangzhou"
   ```

4. 安装脚本依赖包

   ```Shell
   pip install tencentcloud-sdk-python
   ```

5. 准备脚本参数，要严格保证参数顺序  

   - `group_id` : 部署组ID。在 TSF 控制台，单击目标应用ID，进入详情页，在【部署组】标签页中获取部署组的ID(如`group-zvw397wa`)。

   - `tag_name` : 镜像版本名称,如v1。

> **注意**：目前容器应用部署脚本只将 group_id和tag_name 作为参数，但实际上用户可以修改脚本，将其他字段（如JVM启动参数 JvmOpts 等）作为脚本参数，参考 [容器应用部署 API](https://cloud.tencent.com/document/product/649/36071)。

6. 将以上参数按照顺序整理，并且加入第一步中用户自己的 docker build 、push命令待用，格式形如下

   ```shell
   python2.7.14 upload_container_deploy.py group-zvw397wa v1
   ```

> **注意：** docker 相关命令必须按照 [制作容器镜像](https://cloud.tencent.com/document/product/649/17007), [镜像仓库](https://cloud.tencent.com/document/product/649/16695) 调整为用户自己的账号和应用名。