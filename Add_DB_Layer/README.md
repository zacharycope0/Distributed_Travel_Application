The code is designed to run on three machines/virtual machines and communicate via RPC. If you are not familiar with virtual machines, look into using VirtualBox or AWS to run the application. 

If you don't want to use virtual machines, you can run all of the code on one machine and communicate to all servers running on the localhost through different ports.

This application has an added MongoDB database layer. In order to run the code, a MongoDB server will need to by set up on one of the machines. The MongoDB server will need a collection to store the list of available flights.
  
 **Data should be input into the collection of available flights as follows:
 db.<name_of_collection>.insert({AirlineID:"<#>",AirlineName:"<name>",FromCity:"<city>",ToCity:"<city>",BookedYesOrNo:"N"})**
  
 #
 **Note: You will have to updated the IP address and port numbers appropriately where noted in the code**
 #
