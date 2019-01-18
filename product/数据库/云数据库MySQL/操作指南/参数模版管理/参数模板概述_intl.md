You can use the parameters in the database parameter template to manage database engine configurations. You can consider the database parameter group as a container for the engine configuration values. You can use these values in one or multiple database instances.
  
If you already created a database parameter template and you wish to include most of the custom parameters and values of this group in the new database parameter template, it can be convenient to simply copy the parameter template.

If you wish to use your own database parameter template, simply create a new database parameter template, modify the required parameters and change your database instances. Note: Database instances that are already using this parameter template will not obtain any parameter updates from the database parameter template. If you wish to apply new parameters to a batch of database instances, you can do so by importing the template when batch-configuring parameters to re-apply the parameters.

Currently, the following functions are supported by parameter template. Log in to [Tencent Cloud Console][1], click "Relational database" in the navigation bar to enter [Cloud Database Console][2]. View and modify templates from the "Parameter Template" in the left panel:
- Default parameter template is supported
- Creating new template is supported. You can create custom parameter optimization solutions simply by slightly modifying the default parameters
- You can import generated templates from the MySQL configuration file my.conf
- You can save parameter configurations as templates
- You can import configuration from template when configuring parameters for one or more instances

[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/ "Cloud Database Console"

