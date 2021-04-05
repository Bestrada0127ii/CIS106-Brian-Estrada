def exam(names,score): 
        for i in range(len(names)):
            print('name: '+ names[i] + ' score: ' + str(score[i]))
#main
names = ['smith', 'Johnson', 'Williams','Jones', 'Brown','Davis','Miller', 'Wilson', 'Moore','Walker']
score = [98, 87, 56, 67, 91, 82, 85, 74, 59, 84]
exam(names,score)