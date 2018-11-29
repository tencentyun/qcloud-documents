"If a workman wishes to do a good job, he must first sharpen his tools." Over years of providing emergency response services and security and countermeasures, Tencent Cloud security service expert has accumulated a wide wealth of experience in security and emergency response including two theoretical methods, mature methodology (which guides the practical operations) and tool set (which can quickly troubleshoot the problem), achieving fast, prompt, and efficient security response.
## Mature Methodology
### Windows Emergency Response
#### Routine Analysis
When a security incident occurs, the reason can often be traced from the following information. When handling the security incident, the support staff may collect such information for analysis in emergency response.

Check Type	| Check Point
---|--- 
Network (illegal link)		| Data transfer to the public, illegal external connections
Progress (server, port)	|	Forged Trojan progresses
Auto-activated item		|Whether the items are still activated upon boot after configuration
File		| Backdoors or malicious files
Log		| Whether hackers' attack paths and methods are recorded
Drive	|	Vulnerable drive version at the underlying layer
Software version		| Some software versions have obvious security vulnerabilities and configuration problems

#### Malicious Codes
For security incidents such as hacker intrusion and virus spread, the support staff must check whether malicious codes are planted in the target.
Typical malicious codes may cause file infection, data encryption, thread injection, SPI, port re-use and hidden external connection. To troubleshoot malicious codes, security service experts need to use third-party inspection tools and make deep reverse analysis.

### Unix/Linux Emergency Response
#### Routine Analysis
Similar to that on Windows, the routine analysis on Unix/Linux includes analysis of network connection, progress status, auto-activated item, file, log, software version and configuration, based on which security service experts make association analysis and locate the problem.
#### Malicious Codes 
Unix is attacked by limited types of malicious codes. The commonly detected malicious codes are Rootkit and Trojans. Other malicious codes can be found and determined in routine inspection and analysis.

### Web Intrusion Analysis
When a security incident occurs on a Web application, support staff uses Web application inspection related technology such as Web application log access analysis, Web configuration analysis, and software version analysis to identify the type of the security incident as follows:
- Application layer security vulnerability (SQL injection, command execution, information leakage, etc.)
- Configuration defects
- Remote scan, etc.

## High-efficient Tool Set
The following displays the common (but not all) emergency response tools in the real environment.
### Information Collection Tools

Tool Name	| Description
---|--- 
Process Explorer	| Microsoft built-in tool set: ysinternalsSuite, analyzing progresses)
Process Monitor 	|	Microsoft built-in tool set: SysinternalsSuite, monitoring file and registry operations
Autoruns		|Microsoft built-in tool set: SysinternalsSuite, checking auto-activated items
Regmon		|Microsoft built-in tool set: SysinternalsSuite, monitoring registries
Tcpview		|Microsoft built-in tool set: SysinternalsSuite, checking network connection
Common Linux tool	|	Linux built-in tool set, such as netstat/ps/ls/nc/iftop
Intrusion analysis script	|	Tencent Cloud security service expert quickly analyzes the automatic script internally

### Detection of Malicious Codes
Tool Name	| Description
---|--- 
IDA Pro commercial version|	Professional reverse tool [Download Link](https://www.hex-rays.com/products/ida/support/download.shtml) 
OllyDbg	| Free open-source tool [Download Link](http://www.ollydbg.de/)
Chrootkit	| Typical backdoor inspection tool for Linux [Download Link](http://www.chkrootkit.org)
Rootkit hunter |	Typical backdoor inspection tool for Linux [Download Link](http://rkhunter.sourceforge.net/) 
Icesword |Unknown program inspection tool
### Web Log Analysis
Tool Name |	Official Website
---|--- 
LogParser	 | Log analysis tool [Official Website](http://www.microsoft.com)
AWstats |	Log file analysis tool [Official Website](http://awstats.sourceforge.net/)
Log analysis script/tool |	The tool set used by Tencent Cloud security and emergency response service expert

