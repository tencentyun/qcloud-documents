## 操作操作

用户创建迁移、同步或订阅任务后，仅需要接收指定任务ID的事件消息推送，其他任务不需要，可参考本操作进行配置。 

## 操作步骤

1. 从[云监控](https://console.cloud.tencent.com/monitor)的**告警配置** > **事件规则**访问，或者直接登录[事件总线](https://console.cloud.tencent.com/eb)。
2. 首次登录系统会提醒用户进行授权，请参考[开通事件总线](https://cloud.tencent.com/document/product/1359/56068)进行操作，如果已授权请跳过此步骤。
3. 在左侧导航选择**事件规则**页签，然后在右侧地域选择**广州**，事件集选择**default**，单击**新建事件规则**。
因为云服务产品的事件集默认统一存储在广州，所以此处的地域和事件集不可选择其他内容。
![](https://qcloudimg.tencent-cloud.cn/raw/5ea92347174a96135787dc3ae053d521.png)
4. 配置事件规则，完成后单击**下一步**。
  - 规则名称：请选择能区分业务的规则名称，配置后不可修改。
  - 事件模式：请选择**自定义事件**。
  - 事件模式预览：请拷贝后面的代码样例并替换任务 ID，这里的 ID 指需要监控的 DTS 任务 ID，多个任务用“，”隔开。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/d758b09db99885d5aad538b1d32e6ba4.png" style="zoom:50%;" />

    ```
    {
     "source":"dts.cloud.tencent",
     "subject":"sync-jtXXXXX"
    }
    ```

    DTS 界面的任务 ID 示例：
    ![](https://qcloudimg.tencent-cloud.cn/raw/857306c38c53b2447429109e2746abf1.png)
5. 配置事件的通知方式、接收对象、接收渠道等，触发方式选择**消息推送**。配置完成后点击**完成**。
   如果需要新建接收告警消息的群组，请参考[新建接收人（组）](https://cloud.tencent.com/document/product/248/50408)进行配置。
   如果需要配置不同的触发方式，可以单击最下方的**添加**增加事件目标。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/22c2af8463e3963e371baa874a670b2c.png" style="zoom:60%;" />
6. 返回事件规则列表，确认创建的事件规则已启动 。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ecb151628ef069a6bdb235baa91ebc07.png)