## Applying for Direct Connect

All applications for Tencent Cloud physical Direct Connect (including Cloud Physical Machine, ECN, etc.) need to be initiated and completed on the console. Tencent Cloud Direct Connect is only available to those enterprise customers qualified by Tencent Cloud. For more information on enterprise certification, please refer to the relevant documents [How to Complete the Enterprise Certification](https://cloud.tencent.com/doc/product/378/3629#.E4.BC.81.E4.B8.9A.E7.94.A8.E6.88.B7.E6.80.8E.E4.B9.88.E5.AE.8C.E6.88.90.E4.BC.81.E4.B8.9A.E8.AE.A4.E8.AF.81.3F).

Please follow the following steps to complete the application and construction of Tencent Cloud physical Direct Connect:

- Submitting Application on Console
- Waiting for Resource Auditing and Verification by Tencent Cloud
- Making Payment via Console
- Completing Physical Direct Connect Access and Acceptance

### Submitting Application on Console

1) Open [Tencent Cloud Direct Connect Console - Physical Direct Connect](https://console.cloud.tencent.com/vpc/dc).

2) Click **New** to initiate the application for the physical Direct Connect. The user initiating construction of a physical Direct Connect should fill in the following information:

| Parameter        | Description                                       | Remarks              |
| -------- | ---------------------------------------- | --------------- |
| Direct Connect Name     | Name of the physical Direct Connect                                  |                 |
| Direct Connect Provider    | The following options are included: China Telecom, China Mobile, China Unicom, China Other (all domestic providers other than the three ones), Outside Others (providers outside the Mainland China) |                 |
| Port Type     | Include the following options: 1000Base-T Gigabit Ethernet, 1000Base-LX Gigabit single-mode optical port (10km), 10GBase-LR 10 Gigabit single-mode optical port (10km) | For special port, please consult the dedicated account manager for Direct Connect business |
| Access Points      | Access point of the physical Direct Connect access to Tencent Cloud. It is recommended to select an access point of the same city to lower the cost paid to your operator. Several access points of the same city with independent network equipment resources can be used for disaster recovery.  |                 |
| Bandwidth       | Support 2 - 10000 Mbps                            |                 |
| IDC Address    | Detailed mailing address                                 |                 |
| Contact Mobile    | Mobile number of the contact for Direct Connect business                              |                 |
| Contact Email    | Email address of the contact for Direct Connect business                           |                 |

After the construction application is submitted, the physical Direct Connect will change to "Applying" status, and the Tencent Cloud's Direct Connect manager will evaluate your application for Direct Connect within 3 business days.

### Evaluating the Physical Direct Connect

After receiving your application for Direct Connect, the Tencent Cloud's Direct Connect manager will execute a comprehensive assessment on Direct Connect resources and check with you the details of the  Direct Connect service via telephone. After the physical Direct Connect is verified and approved, the manager will change its status to "Payment Pending".

However, the application for physical Direct Connect may be refused in the following circumstances:

- Inaccurate information: Access information input is not complete. Please update the application according to the Direct Connect manager's feedback.
- Insufficient resource: Access port or uplink bandwidth resources are not satisfied. Please resubmit the application again according to the Direct Connect manager's feedback after the resources are satisfied.
- No qualification: The physical Direct Connect is only available for enterprise customers of a certain scale. Please resubmit your application after updating your enterprise qualification.

### The Payment and Construction of the Physical Direct Connect

You can make payment in the console after the application for the physical Direct Connect is approved by the Tencent Cloud's Direct Connect manager.

1) Open [Tencent Cloud Direct Connect Console - Physical Direct Connect](https://console.cloud.tencent.com/vpc/dc).

2) In the physical Direct Connect list, locate the physical Direct Connect to be paid and click "Make Payment".

3) After confirming the Direct Connect access information again in the pop-up window, click "OK".

4) Enter the billing platform to complete the payment.

After the payment is successfully made via the console, the Direct Connect manager will immediately take up the access request, and coordinate consequential construction and access matters. The physical Direct Connect will change to "In Operation" status automatically after its construction.

## Canceling Direct Connect

Currently, you can't cancel a physical Direct Connect in the console, but you can do it offline with your dedicated physical Direct Connect manager.

## Sharing Direct Connect

You can setup a Direct Connect tunnel by sharing the physical Direct Connect under other accounts. You can also share a physical Direct Connect under your account with other Tencent Cloud customers. For operation guide, please refer to the [Operation Documentation](https://cloud.tencent.com/doc/product/216/548) of Direct Connect.

## Viewing the Monitoring Information

It's possible to query monitoring information (outbound and inbound bandwidth, packet loss rate, latency) of a physical Direct Connect, and this can be done in the console or via API. The procedure in the console is as follows:

1) Open [Tencent Cloud Direct Connect Console - Physical Direct Connect](https://console.cloud.tencent.com/vpc/dc).

2) Locate the physical Direct Connect in the list, and click the "Monitoring" button to query its monitoring information.

## Configuring Alarm

It's possible to configure alarms for a physical Direct Connect. The configuration steps are as follows:

1) Open [Tencent Cloud Cloud Monitoring - Alarm Policy Console](https://console.cloud.tencent.com/monitor/policylist).

2) Enter the name of the alarm policy.

3) Click "Add alarm policy" to edit the alarm policy:

- Select "Physical Direct Connect" for Policy Type.
- The alarm trigger condition can be selected as "outbound bandwidth", "inbound bandwidth", "packet loss rate", and "latency".

4) Click "Next: Associate Alarm Object", and select the associated physical Direct Connect.

5) Set the receiving group and click OK to complete the configuration of the alarm policy.

After the physical Direct Connect alarm is configured, you can receive the system alarm according to the setting of the alarm receiving group. For more information on monitoring, refer to [Help for Cloud Monitoring](https://cloud.tencent.com/doc/product/248/967).
