nome = "Mika"
cognome = "Souza"
print(nome, cognome)

with open("output.txt", mode = "a") as file:
    file.write("hello world")

print("\nStringa 'hello word' scritta sul file 'output.txt' corretamente.")
