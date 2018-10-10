#!/usr/bin/env bash
rm ./database/test.db
cp ./database/golden/test.db ./database/test.db
DATABASE_TYPE=test pytest -vv
