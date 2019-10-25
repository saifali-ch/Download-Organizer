# Name : Downloads_Organizer
# Version : v1.0.0
# Author : Saif Ali
# Email : chsaifali097@gmail.com
# Contact : 03065292097
# LabelFrame, PanedWindow, TopLevel, MenuButton #todo List
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import simpledialog
from ttkthemes import themed_tk as tk
import tkinter.messagebox
import os


'''/////////////////////////////////////Root///////////////////////////////////////////////'''
root = tk.ThemedTk()
root.resizable(width=FALSE, height=FALSE)
root.title("Download Organizer v1.0.0")
root.iconbitmap(r"icon.ico")
root.set_theme("clearlooks")


'''/////////////////////////////////////Global Data///////////////////////////////////////////////'''
path = ""
extention_list = ['.mp4', '.mkv', '.3gp',
                  '.png', '.jpg', '.jpeg',
                  '.mp3', '.m4a', '.wav',
                  '.pdf', '.exe', '.zip',
                  '.txt', '.torrent']
directory_selected = FALSE


'''////////////////////////////////////Internal Functions/////////////////////////////////////////'''
def get_folder_name(extention):
    # extention = .mp4 This Func Will converted extention to Mp4 and return
    dot , extention = extention.split(".")
    dir_name = extention.title()
    return dir_name
      
def organize_files():
    global directory_selected, extention_list, path    
    '''/////////////////////////////Exception Handling///////////////////////////////////////'''
    if directory_selected:    
        os.chdir(path)
        total_exists = 0
        already_existing_files = []
        total_moved = 0
        dir_flag = 0    
        for file in os.listdir():   
            filename , extention = os.path.splitext(file)
            print(file)
            if extention in extention_list:
                '''/////////////////////////////Checking & Creating Floder////////////////////////////////'''
                folder_name = ""
                folder_name = get_folder_name(extention)
                folder_path = ""
                if folder_name not in os.listdir():
                    dir_flag += 1
                    folder_path = os.path.join(path, folder_name)
                    os.mkdir(folder_path)
                    status=tree.insert("", 'end', text=f"Creating {folder_name} Directory", tags='F')
                    
                '''/////////////////////////////Moving File///////////////////////////////////////////////'''
                folder_path = os.path.join(path, folder_name)   
                file_src = os.path.join(path, file)
                file_dest = os.path.join(folder_path, file)
                if os.path.exists(file_dest):
                    already_existing_files.append(file_src)
                    total_exists += 1
                else:
                    os.rename(file_src, file_dest)
                    total_moved += 1
                    
        status=tree.insert("",'end', text=f"<{'~'*50}>", tags='Line')
        status=tree.insert("",'end', text=f"[+] {dir_flag} New Directories Have Been Created", tags='F')
        status=tree.insert("",'end', text=f"[+] {total_exists} Files Already Exists", tags='F')
        status=tree.insert("",'end', text=f"[+] {total_moved} Files Has Been Moved", tags='F')

        '''/////////////////////////////Deleting Already Existing Files///////////////////////////////////////'''
        if total_exists > 0:
            ans = tkinter.messagebox.askyesno("Some Files Already Exists", "Do You Want To Delete Them?")
            if ans:
                tree.insert('','end',text="\n")
                if total_exists == 1:
                    file = "File"
                else:
                    file = "Files"            
                tree.insert('','end',text=f"[+] Deleting {total_exists} {file}...", tags='Deleting')
                total_exists = 0
                for file_to_delete in already_existing_files:
                    deleted = os.path.basename(file_to_delete)
                    deleted = f"Deleting -> {deleted}"
                    deleted = tree.insert("",'end',text=deleted, tags='F')
                    os.remove(file_to_delete)   
    else:
        tree.insert("","end", text="Please Select Directory First!", tags='F')
    
    
