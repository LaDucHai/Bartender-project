
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}

ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}



#############################    
def select(k):
    i = ingredients[k]
    x = i[0]
    for x in i:
        print(x)

def sp_answer_01(k):
    i = ingredients[k]
    return i[0] or i[1] or i[2]

    
############################

def verify_answer(k,m):
  
    while True:
        answer = input('yes or no -> Enter \n')
        
        if answer == 'yes':
            print('\nPlease chose one of its :\n',)
            select(k)
            answer_01 = input()
            if answer_01 == sp_answer_01(k):
                print("oke\n\n\n")
                break
              
        if answer == 'no' :
            print("Thank you\n\n\n")
            m+=1
            break
        else:
            print('Please chose again\n\n\n')
            
        break

#######################################    
def main():
    i = ['strong', 'salty', 'bitter', 'sweet', 'fruity']
    x = 0
    while(x < 5):
        m = 0
        k = i[x]
        print(questions[i[x]])
        verify_answer(k,m)
        x+=1
    while True:
        if m == 4:
            print("Call me if you need to order, please. \n Thank you")
            break
        else:
            print("Thank you, Please wait for me a minute")
            break

main()


