# Video Paradise

Video Paradise is a simple CRUD application for managing your home movie database.<br>
That is, if you are a neanderthal and still have movies on physical media.<br>
Offers basic functionalities (besides creating/retrieving/updating and deleting) like filtering, simple text search, possibility to upload covers.<br>
Creating cool logo was a huge part of the development process, so I hope you'll enjoy it.<br>
The logo, I mean.

## Movies/Users

There are already some movies added, as well as users:<br>
- admin login/password: burt_gummer/MyCannon
- user login/password: val_mckee/CanYouFlySucker

## Requirements

- Python 3.6
- Django 3.1.3

## Run
```
cd video_paradise_crud
python manage.py runserver
```
Go to your browser and type: http://127.0.0.1:8000/movies

## To do

- Mass data upload/export
- Sorting data and search results
- Pagination
- Movie covers gallery
- Thumbnails
- "Movie of the day" feature