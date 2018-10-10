#import os

#from definitions import ROOT_DIR, TEST_DB

connection_strings = {
    "prod": "mysql+pymysql://root:password123==@quorum-db-instance.cmozvfqehajr.ap-southeast-2.rds.amazonaws.com:3306/quorumdb",
    # "test": 'sqlite:///' + os.path.join(ROOT_DIR, 'database', TEST_DB)
}
