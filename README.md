[![Build Status](https://travis-ci.org/RachelleMaina/SendIT-API.svg?branch=challenge-3)](https://travis-ci.org/RachelleMaina/SendIT-API) [![Coverage Status](https://coveralls.io/repos/github/RachelleMaina/SendIT-API/badge.svg?branch=api)](https://coveralls.io/github/RachelleMaina/SendIT-API?branch=api) <a href="https://codeclimate.com/github/RachelleMaina/SendIT-API/maintainability"><img src="https://api.codeclimate.com/v1/badges/bb166ed9f2d15ef34fa0/maintainability" /></a>

## SENDIT

This is the API backend of SendIT, a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.

## Getting Started

1. `git clone https://github.com/RachelleMaina/SendIT.git`
2. Set up and activate a virtual environment on SendIT/backend/ folder with the commamnd `virtualenv venv`
3. Activate the virtual environment with `source venv/bin/activate`
4. Install flask, flask_resful and pytest among other requirements with `pip install -r requirements.txt`
3. To run tests, use the command `pytest`
4. To run the application, Export flask with the command `FLASK_APP=run.py`
5. Then Run flask with the command `flask run`
6. Test the following endpoints on Postman

## Endpoints

1. Signup
http://rachel-sendit-api.herokuapp.com/api/v2/auth/signup

2. Login
http://rachel-sendit-api.herokuapp.com/api/v2/auth/login

3. Fetch all parcel delivery orders in the application:
http://rachel-sendit-api.herokuapp.com/api/v2/parcels`

4.  Fetch all parcel delivery orders by a specific user
http://rachel-sendit-api.herokuapp.com/api/v2/user/parcels

5. Change location
http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/presentLocation

6. Change destination
http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/destination

7. Change status
http://rachel-sendit-api.herokuapp.com/api/v2/parcels/1/status

8. Create Order
http://rachel-sendit-api.herokuapp.com/api/v2/parcels


## Prerequisites

Postman, Git


## Installing
install postman from https://www.getpostman.com/apps
install git from https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/



## Output of terminal
git clone https://github.com/RachelleMaina/SendIT.git  on your terminal

## Built With

* Python

## Authors

**Rachel Maina** 


## License

No Licencing yet

##Hosting Link
https://rachel-sendit-api.herokuapp.com/




