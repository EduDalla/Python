# Example with one "except"

# try:
#     value = int(input('Insira um número natural:'))
#     print('O recíproco de', value, 'é', 1 / value)
# except: # In case you make a mistake tying in the "value" or writing the code, the code will run except
#     print('Não sei o que fazer.')

# Example with two "except" specifying where the error goes

try:
    value = int(input('Digite um número natural: '))
    print('O recíproco de', value, 'é', 1/value)
except ValueError:
    print('Eu não sei o que fazer.')
except ZeroDivisionError: # none of the exceptions cann be specified more than one time, ex: except ZeroDivisionError and ValueError:
    print('A divisão por zero não é permitida em nosso Universo.')
except:
    print('algo de estranho aconteceu aqui ... Desculpe! ') # O except padrão deve ser o último except. Sempre!