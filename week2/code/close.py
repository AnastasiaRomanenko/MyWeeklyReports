import os 
  
close = input("Do you want to close your computer? ") 
  
if close == 'yes': 
    os.system('sudo shutdown -h now')