使用 GPU 计算型实例的过程中，如果在系统内部使用 nvidia-smi 查看GPU状态，可能遇到没有运行任何使用 GPU的应用，但GPU使用率显示 100% 的情况。这个可能是因为实例加载NVIDIA 驱动时ECC Memory Scrubbing 机制造成。
**处理方法：**
在实例系统内执行如下命令，让GPU driver 进入persistence模式，即可解决GPU使用率显示不正常问题。
```
nvidia-smi -pm 1
```
![](//mc.qcloudimg.com/static/img/7a4b0b9868138d634c21954638bf6ecd/image.png)

执行 nvidia-smi 显示 GPU 使用率 100%异常图：
![](//mc.qcloudimg.com/static/img/1433ef30c3bdfef74026d9a547d984aa/image.png)

处理完毕显示正常示意图：
![](//mc.qcloudimg.com/static/img/40b69a136ee851c37a058df08ec9e86a/image.png)


