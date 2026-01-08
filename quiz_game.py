choices = ('a', 'b', 'c')

score = 0

try:
    start = input("Press enter to start!")
    
    question1 = (
    '''
    Question 1: What is the capital city of Kenya?
    (a) Nairobi
    (b) Kampala
    (c) Capetown 
    '''                 
    )

    question2 = (
    '''
    Question 2: What is 4*4?
    (a) 12
    (b) 16
    (c) 0                  
    '''
    )
    
    questions = (question1, question2)
    
    answers = {
    question1: 'a',
    question2: 'b'
    }
    
    
    for question in questions:
        while True:
            print(question)
        
            user_answer = input("Your answer: ").lower()
            
            if user_answer not in choices:
                print("Invalid choice")
            else:
                break
            
        correct_answer = answers[question]
        if user_answer == correct_answer:
            score +=1
  
except(TypeError, ValueError):
    print("Enter correct input")

print(f"Your final score is :{score}/{len(questions)}")


