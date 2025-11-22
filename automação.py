import pyautogui
import time

pyautogui.PAUSE = 0.10

# pyautogui.press() - Apertar tecla
# pyautogui.click - Clicar com o mouse
# pyautogui.write - Escrever um texto
# pyautogui.hotkey - selecionar tecla de comando

# abrir o navegador (Chorme, opera)
pyautogui.press("win")
pyautogui.write("navegador opera")
pyautogui.press("enter")
time.sleep(5)

# entrar no site (hashtagtreinamentos.com/curso-python)
pyautogui.write("hashtagtreinamentos.com/curso-python")
pyautogui.press("enter")
time.sleep(5)

# preencher o formulário
pyautogui.click(x=388, y=832)
pyautogui.write("Gabriel Rodrigues")
pyautogui.press("tab")

pyautogui.write("gabrielrodriguesilva07@gmail.com")
pyautogui.press("tab")

pyautogui.write("61991083245")
# enviar o formulário
pyautogui.press("tab")
pyautogui.press("enter")