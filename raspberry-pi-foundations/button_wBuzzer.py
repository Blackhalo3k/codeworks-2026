from gpiozero import Button 
button = button(2)
button.wait_for_press()
print("Hiiii! :3")
