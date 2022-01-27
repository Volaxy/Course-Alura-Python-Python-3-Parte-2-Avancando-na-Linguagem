Além do `r`, `w` e `a` existe o modificador `b` que devemos utilizar quando queremos trabalhar no modo binário. Para abrir uma imagem devemos usar:

`imagem = open("foto.jpg", "rb")`

Por exemplo, o código abaixo cria uma cópia de uma imagem:
```
#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()
```