def dni(numero):
  letras="TRWAGMYFPDXBNJZSQVHLCKE"
  return "{}".format(letras[numero%23])

def comprobarLuhn(numero):
  comprobante=0
  for i in range (16):
    valor=int(numero[i])
    if i % 2 == 0:
      valor=int(numero[i])*2
      if valor >= 10:
        valor=valor-9
    comprobante = comprobante+valor
  if comprobante %10 == 0:
    return True
  else:
    return False
