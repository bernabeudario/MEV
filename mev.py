import msvcrt
import os

invocationPhrase='monstruo de spagueti volador responde a mi pregunta'
secretKey=','
exitKey='q'
helpKey='h'

def initSecretMode():
    resp=[]
    for item in invocationPhrase:
        print(item,end='',flush=True)
        currentKey = msvcrt.getwch()
        if currentKey == secretKey:
            break
        resp.append(currentKey)
    return resp

def responseDefault():
    resp=['No puedo responder ahora']
    return resp[0]

def printResponse(resp):
    print('\nRespuesta:')
    if len(resp) > 0:
        print(''.join(resp).upper())
    else:
        print(responseDefault().upper())

def main():
    os.system ('cls')
    while True:
        responsePhrase = []
        print(f'\nHaz tu invocación ("{exitKey}" para salir, "{helpKey}" para ayuda):')
        currentKey = msvcrt.getwch()
        if currentKey == secretKey:
            responsePhrase=initSecretMode()
        elif currentKey == exitKey:
            exit(0)
        elif currentKey == helpKey:
            print(f'Para invocar al MEV tipea: {invocationPhrase}')
            continue
        else:
            print(currentKey,end='',flush=True)
        input()
        input('\nHaz tu pregunta al MEV: ')
        printResponse(responsePhrase)

if __name__ == '__main__':
    main()