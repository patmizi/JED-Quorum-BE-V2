#!/usr/bin/env bash
rm ./database/test.db
cp ./database/golden/test.db ./database/test.db
pytest