
<dx-alert infotype="explain" title="">
本文来自 [GPU 云服务器用户实践征文](https://cloud.tencent.com/document/product/855/71869)，仅供学习和参考。
</dx-alert>

## 操作场景
您可通过 Docker 快速在 GPU 实例上运行 TensorFlow，且该方式仅需实例已安装 NVIDIA® 驱动程序，无需安装 NVIDIA® CUDA® 工具包。

本文介绍如何在 GPU 云服务器上，使用 Docker 安装 TensorFlow 并设置 GPU/CPU 支持。


## 说明事项
- 本文操作步骤以 Ubuntu 20.04 操作系统的 GPU 云服务器为例。
- 您的 GPU 云服务器实例需已安装 GPU 驱动。
<dx-alert infotype="explain" title="">
建议使用公共镜像创建 GPU 云服务器。若选择公共镜像，则勾选“后台自动安装GPU驱动”即可预装相应版本驱动。该方式仅支持部分 Linux 公共镜像，详情请参见 [各实例支持的 GPU 驱动版本及安装方式](https://cloud.tencent.com/document/product/560/76423#supportList)。
</dx-alert>



## 操作步骤

### 安装 Docker
1. 登录实例，依次执行以下命令，安装所需系统工具。
```shellsession
sudo apt-get update
```
```shellsession
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
2. 执行以下命令，安装 GPG 证书，写入软件源信息。
```shellsession
sudo mkdir -p /etc/apt/keyrings
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
3. 依次执行以下命令，更新并安装 Docker-CE。
```shellsession
sudo apt-get update
```
```shellsession
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```



### 安装 TensorFlow

#### 设置 NVIDIA 容器工具包
1. 执行以下命令，设置包存储库和 GPG 密钥。详细信息请参见 [Setting up NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit)。
```shellsession
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
2. 执行以下命令，安装 nvidia-docker2 包及依赖项。
```shellsession
sudo apt-get update
```
```shellsession
sudo apt-get install -y nvidia-docker2
```
3. 执行以下命令，设置默认运行时重启 Docker 守护进程完成安装。
```shellsession
sudo systemctl restart docker
```
4. 此时可执行以下命令，通过运行基本 CUDA 容器来测试工作设置。
```shellsession
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
返回结果如下所示：
```shellsession
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.51.06    Driver Version: 450.51.06    CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            On   | 00000000:00:1E.0 Off |                    0 |
| N/A   34C    P8     9W /  70W |      0MiB / 15109MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

#### 下载 TensorFlow Docker 镜像

官方 TensorFlow Docker 镜像位于 [tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/) Docker Hub 代码库中。镜像版本按照以下格式进行 [标记](https://hub.docker.com/r/tensorflow/tensorflow/tags/)：

<table>
<thead>
<tr>
<th align="left">标记</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>latest</code></td>
<td align="left">TensorFlow CPU 二进制镜像的最新版本。（默认版本）</td>
</tr>
<tr>
<td align="left"><code>nightly</code></td>
<td align="left">TensorFlow 镜像的每夜版。（不稳定）</td>
</tr>
<tr>
<td align="left"><code>version</code></td>
<td align="left">指定 TensorFlow 二进制镜像的版本，例如 2.1.0。</td>
</tr>
<tr>
<td align="left"><code>devel</code></td>
<td align="left">TensorFlow <code>master</code> 开发环境的每夜版。包含 TensorFlow 源代码。</td>
</tr>
<tr>
<td align="left"><code>custom-op</code></td>
<td align="left">用于开发 TensorFlow 自定义操作的特殊实验性镜像，详情请参见 <a href="https://github.com/tensorflow/custom-op">tensorflow/custom-op</a>。</td>
</tr>
</tbody></table>
每个基本标记都有会添加或更改功能的变体：
<table>
<thead>
<tr>
<th align="left">标记变体</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>tag</code> <code>-gpu</code></td>
<td align="left">支持 GPU 的指定标记版本。</td>
</tr>
<tr>
<td align="left"><code>tag</code> <code>-jupyter</code></td>
<td align="left">针对 Jupyter 的指定标记版本（包含 TensorFlow 教程笔记本）。</td>
</tr>
</tbody></table>

您可以一次使用多个变体。例如，以下命令会将 TensorFlow 版本镜像下载到计算机上：
```shellsession
docker pull tensorflow/tensorflow                     # latest stable release
docker pull tensorflow/tensorflow:devel-gpu           # nightly dev release w/ GPU support
docker pull tensorflow/tensorflow:latest-gpu-jupyter  # latest release w/ GPU support and Jupyter
```


#### 启动 TensorFlow Docker 容器
启动配置 TensorFlow 的容器，请使用以下命令格式。如需了解更多信息，请参见 [Docker run reference](https://docs.docker.com/engine/reference/run/)。
```shellsession
docker run [-it] [--rm] [-p hostPort:containerPort] tensorflow/tensorflow[:tag] [command]
```


## 示例
### 使用仅支持 CPU 的镜像的示例
如下所示，使用带 `latest` 标记的镜像验证 TensorFlow 安装效果。Docker 会在首次运行时下载新的 TensorFlow 镜像：
```shellsession
docker run -it --rm tensorflow/tensorflow \
   python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
其他 TensorFlow Docker 方案示例如下：

- 在配置 TensorFlow 的容器中启动 `bash` shell 会话：
```shellsession
docker run -it tensorflow/tensorflow bash
```
- 如需在容器内运行在主机上开发的 TensorFlow 程序，请通过 `-v hostDir:containerDir -w workDir` 参数，装载主机目录并更改容器的工作目录。示例如下：
```shellsession
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
```
<dx-alert infotype="explain" title="">
向主机公开在容器中创建的文件时，可能会出现权限问题。通常情况下，最好修改主机系统上的文件。
</dx-alert>
- 使用 nightly 版 TensorFlow 启动 Jupyter 笔记本服务器：
```shellsession
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-jupyter
```
请参考 [Jupyter 官网](https://jupyter.org/) 相关说明，使用浏览器访问 `http://127.0.0.1:8888/?token=...`。


### 使用支持 GPU 的镜像的示例
执行以下命令，下载并运行支持 GPU 的 TensorFlow 镜像。
```shellsession
docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
设置支持 GPU 镜像可能需要一段时间。如果重复运行基于 GPU 的脚本，您可以使用 `docker exec` 重复使用容器。
执行以下命令，使用最新的 TensorFlow GPU 镜像在容器中启动 `bash` shell 会话：
```shellsession
docker run --gpus all -it tensorflow/tensorflow:latest-gpu bash
```
