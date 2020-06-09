CUDA（Compute Unified Device Architecture）是显卡厂商 NVIDIA 推出的运算平台。 CUDA™ 是一种由 NVIDIA 推出的通用并行计算架构，该架构使 GPU 能够解决复杂的计算问题。 它包含了 CUDA 指令集架构（ISA）以及 GPU 内部的并行计算引擎。 开发人员现在可以使用 C 语言, C++ , FORTRAN 来为 CUDA™ 架构编写程序，所编写出的程序可以在支持 CUDA™ 的处理器上以超高性能运行。
GPU 云服务器采用 NVIDIA 显卡，需要安装 CUDA 开发运行环境。以目前最常用的 CUDA 7.5 为例，可参照以下步骤进行安装。
## Linux 系统指引
1. 登录 [CUDA 驱动下载](https://developer.nvidia.com/cuda-toolkit-archive) 或复制链接https://developer.nvidia.com/cuda-toolkit-archive 。

2. 选择对应的CUDA版本，以CUDA Toolkit 10.1为例。

  ![](https://main.qcloudimg.com/raw/06c748a5d801bbf72cf1129e8f2731a3.png)

3. 根据指引，依次选择操作系统和安装包。可按如下方式进行选择：

  ![](https://main.qcloudimg.com/raw/4a86015192c428d753b535d837b1830e.png)
>!
>- Installer Type 推荐选择 runfile（local）。
>- network：网络安装包，安装包较小，需要在主机内联网下载实际的安装包。
>- local：本地安装包。安装包较大，包含每一个下载安装组件的安装包。

3. 选择完成出现如下图信息时，右击【Download】，右键菜单里选择复制链接。

![](https://main.qcloudimg.com/raw/536c988aaf8326276fe821efe22daf62.png)

4. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 CUDA 安装包， 上传到 GPU 实例的服务器。

![](https://main.qcloudimg.com/raw/d96e4c0456686c2a3159297c3ab3b12b.png)

5. 对安装包加执行权限。例如，对文件名为 `cuda_10.1.105_418.39_linux.run` 加执行权限：

   ```
     sudo chmod +x cuda_10.1.105_418.39_linux.run
   ```

   ```
     ./cuda_10.1.105_418.39_linux.run --toolkit --samples --silent
   ```

6. 重启系统。

7. 配置环境变量

     ```
     echo 'export PATH=/usr/local/cuda/bin:$PATH' | sudo tee /etc/profile.d/cuda.sh
     ```

     ```
     source /etc/profile
     ```

8. 验证CUDA安装是否成功。进入目录 `cd /usr/local/cuda-10.1/samples/1_Utilities/deviceQuery` ，执行`make`命令。如果出现如下图所示错误：

   ![](https://main.qcloudimg.com/raw/5806df458bae9565139d790881c45520.png)

   则执行`yum install -y gcc-c++` 命令，安装对应的gcc包即可。

   安装完成后，依次执行 `make`命令和 `./deviceQuery`命令，如果结果显示Result=PASS，则证明CUDA安装成功。

## Windows 系统指引
要在 Windows 实例上安装 CUDA ，请使用远程桌面以管理员的身份登录您的 Windows 实例。
1. 登录 [CUDA 驱动官网](https://developer.nvidia.com/cuda-toolkit-archive) 。

2. 选择对应的CUDA版本，以CUDA Tookit 10.1为例，选择要安装的CUDA版本。

   ![](https://main.qcloudimg.com/raw/06c748a5d801bbf72cf1129e8f2731a3.png)

3. 根据指引，操作系统和安装包，如下图所示：

   ![](https://main.qcloudimg.com/raw/d2410cf9db9f455364684c0b1f11930d.png)

4. 打开下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装CUDA并重启实例。
   
5. 启动安装程序，按提示进行安装，如果最后出现完成对话框，则安装成功。
    ![](https://main.qcloudimg.com/raw/95f81b3da548d2ab0444ca2df9d4a06a.png)



