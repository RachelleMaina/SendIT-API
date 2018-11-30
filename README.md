[![Build Status](https://travis-ci.org/RachelleMaina/SendIT-API.svg?branch=challenge-3)](https://travis-ci.org/RachelleMaina/SendIT-API) [![Coverage Status](https://coveralls.io/repos/github/RachelleMaina/SendIT-API/badge.svg?branch=api)](https://coveralls.io/github/RachelleMaina/SendIT-API?branch=api) <a href="https://codeclimate.com/github/RachelleMaina/SendIT-API/maintainability"><img src="https://api.codeclimate.com/v1/badges/bb166ed9f2d15ef34fa0/maintainability" /></a>

# SendIT

This is the API backend of SendIT, a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.

### Prerequisites
```
Postman, Linux Terminal
```

### Installing

1. Download project files from `https://github.com/RachelleMaina/SendIT-API`
2. On your local machine, cd to the project folder and Set up the commamnd `virtualenv venv`
3. Activate the virtual environment with `source venv/bin/activate`
4. Install dependencies with  the command`pip install -r requirements.txt`

## Testing Endpoints

1. Setup the database and create tables with the command `python migrations.py`
2. Then set your environment command `FLASK_APP=run.py`
3. Lastly Run flask with the command `flask run`

   Test the following endpoints on Postman
  
1. Signup:  POST:`http://rachel-sendit-api.herokuapp.com/api/v2/auth/signup`
   ```payload: {"username": "Rachel", "password": "root", "phone": 254412345123, "email": "mainarachelle@gmail.com"}
   _To get email notification, use an email address you can access_```
   
2. Login:   POST: `http://rachel-sendit-api.herokuapp.com/api/v2/auth/login`
   ```payload: {"username": "Rachel", "password": "root"}```
   
   *To access the following endpoints, login with the credentials you used to signup.*
   e.g payload: {"username": "Rachel", "password": "root"}`
   
3. Create Order: POST: `http://rachel-sendit-api.herokuapp.com/api/v2/parcels`
  ``` payload: {"pickup_location": "Nairobi","destination": "Kisumu", "weight": 20} ```
  
4. Fetch all parcel delivery orders by a specific user: GET: `http://rachel-sendit-api.herokuapp.com/api/v2/user/parcels`
  
5. Change destination: PUT: `http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/destination`
   ```payload:  {"destination": "Malindi"}```
   
    *To access the following endpoints, login as an Admin.*

6. Fetch all parcel delivery orders in the application: GET: `http://rachel-sendit-api.herokuapp.com/api/v2/parcels`

7. Fetch all users in the Application: GET: `http://rachel-sendit-api.herokuapp.com/api/v2/users`

8. Change location: PUT: `http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/presentLocation`
    ```payload: {"current_location": "Marsabit"}```
     
9. Change status: PUT: `http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/status`
``` {"status": "Delivered"}```

## Running Tests
To run tests, use the command `pytest`

## Hosting Link
```
https://rachel-sendit-api.herokuapp.com/
```

## Documentation
```
https://documenter.getpostman.com/view/5893140/RzfZPDAD
```

## Built With
```
* Python
```

## Authors
```
**Rachel Maina** 
```


## License
```
No Licensing yet
```






