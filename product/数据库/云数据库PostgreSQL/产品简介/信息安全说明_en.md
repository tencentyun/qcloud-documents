> The following statement is hereby made for this document.
>
>1. This document is designed to provide an overview of security features of Tencent CDB for PostgreSQL products and services. The security features of some products and services may be subject to adjustment. Any of your mandatory requirements for the security of Tencent Cloud PostgreSQL can be agreed on with Tencent Cloud by entering into a written Service Level Agreement (SLA). Tencent Cloud does not make any express or implied representation or warranty concerning the contents of this document.
> 2. This document only involves "part of" the technical security features among the wide range of security features.
> 3. This document is not intended as the reference document for national or industry information security standards or requirements.
>4. This document has been refined for readability. In the event of any ambiguity or inaccuracy, please refer to Item 1.
> 5. Tencent Cloud reserves the right of interpretation of this document.

## 1. Overview
Tencent CDB for PostgreSQL has been certified by the following standards and complies with the related security requirements:
- ISO 22301
- ISO 27001
- ISO 20000
- ISO 9001
- Trusted cloud services certification
- Classified protection of information security (Class 3)
- STAR certification

Some features of PostgreSQL are designed by referring to:

- GBT 20273-2006 Information Security Technology - Security Techniques Requirement for Database Management System (Class 2 or above)
- JRT 0072-2012 Testing and Evaluation Guide for Classified Protection of Information System of Financial Industry (Class 4)

## 2. Tencent Cloud PostgreSQL Service Security Protection (OPS Security)
### 2.1 Overview
PostgreSQL complies with the requirements of National Classified Protection of Information Security (Class 3). Some of the product features meet the standards for Financial Industry Information Security (Class 4).


### 2.2 Internal personnel and system authentication

To improve the security of database server system and ensure the security of various OPS activities, Tencent Cloud has implemented a series of security reinforcement measures, including but not limited to:
- Carry out identification and authentication for the users who log into the operating system and database system, and guarantee the username uniqueness;
- Configure username/password as required. The password must be a combination of at least 3 types of characters with a length of not less than digits, and should be changed regularly;
- Enable login failure mechanism where actions such as ending session, limit of number of unauthorized logins and automatic exit are taken in case of login failures;
- Access the system under Tencent enterprise IT monitoring in remote management to provide internal risk control and audit, with all the sensitive operations encrypted.
- Two-factor authentication (dynamic token + password) is performed on the database server administrators who log in to OPS system

### 2.3 Internal personnel and system access control
For Tencent Cloud database management systems and administrators, discretionary access control scheme is implemented, including but not limited to:
- Internal OPS staff and systems are controlled based on Tencent Cloud security policies (audit requirements are met);
- The granularity of subject is down to user level, and that of object is to database table level;
- Implement strict code management and access control;
- High-risk systems can only be accessed by Tencent private network (development network), which is physically isolated from the Internet.


### 2.4 Internal security audit
Provide comprehensive security audit and risk control mechanism: audit features include but not limited to database operation audit, management system operation audit, document operation audit, plug-in device operation audit, unauthorized external connection audit, IP address change audit, and service and process audit , etc. The audit covers every operating system user and database user on the server, for example, Tencent Cloud administrator behaviors, abnormal use of system resources, use of important system commands and other security-related events. The audit logs, which contain the date, time, type, subject IDs, object IDs and results of the events, are retained for more than one year at a location with a higher-level security to prevent from being accidentally deleted, modified or overwritten.

- Database security audit: all the operations on database server and database will go through database security audit system. [Currently unavailable]
- Management system operation audit: Tencent Cloud keeps detailed logs of all the operations on both internal and external management systems for an effective risk traceability.
- Regular risk evaluation: Tencent Cloud security team performs security evaluation on database OPS management on a regular basis.


### 2.5 Internal intrusion prevention
Tencent Cloud takes multi-dimensional approaches to intrusion prevention for database servers:

- Intrusion detection system can defend against intrusions into database servers;
- Deploy vulnerability scanning and perform system security inspection regularly;
- Deploy terminal security management system and enable patch distributing module to update system with patches timely;
- Operating system is installed on a minimal installation basis, with only required components and applications installed and unwanted services disabled.
- Implement enhancements on other security configurations based on system type.

### 2.6 Backup and recovery
Tencent Cloud Database provides data backup and recovery features by default. 

### 2.7 Secure reuse of objects
For returned or replaced devices, Tencent Cloud will clear the residual information timely to ensure the previous user's sensitive information such as authentication information, files, directories and database records are released in time or completely cleared before reassigning the devices to other users.

### 2.8 Non-repudiation
Tencent Cloud's internal OPS staff are required to go through two-factor authentication and non-repudiation scheme before logging into the system. All the personnel involved have signed a confidentiality agreement.

### 2.9 More security features
> More details will be provided later.


