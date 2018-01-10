
print("assign expression and addition expression")
a=3
b=a+1
e=b+1
d=e-e
print(d)
a = 2
print(a)
if(a %% 2 == 0){
    print("oushu")
}else{
    print("jishu")
}
a = 5
repeat{
    print(a)
    a = a - 1
    if(a == 0){
        break
    }
}
a = 5
repeat{

    if(a == 4){
        a = a - 1
        next
    }
    if(a == 0){
        break
    }
    print(a)
    a = a - 1
}
i = 10
repeat{
    i = i - 1
    print(i)
    if(i == 0){
        break
    }
}
c_test <-c (1,"b",2,9)
d_test <-c (1,2,3,4)
print(c_test)
print('=================')
for(i in c_test){
    print(i)
}
print('=================')
x <- function(f,s){
    g=s+f
    print(g)
}
x(9,7)
pie(d_test)