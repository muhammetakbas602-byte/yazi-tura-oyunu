import random

para = ["Yazı", "Tura"]
yenidenOyna = "evet"

while yenidenOyna == "evet":
    soru = input("Yazı mı, Tura mı: ")

    cevap = random.choice(para)

    if soru == cevap:
        print("Cevap Doğru :)")
    else:
        print("Cevap Yanlış :(")

    yenidenOyna = input("Yeniden oynayalım mı:").lower()
    
input("Çıkmak İçin Enter'a basın...") 