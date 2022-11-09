def dni(numero):
  letras=("TRWAGMYFPDXBNJZSQVHLCKE")
  return "{}{}.".format(numero, letras[numero%23])
