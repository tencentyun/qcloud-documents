Tensorflow 组件为用户提供了基于 Python API 的 Tensorflow 运行环境，用户可将编写好的脚本及依赖文件上传至组件进行算法训练。

### 使用阶段
####  1. 添加组件  
 从TI-ONE __组件 → 深度学习__ 列表下拖拽出 Tensorflow 节点至画布中。
![](https://main.qcloudimg.com/raw/8a027a2862ef1bccaca4f6147cfcd312.png)



####   2. 参数配置
  - 脚本及依赖包文件上传  
      将任务脚本上传至 __程序脚本__ 框。如果需要依赖文件，则压缩为zip文件后通过 __依赖包文件__ 框上传。

  ![](https://main.qcloudimg.com/raw/df11dee8b44c5a2ccac3caf81c04dd93.png)



 - 程序依赖 :
   指定位于Cephfs中的用户依赖文件路径。
 - 程序参数 :
   指定运行任务脚本的参数。
 - TensorBoard目录 :
   指定Tensorboard保存路径。
 - Python版本:
   指定Tensorflow运行的Python版本，支持python2.7及python3.4两个版本。

####   3. 资源配置
  在 __资源参数__ 列表配置任务的资源参数。

  ![](https://main.qcloudimg.com/raw/e0ec88563a76347e06d9af1383c5c581.png)



####   4. Tensorboard查看
  组件处于 __运行中__ 状态时可以右键任务栏，用过 __Tesnorflow控制台 → Tensorboard__ 查看Tensorboard信息。

   ![](https://main.qcloudimg.com/raw/f1b9b972b45638e71c8216b412b38988.png)



