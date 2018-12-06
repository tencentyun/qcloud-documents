You can configure monitoring alarms for a physical direct connect by following the steps below:
1. Open [Tencent Cloud Cloud Monitor - Alarm Policy Console](https://console.cloud.tencent.com/monitor/policylist).
2. Enter the alarm policy name.
3. Click **Add** and edit the alarm policy:

 - Select **Physical Direct Connect** for **Policy Type**.
 - Select **Outbound Bandwidth**, **Inbound Bandwidth**, or **Packet Loss** for **Trigger Condition**.
4. Click **Next: Associate Alarm Object**, and select the physical direct connect to be associated.
5. Set the **Alarm Receiver Group**, and then click **OK** to complete the alarm policy configuration.

After the physical Direct Connect alarm is configured, you can receive system alarms according to the setting of the alarm receiver group. For more information on monitoring, please see [Cloud Monitor](https://cloud.tencent.com/doc/product/248/967).