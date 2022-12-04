import sys

class Main:
    def run_db(self):
        import DB_connection
    
    def run_Router_Packet_Details(self):
        import Router_Packet_Details
        
    def run_Ping_monitoring(self):
        import Ping_monitoring
        
    def get_bandwidth(self):
        import Bandwidth
        
def exitprogram():
    sys.exit("system exiting")
    
def printerror():
    print("Invalid option entered")
    
main = Main()
def run():
    menu={
    1:main.run_db,
    2:main.run_Router_Packet_Details,
    3:main.run_Ping_monitoring,
    4:main.get_bandwidth,
    5:exitprogram
    }
    while True:
        print("\n 1:Establish DataBase connection\n2:Get router packet details\n3:Ping Monitoring\n4:Get Bandwidth\n5:Exit Program\nEnter your choice?",end='')
        try :
            choice = int(input())
        except ValueError:
            print("Please enter a valid input!")
        menu.get(choice,printerror)()
run()
