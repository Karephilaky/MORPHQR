import pandas as pd
import qrcode
from tkinter import Tk, filedialog, Button, Label, Listbox, Scrollbar, RIGHT, Y
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Función para cargar el archivo Excel
def cargar_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    if file_path:
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file_path)
            
            # Verificar que haya al menos una fila y una columna
            if df.empty:
                messagebox.showerror("Error", "El archivo Excel está vacío.")
                return

            lista_invitados.delete(0, 'end')  # Limpiar la lista
            for _, row in df.iterrows():
                # Mostrar la fila completa con las columnas disponibles
                invitado_info = ' - '.join([f"{col}: {row[col]}" for col in df.columns])
                lista_invitados.insert('end', invitado_info)

            # Guardar los datos del Excel para usarlos después
            global datos_invitados
            datos_invitados = df
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

# Función para generar los códigos QR
# Función para generar los códigos QR
def generar_qr():
    if datos_invitados.empty:
        messagebox.showwarning("Advertencia", "No hay datos cargados para generar códigos QR.")
        return
    
    output_dir = "codigos_qr"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, row in datos_invitados.iterrows():
        # Crear un string con toda la información de la fila
        informacion_invitado = '\n'.join([f"{col}: {row[col]}" for col in datos_invitados.columns])
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(informacion_invitado)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        qr_file = os.path.join(output_dir, f'invitado_{index+1}.png')
        img.save(qr_file)

        lista_invitados.delete(index)  # Eliminar el invitado de la lista
        lista_invitados.insert(index, f"{row[datos_invitados.columns[0]]} - QR generado")  # Marcar como generado

    messagebox.showinfo("Éxito", "Códigos QR generados correctamente.")


# Función para previsualizar el código QR de un invitado seleccionado
def previsualizar_qr(event):
    seleccion = lista_invitados.curselection()
    if seleccion:
        index = seleccion[0]
        row = datos_invitados.iloc[index]
        
        # Crear un string con toda la información de la fila
        informacion_invitado = '\n'.join([f"{col}: {row[col]}" for col in datos_invitados.columns])
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(informacion_invitado)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        img.thumbnail((150, 150))  # Redimensionar para previsualizar
        img_tk = ImageTk.PhotoImage(img)
        
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk

# Configuración de la interfaz gráfica con tkinter
root = Tk()
root.title("Generador de Códigos QR para Invitados")

# Etiquetas y botones
Label(root, text="Cargar archivo Excel con datos de invitados").pack(pady=10)
btn_cargar = Button(root, text="Cargar Excel", command=cargar_excel)
btn_cargar.pack(pady=5)

Label(root, text="Lista de Invitados").pack(pady=10)
lista_invitados = Listbox(root, height=10, width=50)
lista_invitados.pack(pady=10)

# Barra de desplazamiento para la lista
scrollbar = Scrollbar(root, orient='vertical', command=lista_invitados.yview)
scrollbar.pack(side=RIGHT, fill=Y)
lista_invitados.config(yscrollcommand=scrollbar.set)

# Etiqueta para previsualizar el QR
label_imagen = Label(root)
label_imagen.pack(pady=10)

# Botón para generar los códigos QR
btn_generar = Button(root, text="Generar Códigos QR", command=generar_qr)
btn_generar.pack(pady=10)

# Lista para almacenar los datos del archivo Excel
datos_invitados = []

# Bind para previsualizar el QR al seleccionar un invitado
lista_invitados.bind("<<ListboxSelect>>", previsualizar_qr)

# Ejecutar la aplicación
root.mainloop()
