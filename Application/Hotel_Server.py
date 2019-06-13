#Import server packages and pandas
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create Hotel server
#
#ADD IP ADDRESS AND PORT NUMBER TO COMMUNICATE WITH CLIENT
#
server = SimpleXMLRPCServer(("INSERT_CLIENT_IP_ADDRESS", INSERT_PORT_NUMBER), allow_none=True)
server.register_introspection_functions()

#Create initial list of Airline availability
# number, Airline, From, To, bookedYN
#
Hotels = pd.DataFrame([
    [1,'HolidayInn','New York', 'N'], 
    [2,'HolidayInn','Philadelphia', 'N'], 
    [3,'Candlewood','New York', 'N'], 
    [4,'Candlewood','Baltimore', 'N'],
    [5,'Marriott','Chicago', 'N']],
    columns = ['HotelID','HotelName','City','BookedYesOrNo'])

Hotels.set_index('HotelID', inplace=True)

Reservations = pd.DataFrame([ ['','','']], columns = ['ResID','HotelID','Name'])
Reservations.set_index('ResID', inplace = True)
resCount = 0

#Create Airline functions

class HotelFunctions:
    # get list of hotels
    def GetList(self):
        print("In the GetList function")
        print(Hotels)
        print("==============================")
        return Hotels.to_string()
    
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
        print("Updated Hotel Reservations List")
        print(Reservations)
        
        Hotels.loc[ID,'BookedYesOrNo'] = 'Y'
        print("Updated Hotels List")
        print(Hotels)
        print("==============================")
        return resCount
    
    #Create a function to remove one reservation
    def RemoveReservation(self, ResID):
        global Reservations
        print("In the RemoveReservation function")        
        HotelID = Reservations.loc[ResID, 'HotelID']

        Reservations = Reservations.drop(ResID)
        print("Updated Hotel Reservations List")
        print(Reservations)
        
        Hotels.loc[HotelID,'BookedYesOrNo'] = 'N'
        print("Updated Hotels List")
        print(Hotels)
        print("==============================")
        return "Hotel reservation #{} has been deleted".format(ResID)


server.register_instance(HotelFunctions())

print("Hotel Server is ready to accept calls....")

# Run the server's main loop
server.serve_forever()
