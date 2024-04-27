import re

def valida_numero_telefone(tel):
   
  pattern = "\(\d{2}\) \d{5}-\d{4}"
    
  if re.match(pattern, phone_number): 
    
    return "Número de telefone válido."
    
  else:
      
    return "Número de telefone inválido."
        
numero_telefone = input()  

resultado = valida_numero_telefone(numero_telefone)

print(result)
