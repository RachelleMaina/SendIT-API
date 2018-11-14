[![Coverage Status](https://coveralls.io/repos/github/RachelleMaina/SendIT/badge.svg?branch=ch-update-endpoints-161859459)](https://coveralls.io/github/RachelleMaina/SendIT?branch=ch-update-endpoints-161859459)  [![Build Status](https://travis-ci.org/RachelleMaina/SendIT.svg?branch=ch-update-endpoints-161859459)](https://travis-ci.org/RachelleMaina/SendIT)  [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

# SENDIT

This is the API backend of SendIT, a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.

## Getting Started

1. `git clone https://github.com/RachelleMaina/SendIT.git`
2. Set up and activate a virtual environment on SendIT/backend/ folder with the commamnd `virtualenv venv`
3. ctivate the virtual environment with `source venv/bin/activate`
4. Install flask, flask_resful and pytest with ` pip install -r requirements.txt`
3. To run tests, use the command `pytest`
4. To run the application, Export flask with the command `FLASK_APP=run.py`
5. Then Run flask with the command `flask run`
6. Test the following endpoints on Postman

*ENDPOINTS*
1. Fetch all parcel delivery orders:
`localhost:5000/api/v1/parcels`

2. Fetch a specific parcel delivery order
`localhost:5000/api/v1/parcels/101`

3. Fetch all parcel delivery orders by a specific user
`localhost:5000/api/v1/users/1/parcels`

4. Cancel the specific parcel delivery order
`localhost:5000/api/v1/parcels/101/cancel`

5. Create a parcel delivery order
`localhost:5000/api/v1/parcels`

6. Create a user
`localhost:5000/api/v1/users`

7. Fetch all users
`localhost:5000/api/v1/users`

8. Fetch a specific user
`localhost:5000/api/v1/users/1`

### Prerequisites

Postman, Git


### Installing
install postman from https://www.getpostman.com/apps

install git from https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/



### Output of terminal
git clone https://github.com/RachelleMaina/SendIT.git  on your terminal

## Built With

* Python

## Authors

**Rachel Maina** 


## License

No Licencing yet




