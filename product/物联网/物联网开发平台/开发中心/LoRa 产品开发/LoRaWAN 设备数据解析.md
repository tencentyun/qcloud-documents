## 操作场景
由于 LoRaWAN 类资源有限设备不适合直接传输 JSON 格式数据，物联网开发平台提供了“设备数据解析”服务。用户通过编写自定义的解析脚本，可以将设备原始数据转化为产品定义的数据模版协议数据。

## 操作步骤

### 编写脚本

在设备数据解析页签下，编写脚本。

上行数据解析的脚本主函数为 RawToProtocol，其带有 fPort、bytes 两个入参：
- fPort：设备上报的 LoRaWAN 协议数据的 FPort 字段。
- bytes：设备上报的 LoRaWAN 协议数据的 FRMPayload 字段。

脚本主函数的出参为产品数据模版协议格式的对象。

下行数据解析的脚本主函数为 ProtocolToRaw，其入参为产品数据模版协议格式的对象，其出参为至少3个字节的数组：
- 第1字节：下发给设备的 LoRaWAN 协议数据的 FPort 字段。
- 第2字节：bytes 为下发给设备的 LoRaWAN 协议数据的 MType（0 表示 Unconfirmed Data Down，1 表示 Confirmed Data Down）。
- 第3字节：开始为下发给设备的 LoRaWAN 协议数据的 FRMPayload 字段。

![](https://main.qcloudimg.com/raw/83318c5e53ecd928ee960ba4a20ca63c.png)

这里以温湿度传感器做示例说明，设备上行数据共4字节: 
- 第1字节：温度。
- 第2字节：相对湿度。
- 第3、4字节：表示上报周期（单位秒）。
- 设备下行数据为2字节：上报周期（单位秒）。

在上行数据解析部分，javascript 示例代码如下：

```javascript
function RawToProtocol(fPort, bytes) {
    var data = {
        "method": "report",
        "clientToken" : new Date(),
        "params" : {}
    };
    data.params.temperature = bytes[0];
    data.params.humidity = bytes[1];
    data.params.period = bytes[2] | (bytes[3] << 8);
    return data;
}
```

在下行数据解析部分，javascript 示例代码如下：

```javascript
function ProtocolToRaw(obj) {
    var data = new Array();
    data[0] = 5;// fport=5
    data[1] = 0;// unconfirmed mode
    data[2] = obj.params.period & 0x00FF;
    data[3] = (obj.params.period >> 8) & 0x00FF;
    return data;
}
```

### 脚本模拟测试

您也可使用数据解析页面下方的模拟调试工具，如需开发更多的功能，请使用以下模拟脚本。

在设备上行数据的编辑框中填入模拟测试的 bytes 数据，为数组类型，编辑框的右上方可以填入模拟测试的 fPort 字段。

- **上行消息**
假设设备上行原始数据为 0x11451E00，我们将其转化为数组，即上行模拟数据为：[17,69,30,0]，填入设备上行数据的编辑框中。单击**运行**，即可在模拟调试界面右侧查看结果。以温湿度传感器为例：
![](https://main.qcloudimg.com/raw/5acd842a170a06f68610629715d238d7.png)


- **下行消息**
在设备下行数据的编辑框中填入模拟测试的产品数据模版协议格式数据，为对象类型。
假设设备下行原始数据如下，将其填入设备下行数据的编辑框中，以温湿度传感器为例：
```json
{
  "params": {
    "period": 15
  }
}
```
单击**运行**，即可在模拟调试界面右侧查看结果。
![](https://main.qcloudimg.com/raw/55fb6d32d23f3f3a26e01316c7c2025c.png)


### 提交脚本
确认脚本可以正确解析数据后，单击**提交**，将该脚本提交到物联网开发平台，以供数据上下行时，物联网开发平台调用该脚本解析数据。
