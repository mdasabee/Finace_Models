%clear
# Binomial Pricng model for American and European Put Option 

import numpy as np

#Parameter definitions:

# n is the time to maturity
# S is the initial stock price
# K is the strike price 
# r is the risk free rate
# Put is the option type(European or American) to choose
# u is the up factor
# d is the down factor
# p is the risk free probability


def Binomial(n, S, K, r, u, d, Put):  
   
    p = (1+r-d) / (u-d) 

    #Binomial price tree
    stockvalue = np.zeros((n+1,n+1))
    stockvalue[0,0] = S
    for i in range(1,n+1):
        stockvalue[i,0] = stockvalue[i-1,0]*u
        for j in range(1,i+1):
            stockvalue[i,j] = stockvalue[i-1,j-1]*d
    
    #option value at final node   
    optionvalue = np.zeros((n+1,n+1))
    for j in range(n+1):
        optionvalue[n,j] = max(0, K-stockvalue[n,j])
    
    #backward calculation for option price    
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if Put =="E":
                optionvalue[i,j] = max(0, (1/(1+r))*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))
            elif Put =="A":
                optionvalue[i,j] = max(0, K-stockvalue[i,j], (1/(1+r))*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))

    print("Stock Price tree: %s" %stockvalue)
    print("Option Price tree: %s" %optionvalue)
    print(" \n Option value: %.4f" %optionvalue[0,0])
    
    return  None

#####  Question 4   ##### ---- European Put Option

print("\n #### European Put Option #### \n")

## A ## 

print("\n When maturity date is 1: \n")
Binomial(1, 100, 90, 0.05, 1.25, 0.8, "E")

## B ## 

print("\n When maturity date is 2: \n")
Binomial(2, 100, 90, 0.05, 1.25, 0.8, "E")

## C ## 

print("\n When maturity date is 3: \n")
Binomial(3, 100, 90, 0.05, 1.25, 0.8, "E")

## D ## 

print("\n When maturity date is 10: \n")
Binomial(10, 100, 90, 0.05, 1.25, 0.8, "E")

###################################################################################################################


# #####  Question 4   ##### ---- American Put Option

print("\n #### American Put Option #### \n")

# ## A ## 

print("\n When maturity date is 1: \n")
Binomial(1, 100, 90, 0.05, 1.25, 0.8, "A")

# ## B ## 

print("\n When maturity date is 2: \n")
Binomial(2, 100, 90, 0.05, 1.25, 0.8, "A")

# ## C ## 

print("\n When maturity date is 3: \n")
Binomial(3, 100, 90, 0.05, 1.25, 0.8, "A")

# ## D ## 

print("\n When maturity date is 10: \n")
Binomial(10, 100, 90, 0.05, 1.25, 0.8, "A")

