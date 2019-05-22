Tencent Cloud Security Center will pay close attention to all kinds of security vulnerabilities.  When any important security vulnerabilities are officially released, Tencent Cloud Security Center will keep track of the vulnerabilities in a timely manner, inform users of information about the vulnerabilities and provide the solutions to fix the vulnerabilities.

## Fixing period of Tencent Cloud official images
- Vulnerability fixing on a regular basis: Tencent Cloud will conduct vulnerability fixing on official images periodically with the frequency being `twice`a year;
- The fixing of high-risk vulnerabilities: For high-risk vulnerabilities, Tencent Cloud will provide emergency fixes for customers at the earliest possible time.

## Image types covered by vulnerability fixing
With its security maintenance principles for images being in consistent with those of the upstream official image releases, Tencent Cloud will conduct security maintenance for the system versions that are within the official maintenance period. 
### CentOS
CentOS only maintains updates of software and vulnerabilities for the latest minor versions of the current major versions. Tencent Cloud, with its maintenance principles being consistent with that of CentOS, only conducts regular vulnerability fixing and emergency fixing for high-risk vulnerabilities for the latest minor versions of the current major versions within the official maintenance period.

Notes on the maintenance of Tencent Cloud's existing CentOS version images:
- Centos 7.2 64-bit (Centos will continue to provide support until the next minor version is released)
- Centos 7.1 64-bit (Centos has officially stopped providing support for this)
- Centos 7.0 64-bit (Centos has officially stopped providing support for this)
- Centos 6.8 32/64-bit (Centos will continue to provide support until the next version is released)
- Centos 6.7 32/64-bit (Centos has officially stopped providing support for this)
- Centos 6.6 32/64-bit (Centos has officially stopped providing support for this)
- Centos 6.5 32/64-bit (Centos has officially stopped providing support for this)
- Centos 6.4 32/64-bit (Centos has officially stopped providing support for this)
- Centos 6.3 32/64-bit (Centos has officially stopped providing support for this)
- Centos 6.2 64-bit (Centos has officially stopped providing support for this)
- Centos 5.11 32/64-bit (Centos will continue to provide support)
- Centos 5.8 32/64-bit (Centos has officially stopped providing support for this)

### Ubuntu
Ubuntu officially provides long-term updating and maintenance services for software and vulnerabilities of the LTS version system. The updating for the server version of each LTS system will last for 5 years. Tencent Cloud officially provides all the LTS version server systems and, aiming to ensure the consistency with Ubuntu's official release, conducts regular vulnerability updates on the images within the maintenance period and conducts emergency fixing on high-risk vulnerabilities.

Notes on the maintenance of Tencent Cloud's existing Ubuntu version images:
- Ubuntu 10.04 LTS 32/64-bit (Ubuntu has officially stopped its maintenance and production)
- Ubuntu 12.04 LTS 64-bit(It is expected that its maintenance will be stopped by April 2017)
- Ubuntu 14.04 LTS 32/64-bit(It is expected that its maintenance will be stopped by April 2019)
- Ubuntu 16.04 LTS 32/64-bit(It is expected that its maintenance will be stopped by April 2021)

### Debian
Debian officially maintains two main branches: stable and oldstable. The stable is current stable version and the oldstable is last stable version. Debian will officially maintain the updates of software and vulnerabilities for the stable system. For oldstable system, volunteers and communities will provide LTS (Long Term Support) maintenance schemes. Tencent Cloud always maintains a consistency with its upstream official system in maintenance strategies and only conducts regular vulnerability fixing on the stable branch system maintained officially by Debian.

Notes on the maintenance of Tencent Cloud's existing Debian version images:
- Debian 8.2 32/64-bit(It is expected that its maintenance will be stopped by June 6, 2018)
- Debian 7.8 32/64-bit (Debian has officially stopped its maintenance)
- Debian 7.4 64-bit (Debian has officially stopped its maintenance)

### openSUSE
According to the life cycle of openSUSE system, Tencent Cloud conducts vulnerability fixing on images on a regular basis for systems that are officially supported.

Notes on the maintenance of Tencent Cloud's existing openSUSE version images:
- openSUSE 13.2(It is expected that its maintenance will be stopped by the first quarter of 2017)
- openSUSE 12.3 32/64-bit (openSUSE has officially stopped its maintenance)

### FreeBSD
Since the FreeBSD 11.0-RELEASE, FreeBSD has been providing a 5-year maintenance period for the stable branch. For the versions earlier than 11.0-RELEASE, FreeBSD provides different maintenance periods for different types.  Tencent Cloud always maintains a consistency with FreeBSD in maintenance principles. 

Notes on the maintenance of Tencent Cloud's existing FreeBSD version images:
- 10.1-RELEASE (It is expected that its maintenance will be stopped by December 31, 2016)

### Commercial version system
Tencent Cloud does not provide updates and maintenance for vulnerabilities of commercial version system. The commercial version images currently provided by Tencent Cloud include: 
- SUSE Linux Enterprise Server 12 64-bit
- SUSE Linux Enterprise Server 11 SP3 64-bit