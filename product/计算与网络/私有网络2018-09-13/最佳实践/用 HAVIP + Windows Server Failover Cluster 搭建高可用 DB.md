1. **创建 HAVIP**
登录 [HAVIP 控制台](https://console.cloud.tencent.com/vpc/havip) ，创建一个 HAVIP，具体方法请参见 [创建 HAVIP]()。
2. **绑定和配置**
此处与传统模式配置一样，由后端机器声明和协商哪一设备绑定创建的 HAVIP。您只要在对应的配置文件中指定 virtual IP为 HAVIP。
在群集管理器里，将刚才创建的 HAVIP 配置进去。
 ![1](https://main.qcloudimg.com/raw/960af4c34f05cf71432c0143176db3c2.png)
3. **验证**
等待配置完成后，直接切换节点进行测试。
 ![2](https://main.qcloudimg.com/raw/528373c391c718451acab0db9594ec04.png)
正常情况下会看到只有短暂中断后网络又通了（若切换较快甚至看不到中断），业务不受影响。
 ![3](https://main.qcloudimg.com/raw/de5e3fd284d55c38c0a134efc1badf23.png)