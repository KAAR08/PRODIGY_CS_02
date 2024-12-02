from customtkinter import *
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from PIL import Image
import os
import numpy as np



#app properties
app = CTk(fg_color="#f7f9fc")
app.title("Image Encryption tool")
app.geometry("1000x768")
app.resizable(0,0)


#Header frame
intro_frame = CTkFrame(master=app, fg_color="transparent")
intro_frame.pack(pady=20)

CTkLabel(master=intro_frame, text="ImaPixMa", text_color="#113799",  justify="center", font=("Arial Bold", 30)).pack(pady=(10, 5))
CTkLabel(master=intro_frame, text="Effortless Image Encryption, Unmatched Security.\nPowerful image encryption. Encrypt and decrypt your images with a few clicks.\nPixel-perfect security, simplified, Easy-to-use.", text_color="#113799",  justify="center", font=("Arial", 16)).pack(pady=(0,20))

#Global variables
original_img_data = None
encrypted_img = None
decrypted_img = None

# Uploading image from the local machine
def upload_image():
    global original_img_data
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")))
    
    if file_path: 
        CTkMessagebox(title="Success", message="Image  selection successful!", 
                  icon="check", 
                  option_1="OK")
        
    else:
        CTkMessagebox(title="Error", 
                        message="Image not loaded!", 
                        icon="cancel", 
                        option_1="Okay"
                        )
        
    
    original_img_data = Image.open(file_path)
    or_img = CTkImage(dark_image=original_img_data, light_image=original_img_data, size=(400,400))
    
    original_cap.configure(text="Original Image")
    original_img.configure(image=or_img)
                                           

def encrypt():
    global original_img_data
    global encrypted_img
    global decrypted_img
    
    decrypted_img = None
    
    if not original_img_data:
        CTkMessagebox(title="Error", 
                        message="No image available for encryption!", 
                        icon="cancel", 
                        option_1="Okay"
                        )
        
        
    img_array = np.array(original_img_data, dtype=np.int16)
    
    encrypted_img_arr = (img_array + 146) %256
    
    encrypted_img = Image.fromarray(encrypted_img_arr.astype('uint8'))
    encrypted_ctk_img = CTkImage(dark_image=encrypted_img, light_image=encrypted_img, size=(400, 400))

    new_cap.configure(text="Encrypted Image")
    new_img.configure(image=encrypted_ctk_img)
    footer.configure(text="Aziizkaar@Prodigy InfoTech")

#Decryption function
def decrypt():
    global original_img_data
    global decrypted_img
    global encrypted_img
    encrypted_img = None
    
    #If there is no image uploaded
    if not original_img_data:
        CTkMessagebox(title="Error", 
                        message="No image available for encryption!", 
                        icon="cancel", 
                        option_1="Okay"
                        )
    
    #Store the image pixels as an array
    img_array = np.array(original_img_data, dtype=np.int16)
    
    #Pixels range from 0-255, incase of negative value, use the absolute
    decrypted_img_arr = (img_array - 146) %256
    
    decrypted_img = Image.fromarray(decrypted_img_arr.astype('uint8'))
    decrypted_ctk_img = CTkImage(dark_image=decrypted_img, light_image=decrypted_img, size=(400, 400))

    new_cap.configure(text="Decrypted Image")
    new_img.configure(image=decrypted_ctk_img)
    footer.configure(text="Aziizkaar@Prodigy InfoTech")
        
        
#Save file to local machine
def save_image():
    if encrypted_img or decrypted_img:
        if encrypted_img:
            file_path = filedialog.asksaveasfilename(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")))
        
            if file_path:
                encrypted_img.save(file_path)
            
                CTkMessagebox(title="Success",
                          message=f"Image save successfully to {file_path}",
                          icon="check", option_1="OK")
            else:
                CTkMessagebox(title="Error", 
                          message="Image not saved!", 
                          icon="warning", option_1="OK")
        if decrypted_img:
            file_path = filedialog.asksaveasfilename(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")))
        
            if file_path:
                decrypted_img.save(file_path)
            
                CTkMessagebox(title="Success",
                          message=f"Image save successfully to {file_path}",
                          icon="check", option_1="OK")
            else:
                CTkMessagebox(title="Error", 
                          message="Image not saved!", 
                          icon="warning", option_1="OK")       
        
    else:
        CTkMessagebox(title="Error", 
                      message="No image to save!", 
                      icon="warning", option_1="OK")
        
        
        
#buttons frame
buttons_frame = tk.Frame(app, bg="white")
buttons_frame.pack(pady=10)

#upload button
button_open = CTkButton(buttons_frame, text="Select image", command=upload_image, corner_radius=10, width=150, height=40, fg_color="#4CAF50", font=("Arial", 14),  text_color="white")
button_open.grid(row=0, column=0, padx=10)

#encrypt button
button_encrypt = CTkButton(buttons_frame, text="Encrypt", command=encrypt, corner_radius=10, width=150, height=40, text_color="white",font=("Arial", 14), fg_color="#2196F3" )
button_encrypt.grid(row=0, column=1, padx=10)

#decrypt button
button_decrypt = CTkButton(buttons_frame, text="Decrypt", command=decrypt, corner_radius=10, width=150, height=40, text_color="white",font=("Arial", 14), fg_color="#FFC107" )
button_decrypt.grid(row=0, column=2, padx=10)

#save button
button_save = CTkButton(buttons_frame, text="Save image", command=save_image, corner_radius=10,fg_color="#F44336", width=150, height=40, text_color="white",font=("Arial", 14) )
button_save.grid(row=0, column=3, padx=10)



#image frames
image_frames = CTkFrame(master=app, fg_color="transparent")
image_frames.pack(pady=20)

#original image
original_frame = CTkFrame(master=image_frames, fg_color="#FFFFFF", width=400, height=450)
original_frame.grid(row=0, column=0, padx=20)
original_cap = CTkLabel(master=original_frame, text="", font=("Arial Bold", 20), text_color="#113799")
original_cap.pack(pady=10)
original_img = CTkLabel(master=original_frame, text="")
original_img.pack()

#new image
new_frame = CTkFrame(master=image_frames, fg_color="#FFFFFF", width=400, height=450)
new_frame.grid(row=0, column=1, padx=20)
new_cap = CTkLabel(master=new_frame, text="", font=("Arial Bold", 20), text_color="#113799")
new_cap.pack(pady=10)
new_img = CTkLabel(master=new_frame, text="")
new_img.pack()

#footer
footer = CTkLabel(master=image_frames, text=" ", text_color="#113799",  justify="center", font=("Arial Bold", 16, "italic"))
footer.grid(padx=(350,0), pady=(20,0))



app.mainloop()