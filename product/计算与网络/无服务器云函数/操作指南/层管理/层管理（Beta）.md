如果您的云函数拥有非常多的依赖库或公共代码文件，您可以使用层进行管理。

使用层，您可以将依赖放在层中而不是部署包中，以使您的部署包保持较小的体积。在函数执行环境中，层将被解压到 /opt 目录。

对于 Node.js、Python 和 PHP 函数，只要将部署程序包保持在 10 MB 以下，就可以在云函数控制台的在线 Cloud Studio Lite IDE 中开发函数代码。

使用层，可以使您的部署包保持较小的体积。对于 Node.js、Python 和 PHP 函数，只要将部署程序包保持在 10 MB 以下，就可以在云函数控制台中开发函数代码。

## 创建层
1. 进入云函数控制台点击左侧“层”按钮，进入“层”界面。如图所示。
![](https://main.qcloudimg.com/raw/19209a4403cf1c0f7014cc6a4a316238.png)

2. 点击“新建”按钮。如图所示。
![](https://main.qcloudimg.com/raw/bdeed523cd0c72de656692e1d0413e8b.png)

3. 在弹出的“新建层版本”界面输入层名称等信息，如图所示。
![](https://main.qcloudimg.com/raw/d91c72f70cfea55e10b6eccf2c232417.png)

4. 点击“确定”完成创建。

## 为云函数绑定层
1. 进入云函数控制台点击左侧“函数服务”按钮，进入“函数服务”界面。如图所示。
![](https://main.qcloudimg.com/raw/5049db3925672d0ac180339d9f064e67.png)

2. 点击任意函数，进入函数配置页面，再点击"层管理"标签，如图所示。点击“绑定层”按钮，即可见层管理弹窗。
![](https://main.qcloudimg.com/raw/1832cd790c58ddf1c261a647b6304fe7.png)

3. 选择“层名称”和对应的“层版本”，处点击“提交”。即可以绑定一个层。
![](https://main.qcloudimg.com/raw/29220f40141449014f8bb69948c02780.png)

4. 在弹出的依赖包选择界面中，选择依赖包，点击确定，如图3所示。
![](https://main.qcloudimg.com/raw/29220f40141449014f8bb69948c02780.png)



##使用层

层中的文件会被放在 /opt 目录中，在函数执行期间可访问。如果您的函数有绑定多个层，这些层将按照序号顺序被合并到 /opt 目录中。如果同一文件出现在多个层中，将会保留最高序号层里的文件。

| 相关环境变量 | 路径                                                         |
| ----------------------- | ------------------------------------------------------------ |
| PYTHONPATH              | /var/user:/opt                                               |
| CLASSPATH               | /var/runtime/java8:/var/runtime/java8/lib/*:/opt             |
| NODE_PATH               | /var/user:/var/user/node_modules:/var/lang/node6/lib/node_modules:/opt:/opt/node_modules |


###以 Node.js 为例
1. 参照创建层的流程将 node_modules 打包上传生成层，并且绑定云函数。
![](https://main.qcloudimg.com/raw/9c61d9afbbbef83d9dc5bd73cf1573ce.png)


2. 函数代码上传打包时，排除 node_modules 文件夹。
![](https://main.qcloudimg.com/raw/3593c35e3a438d8b5f55662d75199ffc.png)

3. 函数使用时，由于 NODE_PATH 环境变量包含 /opt/node_modules 路径，Node.js 运行时启动时可以查找到层中的依赖，您使用依赖的方式和原来一样，不需要修改代码。
![](https://main.qcloudimg.com/raw/5ab54f5d146c037e8ed6b5a5a28dcf28.png)

