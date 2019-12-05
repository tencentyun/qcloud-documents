## Note
**1. PostgreSQL already provides account with permissions including creating/modifying databases, creating/modifying accounts. But it does not provide super admin account.**


**2. It is recommended that you use public network address for routine maintenance, rather than connecting business servers.**


**3. The network to which the instance belongs can no longer be modified once the instance has been created.**


**4. Why is occupied disk capacity larger than actual data volume?**

Updates will cause xlog to rapidly grow in size. The logs occupy disk space if the system doesn't archive and delete them in time. Or, the query operations include large number of sort and connection operations involving huge amount of data. This process produces temporary tables which will overflow to the disk and occupy disk space for a short time.


**5. Enable/Use Plug-ins**

Most commonly used plug-ins are supported by Tencent Cloud PostgreSQL and can be directly used. Certain plug-ins require super admin permission to be enabled. You can enable them from the Tencent Cloud console. Or you can contact Tencent personnel and describe your instance ID and name of the plug-in to enable it.



