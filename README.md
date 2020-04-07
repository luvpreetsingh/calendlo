### Overview

This project is built using the Python Django framework. It is built using python=3.6.0, Django=2.2 and postgres=11.4.

### Setup
To run this project in your server, clone the git repo. Create a python virtual environment and activate it. Run the command `pip install -r requirements.txt`.

After setting the environment, you need to provide values to the required environment variables which are given in `sample_vars.sh`. You will need a postgresql database to run this project.


### Testing

After the setup, run the following command to run tests,

NOTE: You will need a database user which can create a new database in postgres.

```bash
./manage.py test
```
