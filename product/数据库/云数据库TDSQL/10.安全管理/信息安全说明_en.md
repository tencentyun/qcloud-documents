>The following statements are specifically made for this document
>
>1. This document is designed to provide customers with Tencent Cloud's security overview on Cloud Database products and services. The content of some products and services may be subject to adjustment. For any mandatory requirements, you are recommended to make agreements with Tencent Cloud using a written business contract (SLA). Otherwise, Tencent Cloud will not make any expressed or implied commitments or warranties on this document.
>2. There is a wide range of security features, but only "some" of the technical security points are covered in this document;
>3. This document is not used as a reference to relevant standards and requirements on national or industrial information security;
>4. This document is enhanced in terms of readability, for any inaccurate descriptions, please see point 1.
>5. Tencent Cloud reserves the right of interpretation of this document.

## 1. Overview
Tencent Cloud Database has passed the following certifications and conforms to the corresponding security requirements
- ISO 22301 certification
- ISO 27001 certification
- ISO 20000 certification
- ISO 9001 certification
- Trusted cloud services certification
- Information security level protection (level 3)
- STAR certification

The following references are also used in the design of some of the Cloud Database features:

- Information security technology - Security techniques requirement for database management system (GBT 20273-2006) (Level 2 or above)
- Testing and Evaluation Guide for Classified Protection of Information System of Financial Industry (JRT 0072-2012) (Level 4)

## 2. Tencent Cloud Database Service Security Protection (OPS Security)
### 2.1 Overview
The requirements for management and technology security of Cloud Database comply with National Information Security Level Protection (Level 3), and some meet the criteria of Financial Industry Information Security (Level 4).


### 2.2 Internal Staff and System Identification

To improve the security of database CVM system and ensure the security of various ops, Tencent Cloud implement a series of reinforcement measures, including but not limited to:
- Identify and authenticate the users who log in to the operating system and database system, to ensure the uniqueness of user name;
- Configure username/password according to basic requirements. The password must contain more than 3 types of characters with a minimum length of 8 characters, and is subject to change on a regular basis;
- Enable login failure handling feature. If login fails, measures such as ending session, setting limit on the number of illegal logins and automatic exit can be taken.
- During remote management, the internal risk control is audited by accessing the system under the monitor of Tencent enterprise IT. Sensitive operations need to be encrypted.
- Two-factor authentication (i.e. authenticate identity using dynamic token + password) is performed on database CVM admin when logging in to OPS system

### 2.3 Internal Staff and System Access Control
Discretionary access control schemes are provided for Tencent Cloud's Cloud Database management systems and admins, including but not limited to:
- Internal ops staff and systems are controlled based on Tencent Cloud security policies (verification requirements are met);
- The granularity of CVM is user level, and the granularity of client is accurate to database table level.
- Strict code management and access control are implemented.
- High-risk system can be only accessed through Tencent Cloud private network (development network), which must be isolated physically from the Internet.


### 2.4 Internal Security Audit
Comprehensive security audit and risk control mechanism is provided: The audit features include but not limited to database operation audit, management system operation audit, file operation audit, plug-in device operation audit, illegal external connection audit, IP address change audit, service and process audit, etc. The audit scope covers every operating system user and database user on the CVM, for example, including: important security-related events in the system, such as the behavior of Tencent Cloud admin, the exceptional use of system resources and the use of important system commands. The audit logs, including the date, time, type, CVM ID, client ID and result of the event, are stored for more than one year in a location with a higher-level security, to prevent them from being accidentally deleted, modified or overwritten.

- Database security audit: Operations performed on the database CVM and database are audited by the database security audit system.
- Management system operation audit: Tencent Cloud records the logs of the operations on internal and external management systems in details to track and trace risks.
- Periodic risk assessment: Tencent Cloud security team performs security assessment on database OPS management on a regular basis.


### 2.5 Internal Intrusion Prevention
To protect database CVM from intrusion, Tencent Cloud has taken measures from different aspects:

- Intrusion detection system can defend the database CVM against intrusion;
- Deploy vulnerability scanning and periodically perform system security detection;
- Deploy terminal security management system, and enable patch distribution function module to upgrade the system patches in time;
- The installation of operating system complies with the minimum installation requirements. Only required components and applications are installed, and unnecessary services should be disabled;
- In addition, other security configurations need to be reinforced based on the system types.

### 2.6 Backup and Recovery
Tencent Cloud Database provides data backup and recovery features in default. 

### 2.7 Secure Reuse of Client
If the client returns the device or replaces the failed device, Tencent Cloud will erase the remaining information in time, to ensure the storage space (memory, hard disk) where all the sensitive information (such as user's authentication information, files, directories, database logs, etc.) are stored is released timely or cleared up before being redistributed to other users.

### 2.8 Non-Repudiation
Tencent Cloud's internal ops staff log in to the system using two-factor authentication and non-repudiation schemes, and all the personnel involved have signed a confidentiality agreement.

### 2.9 More Security Measures
>More details will be available soon.


