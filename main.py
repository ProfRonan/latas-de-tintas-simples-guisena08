print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)


# Coloque o código para resolver o problema nessa parte do programa
cobertura_da_tinta = 3
litros_lata = 18 
valor_da_tinta = 80 
cobertura_da_lata = int(cobertura_da_tinta * litros_lata)
litros_necessarios = metros_quadrados/cobertura_da_tinta
if litros_necessarios <=18:
    qtd_de_latas = 1 
else:   
   qtd_de_latas = int(litros_necessarios/litros_lata)
   if litros_necessarios % litros_lata !=0:
    qtd_de_latas += 1 

    




# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.

valor_total = qtd_de_latas * 80


print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")