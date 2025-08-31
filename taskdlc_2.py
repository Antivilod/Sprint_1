def digit_root(num):
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10 
            num //= 10
        
        num = digit_sum
    
    return num


if __name__ == "__main__":
    print(f"Цифровой корень 4851: {digit_root(4851)}")      
    print(f"Цифровой корень 97569: {digit_root(97569)}")    
    print(f"Цифровой корень 889987: {digit_root(889987)}")  