#!/usr/bin/env python3

import BlackboardQuiz

#You need a package, which is what you'll eventually upload to
#Blackboard/MyAberdeen
with BlackboardQuiz.Package("MyQuestionPools") as package:        
    #You may have multiple question pools in a single package, just
    #repeat this block with different pool names.
    with package.createPool('Lala', description="Questions which are not generated/calculated", instructions="") as pool:
        #We can do numerical questions

        # #Or multiple choice questions
    #     #Or multiple answer questions (with automatic choice of partial mark weights)
    #     pool.addMAQ('Primes','Which of the following are prime numbers?', answers=["2", "3", "4", "5", "6", "87"],  correct=[0,1,3], positive_feedback="", negative_feedback="")
                
    #     # Can adjust the partial mark weights on the multiple answer questions as well
    #     pool.addMAQ('Composites','Which of the following are composite numbers? (this question has custom weights)', answers=["2", "3", "4", "5", "6", "87"],  correct=[2,4,5], positive_feedback="", negative_feedback="", weights=[-33.33,-33.33,25,-33.34,25,50])
        
    #     #Short Response question
    #     pool.addSRQ('CDF','What are the necessary properties of a cumulative distribution function', answer='Non-decreasing, goes to 0 at minus infinity, goes to 1 at plus infinity', positive_feedback="", negative_feedback="", rows=3, maxchars=0)
        
    #     #True/False question
    #     pool.addTFQ('PDF','True or False: A probability density function must be less than or equal to one everywhere.', istrue=False, positive_feedback="", negative_feedback="")
        
    #     #Ordering question
    #     pool.addOQ('Ordering','Order the following numbers from smallest to largest:', answers=["2","5","11","18"], positive_feedback="", negative_feedback="")
        
    #     #Matching question
    #     pool.addMQ('Matching','Match the following:', answer_pairs=[["one","1"],["two","2"],["three","3"],["four","4"]], unmatched=["5","6"], positive_feedback="", negative_feedback="")

    #     #Maths can be included using latex
    #     pool.addMCQ('Math question', 'Please solve this "display" equation: $$\\int x\,dx=?$$',
    #                 answers=['$x$', '$\\frac{x^2}{2}$', '$gh$'],
    #                 correct=1,
    #                 positive_feedback="Well done!",
    #                 negative_feedback="Sorry, but the general rule for polynomial integration is $\\int x^n\\,dx=\\frac{x^{n+1}}{n+1}$ for $n\\neq -1$"
    #     )
        
    #     #Embedding external images is easy too and will automatically
    #     #be included into the package. Other HTML can also be used for
    #     #formatting, I don't check it.
        pool.addMCQ('HTML question', 'I can\'t believe that you can embed images! <img src="nw.png" width="100"> Cool huh?',
                    ['Really cool.', 'Well, it\'s not that impressive, it\'s basic functionality.', 'Blackboard sucks.'],
                    correct=0)
    
    
        
    # #One of the most interesting implementations, multi-part REGEX questions!
    # with package.createPool('Regex questions', description="Unlimited regex power", instructions="") as pool:
    #     pool.addFITBQ(title="Crazy regex1", text=r'''How much [A] would a [B] chuck chuck if a [C] chuck could [D]
    #     wood?''',
    #                   answers={
    #                       'A':['wood'], #basic word matching
    #                       'B':['(WOOD|wood)'], # Match allcaps too
    #                       'C':[r'''w[o0]{2}d'''], # Allow leet speak (i.e. w00d or wo0d or w0od)
    #                       'D':['chuck', 'Chuck', 'CHUCK'], #Multiple matching patterns if needed
    #                   })

    
    # If you create hundreds of pools, you might want to organise them into tests, this can be done like so:
    # with package.createTest("Test: Creating using add_pool and per question points etc") as test:
        #Note, the pool is created from the test, instead of the
        #package. We also use the optional points_per_q and
        #questions_per_test now
        # with test.createPool('Unique questions (in a test)', description="", instructions="", points_per_q=6, questions_per_test=2) as pool:
        #     # pool.addNumQ('Test question 1', 'What is the number four in arabic numerals?', 4, erramt=0.1, positive_feedback="Good!", negative_feedback="Duh?")
        #     # pool.addNumQ('Test question 2', 'What is the number four in arabic numerals?', 4, erramt=0.1, positive_feedback="Good!", negative_feedback="Duh?")
        #     # pool.addNumQ('Test question 3', 'What is the number four in arabic numerals?', 4, erramt=0.1, positive_feedback="Good!", negative_feedback="Duh?")
        
        #     pool.addMCQ('Shakespeare','To be, or not to be', answers=["To be.", "Not to be.", "That is the question.", "Both."],  correct=2, positive_feedback="Again, you have read well.", negative_feedback="Try reading Hamlet.")
        #     pool.addMCQ('Shakespeare','To be1, or not to be', answers=["To be.", "Not to be.", "That is the question.", "Both."],  correct=2, positive_feedback="Again, you have read well.", negative_feedback="Try reading Hamlet.")
        #     pool.addMCQ('Shakespeare','To be2, or not to be', answers=["To be.", "Not to be.", "That is the question.", "Both."],  correct=2, positive_feedback="Again, you have read well.", negative_feedback="Try reading Hamlet.")
        #     pool.addMCQ('Shakespeare','To be3, or not to be', answers=["To be.", "Not to be.", "That is the question.", "Both."],  correct=2, positive_feedback="Again, you have read well.", negative_feedback="Try reading Hamlet.")
            
