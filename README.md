# JED-Quorum-BE-V2
Python backend for the quorum application

Uses the chalice framework with sql-alchemy for ORM interface to the database

Test database uses sqlite. Prod db uses MySQL

## Build Setup

```
# install dependencies
pip install -r requirements.txt
  
## Choose database type (Linux)
# Test
source ./environment/test_setup.sh
# Prod
source ./environment/prod_setup.sh
  
# run local api (need connection/config.py for db connection)
chalice local
  
# deploy to aws environment (need aws credentials set up)
chalice deploy
```

![org_logo](http://www.jimspestcontrol.com.au/wp-content/uploads/2016/07/Jims-Termite-and-Pest-Control-Team-313x390.gif)