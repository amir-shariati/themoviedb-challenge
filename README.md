
---

# Project Setup Guide

To run the project in the development environment, follow the steps below:

1. Make sure you have Docker installed on your system.

2. Open a terminal window.

3. Navigate to the project directory.

4. Run the following command to build and start the project:
   ```
   docker-compose up --build
   ```

5. After the project is up and running, you can perform additional tasks as follows:

   - To create an admin user, use the following command:
     ```
     docker-compose exec back-movie-dev python manage.py createsuperuser
     ```

   - To access the admin page, go to the following address in your web browser:
     [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)

   - To view the Swagger documentation, visit the following address:
     [http://0.0.0.0:8000/api/schema/swagger/](http://0.0.0.0:8000/api/schema/swagger/)

   - To view the Redoc documentation, go to the following address:
     [http://0.0.0.0:8000/api/schema/redoc/](http://0.0.0.0:8000/api/schema/redoc/)

   - To explore the Browsable API, navigate to:
     [http://0.0.0.0:8000/api/movie/](http://0.0.0.0:8000/api/movie/)

   - To visit the front page of the project, go to:
     [http://0.0.0.0:3000/](http://0.0.0.0:3000/)

