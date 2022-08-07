# Spacex - Starlink (search for satellite position)
##### 1 - First of all, clone my repository with the command below:
```git clone https://github.com/dinizleonardo5/spacex-position-analysis.git```
##### 2 - Navigate to where you did clone the repository and run the following command in the principal folder:
```docker-compose up --build```
wait about 1 minute for the application to build...
##### 3 - Open the following URL to access the web interface:
http://localhost:9001/search
[![](web_app.png)](http://localhost:9001/search)
##### 4 - Do your search!
[![](https://i.gifer.com/7yrz.gif)](http://localhost:9001/search)

# After the first steps, you can access the MYSQL Database and query if you want!

##### Open a terminal and access our MYSQL server with the following command:
```docker exec -it mysql-container /bin/bash```
##### Once inside the server, let's connect to our mysql:
```mysql -uroot -p123```
##### Use our database created for our satellite search:
```sql
USE db_spacex;
```
##### Here is the query that we did use to query our database:
```sql
SELECT   id, longitude, latitude, creation_date, 
         ABS(DATEDIFF(creation_date, CAST('{T}' as DATE))) as diff_days_search_date_x_found_date
FROM     starlink_hst
WHERE    LTRIM(RTRIM(id)) = '{id}'
ORDER BY 5,4 DESC
LIMIT    1;
```