Initialization (batch initialization) is required for the purchased Cloud Database (PostgreSQL) instances before you can use them, as shown below:

![](https://mc.qcloudimg.com/static/img/375b50ba38f54f1f700e472afd35976b/image.jpg)

The following parameters need to be initialized:
- 	Admin user name: Case-insensitive, start with letter and end with letter or number. 16 characters at most. You cannot use:  postgres
- 	Admin password: The password should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, and special characters (!, @, #, $, %, ^, *, (, )). You can change it later in "Account Management".
- 	Supported character set: global instance character set. This cannot be changed once determined. (Under instances, global character set can be different from database. You can configure this when creating libraries)
