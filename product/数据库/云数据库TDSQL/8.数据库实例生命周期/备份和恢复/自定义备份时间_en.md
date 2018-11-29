Tencent Cloud Database can back up the database automatically by executing user-defined backup policy.

1. Log in to Cloud Database console, and select destination instance.
2. Select MariaDB (TDSQL) -> Management -> Backup and Recovery -> Backup and Log Settings in the menu.
3. Click "Edit" in "Backup and Log Settings".
4. Parameter Description:

	- Storage period: The period during which the data backup files are stored (7 days by default). You can set it to 7-30 days, and need to submit a ticket for the period exceeding 30 days. The maximum period is 3,650 days.
	- Backup cycle: Currently, the data is backed up every day by default. The configuration API will be available soon.
	- Backup time span: You can set it to any period of time (in hr).
	- Log backup: Always enabled by default. The logs include error logs, slow logs, transaction logs (Binlog), etc.
	- The retention period for log backups: Equal to storage period.
