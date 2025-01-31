import pytesseract
import pyautogui
from PIL import Image

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

text = pytesseract.image_to_string(Image.open("screenshot.png"))
print("Extracted Text:\n", text)
