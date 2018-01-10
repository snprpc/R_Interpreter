isEven<-function(num){
    if(num %% 2 == 0){
        print("Is Even")
    }else{
        print("Not Even")
    }
}

num_vector <- c(1,2,3,4,5,6)

for(num in num_vector){
    isEven(num)
}