'''/////////////////////////////////////Gui Functions/////////////////////////////////////////////'''
def password_checking():
    password = simpledialog.askstring("Password", "Please Enter Password")
    if password == None:
        root.destroy()
    elif password == 'None':
        again = tkinter.messagebox.showerror("Wrong Password", "Incorrect Password!            ")        
        root.destroy()
    elif password.lower() == 'sp19-bse-036':
        pass
    else:
        again = tkinter.messagebox.showerror("Wrong Password", "Incorrect Password!            ")
        if again == 'ok':
            password_checking()
        
def select_directory():
    global path, directory_selected
    path = filedialog.askdirectory()
    show_path['text'] = path
    if os.path.isdir(path):
        directory_selected = TRUE
        
def extention_txt_list():
    txt_list = filedialog.askopenfilename()
    tree.insert("","end", text="[+] Adding Extention List")
    extention_folder = tree.insert("",'end',text="Extention List")
    
    with open(txt_list,"r") as file:
        for line in file:
            tree.insert(extention_folder,"end",text=line)
            print(line, end="")
    
def change_extentions():
    global extention_list
    try: 
        extensions = simpledialog.askstring("Replace Current Extentions",
                                            "Add Space Seprated Extensions e.g (mp4 exe zip)")
        if extensions == '':
            pass
        else:
            new_extentions =  extensions.split()
            extention_list.clear()
            for x in range(0, len(new_extentions)):
                dot_append = "." + new_extentions[x]
                extention_list.append(dot_append)
    except:
        pass
    ext_list['text'] = extention_list
          
def default_extentions():
    default_ext_list = ['.mp4', '.mkv', '.3gp',
                        '.png', '.jpg', '.jpeg',
                        '.mp3', '.m4a', '.wav',
                        '.pdf', '.exe', '.zip',
                        '.txt', '.torrent']
    message = tkinter.messagebox.showinfo("Default Extentions",default_ext_list)

def change_theme():
    root.set_theme(selected.get())
    style.configure   ('Treeview', rowheight=25)
    tree.column ("#0", width=850)
    
def about_us():
    tkinter.messagebox.showinfo("About Us",
                                "Download Organizer v1.0.0\n"
                                "Organization: Comsats University Islamabad, Sahiwal Campus\n\n"
                                "Developed By Saif Ali\n"
                                "Email: chsaifali097@gmail.com\n"
                                "Contact: +923065292097")

def usage_guide():
    tkinter.messagebox.showinfo("Usage Guide", "This Tool Organizes "
                                "Your Files On The Basis Of Their Extentions.\n"
                                "There Are Some Built-in Extentions Which You "
                                "Can Use Or You Can Replace Them With Your Own Once.\n"
                                "\nProcedure:\n-> Select Your Desired Folder Using \'Select Directroy\' Button\n"
                                "-> Click \'Organize Files\' Button\n"
                                "It Will Create Folders Using Given Extensions e.g (.mp4 -> Mp4)\n"
                                "After That It Will Move .mp4 Files to Mp4 Folder, .zip Files To Zip Folder and So on.\n")
 
def on_close():
    ans = tkinter.messagebox.showwarning("Quit", "Are You Sure To Quit ?", type="yesno", default="yes")
    if ans == 'yes':
        root.destroy()
        
def Exit():
    root.destroy()
      
       
'''/////////////////////////////////////Menu Bar///////////////////////////////////////////////'''
MenuBar  = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
Options = Menu(MenuBar, tearoff=0)
Help = Menu(MenuBar, tearoff=0)

MenuBar.add_cascade(label="File", menu=FileMenu)
MenuBar.add_cascade(label="Options", menu=Options)
MenuBar.add_cascade(label="Help", menu=Help)

FileMenu.add_command(label="Exit", command=Exit)
Options_SubMenu = Menu(Options, tearoff=0)
Options.add_cascade(label="Select Theme", menu=Options_SubMenu)
Help.add_command(label="Usage Guide", command=usage_guide)
Help.add_separator()
Help.add_command(label="About Us", command=about_us)

root.config(menu=MenuBar)


'''/////////////////////////////////////Bottom Bar///////////////////////////////////////////////'''
bottom_bar = ttk.Label(root, text="Welcome To Download Organizer v1.0.0", relief=RIDGE, borderwidth=4, anchor = W)
bottom_bar.pack(side=BOTTOM, fill=X)


