### Rename Database Instance
You can use the CDB console to rename a database instance, and note the following when you rename the database:
*Modification to the CDB database instance name will not change the database's private IP or affect the database connection.
*You cannot use an existing database instance name when renaming an instance.
*After renaming, all read-only instances associated with the database instance will remain associated with the instance.
*After renaming, the database instance belongs to the same project and network as before.
*For renamed database instances, database backups and slow\_log will also be preserved.
*An instance cannot be renamed while it's in another task process (e.g., upgrading or initializing).  

### Console
You can rename a database instance both in the instance list and in the instance details:
![][image-1]
![][image-2]

[image-1]:	//mc.qcloudimg.com/static/img/eada0e01c81e1a1f346770507770b087/111.png
[image-2]:	//mc.qcloudimg.com/static/img/8c17891f007fa5fdbdb3fe87d79c8141/222.png
