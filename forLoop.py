
#! count alphabet i

word = "artificial intelligence"

count = 0

for ch in word:
    if(ch == 'i'):
        count+=1;

print("Count of i : ", count) 

#! Vovels count

word2 = "artificial";

vovels = 0;

for ch2 in word2:
    if(ch2 =='a' or ch2 =='e' or ch2 =='i' or ch2 =='o' or ch2 =='u'):
        vovels+=1;

print("No of vovels : ", vovels);
        

#! Range()
for i in range(1, 5):
    print(i)

print("\n")  
for i in range(1, 10, 2): #? Skips
    
    print(i)

#! Sum of natural nos
sum = 0

print("\n")  
for i in range(1, 5+1):
    sum+=i;
print("Sum of natural nos : ", sum) 