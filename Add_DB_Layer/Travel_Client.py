#
#
#UPDATE CODE BETWEEN <>
#
#

#Import packages
import xmlrpc.client
import sys


#  TESTING AIRLINE SERVER


name = input("Enter your name to begin the reservation process:")


airlineServer = xmlrpc.client.ServerProxy('http://<INSERT_AIRLINE_SERVER_IP_ADDRESS>:<INSERT_PORT_NUMBER>')
# Call function to get list of airline tickets
print("Calling GetList of airline Tickets")
#print(airlineServer.GetList() + '\n')
print(airlineServer.GetList())

air_ID = int(input("Enter the AirlineID number of the flight you would like to book:"))


# call function to add a reservation
print("\nCalling AddReservation")
air_res = airlineServer.AddReservation(air_ID, name)
print("\nYour flight has been booked. You reservation ID number is #{}.\n".format(air_res))

print('##########################################################################################\n')

input()

#print(airlineServer.RemoveReservation(air_res))
print(airlineServer.RemoveReservation(air_res))
print("Your trip has been canceled")

input()
sys.exit()

