import random 
import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import choice
import math
import time
import statistics

random.seed()

#---------Tak 01----------------------
def random_walk(n,start):
    x = start
    distance = 0
    randomwalk =[]
    for i in range(n):
        step = random.choices(['left','center','right'],[0.1,0,0.9])
        #print(step)
        if step == ['left']:
            x = x - 1
            randomwalk.append(x)
        elif step == ['center']:
            x = x
            randomwalk.append(x)
        else:
            x = x+1
            randomwalk.append(x)
    #plt.plot(randomwalk)
    #plt.show()
   
    distance = math.sqrt(((x-start))**2)
    return (x,distance)

#random_walk(100,0)
    
def expected_distance(n,steps):
    walks = []
    distance = []
    for i in range(n):
        randomwalk = random_walk(steps,0)
        walks.append(randomwalk[0])
        distance.append(randomwalk[1])
    distance_length = sum(distance)/(n)
    #plt.plot(walks) 
    #plt.show()
    return distance_length
#expected_distance(1000,100)

def frequentist_one(simulations,experiments,steps):
    distance = []
    for i in range (simulations):
        distance.append(expected_distance(experiments,steps))
    plt.hist(distance)
    plt.xlabel("Expected distance");
    plt.ylabel("frequency")
    plt.title("Histogram for Expected position ")
    plt.show()

#frequentist_one(1000,1000,50)
#print(expected_distance(100,100))


#-----------Task 02-----------------------------
def two_walks(difference):
    x = 0
    y = x - difference
    time = 0
    distance = math.sqrt((y-x)*(y-x))
    while(distance !=0):
        #print(distance)
        stepx = random.choices(['left','right'],[0.25,0.75])
        stepy = random.choices(['left','right'],[0.4,0.6])     
        if stepx == ['left']:
            time+=1
            x-=1
            distance = math.sqrt((y-x)*(y-x))
        elif stepy ==['right']:
            time +=1
            y+=1
            distance = math.sqrt((y-x)*(y-x))   
        elif stepx ==['right']:
            x+=1
            time+=1
            distance = math.sqrt((y-x)*(y-x))
        elif stepy == ['left'] :
            time+=1
            y-=1
            distance = math.sqrt((y-x)*(y-x))
        
        
       
    return time
            
               
#print(two_walks(4))
def expected_time(n,difference):
    walks = []
    distance = []
    n1 =[]
    for i in range(n):
        randomwalk = two_walks(difference)
        walks.append(randomwalk)

    time_length = (sum(walks)/2)/n
    return time_length
    
#expected_time(1000,50)

def frequentist2(n,difference):
    time = []
    for i in range(n):
        print(i)
        time.append(expected_time(n,difference))


    plt.hist(time)
    plt.xlabel("Expected time");
    plt.ylabel("frequency")
    plt.title("Histogram for Expected time ")
    plt.show()
    
#frequentist2(1000,50)        

#---------task 03----------------------
def inside_circle(x,y,theta,centerx,centery):           #tangential reflection
    radius = 100
    tempx = (radius - 0.5)*math.cos(theta)         #point just inside the boundary
    tempy = (radius - 0.5)*math.sin(theta)
    a = (tempx - x)**2 + (tempy -y)**2
    b = 2*(tempx - x)*(x-centerx)+2*(tempy - y)*(y- centery)
    c = (x - centerx)**2 + (y- centery)**2 - radius**2
    step = (2*c)/(-b +math.sqrt((b*b)-4*a*c))
    intersectx = (tempx - x)*step + x               #points of intersection of the line with the circle boundary
    intersecty = (tempy - y)*step + y
    m = -1/((intersecty - centery)/(intersectx - centerx))    #slope of the tangent
    b1 = intersecty - m*intersectx
    d = (x+(y-b1)*m)/(1+m*m)
    newx = 2*d -x
    newy = 2*d*m - y +2*b1        #new points inside the circle after reflection

    return newx , newy

