# Python 3 - Parte 2 - Avançando na Linguagem

Curso da Alura sobre Introdução à Linguagem Python

## Objetivo Final &#x1F3AF;

Criar um jogo da forca, onde o usuário terá que acertar a palavra ou perderá o jogo.

URL do curso -> [Python 3 - Parte 2 - Avançando na Linguagem](https://cursos.alura.com.br/course/python-3-avancando-na-linguagem)

![Python 3 - Parte 2 - Avançando na Linguagem](https://www.alura.com.br/assets/api/share/curso-python-3-avancando-na-linguagem.png)

## Links Úteis &#x1F517;
* [Python](https://www.python.org/) - Site oficial do pyhton.
* [PyCharm](https://www.jetbrains.com/pycharm/) - Site da IDE PyCharm muito utilizada para o desenvolvimento de Python.
* <a href="Arquivos Base/Arquivos Base.rar" download="Arquivos Base.rar" type="application/zip">Arquivos Base</a> - Arquivos necessários para o inicio do projeto.

<hr>

## 01 - Preparando o Jogo da Forca

### 01 - Game Loop
* A palavra chave `not` significa negação no python, invertendo valores **bool** por exemplo.

## 02 - Manipulando Strings

### 01 - Encontrando Letras
* A função `find()` presente nas **strings** retorna o *index* do caractere passado por parâmetro na função.
* É possível iterar sobre **string** utilizando o laço **for**.

### 02 - Funções Importantes da String
* A função `strip()` retorna uma nova **string** sem espaços em branco.
* A função `lower()` transforma uma string em *lowercase*.

## 03 - Conhecendo e Trabalhando com Listas

### 01 - Estrutura de Dados - List
* Para declarar uma lista, utiliza-se o `[]` para atribuição de uma variável.

### 02 - Guardando as Letras Acertadas
* Como substituir um valor de uma **lista**.
* Como imprimir uma **lista** passando ela como parâmetro para o `print()`.

## 04 - Conhecendo e Trabalhando com Tuplas

### 01 - O que são Tuplas
* Uma **Tupla** é uma lista que não pode ser alterada.
* Para declarar uma **Tupla**, basta colocar os valores entre `()`, `days = ("Monday", "third", ...)`.

### 02 - Listas e Tuplas Juntas
* É possível criar uma **lista** de **tuplas**, como:
```
p1 = (1, 2)
p2 = (3, 4)
p3 = (5, 6)
line = [p1, p2, p3]
"[(1, 2), (3, 4), (5, 6)]"
```
* A função `tuple()` recebe um conjunto de elementos e retorna uma **tupla**.
* A função `list()` recebe um conjunto de elementos e retorna uma **lista**.
* Como declarar um **set**.
* Um **set** não pode conter elementos duplicados.
* Como declarar um **dicionary**.
* Um **dictionary** é um conjunto **chave : valor**, em que o *index* é procurado pela **chave** para acessar o **valor**.

## 05 - Implementando o Encerramento do Jogo

### 01 - Estipulando Tentativas de Erros
* Como parar um loop com a palavra reservada **break**.

### 02 - Compreensão de Lista
* É possível inicializar o conteúdo de uma **lista** dentro dos `[]`, como por exemplo: `correct_letters = ["_" for letter in secret_word]`, essa funcionalidade se chama ***List Comprehension***.
* Para filtrar um resultado de um `for` e coloca-lo dentro de uma **lista**, usamos a sintaxe `pairs = [number for number in integers if number % 2 == 0]`, onde o filtro `if` é colocado logo após o `for`.

## 06 - Escrita e Leitura de Arquivos

### 01 - Escrevendo em um Arquivo
* Abrir um **arquivo** com o comando `open()` passando:
    * O nome do **arquivo** como parâmetro.
    * O modo que o **arquivo** deve ser lido, como por exemplo, leitura (`"r"`) ou escrita (`"w"`).
* Ao usar o comando `open()`, ele irá apagar o **arquivo** caso ele exista no diretório, para somente *adicionar* conteúdo, na passagem do 2º parâmetro, se usa o `"a"`.
* A função `FILE.write("banana")` escreve algo no **arquivo** e retorna o número de caracteres que foram adicionados no arquivo.
* A função `FILE.close()` fecha a conexão do **arquivo** entre o computador e o **Python**.

### 02 - Lendo um Arquivo
* Ler um **arquivo** utilizando o comando `read()`.
* Ler uma linha usando `readLine()`.

### 03 - Escolhendo uma Palavra
* Escolher aleatoriamente um valor com a função `random.randrange()` onde o primeiro parâmetro é o valor inicial e o segundo parâmetro é o valor final.

## 07 - Melhorando o Código e a Apresentação

### 01 - Organizando o Código em Funções
* Separando partes do código em funções.
* Retornar um valor de uma função.
* Sabemos que quebrar uma grande função complexa em pequenas funções é uma boa prática por causa de diversos fatores, mas podemos citar como os principais deles:
* Dar manutenção ao código fica muito mais fácil, visto que agora podemos examinar vários pequenos blocos, que são muito mais fáceis de compreender do que um grande bloco de código.
* Ao quebrar uma grande função, também estamos deixando ela com menos responsabilidades, com a meta de atingir o ideal de que cada função tenha apenas uma única responsabilidade.
* O código também fica muito mais fácil de testar, pois se temos diversas funções pequenas, conseguimos testar uma a uma em busca de erros no código.
* E por último, a legibilidade do código aumenta muito, pois dando nomes semânticos a cada uma das funções menores, conseguimos deixar bem claro o que aquela parte do código deve fazer e facilita o entendimento do todo como um geral.