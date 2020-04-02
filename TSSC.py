print(' ____________________________________________________________________________________________________')

print('oooo     oooo ooooo  oooo         oooo   oooo oooooooo8 ooooooooooo oooooooooo       o   ooooooooooo ')
print(' 8888o   888   888    88           8888o  88 888         888    88   888    888     888  88  888  88 ')
print(' 88 888o8 88   888    88 ooooooooo 88 888o88  888oooooo  888ooo8     888oooo88     8  88     888     ')
print(' 88  888  88   888    88           88   8888         888 888    oo   888  88o     8oooo88    888     ')
print('o88o  8  o88o   888oo88           o88o    88 o88oooo888 o888ooo8888 o888o  88o8 o88o  o888o o888o    ')
print('                      Testing System The Symptoms of Coronavirus                                     ')
print(' ____________________________________________________________________________________________________')



mm= "************************************************"
arb1 =["هل تعاني من صعوبه التنفس ؟ ","هل تشعر بوجع في الجسم؟ ", "هل تعاني من الضعف الجسدي ؟","هل لديك الحمى؟ ","هل تقوم بالعطس المستمر ؟ ","هل تعاني من   سعال الجاف مستمر ؟"]
arb2= ["هل تعاني من سعال عادي ؟","هل لديك مخاط ؟","هل تعاني من سيلان بالانف ","هل تشعر بوجع في الجسم؟","هل تعاني من الضعف الجسدي ؟","هل لديك الحمى؟","هل تقوم بالعطس المستمر ؟"]
arbn = ["نعم","لا","الرجاء الاجابة ب (نعم) او (لا) ","قم بادخال الاسم الخاص بك : ","مرحبا بك ","لاتمام عملية الفحص يرجى الاجابة بنعم او لا على الاسئله التاليه :"]
eng1=["Do you suffer from difficulty breathing?","Do you feel pain in the body?","Do you suffer from physical weakness?" ,"Do you have a fever?",
"Are you constantly sneezing?","Do you have a persistent dry cough?"]
eng2=["Do you have a normal cough?","Do you have mucus?","Do you suffer from a runny nose?","Do you feel pain in the body?","Do you suffer from physical weakness?" ,"Do you have a fever?",
"Are you constantly sneezing?"]
engn =["yes","no","Please answer (yes) or (no)","please enter your name :","welcome","To complete the examination process, please answer yes or no to the following questions:"]
word=['a', 's', 'd', 'f', 'g', 'o', 'j', 'k', 'l']
anser= [0,0,0,0,0,0,0]
ty = [" "]
edis = ["air pollution","Colds","flu"]
adis = ["تلوث هواء","نزلات البرد","الانفلونزا"]
asol1 =  ("ان الاعراض التي لديك هي اقرب الى",ty[0],"، فلا تقلق ، يجب عليك المداومه على النظافة الشخصة وبالاخص نظافة الايدي بشكل دوري ، مع تمنياتي لك بالسلامه ...")
esol1 =  ("The symptoms that you have are closer to the symptoms of",ty[0],", do not worry, you must maintain personal hygiene, especially hands clean periodically, with my best wishes for your safety ...")
asol2 = ("ناسف ان الاعراض التي لديك هي اقرب الى مرض coronavirus .. يرجى  العمل على عزل نفسك فورا والذهاب الى  الجهات المختصه للقيام بفحص كورونا ")
esol2 = ("We apologize that the symptoms you have are closer to coronavirus .. please work to isolate yourself immediately and go to the relevant authorities to do a corona examination.")
asol3 = ("ان الاعراض لديك غير واضحه تماما ، ان كان الجو لديك غير مستقر فاعلم ان الاعراض تدل على تلوث الهواء اما اذا كانت غير ذلك فانه في الغالب بداية اعراض فيروس كورونا")
esol3 = ("The symptoms you have are not entirely clear. If the atmosphere you have is unstable, know that the symptoms indicate air pollution. If they are not, then it is often the beginning of symptoms of the Corona virus")
asol4 = ("الشكر لله ، انت لا تعاني اي مشاكل صحيه ")
esol4 =("Thank God, you do not have any health problems")
for i in range(20):
    print(mm)
    print ("1.العربيه","   ","2.English ")
    la = input('Please choose a language number: ')

    if (la == "1"):
        qus1= arb1
        qus2= arb2
        an= arbn
        dis = adis
        sol1 = asol1
        sol2 = asol2
        sol3 = asol3
        sol4= asol4
        break

    elif(la == "2"):
        qus1 = eng1
        qus2 = eng2
        an = engn
        dis = edis
        sol1 = esol1
        sol2 = esol2
        sol3= esol3
        sol4 = esol4
        break
    else:
        print ("You entered incorrectly","لقد قمت بادخال غير صحيح")

name = input(an[3])
print(an[4],name,an[5])
class test :

    qm="none"
    def testing(self):
        for i in range(5):
            print(mm)
            ans = input(self.qm)
            if (ans == an[0]):
                return 1
                break
            elif (ans == an[1]):
                return 0
                break
            else:
                print(mm)
                print(an[2])
                print(mm)
        print(mm)
word[-1]=test()
word[-1].qm= qus1[-1]
s= word[-1].testing()
if (s ==1):
    for i in range(5):
        word[i] = test()
        word[i].qm = qus1[i]
        anser[i] = word[i].testing()
    if (sum(anser) > 1):
        print (sol2)
    elif ( anser[4] == 1 ):
        ty = dis[0]
        print(sol1)
    else:
        print(sol3)
else:
    for i in range(7):
        word[i] = test()
        word[i].qm = qus2[i]
        anser[i] = word[i].testing()
    if (sum(anser) > 4):
        ty[0] = dis[2]
        print(sol1)
    elif (sum(anser) == 0) :
        print(sol4)
    elif (anser[3] == 1 or anser[4] == 1 or anser[5] == 1):
        ty[0] = dis[2]
        print(sol1)
    else:
        ty[0]= dis[1]
        print(sol1)