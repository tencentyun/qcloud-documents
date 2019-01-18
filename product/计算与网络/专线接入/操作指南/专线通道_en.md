## Applying for a Tunnel

1) Open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn).
2) Click "New" to initiate the application for a Direct Connect tunnel. You need to enter the following information to create a Direct Connect tunnel:
<style>
table th:first-of-type {
    width: 150px;
}
</style>

| Parameter        | Description                               | Remarks       |
| --------- | -------------------------------- | -------- |
| Direct Connect Tunnel Name    |                                  |          |
| Direct Connect Type      | My Direct Connect refers to the physical Direct Connect under your own account, and Shared Direct Connect refers to the physical Direct Connect under others account |          |
| Direct Connect ISP     | It's required to enter the account under which the physical Direct Connect is shared with you                | It's valid only for shared Direct Connect |
| Physical Direct Connect      | Select or enter a ID of the physical Direct Connect for which you want to setup a tunnel            |          |
| Access Network      | Virtual Private Cloud and Blackstone Network are supported                      |          |
| Virtual Private Cloud / Blackstone Network | Select the ID of the network to which your physical Direct Connect is accessed                    |          |
| Max Bandwidth      | Bandwidth limit for Direct Connect tunnel, with no limit when left blank              |          |
| Route Mode      | BGP route and static route are supported                     |          |
| BGP ASN   | Optional, assigned by system when left blank                     |          |
| BGP Key   | Optional, assigned by system when left blank                     |          |
| Note        |                                  |          |

After the application for a Direct Connect Tunnel is submitted, the system will issue a ticket to the Direct Connect manager within 3 business days. The manager will coordinate relevant staff to complete the configuration for you. During configuration process, the system will automatically configure a Vlan ID and a PEER IP for you and you can consult the Direct Connect manager if any question.

## Editing a Tunnel

Currently, the system only supports the creation and deletion of a Direct Connect tunnel. To change the information about a Direct Connect tunnel, you have to delete the existing tunnel and re-create it.

## Deleting a Tunnel

1) Open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn).

2) Locate the Direct Connect tunnel to delete in the list, click "Delete" and then "OK".

3) Direct Connect managers will complete the deletion within three business days.

## Viewing the Monitoring Information

It's possible to query monitoring information (outbound and inbound bandwidth, latency) of a Direct Connect tunnel, and this can be done in the console or via API. The procedure in the console is as follows:

1) open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn).

2) Locate the Direct Connect tunnel in the list, and click the "Monitoring" button to query its monitoring information.

## Configuring Alarm

It's possible to configure alarms for a Direct Connect tunnel. The configuration steps are as follows:

1) Open [Tencent Cloud Cloud Monitoring - Alarm Policy Console](https://console.cloud.tencent.com/monitor/policylist).

2) Enter the name of the alarm policy.

3) Click "Add alarm policy" to edit the alarm policy:

- Select "Direct Connect Tunnel" for Policy Type.
- The alarm trigger condition can be selected as "outbound bandwidth", "inbound bandwidth", "packet loss rate", and "latency".

4) Click "Next: Associate Alarm Object", and select the associated Direct Connect tunnel.

5) Set the receiving group and click OK to complete the configuration of the alarm policy.

After the Direct Connect tunnel alarm is configured, you can receive the system alarm according to the setting of the alarm receiving group. For more information on monitoring, refer to [Help for Cloud Monitoring](https://cloud.tencent.com/doc/product/248/967).
