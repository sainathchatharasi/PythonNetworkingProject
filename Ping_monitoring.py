#Author : Bhavya Medisetty

from netmiko import ConnectHandler
import os

class Ping_test:
  def __init__(self):

    ip = input("Enter an IP address to ping : ")
    # ping for each ip in the file
    
    response = os.popen(f"ping {ip} ").read()
       
    #saving some ping output details to output file
       
    if("Request timed out." or "unreachable") in response:
        print(response)
        f = open("ping_output.txt","a")
        f.write(str(ip) + ' link is down'+'\n')
        f.close()
    else:
        print(response)
        f = open("ping_output.txt","a")  
        f.write(str(ip) + ' is up '+'\n')
        f.close()
    # print output file to screen
    with open("ping_output.txt") as file:
        output = file.read()
        f.close()
        print(output)

Ping_test()
