sum=0
while(True):
    user_input=input("Enter the item Price or press q to quit: \n")
    if(user_input!='q'):
        sum=sum+int(user_input)
        print(f"Order Total so far:{sum}")
    else:
        print(f"Your Bill Total is {sum}. Thanks for shopping with us")
        break
