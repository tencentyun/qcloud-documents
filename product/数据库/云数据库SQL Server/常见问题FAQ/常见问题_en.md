
**1. After the creation of SQL Server database, no or little data has been written to the database - Why does the storage monitor show that 500 MB space has been occupied?**
When created, each SQL Server database will be automatically assigned 500 MB initial space, where the data will be preferably written into. Therefore, even if no or little data has been written to the database, the storage monitor shows 500 MB occupied space. 

**2. When I have deleted the written data, the storage monitor still shows a certain amount of occupied space  - Can't it be released?**
When the data is deleted from SQL Server database, expanded data file will not shrink, but the free space inside the file can be used for the subsequent operations, such as insertion, update. For example, suppose you have applied for a 50 GB instance. If 50 GB data is written to the database and then is completely deleted, the storage monitor indicates you have used 50 GB space. But you still can write a large amount data files into the database.

**3. When I use Microsoft SQL Server Management to manage database, the message "Login failed. The login is from an untrusted domain and cannot be used with Windows authentication" is displayed**
Please change the authentication method to "**SQL Server Authentication**".
