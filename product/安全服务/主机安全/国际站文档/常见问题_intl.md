### What will happen when a server is attacked?
1. Interrupted service: Databases and files are tampered with or deleted, resulting in unavailability of service and corruption of system.
2. Data theft: The act of hacker of stealing and selling company data compromises the customers' privacy and causes leakage of confidential data, leading to the damage to company's brand and churn of users.
3. Encryption by ransomware: A hacker who intrudes into a company's server encrypts data and extorts money from the company by embedding irreversible encryption ransomware.
4. Unstable service: A hacker runs mining and DDoS Trojan programs in a server to consume considerable system resources, causing the failure of server to provide services normally.

### How do I achieve data back-up automatically through quick snapshots?
Snapshot is a data backup method provided by Tencent Cloud. It creates a fully available copy of the specified cloud disk to make the backup independent of the cloud disk's lifecycle. By creating snapshots on a regular basis, you can recover data quickly in the event of accidental data loss.
To create a snapshot on the console:
1. Log in to [CVM Console](https://console.cloud.tencent.com/cvm/overview).
2. Click **Cloud Block Storage** in the navigation pane.
3. Locate the row of the instance for which you want to create a snapshot, and then click **Create a Snapshot**.
4. The snapshot is created.

For more information, please see [Snapshot Overview](/document/product/362/5754).

### What should I do when I receive an alert indicating the password has been cracked successfully by brute force attack?
When the password is cracked, the server may be hacked, with a backdoor program embedded into it.
1. Check the security of the server to verify whether other unknown accounts and Trojan files exist. If any, delete them and repair the server immediately, and then modify the login password of the server.
2. If necessary, reset the server, and then set a complicated password that is composed of letters, numbers and special characters with a length of at least 15 characters.

### What should I do when I'm alerted to an abnormal login?
The judgment about abnormal login is based on the administrator's common login location. Check the login log carefully. Any record indicating a login attempt made by a user other than administrator means the password may be leaked. In this case, you need to check the server security thoroughly.

### Why is the protection status of server is displayed as offline? How do I solve it? 
If the Tencent Cloud CVM security component is not connected to the server, the protection status is displayed as offline at backend. It is recommended to download and install the security component again.
The reasons are as follows:
1. Firewall rules are enabled for the server.
2. The installation of third-party malware compromises the security protection program.

### What should I do in case of a failure to detect Trojan file (false negative)?
If any undetected Trojan file is found, please submit a ticket to Tencent Cloud security team for a quick identification.

### How do I uninstall the Tencent Cloud CVM security component?
Log in to the Tencent Cloud CVM security product console, click **Uninstall** on the server list page, or open the installation directory to uninstall it through the uninstall.exe in the directory.
