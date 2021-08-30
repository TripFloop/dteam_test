<h2 align="center">
	Dteam test
</h2>

[Dteam site](https://dteam.dev/)


## Setup

##### Clone from github

```shell script
git clone https://github.com/TripFloop/dteam_test.git
```

##### Build and setup your docker containers

```shell script
sudo docker-compose build
sudo docker-compose up -d
```

##### Migrations into django

```shell script
sudo docker-compose exec django python manage.py migrate
```

##### Createsuperuser for admin panel

```shell script
sudo docker-compose exec django python manage.py createsuperuser
```

#### Change in admin panel domain for Site model



Made with this requirements https://github.com/odwyersoftware/python-tech-test
