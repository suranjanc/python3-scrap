sample_price = 250

if sample_price >= 300: 
    final_price=sample_price*(100-30)/100
elif 200 <= sample_price < 300:
    final_price=sample_price*(100-20)/100
elif 100 <= sample_price < 200: 
    final_price=sample_price*(100-10)/100
elif 0 <= sample_price < 100:
    final_price=sample_price*(100-5)/100    
else:
    final_price=sample_price

print(final_price)    

