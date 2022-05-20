from tkinter import* # Basic tkinter template
root=Tk()

root.title("Drivers license")
root.geometry("600x400")
root.configure(bg="white")
canvas=Canvas(root,width=600,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 600, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehical_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")
label_id=Label(root)
label_name=Label(root)
label_dob=Label(root)
label_pin=Label(root)
label_address=Label(root)
label_vehical_type=Label(root)
# Create all the labels required to be displayed



# Define the function
def show():
    var_id=9530640279
    label_id["text"]=var_id
    var_name="Yuthishree"
    label_name["text"]=var_name
    var_dob="May, 29 2010"
    label_dob["text"]=var_dob
    var_pin=560097
    label_pin["text"]=var_pin
    var_address="Banglore,Karnataka,India"
    label_address["text"]=var_address
    var_vehical_type="Two Wheelers, Three Wheelers, Four Wheelers, LMVs, HMVs"
    label_vehical_type["text"]=var_vehical_type
    
        
    
    
# Create a button
btn=Button(root, text="Show", command=show() )
btn.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
btn_window = canvas.create_window(200, 235, anchor=CENTER, window=btn)
label_id= canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name= canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehical_type = canvas.create_window(335, 180, anchor=CENTER, window=label_vehical_type)
canvas.pack()
root.mainloop()
# tkinter basic template end statement
