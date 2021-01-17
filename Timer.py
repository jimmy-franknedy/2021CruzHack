# import the time module import time 
import time
# define the countdown func.
#def countdown(t,p) where p = if trash was clicked 
def countdown(t): 
    
    while t:
      # if clicked then make boolean true
        a = 0
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1)
        #if clicked   #based on boolean user interaction
        if (a <= 0) : #insert the function to check if the trash was clicked where
                      #only update the output if the trash was clicked!
            t -= 1
        else:
            t += 5
        a = input()
    print('Fire in the hole!!') 
  
  
# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(t))



