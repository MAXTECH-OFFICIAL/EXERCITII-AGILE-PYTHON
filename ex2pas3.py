def calculator_varsta():
    varsta_initiala=input("Introdu varsta ta actuala: ")
    varsta=int(varsta_initiala)
    acum3ani=varsta-3
    peste7ani=varsta+7
    print(f"Varsta ta acuala este {varsta} ani.")
    print(f"Acum 3 ani ai avut {acum3ani} ani.")
    print(f"Varsta ta peste 7 ani va fi de {peste7ani} ani.")

calculator_varsta()