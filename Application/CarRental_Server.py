#
#UPDATE CODE BETWEEN <>
#

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
server = SimpleXMLRPCServer(("<INSERT_SERVER_IP_ADDRESS>", <INSERT_PORT_NUMBER>), allow_none=True)
server.register_introspection_functions()

#Create initial list of Airline availability
# number, Airline, From, To, bookedYN
#
CarRentals = pd.DataFrame([
    [1,'Enterprise','LA', 'Ford F150', 'N'], 
    [2,'Enterprise','San Francisco', 'Honda Accord', 'N'], 
    [3,'Dollar','New York', 'Honda Accord', 'N'], 
    [4,'Dollar','Newark', 'Subaru Outback', 'N'],
    [5,'Hertz','Salt Lake City', 'Mini Cooper', 'N']],
    columns = ['CarRentalID','CarRentalName','City', 'CarType', 'BookedYesOrNo'])
CarRentals.set_index('CarRentalID', inplace = True)

Reservations = pd.DataFrame([ ['','','']], columns = ['ResID','CarRentalID','Name'])
Reservations.set_index('ResID', inplace = True)
resCount = 0

#Create CarRental functions

class CarRentalFunctions:
    # get list of rentals
    def GetList(self):
        print("In the GetList function")
        print(CarRentals)
        print("==============================")
        return CarRentals.to_string()
    
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
        
        CarRentals.loc[ID,'BookedYesOrNo'] = 'Y'
        print("Updated CarRentals List")
        print(CarRentals)
        print("==============================")
        return resCount
    
    #Create a function to remove one reservation
    def RemoveReservation(self, ResID):
        global Reservations
        print("In the RemoveReservation function")        
        CarID = Reservations.loc[ResID, 'CarRentalID']
        
        Reservations = Reservations.drop(ResID)
        print("Updated Car Rental Reservations List")
        print(Reservations)

        CarRentals.loc[CarID,'BookedYesOrNo'] = 'N'
        print("Updated CarRentals List")
        print(CarRentals)
        print("==============================")
        return "Rental car reservation #{} has been deleted".format(ResID)


server.register_instance(CarRentalFunctions())

print("Car Rental Server is ready to accept calls....")

# Run the server's main loop
server.serve_forever()
