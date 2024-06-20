# Teoria - Python

## Tipo de variaveis

- Integer(int) -  Numeros inteiros
- Float - numero com ponto
- String - conjunto de caracteres -> "" ou ''
- Boolean(bool) - True ou False / 1 e 0

## Operadores Aritmeticos

- soma -> +
- subtracao -> -
- divisao -> /
- multiplicacao -> *
- exponenciacao -> **
- divisao inteira -> //
- resto -> %

## Output

> saida de dados de qualquer forma

### No terminal -> print

```python
print("valor")
```

## Input 

> Entrada de informacoes em um codigo

### Input no terminal -> Input()

> input() SO ENTENDE STRING!!!

```python
a = float(input())
print(2*a)
```

## Comparadores

- igualdade ==
- maior que >
- maior igual >=
- diferente !=

## Condicionais -> If, else ,elif

>controles de fluxo de codigo

```python
idade = int(input())

if idade>18:
    print('maior de idade')
else:
    print('menor de idade')
```

## Estrutura de repeticao - While e o For

### Comandos

- continue -> pula para proxima interacao 
- Break -> forca a saida do while imediatamente

### While 

```python

while condicao:
    ...

```