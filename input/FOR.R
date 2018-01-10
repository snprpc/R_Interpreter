fruit_vector <- c("apple","banana","pear","orange")

for(fruit in fruit_vector){
    print(fruit)
}

num = 5
repeat{
    print("REPEAT")
    num = num - 1
    if(num==0){
        break
    }
}