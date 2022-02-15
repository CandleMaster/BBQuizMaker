import BlackboardQuiz
from flask import send_file
from question_bank import questions
# create a function where it takes video ids, search through the question base indexed by ID and turns it into a BB package
# question bank format

def find_questions(video_ids):
    id_list=video_ids.split(',')

    with BlackboardQuiz.Package("MyQuestionPools") as package:        
        #You may have multiple question pools in a single package, just
        #repeat this block with different pool names.
        with package.createPool('Customized BB Demo', description="Questions which are not generated/calculated", instructions="") as pool:
            for ids in id_list:
                if questions[ids]:
                    all_question = questions[ids]
                    for question in all_question:
                            pool.addMCQ(ids, question[0].replace('ppg/d6/',''), question[1],correct=question[2])
                # return str(questions[ids])
    return send_file("MyQuestionPools.zip",as_attachment=True)
        