def circular_walk2(n):
    xcount = 0
    ycount = 0
    x = 0
    y = 0
    centerx = 0
    centery = 0
    distance = 0
    tempx = 0                                      
    tempy = 0
    tempd = 0
    randomwalkx =[]
    randomwalky = []
    
    i = 0
    while (i < n):
        step = random.choices([0,0.5,1],[0.33,0.33,0.33])
        theta = random.choices([((0*math.pi)/180),((90*math.pi)/180),((180*math.pi)/180),((270*math.pi)/180)])
        tempx = step[0]*math.cos(theta[0])
        tempy = step[0]*math.sin(theta[0])
        tempd = math.sqrt((x*x +y*y))
        if (tempd <= 100):
            x+=tempx
            y+=tempy
            randomwalkx.append(x)
            randomwalky.append(y)
            plt.scatter(x,y)
        else:
            x,y = inside_circle(x,y,theta[0],centerx,centery)
            plt.scatter(x,y)
            randomwalkx.append(x)
            randomwalky.append(y)
        i+=1
       
    plt.plot(randomwalkx,randomwalky)
    plt.xlabel("X");
    plt.ylabel("Y")
    plt.title("Circular Random Walk of 200000 steps")
    plt.show()

#circular_walk2(200000)
    

#---------task 04------------------------
def random_walk2(n,start):
    x = start
    distance = 0
    randomwalk =[]
    for i in range(n):
        step = random.choices(['left','right'],[0.1,0.9])
        step_size = random.random()
        if step == ['left']:
            x = x - step_size
            randomwalk.append(x)
        else:
            x = x+step_size
            randomwalk.append(x)
    #plt.plot(randomwalk)
    #plt.show()
   
    distance = math.sqrt(((x-start))**2)
    return (x,distance)

#random_walk(100,0)
    
def expected_distance1(n,steps):
    walks = []
    distance = []
    for i in range(n):
        randomwalk = random_walk2(steps,0)
       # print(randomwalk)
        walks.append(randomwalk[0])
        distance.append(randomwalk[1])
    distance_length = sum(distance)/(n)
    #plt.plot(walks) 
    #plt.show()
    return distance_length
#expected_distance(1000,100)

def frequentist_three(simulations,experiments,steps):
    distance = []
    for i in range (simulations):
        print(i)
        distance.append(expected_distance1(experiments,steps))
    plt.hist(distance)
    plt.xlabel("Expected distance");
    plt.ylabel("frequency")
    plt.title("Histogram for Expected position of 50 steps")
    plt.show()

#frequentist_three(1000,1000,50)
#print(expected_distance(100,100)
        
#----------task 05----------------    

def circular_walk(n):
    xcount = 0
    ycount = 0
    x = 0
    y = 0
    centerx = 0
    centery = 0
    distance = 0
    tempx = 0
    tempy = 0
    tempd = 0
    randomwalkx =[]
    randomwalky = []
    newx1 =[]
    newy1 = []
    
    i = 0
    counter = 0
    while (i < n):
        step = random.uniform(0,1)
        theta = 2.*math.pi*random.uniform(0,1)
        tempx = step*math.cos(theta)
        tempy = step*math.sin(theta)
        tempd = math.sqrt((x*x +y*y))
        if (tempd <= 100):
            x+=tempx
            y+=tempy
            randomwalkx.append(x)
            randomwalky.append(y)
            plt.scatter(x,y)
            
        else:
            counter+=1
            x,y = inside_circle(x,y,theta,centerx,centery)
            randomwalkx.append(x)
            randomwalky.append(y)
            plt.scatter(x,y)
        i+=1
 
    plt.plot(randomwalkx,randomwalky)
    plt.xlabel("X");
    plt.ylabel("Y")
    plt.title("Circular Continuous Random Walk of 20000 steps")
    plt.show()
    

#circular_walk(20000)

#-------------------task 07-------------------------------
def circular_walk3(n):
    xcount = 0
    ycount = 0
    x = 0
    y = 0
    centerx = 0
    centery = 0
    distance = 0
    tempx = 0
    tempy = 0
    tempd = 0
    randomwalkx =[]
    randomwalky = []
    newx1 =[]
    newy1 = []
    
    i = 0
    counter = 0
    while (i < n):
        step = random.choices([0,0.5,1],[0.33,0.33,0.33])
        theta = 2.*math.pi*random.uniform(0,1)
        tempx = step[0]*math.cos(theta)
        tempy = step[0]*math.sin(theta)
        tempd = math.sqrt((x*x +y*y))
        if (tempd <= 100):
            x+=tempx
            y+=tempy
            randomwalkx.append(x)
            randomwalky.append(y)
            plt.scatter(x,y)
            
        else:
            counter+=1
            x,y = inside_circle(x,y,theta,centerx,centery)
            randomwalkx.append(x)
            randomwalky.append(y)
            plt.scatter(x,y)
        i+=1
   
    plt.plot(randomwalkx,randomwalky)
    #plt.plot(newx1,newy1)
    plt.xlabel("X");
    plt.ylabel("Y")
    plt.title("Circular Semi-Continuous Random Walk of 20000 steps")
    plt.show()

