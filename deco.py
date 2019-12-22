def product_buying(function): # 1
    def wrapper(arg,arg2):
        arg = arg-5000
        arg2 = "민기"
        return function(arg, arg2) # 5
    return wrapper # 6

@product_buying # 2-1
def money_eating_machine(money,name): # 2
    money_you_have = money
    return  name + '에게 거스름 돈 {}'.format(money_you_have) + "원을 주었다."

sender = "민수"
print(sender + "가 ")
print(money_eating_machine(10000,sender)) # 3