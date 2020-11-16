## 操作场景
本文档将向您介绍如何在 Tensorflow 训练过程中使用 Tensorboard 查看训练模型。

## 操作步骤
### 注意事项
1. 您的训练代码需要处理 Tensorflow 检查点逻辑，写入到`/opt/ml/checkpoints/`目录中，TI SDK 后台将会自动同步`/opt/ml/checkpoints/`至训练任务的 COS 路径中的`output/checkpoints`目录中。
2. Tensorboard 服务默认监听端口为6006，若6006端口不可用时，将会以此从端口6007至端口6105范围尝试可用端口，您可在训练日志输出日志中查看 Tensorboard 服务端口 port。
3. 若提交环境为 Notebook 环境时，您可以通过浏览器中输入域名`{notebook_url}/proxy/{port}/`来访问 Tensorboard 服务，其中{notebook_url}为您的 Notebook 域名，即 Notebook 的域名后加入后缀`/proxy/{port}/`访问 Tensorboard 服务。
4. 若提交环境为本地环境时，您可通过浏览器中输入本机域名`localhost:{port}`来访问 Tensorboard 服务。

### 使用 Tensorboard 查看训练模型
如果在训练任务 fit 函数中传入参数 run_tensorboard_locally，值为 True 时，TI SDK 将会在提交环境中启动 Tensorboard 服务。

以下例子创建了一个使用 Tensorboard 查看模型的训练任务。

```python
tf_estimator = TensorFlow(role=role,
                          train_instance_count=1,
                          train_instance_type='ML.GN8.3XLARGE112',
                          py_version='py3',
                          script_mode=True,
                          framework_version='1.14.0',
                          entry_point='train.py',
                          source_dir='gpu/code')

tf_estimator.fit(inputs, run_tensorboard_locally=True)
```

### Tensorboard 参数
- `run_tensorboard_locally (bool)`：默认值为 False。如果设置为 True，将打印 Tensorboard 服务端口等信息，并在提交环境中启动 Tensorboard 服务。
