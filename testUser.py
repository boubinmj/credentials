from credentials_connection import User
from simple_salesforce import Salesforce

matt = User('dev')
matt.getCredentials()
sf = matt.sf_login()

# test query
response = sf.query_all("SELECT Id, FirstName FROM Contact WHERE LastName LIKE 'Boubin'")
if(len(response['records'])>0):
    print(response['records'][0]['FirstName'])