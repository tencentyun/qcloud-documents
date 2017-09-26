
Dear User:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tencent Cloud found that when Tomcat and Hadoop are installed by using apt-get on the Ubuntu14.04 CVM purchased from Tencent Cloud official website, the port can be listened normally but can not respond to requests. Tencent Cloud has provided solution to this problem. You're recommended to deal with the problem with the suggested solution.

**[Cause of the problem]**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is caused by a [known problem] of Java Runtime Environment(http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6202721).
 **【Problem Analysis】**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tomcat and Hadoop are developed with Java and thus use API of java.security.SecureRandom.
The API is generated with '/dev/random' by default in some JREs, whereas '/dev/random' receives CPU temperature as well as noises of such hardware as keyboard to generate entropy. As CVM is a virtual machine environment using virtualization technology, it is difficult for it to sense the signals such as CPU temperature and to generate entropy. For this reason, the 'cat /dev/random' is almost blocked, thus preventing Tomcat and Hadoop from being started.
**[Solution]**
**Change the JRE configuration**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please change the 'securerandom.source=file:/dev/urandom' in the original '/etc/java-7-openjdk/security/java.security' (the URL depends on the situation) to 'securerandom.source=file:/dev/./urandom' to avoid the above problems.


October 14, 2016    
Tencent Cloud




