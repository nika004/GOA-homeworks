num = int(input("შეიყვანეთ რიცხვი: "))


if num % 2 == 0:
    print("even") 
else:
    print("odd")   




my_name = "ნიკა" 
user_name = input("შეიყვანეთ თქვენი სახელი: ")

if user_name == my_name:
    print("Hello")
else:
    print("Bye")



score = int(input("შეიყვანეთ ქულა: "))

if score > 90:
    print("A")
elif score > 70:
    print("B")
elif score > 50:
    print("C")
else:
    print("D")


i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, " ლუწია")
    else:
        print(i, " კენტია")
    i += 1