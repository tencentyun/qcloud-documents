You can use any standard SQL client to connect to your instance once it has been initialized. Next, we will provide an example showing how to connect to PostgreSQL instance using pgAdmin.

## Step 1
(To ensure data security, only private network IP is available now. You need a Tencent CVM within your region.)
You can download and install pgAdmin from https://www.pgadmin.org/download/.

## Step 2
Click "File" menu and select "Add Server".

## Step 3
In the "New Server Registry" dialog, enter name, CVM IP address, port number, user name and password. You can find the CVM IP address and port number from "Private Network Address" in the PGSQL instance management page. Click "OK" once you've entered the information.
![](//mccdn.qcloud.com/static/img/fd480ec9413eb6b7ff53d212fafd3ecd/image.png)
## Step 4
In the object browser menu in the left, double-click "Server groups" to expand the list. Select the connected server (database instance) and choose database name.
![](//mccdn.qcloud.com/static/img/a66c259deee8524a0cf35cb3c5e29642/image.jpg)
## Step 5
Launch the PSQL console. Click the icon as shown in the figure and choose PSQL CONSOLE. Now, you can work with your database in the console.
![](//mccdn.qcloud.com/static/img/21e18377780799f20c40c48421c041a1/image.jpg)


