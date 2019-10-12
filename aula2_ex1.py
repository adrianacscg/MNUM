
def func(a):                    #this does the sqrt for perfect squares

    #a = float(x);
    if a > 1:
        for i in range (0, a//2, 1):
        
            if a == i * i:
        
                return i;
            else:
                continue;
            
    if a <= 1:
        for i in range (a//2, a, 1):
        
            if a == i * i:
        
                return i;
            else:
                continue;
        
            
            
    return 0;


#print(func(9));

def another_func(b):
    a = 0;   #start value
    
    while(a <= b):
       mid = (a+b)/2;
       
       if (b == mid * mid):
           return mid;
       if (b > mid * mid):
           a = mid +1;
           ans = mid;
           
       if (b < mid*mid):
           b = mid -1;
           
    return ans;

print(another_func(16));
