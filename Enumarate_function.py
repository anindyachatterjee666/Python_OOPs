
    #1st

# lst = ["Alu", "Gazar", "Egg", "Mutton", "Bread"]
#
# i = 0
# for item in lst:
#     if i % 2 == 0:
#         print(f"Anindya please buy {item}")
#     i += 1

       # 2nd

lst = ["Alu", "Gazar", "Egg", "Mutton", "Bread", "Kaju", "Almond"]

for index, item in enumerate(lst):      # index always  starts from 0
    if index % 2 != 0:
        print(f"Anindya please buy {item}")