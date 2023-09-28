# ad_profit_task
Steps to run project
1. run postgre database
~~~
docker-compose up -d
~~~
2. make migrations
~~~
python3 manage.py migrate
~~~
3. run tests
~~~
python3 manage.py test .
~~~
4. run server
~~~
python3 manage.py runserver
~~~
5. go to swagger documentation
http://localhost:8000/swagger/
