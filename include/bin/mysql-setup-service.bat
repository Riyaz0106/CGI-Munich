@ECHO OFF 
:: This batch file details Mysql configuration.
TITLE My MySQL\MySQL config Info
ECHO Please wait... Checking MYSQL system information.
ECHO ============================
ECHO MYSQL INFO
ECHO ============================
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" -V
for /f %%i in (".my.cnf") do set size=%%~zi
if %size% equ 0 ECHO [mysql]>>".my.cnf" & ECHO user = "root">>".my.cnf" & ECHO password = "root1234">>".my.cnf"
ECHO Mysql Tabels importing started....
ECHO Importing cgi Database and its tables...
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" --defaults-file=".my.cnf" --force < "C:\Program Files\CGI Munich\templates\cgi_munich.sql"
ECHO Import successfully completed...