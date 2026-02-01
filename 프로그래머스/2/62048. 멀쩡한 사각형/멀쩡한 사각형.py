import math

def solution(w,h):
    if w==h :
        return w*h-w
    else:
        temp = math.gcd(w,h)
        return w*h-(w+h-temp) 
    