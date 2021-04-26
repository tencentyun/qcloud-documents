## 采集对象
为了提升 SCF SLI 使用体验，了解用户使用情况以及收集规划部分功能的信息，SCF CLI 会采集以下命令的相关数据：

- scf init
- scf deploy
- scf function
- scf eventdata
- scf local
- scf logs
- scf native
- scf state

## 采集内容及用途
**内容：**所采集的数据只有命令和其参数的使用频次，不包括参数值等信息。
**用途：**获取到的统计数据，仅用于 SCF 团队对 CLI 模块的功能升级和性能优化。

## 关闭数据采集

您可以执行 `scf configure set -ar n` 命令关闭数据采集。



