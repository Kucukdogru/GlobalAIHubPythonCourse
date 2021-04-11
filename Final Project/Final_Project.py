#!/usr/bin/env python
# coding: utf-8

# ### Final Project
# - Knowledge competition
# - Write a knowledge competition program.
# - It should consist of 10 questions in total.
# - Each question will have only one answer.
# - Adjust the answers of the questions according to case sensitivity.
# - Each question should be worth 10 points.
# - If User answers 5 or fewer questions, it will be considered unsuccessful.
# - If the user answers more than 5 questions correctly, It will be considered successfull.


score = 0;
print("*******************************Welcome*****************************")
print("Yarışmamız 10 sorudan oluşmaktadır ve her soru 10 puandır. 50 puan üzeri aldığınız takdirde başarılı sayılacaksınız.")
print("Şıklarımız küçük büyük harfe duyarlı değildir!!!")

answer1 = input("Soru1:\na=5\nb=a ise b değeri kaçtır?\nA)5    B)null   C)0\nCevabınız: ")
if(answer1=="A" or answer1=="a"):
    score+=10
      
answer2 = input("\nSoru2:\nPython'da len() fonksiyonunun görevi nedir?\nA)Toplama işlemi yapmak   B)Eleman sayısını bulmak   C)Çıkarma işlemi yapmak\nCevabınız: ")
if(answer2=="B" or answer2=="b"):
    score+=10

answer3 = input("\nSoru3:\nAşağıdaki kütüphanelerden hangisi Python'da kullanılan kütüphanelerden birisi değildir?\nA)Numpy    B)Pandas   C)Entity Framework\nCevabınız: ")
if(answer3=="C" or answer3=="c"):
    score+=10
      
answer4 = input("\nSoru4:\nrandom() fonksiyonun görevi nedir?\nA)Belli bir değer aralığında rastgele değer üretmek     B)Uzunluk hesaplamak   C)Dairenin yarı çapını hesaplamak \nCevabınız: ")
if(answer4=="a" or answer4=="A"):
    score+=10

answer5 = input("\nSoru5:\n'Hello World' ifadesi hangi değişken tipini ifade eder?\nA)Bool     B)String   C)Char\nCevabınız: ")
if(answer5=="b" or answer5=="B"):
    score+=10
      
answer6 = input("\nSoru6:\nAşağıdaki şıklarda verilen liste oluşturma yöntemlerinden hangisi Python için doğru değildir?\nA)liste = list(range(5))     B)liste = [1,2,3]   C)List<int> numbers = new List<int>()\nCevabınız: ")
if(answer6=="C" or answer6=="c"):
    score+=10
      
answer7 = input("\nSoru7:\nPython'da excel dosyası nasıl okunur?\nA)read_csv('veriler.csv')     B)StreamReader sr=new StreamReader('veriler.csv')   C)fp = fopen('veriler.csv', 'r')\nCevabınız: ")
if(answer7=="A" or answer7=="a"):
    score+=10
      
answer8 = input("\nSoru8:\nPython'da ilk 5 kaydı listelemek için hangi fonksiyonu kullanırız?\nA)list()    B)tail()   C)head() \nCevabınız: ")
if(answer8=="C" or answer8=="c"):
    score+=10
    
answer9 = input("\nSoru9:\ndictionary = {'name':'Merve', 'surname':'KÜÇÜKDOĞRU', 'job':'Computer Engineer'}\nprint(dictionary['job'])\nYukarıdaki kodun ekran çıktısı nedir? \nA)Merve   B)Computer Engineer   C)job\nCevabınız: ")
if(answer9=="b" or answer9=="B"):
    score+=10
    
answer10 = input("\nSoru10:\nmy_list = [1, 2, 3, 4 , 5]\nmy_list.pop();\nprint(my_list)\nYukarıdaki kodun ekran çıktısı nedir ? \nA)[1, 2, 3, 4, 5]   B)[1, 2, 3, 4, 5, 6]   C)[1, 2, 3, 4] \nCevabınız: ")
if(answer10=="C" or answer10=="c"):
    score+=10
    
    
    
print("\n\nToplam puan : {} " .format(score))
if score>50:
    print("####################Tebrikler###################")
else:
    print("Üzgünüz, sınavı geçemediniz!!!")
