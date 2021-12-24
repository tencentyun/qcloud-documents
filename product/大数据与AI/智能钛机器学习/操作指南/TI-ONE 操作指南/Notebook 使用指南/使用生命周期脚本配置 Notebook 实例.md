## 生命周期脚本配置规则
生命周期配置提供 SHELL 脚本，在用户创建 Notebook 实例或每次启动 Notebook 实例时运行，可以帮助用户安装自定义依赖，个性化配置 Notebook 环境。

生命周期配置遵循以下规定：
- 创建脚本：第一次新建 Notebook 后启动 Notebook 实例会运行的脚本，只会运行一次。
- 启动脚本：每次启动 Notebook 实例时都会运行的脚本，包括第一次创建时。
- 每个脚本 BASE64 编码后不能超过16384个字符。
- 每个脚本将以 root 用户的角色运行。
- 每个脚本的 $PATH 环境变量为 `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin`
- 每个脚本最长运行时间为5分钟，超过5分钟 Notebook 将启动失败，请避免在脚本中安装大型依赖包。可在详情页中查看失败原因如“启动脚本超时”。
- 如果脚本出错，Notebook 也将启动失败，可在详情页中查看具体失败原因。
- 如果脚本是从自己的编辑器复制到 TI-ONE 网页上的，请确保编辑脚本的编辑器使用 Unix 风格的编排。


## 生命周期脚本最佳实践
以下是使用生命周期配置的一个实践案例： 
- 生命周期脚本以 root 用户权限运行，Notebook 进程以 tione 用户运行。如果需要切换用户，可以在脚本中运行 sudo -u tione 切换到 tione 用户。
- Notebook 使用 conda 管理多内核，可以激活 conda env 来为不同的内核安装依赖包。

例如：在 conda_python3 的内核中安装 Python 依赖包 fire，可以编写如下启动脚本：

```bash
  #!/bin/bash
  sudo -u tione -i <<'EOF'
  
  # This will affect only the Jupyter kernel called "conda_python3".
  source /opt/conda/bin/activate python3
  
  # Replace fire with the name of the package you want to install.
  pip install fire
  # You can also perform "conda install" here as well.
  
  source /opt/conda/bin/deactivate
  
  EOF
```

例如：在所有内核中都安装 fire 依赖包，可以这样编写脚本：

```bash
  #!/bin/bash
  sudo -u tione -i <<'EOF'
  
  # Note that "base" is special environment name, include it there as well.
  
  for env in base /opt/conda/envs/*; do
      source /opt/conda/bin/activate $(basename "$env")
  
      # Installing packages in the Jupyter system environment can affect stability of your tione
      # Notebook Instance.  You can remove this check if you'd like to install Jupyter extensions, etc.
      if [ $env = 'JupyterSystemEnv' ]; then
        continue
      fi
  
      # Replace myPackage with the name of the package you want to install.
      pip install fire
      # You can also perform "conda install" here as well.
  
      source /opt/conda/bin/deactivate
  done
  
  EOF
```