'''/////////////////////////////////////Frames///////////////////////////////////////////////'''
left_frame          = Frame(root,         relief=SUNKEN, borderwidth=4)
center_frame        = Frame(root,         relief=GROOVE, borderwidth=4)
center_frame_upper  = Frame(center_frame, relief=RAISED, borderwidth=4)
center_frame_middle = Frame(center_frame, relief=RIDGE, borderwidth=4)
center_frame_bottom = Frame(center_frame, relief=SUNKEN, borderwidth=4)
left_frame.pack         (side=LEFT, fill=Y)
center_frame.pack       (side=LEFT, fill=BOTH)
center_frame_upper.pack (side=TOP)
center_frame_middle.pack(side=TOP, fill=X)
center_frame_bottom.pack(side=BOTTOM, fill=X)


'''/////////////////////////////////////TreeView///////////////////////////////////////////////'''
tree = ttk.Treeview(center_frame_upper)
tree.pack(side=LEFT, ipady=60)
style = ttk.Style (center_frame_upper)
style.configure   ('Treeview', rowheight=25)
tree.column ("#0", width=850, minwidth=860)
tree.heading      ("#0",text="Status",anchor=S)
tree.tag_configure('F', font='TimesNewRoman 10')
tree.tag_configure('Deleting', font='Arial 11 bold')
tree.tag_configure('Line', font='Arial 11 bold')


'''///////////////////////////////////Scroll Bar/////////////////////////////////////////////'''
vertical_bar   = ttk.Scrollbar(center_frame_upper,  orient="vertical",  command=tree.yview)
horizontal_bar = ttk.Scrollbar(center_frame_middle, orient="horizontal",command=tree.xview)
tree.configure     (xscrollcommand=horizontal_bar.set, yscrollcommand=vertical_bar.set)
vertical_bar.pack  (side=LEFT, fill=Y)
horizontal_bar.pack(side=BOTTOM, fill=X)


'''/////////////////////////////////////Labels///////////////////////////////////////////////'''
current_path       = Label(center_frame_bottom, text="Current Path",       font='Arial 10 bold')
show_path          = Label(center_frame_bottom, text="Set Path Please")
current_extentions = Label(center_frame_bottom, text="Current Extentions", font='Arial 10 bold')
ext_list           = Label(center_frame_bottom, text=extention_list)
current_path.pack      (side=TOP, padx=100, pady=10)
show_path.pack         (side=TOP)
current_extentions.pack(side=TOP, pady=10)
ext_list.pack          (side=TOP)


'''/////////////////////////////////////Buttons///////////////////////////////////////////////'''
select_directory   = ttk.Button(left_frame,  text="Select Directory",   command=select_directory)
move_file          = ttk.Button(left_frame,  text="Organize Files",     command=organize_files)
change_extention   = ttk.Button(left_frame,  text="Change Extentions",  command=change_extentions)
default_extentions = ttk.Button(left_frame,  text="View Default Extentions", command=default_extentions)
select_directory.pack  (padx=20, pady=30, anchor=S)
move_file.pack         (padx=20, pady=30, anchor=S)
change_extention.pack  (padx=20, pady=30, anchor=S)
default_extentions.pack(padx=20, pady=30, anchor=S)


'''/////////////////////////////////////Radio Buttons//////////////////////////////////////////'''
themes = ['aquativo', 'alt', 'arc', 'black', 'blue', 'clam', 'classic', 'clearlooks',
          'elegance', 'itft1', 'keramik', 'kroc', 'plastik', 'radiance','scidsand', 'smog',
          'vista', 'winnative', 'winxpblue', 'xpnative']
selected = StringVar()
for theme in themes:
    Options_SubMenu.add_radiobutton(label=theme.title(), value=theme, variable=selected, command=change_theme)
    Options_SubMenu.add_separator() 
selected.set("clearlooks")     

# password_checking()
# If Clicks On Close Button Then Error Can Occur
try:
    root.protocol("WM_DELETE_WINDOW", on_close)
except:
    pass
root.mainloop()