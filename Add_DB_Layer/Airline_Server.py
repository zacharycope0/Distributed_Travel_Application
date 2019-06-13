#Import server packages and pandas
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from pymongo import MongoClient
import pandas as pd
import sys


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create airline server
server = SimpleXMLRPCServer(("172.31.40.61", 8801), allow_none=True)
server.register_introspection_functions()

#Create initial list of Airline availability
# number, Airline, From, To, bookedYN
#
"""
Airlines = pd.DataFrame([
    [1,'AA','Chicago','LA', 'N'], 
    [2,'AA','Chicago','San Francisco', 'N'], 
    [3,'UA','Chicago','New York', 'N'], 
    [4,'UA','Chicago','Newark', 'N'],
    [5,'Delta','Chicago','Salt Lake City', 'N']],
    columns = ['AirlineID','AirlineName','FromCity','ToCity','BookedYesOrNo'])

Airlines.set_index('AirlineID', inplace = True)


Reservations = pd.DataFrame([ ['','','']], columns = ['ResID','AirlineID','Name'])
Reservations.set_index('ResID', inplace = True)
"""
resCount = 0

#Create Airline functions

class AirlineFunctions:
    # get list of tickets
    def GetList(self):
        print("In the GetList function")
        try:

            client = MongoClient('172.31.40.70',27017)


            #retrieve all records
            cursor = client.test.airlines.find({}, {'_id' : False})

            #convert to DataFrame
            airlines = pd.DataFrame(list(cursor))
                
            print(airlines)
            print("==============================")
            return airlines.to_string()  

        except:
            print("Couldnt connect to MongoDB")
            sys.exit()
       
    # get list of reservations
    def GetReservationList(self):
        try:

            client = MongoClient('172.31.40.70',27017)


            #retrieve all records
            cursor = client.test.airline_res.find({}, {'_id' : False})

            #convert to DataFrame
            airline_res = pd.DataFrame(list(cursor))
                
            print(airline_res)
            print("==============================")
            return airlines_res.to_string()  

        except:
            print("Couldnt connect to MongoDB")
            sys.exit()
    
    #Create a reservation
    def AddReservation(self, ID, Name):      
        
        try:
            global resCount
            print("In the AddReservation function")
            resCount += 1

            client = MongoClient('172.31.40.70',27017)

            #get the database
            db = client.test

            #get the collection
            collection = db.airlines

            #set airline flag to Y
            cursor = collection.update({'AirlineID':str(ID)}, {'$set' : {"BookedYesOrNo":"Y"}})                   

            #create new reservation in res table
            newres = {'ResID': resCount,'AirlineID': ID,'Name':Name}
            
            db.airline_res.insert(newres)
            
            return resCount
        
        except:
            print("Couldnt connect to MongoDB")
            sys.exit()
        
        print("==============================")
        
    
    #Create a function to remove one reservation
    def RemoveReservation(self, ResID):
        #try:
        print("In the RemoveReservation function")
        
        client = MongoClient('172.31.40.70',27017)

        #get the database
        db = client.test
        
        
        #get AirlineID for the Res
        res = db.airline_res.find({'ResID':ResID}, {'_id' : False})
        AirID = list(res)[0]['AirlineID']
                     
        #set airline flag to N
        cursor = db.airlines.update({'AirlineID':str(AirID)}, {'$set' : {"BookedYesOrNo":"N"}})                   
        print('Updated Airlines DB')

        #Delete reservation in res table[]
        db.airline_res.remove({'ResID': ResID})        
        print('Update Airline_Res DB')
       
        return "Airline reservation #{} has been deleted".format(ResID)
        
        #except:
            #print("Couldnt connect to MongoDB")
            
server.register_instance(AirlineFunctions())

print("Airline Server is ready to accept calls....")

# Run the server's main loop
server.serve_forever()
