# Here are the steps to setup a GCP virtual machine & mySQL
*Your virtual machine must reach the minimum specs for mySQL*

### Initial VM setup
1. Boot up your virtual machine & connect to it via terminal/command prompt
2. Update your virtual machine with:
> $ sudo apt-get update
3. Install nano:
> $ sudo apt-get install nano
4. Select nano as the editor:
> $ select-editor
> *select nano*
5. Add port 3306 as an inbound security rule (Azure/GCP)

### mySQL Installation
1. Install mySQL on the virtual machine
> $ sudo apt install mysql-server mysql-client
2. Login with elevated credentials
> $ sudo mysql
3. View current databses
> mysql> show databases;
4. Create a new user
> mysql> CREATE USER 'name'@'%' IDENTIFIED BY 'password';
5. Confirm account creation
> mysql> SELECT USER FROM mysql.user;

### Allowing mySQL Connections
1. Edit configuration on elevated permissions
> $ sudo nano etc/mysql/mysql.conf.d/mysqld.cnf
2. Change IP permission to wild-card
> bind-address = ~~127.0.0.1~~ 0.0.0.0
3. Save changes
> Control + O to save
> Control + X to exit
4. Restart service on elevated permissions
> $ sudo /etc/init.d/mysql restart

