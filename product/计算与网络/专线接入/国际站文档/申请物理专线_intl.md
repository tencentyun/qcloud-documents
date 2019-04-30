All applications for Tencent Cloud physical Direct Connect (such as BM and ECN) shall be initiated and completed in the console. Tencent Cloud Direct Connect is only available to enterprise customers verified by Tencent Cloud. For more information on enterprise verification, please see [how to complete enterprise verification](https://cloud.tencent.com/doc/product/378/3629#.E4.BC.81.E4.B8.9A.E7.94.A8.E6.88.B7.E6.80.8E.E4.B9.88.E5.AE.8C.E6.88.90.E4.BC.81.E4.B8.9A.E8.AE.A4.E8.AF.81.3F).

Complete the application for and setup of Tencent Cloud physical Direct Connect by following the steps below:
![](https://main.qcloudimg.com/raw/1f014b8535afd21c4f7df3e5957a408d.png)

## Apply in the console

1. Open [Tencent Cloud Direct Connect Console - Physical Direct Connect](https://console.cloud.tencent.com/vpc/dc).
2. Click **+ New** to initiate an application for physical Direct Connect. You will be required to fill in the following information:
<style>
table th:first-of-type {
    width: 150px;
}
</style>

| Parameter | Description | Remarks |
| -------- | ---------------------------------------- | --------------- |
| Direct Connect Name | You can define the name of your physical direct connect | Modification allowed |
| Direct Connect Provider | Available options: China Telecom, China Unicom, China Mobile, other providers in Mainland China (select this if your direct connect is provided by a provider in Mainland China other than China Telecom, China Unicom and China Mobile), and providers outside Mainland China (select this if your direct connect is provided by a provider outside Mainland China) |                  |
| Cloud API Type | Indicates the type of the API for connecting the physical direct connect with the Tencent Cloud access device | Select the API type based on your bandwidth. You can consult with your Direct Connect provider or Tencent Cloud's architect or after-sales manager |
| Access Point | The access point for Tencent Cloud physical Direct Connect. We recommend that you select the one nearest to you | The city where the access point locates should at least have two access points for dual-line disaster recovery |
| Bandwidth | Supports 2-100,000 Mbps |                  |
| Your IDC Location | Detailed address | The floor of the IDC should be provided in the address |
| IDC API Type | The type of the API for connecting your IDC device with Direct Connect |          -        |
| Redundant Physical Direct Connect | Determining the master/slave relation between physical direct connects can avoid single point of failure caused by two physical direct connects connecting to the same access device | Determining the master/slave relation is to avoid two lines connecting to the same access point. The master/slave relation of Direct Connect tunnel needs to be applied for on the Direct connect tunnel product page |
| Contact Number | The mobile number of the contact for Direct Connect |           -       |
| Contact Email | The email of the contact for Direct Connect |        <nbsp;> |

After a setup application is submitted, the physical direct connect will go into the "Applying" status, and Tencent Cloud's Direct Connect manager will evaluate your application for Direct Connect within 3 work days.

## Resource review and confirmation by Tencent Cloud

After receiving your application for Direct Connect, Tencent Cloud's Direct Connect manager will execute a comprehensive assessment on Direct Connect resources and check with you the details of the Direct Connect service via telephone. After the physical direct connect is verified and approved, the manager will change its status to "To Be Paid".
However, the application for physical Direct Connect may be rejected under the following circumstances:
- Inaccurate information: The access information you entered is incomplete. Please update the information according to the feedback of the Direct Connect manager and resubmit an application.
- Insufficient resources: Access port or uplink bandwidth resources are insufficient. Please resubmit an application according to the Direct Connect manager's feedback after the resources are sufficient.
- Disqualification: Physical Direct Connect is only available to large-scale enterprise customers. Please resubmit an application after updating the enterprise qualification.

## Payment and acceptance

After your application for physical Direct Connect is approved by Tencent Cloud's Direct Connect manager, you can complete the payment in the console.
1. Open [Tencent Cloud Direct Connect Console - Physical Direct Connect](https://console.cloud.tencent.com/vpc/dc).
2. Find the physical direct connect to be paid in the physical Direct Connect list, and click **Pay**.
3. Confirm the Direct Connect information in the pop-up window, and click **OK**.
4. Enter the billing platform to complete the payment.

Once the payment is completed, the Direct Connect manager will handle the access application and allocate related resources for the setup. The physical direct connect will go into the "Running" status automatically after set up.