#circular_walk3(20000)

#-------------------task 08 -------------------------------
   
def circular_two_walk(centerx, centery):
    radius = 100
    randomwalkx1 = []
    randomwalky1 = []
    randomwalkx2 = []
    randomwalky2 = []
    random1 = random.random()
    r1 = radius * math.sqrt(random1)
    theta1 = random.random() * 2 * math.pi
    x1 = r1*math.cos(theta1)
    y1 = r1*math.sin(theta1)

    random2 = random.random()
    r2 = radius * math.sqrt(random2)
    theta2 = random.random() * 2 *math.pi
    x2 = r2*math.cos(theta2)
    y2 = r2*math.sin(theta2)
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    count = 0
    while (distance >= 1):
        step = random.random()
        theta = 2.*math.pi*random.random()
        tempx = step*math.cos(theta)
        tempy = step*math.sin(theta)
        step1 = random.random()
        theta1 = 2.*math.pi*random.random()
        tempx1 = step1*math.cos(theta1)
        tempy1 = step1*math.sin(theta1)
        tempd1 = math.sqrt((x1*x1)+(y1*y1))
        tempd2 = math.sqrt((x2*x2)+(y2*y2))
        count+=1
        if ((tempd1 <= radius) and (tempd2<= radius)):
            x1+=tempx
            y1+=tempy
            randomwalkx1.append(x1)
            randomwalky1.append(y1)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            x2+=tempx
            y2+=tempy
            randomwalkx2.append(x2)
            randomwalky2.append(y2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        elif ((tempd1<= radius) and (tempd2) >= radius):
            x1+=tempx
            y1+=tempy
            randomwalkx1.append(x1)
            randomwalky1.append(y1)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            x2 = inside_circle(x2,y2,theta,centerx,centery)[0]
            y2 = inside_circle(x2,y2,theta,centerx,centery)[1]
            randomwalkx2.append(x2)
            randomwalky2.append(y2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        elif (tempd2 <= radius and tempd1 >= radius):
            x2+=tempx
            y2+=tempy
            randomwalkx2.append(x2)
            randomwalky2.append(y2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            x1 = inside_circle(x1,y1,theta,centerx,centery)[0]
            y1 = inside_circle(x1,y1,theta,centerx,centery)[1]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            randomwalkx1.append(x1)
            randomwalky1.append(y1)
        else:
            x1, y1 = inside_circle(x1,y1,theta,centerx,centery)
            randomwalkx1.append(x1)
            randomwalky1.append(y1)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            x2 = inside_circle(x2,y2,theta,centerx,centery)[0]
            y2 = inside_circle(x2,y2,theta,centerx,centery)[1]
            randomwalkx2.append(x2)
            randomwalky2.append(y2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
            
##    plt.plot(randomwalkx1,randomwalky1)
##    plt.plot(randomwalkx2,randomwalky2)
##    plt.show()
    return count 

#print(circular_two_walk(0,0))
        
def expected_steps(n):
    walks = []
    distance = []
    n1 =[]
    for i in range(n):
        walks.append(circular_two_walk(0,0))

    step_length = sum(walks)/n
    
    return step_length,statistics.stdev(walks)


def deviation():    
    a = []
    for i in range(50):
        a.append(expected_steps(50)[1])
    dev = sum(a)/50
    return dev

#print(deviation())

def frequentist4(n):
    steps = []
    for i in range(n):
        steps.append(expected_steps(550)[0])
       

    plt.hist(steps)
    plt.xlabel("Expected number of steps");
    plt.ylabel("frequency")
    plt.title("Histogram of Expected number of steps taken by both collectively")
    plt.show()

frequentist4(100)
    

    
        
        
    
    
    
    

    
