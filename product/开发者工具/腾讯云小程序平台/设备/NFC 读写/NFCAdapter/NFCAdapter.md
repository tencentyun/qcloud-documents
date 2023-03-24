# NFCAdapter

> 支持度：
>
> Android版：支持
>
> iOS版：不支持

## 属性

### Object tech

标签类型枚举

| 属性             | 类型   | 说明                                                         |
| :--------------- | :----- | :----------------------------------------------------------- |
| ndef             | string | 对应 Ndef 实例，实例支持对 NDEF 格式的 NFC 标签上的 NDEF 数据的读写 |
| nfcA             | string | 对应 NfcA 实例，实例支持NFC-A (ISO 14443-3A)标准的读写       |
| nfcB             | string | 对应 NfcB 实例，实例支持NFC-B (ISO 14443-3B)标准的读写       |
| isoDep           | string | 对应 IsoDep 实例，实例支持ISO-DEP (ISO 14443-4)标准的读写    |
| nfcF             | string | 对应 NfcF 实例，实例支持NFC-F (JIS 6319-4)标准的读写         |
| nfcV             | string | 对应 NfcV 实例，实例支持NFC-V (ISO 15693)标准的读写          |
| mifareClassic    | string | 对应 MifareClassic 实例，实例支持MIFARE Classic标签的读写    |
| mifareUltralight | string | 对应 MifareUltralight 实例，实例支持MIFARE Ultralight标签的读写 |

## 方法

### [NFCAdapter.startDiscovery()](./NFCAdapter.startDiscovery.md)

### [NFCAdapter.stopDiscovery()](./NFCAdapter.stopDiscovery.md)

### [Ndef NFCAdapter.getNdef()](./NFCAdapter.getNdef.md)

获取 Ndef 实例，实例支持对 NDEF 格式的 NFC 标签上的 NDEF 数据的读写

### [NfcA NFCAdapter.getNfcA()](./NFCAdapter.getNfcA.md)

获取 NfcA 实例，实例支持NFC-A (ISO 14443-3A)标准的读写

### [NfcB NFCAdapter.getNfcB()](./NFCAdapter.getNfcB.md)

获取 NfcB 实例，实例支持NFC-B (ISO 14443-3B)标准的读写

### [IsoDep NFCAdapter.getIsoDep()](./NFCAdapter.getIsoDep.md)

获取 IsoDep 实例，实例支持ISO-DEP (ISO 14443-4)标准的读写

### [NfcF NFCAdapter.getNfcF()](./NFCAdapter.getNfcF.md)

获取 NfcF 实例，实例支持NFC-F (JIS 6319-4)标准的读写

### [NfcV NFCAdapter.getNfcV()](./NFCAdapter.getNfcV.md)

获取 NfcV 实例，实例支持NFC-V (ISO 15693)标准的读写

### [MifareClassic NFCAdapter.getMifareClassic()](./NFCAdapter.getMifareClassic.md)

获取 MifareClassic 实例，实例支持MIFARE Classic标签的读写

### [MifareUltralight NFCAdapter.getMifareUltralight()](./NFCAdapter.getMifareUltralight.md)

获取 MifareUltralight 实例，实例支持MIFARE Ultralight标签的读写

### [NFCAdapter.onDiscovered(function listener)](./NFCAdapter.onDiscovered.md)

监听 NFC Tag

### [NFCAdapter.offDiscovered(function listener)](./NFCAdapter.offDiscovered.md)

移除 NFC Tag的监听函数

