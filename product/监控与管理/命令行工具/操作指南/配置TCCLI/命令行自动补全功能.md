本文介绍如何使用 TCCLI 命令行自动补全功能。

## 操作步骤
若您使用 Linux 环境，则可执行以下命令，启动命令自动补全功能。
```bash
complete -C 'tccli_completer' tccli
```
>?您也可以将该命令加入环境变量（`/etc/profile`）中，使自动补全功能一直有效。
