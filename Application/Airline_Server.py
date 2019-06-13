#Import server packages and pandas
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create airline server
#
#ADD IP ADDRESS AND PORT NUMBER TO COMMUNICATE WITH CLIENT
#
server = SimpleXMLRPCServer(("INSERT_CLIENT_IP_ADDRESS", INSERT_PORT_NUMBER), allow_none=True)
server.register_introspection_functions()

#Create initial list of Airline availability
# number, Airline, From, To, bookedYN
#
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
resCount = 0

#Create Airline functions

class AirlineFunctions:
    # get list of tickets
    def GetList(self):
        print("In the GetList function")
        print(Airlines)
        print("==============================")
        return Airlines.to_string()
    
    # get list of reservations
    def GetReservationList(self):
        print("In the GetReservationList function")
        print(Reservations)
        print("==============================")
        return Reservations.to_string()
    
    #Create a reservation
    def AddReservation(self, ID, Name):
        global Reservations       
        global resCount
        print("In the AddReservation function")
        resCount += 1
        Reservations.loc[resCount] = [ID, Name]
        print("Updated Reservations List")
        print(Reservations)
        
        Airlines.loc[ID,'BookedYesOrNo'] = 'Y'
        print("Updated Airlines List")
        print(Airlines)
        print("==============================")
        return resCount
    
    #Create a function to remove one reservation
    def RemoveReservation(self, ResID):
        global Reservations
        print("In the RemoveReservation function")
        AirID = Reservations.loc[ResID, 'AirlineID']
                        
        Reservations = Reservations.drop(ResID)
        print("Updated Reservations List")
        print(Reservations)

        Airlines.loc[AirID,'BookedYesOrNo'] = 'N'
        print("Updated Airlines List")
        print(Airlines)
        print("==============================")
        return "Airline reservation #{} has been deleted".format(ResID)


server.register_instance(AirlineFunctions())

print("Airline Server is ready to accept calls....")

# Run the server's main loop
server.serve_forever()
