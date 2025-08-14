import os
import shutil
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

image_folder = r"C:\Users\acer\Desktop\maske_fotograflar"
output_folder = r"C:\Users\acer\Desktop\maske_kontrol"
class_names = ["maske", "maskesiz"]

image_list = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(f"Toplam {len(image_list)} resim bulundu:")
print(image_list)

index = 0

for cname in class_names:
    os.makedirs(os.path.join(output_folder, cname), exist_ok=True)

def load_image():
    global index, img_label
    if index >= len(image_list):
        img_label.config(image=None, text="Tüm resimler etiketlendi.")
        root.title("Etiketleme Tamamlandı")
        return
    path = os.path.join(image_folder, image_list[index])
    img = Image.open(path)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo, text='')
    img_label.image = photo
    root.title(f"{index+1}/{len(image_list)} - {image_list[index]}")

def key_pressed(event):
    global index
    if index >= len(image_list):
        print("Tüm resimler etiketlendi, işlem tamam.")
        return

    key = event.char.lower()
    if key in ["0", "1"]:
        class_idx = int(key)
        if 0 <= class_idx < len(class_names):
            class_folder = os.path.join(output_folder, class_names[class_idx])
            src_path = os.path.join(image_folder, image_list[index])
            dst_path = os.path.join(class_folder, image_list[index])
            shutil.move(src_path, dst_path)
            index += 1
            load_image()
        else:
            print(f"Geçersiz sınıf indeksi: {class_idx}")
    elif key == 'q':
        root.destroy()

root = Tk()
root.geometry("400x450")  # pencere boyutu genişletildi
img_label = Label(root, font=("Arial", 20), width=300, height=300)
img_label.pack()

info_text = "Etiketleme Tuşları:\n" + "\n".join([f"{i}: {name}" for i, name in enumerate(class_names)])
info_label = Label(root, text=info_text, font=("Arial", 14))
info_label.pack()

quit_button = Button(root, text="Çık", command=root.quit)
quit_button.pack()

root.bind("<Key>", key_pressed)
load_image()
root.mainloop()
