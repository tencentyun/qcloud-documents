### WebShell Detection
WebShell is a tool commonly used by hackers for intrusion into users' systems. Host Security client analyzes the suspicious risks for the new Web program files on the server, and reports a small number of suspected WebShell files to the cloud, where a further detection is performed through the machine learning-based detection engine module. After the detection is completed, the sample file is deleted in real time, and no data related to user privacy is fetched during the process. 

### Abnormal Login Alert
This module allows you to identify abnormal administrator login behaviors. The source IP, time, login user name and login status data in the login log need to be collected for computing risks. The login log data is retained on cloud for one month. 

### Password Cracking Alert
Password cracking alert notifies you of the current password cracking event and cracking result. The source IP, time, login user name and login status data in the login log need to be collected for computing risks. The login log data is retained on cloud for one month. 

### Trojan Detection
Malicious Trojan programs steal user data or attack users' systems, consuming a large amount of system resources and causing the failure of servers to provide services normally. The client collects the hash fingerprints of suspected malicious programs to the cloud and detects hash values through the Cloud Antivirus module. If the hash library on cloud does not have the file record, it reports the executable files to the cloud, where a further detection is performed through the antivirus engine on cloud. After the detection is completed, the sample file is deleted in real time, and no data related to user privacy is fetched during the process. 

### Vulnerability Alert
The vulnerability management module presents the vulnerability risks on the current server and provides a repair solution to you for reference. This module downloads vulnerability policy library from the cloud to perform detection locally, and reports the name, version number, path, and discovery time of application for a server with vulnerability risk. No data related to user privacy is fetched during the process. 

### Upgrade and Maintenance
The upgrade and maintenance module is used to remind you to upgrade the client to enjoy the latest security protection services. The client software needs to collect the Host Security version number, operating system configuration information, and security rule version number to the cloud for analysis and reminding users. No data related to user privacy is fetched during the process. 
