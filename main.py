# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:17:24 2023

@author: zuran
"""

"""
So this is how i want it to work:
    it should predict values instead of calculating + - * /
    
    functions: 
        
        predict()
        what algorithm to use?
        
        training(n)
        for n repeat
        generate random 1st number integer assign to n1
        generate random number between 1 to 4 assign to sign
        generate random 2nd number integer assign to n2
        calculate() n1 sign n2 assign to result
        predict() n1 sign n2 asign to prediction
            in predict also save use weights for future use in some txt file
        compare result and prediction
        modify predict() accordingly
        
        
        testing(n)
        generate random 1st number integer assign to n1
        generate random number between 1 to 4 assign to sign
        generate random 2nd number integer assign to n2
        calculate() n1 sign n2 assign to result
        predict() n1 sign n2 asign to prediction
        count correct predictions
        return count
        
        main()
        send n to training first
        then n to testing
        get count and calculate accuracy
        
    
    
    
"""