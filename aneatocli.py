"""
aneatocli : a Neato Robot command and state querying cli.

Usage:
    aneatocli.py --go | --start-cleaning 
    aneatocli.py --stp | --stop-cleaning 
    aneatocli.py --pse | --pause-cleaning 
    aneatocli.py --res | --resume-cleaning  
    aneatocli.py --base |--send-to-base 
    aneatocli.py --gc | --get-commands 
    aneatocli.py --lsec | --load-secrets
    aneatocli.py --acc | -account
    aneatocli.py -h | --help
    aneatocli.py -v | --version

Options:
    -h , --help                  Show this message.
    -v , --version               Show version.
    --go , --start-cleaning      Tell the robot to start cleaning.
    --stp , --stop-cleaning      Tell the robot to stop cleaning.
    --pse , --pause-cleaning        Tell the robot to pause cleaning.
    --res , --resume-cleaning       Tell the robot to resume cleaning.
    --base ,--sendtobase             Tell the robot to go back to its dock.
    --gc , --get-commands        Get the available commands.
    --lsec , --load-secrets       Get the Serial Number and the secret. You will be prompted for login.

"""
from sys import exit
from os.path import exists as chkf
from pprint import pprint
import json
global robot

def loadCreds()
    try:
        with open("robotCreds.json","r") as json_file:
            creds=json.load(json_file)
            print("Your serial number is "+creds["serialID"]
              +". \n Your secret is "+creds["secretID"]
              +".\n Your robot "+creds["name"]+" have the following traits"+creds["traits"])
        robot = Robot(creds["serialID"],creds["secretID"],creds["traits"],creds["name"])
    except:
        print("Cannot log your robot(s) with the provided infos.")

def getCmds():
    cmds=robot.state["availableCommands"]
    try:
        with open("robotstate.json", "w") as json_file:
                json.dump(cmds, json_file)
        print("File robotstate.json created")
    except:
        raise
        exit()
        
def startC():
    if robot.state["availableCommands"]["start"]:
d        robot.start_cleaning()
    else:
        print("Cannot start the robot.")
        
def stopC():
    if robot.state["availableCommands"]["stop"]:
        robot.stop_cleaning()
    else:
        print("Cannot stop the robot.")
        

def pauseC():
    if robot.state["availableCommands"]["pause"]:
        robot.pause_cleaning()
    else:
        print("Cannot pause the robot.")
        
def resumeC():
    if robot.state["availableCommands"]["resume"]:
        robot.resume_cleaning()
    else:
        print("Cannot resume the robot.")
        
def go2B():
    if robot.state["availableCommands"]["goToBase"]:
        robot.send_to_base()
    else:
        print("Cannot send the robot to base.")


    

def funCall(simpleArg, verboseArg, func, *args):
    if arguments[simpleArg] or arguments[verboseArg]:
        func( *args )




getSecrets()

try:
	from pybotvac import Robot
except:
	print("pybotvac package is not installed.\n\nPlease run 'pip install pybotvac' from your command prompt\n")
	exit()
	
try:
    from docopt import docopt
    
except:
	print("docopt package is not installed.\n\nPlease run 'pip install docopt==0.6.2' from your command prompt\n")
	exit()

if __name__ == '__main__':
        arguments = docopt(__doc__, version='aneatocli 0.1')
        #nts:useful pour debugging
        pprint(arguments)
        

        
funCall("--go","--start-cleaning",startC)
funCall("--stp","--stop-cleaning",stopC)
funCall("--pse","--pause-cleaning",pauseC)
funCall("--res","--resume-cleaning",resumeC)
funCall("--base","--send-to-base",go2B)
funCall("--gc","--get-commands",getCmds)
funCall("--lsec","--load-secrets",loadCreds)

    
