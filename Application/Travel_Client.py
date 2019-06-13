#
#UPDATE CODE BETWEEN <>
#
#Import packages
import xmlrpc.client
import sys

#  TESTING AIRLINE SERVER

name = input("Enter your name to begin the reservation process:")

#Except blocks will cancel reservation there is a communication error with the server.
#
#ADD IP ADDRESS AND PORT NUMBER TO COMMUNICATE WITH SERVER
#
try:
    airlineServer = xmlrpc.client.ServerProxy('http://<INSERT_AIRLINE_SERVER_IP_ADDRESS>:<INSERT_PORT_NUMBER>')
    # Call function to get list of airline tickets
    print("Calling GetList of airline Tickets")
    print(airlineServer.GetList() + '\n')

    air_ID = int(input("Enter the AirlineID number of the flight you would like to book:"))

    # call function to add a reservation
    print("\nCalling AddReservation")
    air_res = airlineServer.AddReservation(air_ID, name)
    print("\nYour flight has been booked. You reservation ID number is #{}.\n".format(air_res))

    print('##########################################################################################\n')
except:
    print("An error has occured. The reservation could not be processed.")
    sys.exit()


#  TESTING CAR RENTAL SERVER

try:
    CarRentalServer = xmlrpc.client.ServerProxy('http://<INSERT_RENTAL_CAR_SERVER_IP_ADDRESS>:<INSERT_PORT_NUMBER>')
    # Call function to get list of Rental Cars
    print("Calling GetList of Rental Cars")
    print(CarRentalServer.GetList() + '\n')

    car_ID = int(input("Enter the CarRentalID number of the vehicle you would like to book:"))

    # call function to add a reservation
    print("\nCalling AddReservation")
    car_res = CarRentalServer.AddReservation(car_ID, name)
    print("\nYour vehicle has been booked. You reservation ID number is #{}.\n".format(car_res))

    print('##########################################################################################\n')

except:
    print("An error has occured. The reservation could not be processed.")
    print(airlineServer.RemoveReservation(air_res))
    print("Your trip has been canceled")
    sys.exit()

#  TESTING HOTEL SERVER


try:
    HotelServer = xmlrpc.client.ServerProxy('<http://INSERT_HOTEL_SERVER_IP_ADDRESS>:<INSERT_PORT_NUMBER>')

    # Call function to get list of Rental Cars
    print("Calling GetList of Hotels")
    print(HotelServer.GetList()+'\n')

    hotel_ID = int(input("Enter the HotelID number of the room you would like to book:"))

    # call function to add a reservation
    print("\nCalling AddReservation")
    hotel_res = HotelServer.AddReservation(hotel_ID, name)
    print("\nYour hotel reservation has been booked. You reservation ID number is #{}.\n".format(hotel_res))
    print('##########################################################################################')
    print('##########################################################################################\n')

except:
    print("An error has occured. The reservation could not be processed.")
    print(airlineServer.RemoveReservation(air_res))
    print(CarRentalServer.RemoveReservation(car_res))
    print("Your trip has been canceled")
    sys.exit()
