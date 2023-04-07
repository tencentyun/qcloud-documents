# MifareClassic

MifareClassic 标签

## 方法

### [MifareClassic.connect()](./MifareClassic.connect.md)

连接 NFC 标签

### [MifareClassic.close()](./MifareClassic.close.md)

断开连接

### [MifareClassic.setTimeout(Object object)](./MifareClassic.setTimeout.md)

设置超时时间

### [MifareClassic.isConnected()](./MifareClassic.isConnected.md)

检查是否已连接

### [MifareClassic.getMaxTransceiveLength()](./MifareClassic.getMaxTransceiveLength.md)

获取最大传输长度

### [MifareClassic.transceive(Object object)](./MifareClassic.transceive.md)

发送数据

对于 MifareClassic 的分块读写

- 指令 0x30 + 块号 可以用于读取某个块的数据
- 指令 0xA0 + 块号 + 待写入数据 可以用于往某个块写入数据