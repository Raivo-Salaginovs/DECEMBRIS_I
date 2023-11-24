cipars=int(input("Ievadi skaitli :"))
skaitlis=[1, cipars]
rezultats=list(filter(lambda x:x%2, skaitlis))
print(rezultats)