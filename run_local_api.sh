#!/usr/bin/env bash

if [ ! -f ./database/test.db ]; then
    echo "Local database not found. Setting up a new one..."
    cp ./database/golden/test.db ./database/test.db
    echo "Using database/test.db"
else
    echo "Local database found. Using database/test.db"
fi
source ./environment/test_setup.sh
chalice local