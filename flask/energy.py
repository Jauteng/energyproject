from flask import Flask
from flask_bootstrap import Bootstrap
import csv
import sys

#Test 

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

def get_devices():
  #Header erstellen
  print "{0:<3}{1:<20} {2:>16} {3:>16} {4:>20}".format("ID",
                               "Device",
                               "Energyusage (W)", 
                               "active time (h)",
                               "average per day (W)")  
  try:
    #CSV öffnen
    devicescsv = open("devices.csv", 'rt')
    devices = csv.reader(devicescsv, delimiter=',')
    IDs = []
    for device in devices:
      #variablen aus datensätzen
      id = device[0]
      IDs += id
      devicename = device[1]
      energy=eval(device[2])
      active=eval(device[3])
      avr = energy*active
      #Tabelle erstelen
      print "{0:>3}{1:<20} {2:>16.2f} {3:>16.2f} {4:>20.2f}".format(id, 
                                      devicename, 
                                      energy,
                                      active,
                                      avr)
    # ToDo Auswertung
  finally:
    devicescsv.close()
  print """Enter "remove" if you wish to remove a device
  Press "Enter" to return to main menu!"""  
  decision = raw_input(">>> ")
  if decision == "remove":
    remove_device(IDs)
  else:
    menu()
      
def add_device():
  devicename = None
  energy = None
  runtime = None
  
  print "You can now add a device"
  #Eingabe
  while True:
    devicename = raw_input("Please enter the device name: ")
    if devicename.strip() != '':
      break
  while True:
    energy = input("Please enter the energy usage: ")
    if energy >= 0 and energy <= 10000:
      break
  while True:
    runtime = input("Please enter, who many hours per day its on: ")
    if runtime >= 0 and runtime <= 24:
      break
  new_entry = "\n%s,%s,%s" % (devicename,energy,runtime)
  
  #datensatz hinzufügen
  devices = open('devices.csv', 'a')
  devices.write(new_entry)
  devices.close()
  print "Adding of %s sucsessfull! Take a Cookie :P" % devicename
  menu()
  
def remove_device(IDs):
  #Eingabe
  while True:
    id = raw_input("You can remove a device by entering the ID:")
    if id in IDs:
      break
  
  #ToDo: datensatz entfernen, klappt noch nicht
  devicescsv = open("devices.csv", 'w')
  for device in csv.reader(devicescsv, delimiter=','):
     if device[0] <> id:
      writer.writerow(device)
  devicescsv.close()
  
  print "removing of %s sucsessfull! Take a Cookie :P" % id
  menu()  
  
#Start    
@app.route('/')
def menu():
  print """what do you wish to do?
  Enter "add" to add a new device
  Enter "info" to get a overview of the device
  Enter something else to exit
  """
  decision = raw_input(">>> ")
  if decision == "info":
    get_devices()
  elif decision == "add":
    add_device()

if __name__ == '__main__':
  app.run(host='0.0.0.0')
