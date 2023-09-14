import pyautogui
from time import sleep

pyautogui.click(1026,352, duration=2)
pyautogui.write('')

pyautogui.click(1078,436, duration=2)
pyautogui.click(1046,494, duration=2)
pyautogui.write('')
pyautogui.click(1079,564, duration=2)

 
 
 # abrir arquivo de texto

with open ('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(1079,564, duration=2)
        pyautogui.write(produto)

        pyautogui.click(1099,564, duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(1179,564, duration=2)
        pyautogui.write(preco)

        sleep(1)
