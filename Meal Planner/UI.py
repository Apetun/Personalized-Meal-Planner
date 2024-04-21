import customtkinter
import tkinter
import oracledb 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.user = ''
        self.login_window()
        self.missing = []
        
    def recipe(self,recipe_id):
        
            def back():
                root_new.destroy()
                self.recipesview()

            
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("RECIPE")
            
            recipe=None
            conn = None
            try:
                    conn = oracledb.connect(
                    user="jeffin",
                    password="jancy123",
                    dsn="localhost/xe")
                        
                    cursor = conn.cursor()
                        
                    cursor.execute("select * from recipe where recipe_id = :id",id=recipe_id)
                            
                    recipe = cursor.fetchone()

                        
                        

            except Exception as err:
                    print('Error while connecting to the db')
                    print(err)
                    exit()
                
            finally:

                    cursor.close()
                    conn.close()
            

        
            my_text = customtkinter.CTkTextbox(root_new,width=450,height=300, corner_radius=10)
            my_text.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            my_text.insert('end',recipe[3])
                
            
            
            back_button = customtkinter.CTkButton(root_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.03,rely=0.03)
            
            
            root_new.mainloop()
        
        
    
    def searchrecipe(self):
            
            def back():
                root_new.destroy()
                self.recipesview()
                
            def add():
                if entry_1.get() != '':
                    conn = None
                    try:
                        conn = oracledb.connect(
                        user="jeffin",
                        password="jancy123",
                        dsn="localhost/xe")
                                                    
                            
                        
                        cursor = conn.cursor()
                        
                        exists = cursor.var(oracledb.NUMBER)
                        
                        recid = entry_1.get()
                        
                        cursor.callproc("check_recipe_id", (recid, exists))
                        result = exists.getvalue()

                        if result == 0:
                            entry_1.configure(fg_color=("#E34234","#E34234"))
                            print("Recipe ID exists in the table.")
                            label = customtkinter.CTkLabel(master=frame_new,text="Recipe ID does not exist!", font= ("Helvetica",13))
                            label.place(relx=0.23, rely=0.12, anchor=tkinter.CENTER)
                            return
                        
                        y = entry_1.get()
                        root_new.destroy()
                        self.recipe(y)       

                    except Exception as err:
                        print('Error while connecting to the db')
                        print(err)
                        exit()
                        
                    finally:
                        cursor.close()
                        conn.close()
                    
                
                     
            
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("RECIPES")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            
            entry_1 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Recipe ID Format:R1,R2,etc")
            entry_1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
            
            back_button = customtkinter.CTkButton(master=frame_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.6,rely=0.05)
            
            button_add = customtkinter.CTkButton(master=frame_new, text="VIEW RECIPE", corner_radius=6, command=add, width=400)
            button_add.place(relx=0.5,rely=0.9,anchor = tkinter.CENTER)
            
            root_new.mainloop()
    
    def shoppinglist(self):
            def back():
                root_new.destroy()
                self.meals()

            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("SHOPPING LIST")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkScrollableFrame(master=root_new,width=450, height=300,label_text="MISSING INGREDIENTS", corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            
            if self.missing:
                for x in range(len(self.missing)):
                    text = self.missing[x]
                    customtkinter.CTkButton(master=frame_new, text=text, width=400).pack(pady=10)
                    
                        
            else:
                customtkinter.CTkButton(master=frame_new, text="All Ingredients Present", width=400).pack(pady=10)
                    
            back_button = customtkinter.CTkButton(root_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.03,rely=0.03)
                
            
            root_new.mainloop()
    
    def recipesadd(self):
        
            def back():
                root_new.destroy()
                self.main_page()
            
            def add():
                list =(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get())
                ingredients = [checkbox_1.get(),checkbox_2.get(),checkbox_3.get(),checkbox_4.get(),checkbox_5.get(),checkbox_6.get(),
                           checkbox_7.get(),checkbox_8.get(),checkbox_9.get(),checkbox_10.get(),checkbox_11.get(),checkbox_12.get(),]
                print(list)
                print(ingredients)
                if '' not in list:
                    print("in")
                    conn = None
                    try:
                        conn = oracledb.connect(
                        user="jeffin",
                        password="jancy123",
                        dsn="localhost/xe")
                        
                        try:
                            list =[(entry_1.get(),entry_2.get(),int(entry_3.get()),entry_4.get())]
                            
                        except Exception as err:
                            entry_3.configure(fg_color=("#E34234","#E34234"))
                            return
                            
                        
                        cursor = conn.cursor()
                        
                        exists = cursor.var(oracledb.NUMBER)
                        
                        recid = entry_1.get()
                        
                        cursor.callproc("check_recipe_id", (recid, exists))
                        result = exists.getvalue()

                        if result == 1:
                            entry_1.configure(fg_color=("#E34234","#E34234"))
                            print("Recipe ID exists in the table.")
                            label = customtkinter.CTkLabel(master=frame_new,text="Recipe ID already exists!", font= ("Helvetica",13))
                            label.place(relx=0.23, rely=0.12, anchor=tkinter.CENTER)
                            return
                        
                        
                        
                        cursor.executemany("INSERT INTO recipe (recipe_id, recipe_name, calorie_count, instructions) VALUES (:1, :2, :3, :4)", list)
                            
                        for i in range (len(ingredients)):
                            if ingredients[i] == 1:
                                cursor.executemany("INSERT INTO recipe_ingredient VALUES (:1,:2)",[(entry_1.get(),i+1)])
                                
                        
                        conn.commit()        

                    except Exception as err:
                        print('Error while connecting to the db')
                        print(err)
                        exit()
                        
                    finally:
                        cursor.close()
                        conn.close()
                    
                
                    root_new.destroy()
                    self.main_page()
        
        
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("RECIPES")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            
            entry_1 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Recipe ID Format:R1,R2,etc")
            entry_1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

            entry_2 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Recipe Name")
            entry_2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
            
            entry_3 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Calorie Count Format:Integer")
            entry_3.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            
            entry_4 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Instructions")
            entry_4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            
            label = customtkinter.CTkLabel(master=frame_new, text = "Ingredients:", font= ("Helvetica",14))
            label.place(relx=0.15, rely=0.6, anchor=tkinter.CENTER)
            
            i = 0.15 
            j=0.17
            checkbox_1 = customtkinter.CTkCheckBox(master=frame_new, text="Milk")
            checkbox_1.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            i=i+0.14
            checkbox_2 = customtkinter.CTkCheckBox(master=frame_new, text="Nuts")
            checkbox_2.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            i=i+j
            checkbox_3 = customtkinter.CTkCheckBox(master=frame_new, text="Eggs")
            checkbox_3.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            i=i+j
            checkbox_4 = customtkinter.CTkCheckBox(master=frame_new, text="Fish")
            checkbox_4.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            i=i+0.15
            checkbox_5 = customtkinter.CTkCheckBox(master=frame_new, text="Pasta")
            checkbox_5.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            i=i+j
            checkbox_6 = customtkinter.CTkCheckBox(master=frame_new, text="Meat")
            checkbox_6.place(relx=i, rely=0.7, anchor=tkinter.CENTER)
            
            i = 0.15
            checkbox_7 = customtkinter.CTkCheckBox(master=frame_new, text="Soy")
            checkbox_7.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            i=i+0.14
            checkbox_8 = customtkinter.CTkCheckBox(master=frame_new, text="Tomato")
            checkbox_8.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            i=i+j
            checkbox_9 = customtkinter.CTkCheckBox(master=frame_new, text="Onion")
            checkbox_9.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            i=i+j
            checkbox_10 = customtkinter.CTkCheckBox(master=frame_new, text="Rice")
            checkbox_10.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            i=i+0.15
            checkbox_11 = customtkinter.CTkCheckBox(master=frame_new, text="Cheese")
            checkbox_11.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            i=i+j
            checkbox_12 = customtkinter.CTkCheckBox(master=frame_new, text="Bread")
            checkbox_12.place(relx=i, rely=0.8, anchor=tkinter.CENTER)
            
            button_add = customtkinter.CTkButton(master=frame_new, text="ADD RECIPE", corner_radius=6, command=add, width=400)
            button_add.place(relx=0.5,rely=0.9,anchor = tkinter.CENTER)
            
            
            
            back_button = customtkinter.CTkButton(master=frame_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.6,rely=0.05)
            
                       
                
            
            root_new.mainloop()
            
            
    def recipedelete(self):
        
            def back():
                root_new.destroy()
                self.recipesview()
                
            def add():
                if entry_1.get() != '':
                    conn = None
                    try:
                        conn = oracledb.connect(
                        user="jeffin",
                        password="jancy123",
                        dsn="localhost/xe")
                                                    
                            
                        
                        cursor = conn.cursor()
                        
                        exists = cursor.var(oracledb.NUMBER)
                        
                        recid = entry_1.get()
                        
                        cursor.callproc("check_recipe_id", (recid, exists))
                        result = exists.getvalue()

                        if result == 0:
                            entry_1.configure(fg_color=("#E34234","#E34234"))
                            print("Recipe ID exists in the table.")
                            label = customtkinter.CTkLabel(master=frame_new,text="Recipe ID does not exist!", font= ("Helvetica",13))
                            label.place(relx=0.23, rely=0.12, anchor=tkinter.CENTER)
                            return
                        
                        
                        cursor.callproc("delete_recipe_and_ingredients", (recid,))

                                
                        
                        conn.commit()        

                    except Exception as err:
                        print('Error while connecting to the db')
                        print(err)
                        exit()
                        
                    finally:
                        cursor.close()
                        conn.close()
                    
                
                    root_new.destroy()
                    self.recipesview()  
            
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("RECIPES")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            
            entry_1 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Recipe ID Format:R1,R2,etc")
            entry_1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
            
            back_button = customtkinter.CTkButton(master=frame_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.6,rely=0.05)
            
            button_add = customtkinter.CTkButton(master=frame_new, text="DELETE RECIPE", corner_radius=6, command=add, width=400)
            button_add.place(relx=0.5,rely=0.9,anchor = tkinter.CENTER)
            
            root_new.mainloop()
        
    
    def recipesview(self):
        
            def back():
                root_new.destroy()
                self.main_page()
            def delete():
                root_new.destroy()
                self.recipedelete()
            def view():
                root_new.destroy()
                self.searchrecipe()
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("RECIPES")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkScrollableFrame(master=root_new,width=450, height=300,label_text="RECIPE LIST", corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            conn = None
            str = []
            try:
                    conn = oracledb.connect(
                    user="jeffin",
                    password="jancy123",
                    dsn="localhost/xe")
                        
                    cursor = conn.cursor()
                        
                    cursor.execute("select * from recipe")
                            
                    rows = cursor.fetchall()

                    for row in rows:
                        str.append(row)
                        
                        

            except Exception as err:
                    print('Error while connecting to the db')
                    print(err)
                    exit()
                
            finally:

                    cursor.close()
                    conn.close()
            
            if str:
                for x in range(len(str)):
                    text = str[x][0]+":"+str[x][1]
                    customtkinter.CTkButton(master=frame_new, text=text, width=400).pack(pady=10)
            else:
                customtkinter.CTkButton(master=frame_new, text="No Recipes Available", width=400).pack(pady=10)
                    
            back_button = customtkinter.CTkButton(root_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.03,rely=0.03)
            
            button_view = customtkinter.CTkButton(root_new, text="VIEW RECIPE", corner_radius=6, command=view, width=200)
            button_view.place(relx=0.25,rely=0.95,anchor = tkinter.CENTER)
            button_delete = customtkinter.CTkButton(root_new, text="DELETE RECIPE", corner_radius=6, command=delete, width=200)
            button_delete.place(relx=0.75,rely=0.95,anchor = tkinter.CENTER)
                
            
            root_new.mainloop()
    
    def inventoryupdate(self):
            def back():
                root_new.destroy()
                self.inventory()
            
            def add():
                    ingredients = [checkbox_1.get(),checkbox_2.get(),checkbox_3.get(),checkbox_4.get(),checkbox_5.get(),checkbox_6.get(),
                            checkbox_7.get(),checkbox_8.get(),checkbox_9.get(),checkbox_10.get(),checkbox_11.get(),checkbox_12.get(),]
                    print(ingredients)
                    conn = None
                    try:
                        conn = oracledb.connect(
                        user="jeffin",
                        password="jancy123",
                        dsn="localhost/xe")
                        
                        
                        cursor = conn.cursor()
                        
                        print(self.user)
                        
                        cursor.execute("DELETE from user_ingredient where user_id = :user_id",user_id=self.user)
                        
                            
                        for i in range (len(ingredients)):
                            if ingredients[i] == 1:
                                cursor.executemany("INSERT into user_ingredient(user_id,ingredient_id) values(:1, :2)",[(self.user,i+1)])
                        
                        conn.commit()        

                    except Exception as err:
                        print('Error while connecting to the db')
                        print(err)
                        exit()
                        
                    finally:
                        cursor.close()
                        conn.close()
                    
                
                    root_new.destroy()
                    self.inventory()
        
        
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("INVENTORY UPDATE")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            
            
            label = customtkinter.CTkLabel(master=frame_new, text = "Ingredients:", font= ("Helvetica",14))
            label.place(relx=0.15, rely=0.3, anchor=tkinter.CENTER)
            
            i = 0.15 
            j=0.17
            checkbox_1 = customtkinter.CTkCheckBox(master=frame_new, text="Milk")
            checkbox_1.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            i=i+0.14
            checkbox_2 = customtkinter.CTkCheckBox(master=frame_new, text="Nuts")
            checkbox_2.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            i=i+j
            checkbox_3 = customtkinter.CTkCheckBox(master=frame_new, text="Eggs")
            checkbox_3.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            i=i+j
            checkbox_4 = customtkinter.CTkCheckBox(master=frame_new, text="Fish")
            checkbox_4.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            i=i+0.15
            checkbox_5 = customtkinter.CTkCheckBox(master=frame_new, text="Pasta")
            checkbox_5.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            i=i+j
            checkbox_6 = customtkinter.CTkCheckBox(master=frame_new, text="Meat")
            checkbox_6.place(relx=i, rely=0.4, anchor=tkinter.CENTER)
            
            i = 0.15
            checkbox_7 = customtkinter.CTkCheckBox(master=frame_new, text="Soy")
            checkbox_7.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            i=i+0.14
            checkbox_8 = customtkinter.CTkCheckBox(master=frame_new, text="Tomato")
            checkbox_8.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            i=i+j
            checkbox_9 = customtkinter.CTkCheckBox(master=frame_new, text="Onion")
            checkbox_9.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            i=i+j
            checkbox_10 = customtkinter.CTkCheckBox(master=frame_new, text="Rice")
            checkbox_10.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            i=i+0.15
            checkbox_11 = customtkinter.CTkCheckBox(master=frame_new, text="Cheese")
            checkbox_11.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            i=i+j
            checkbox_12 = customtkinter.CTkCheckBox(master=frame_new, text="Bread")
            checkbox_12.place(relx=i, rely=0.5, anchor=tkinter.CENTER)
            
            button_add = customtkinter.CTkButton(master=frame_new, text="UPDATE INVENTORY", corner_radius=6, command=add, width=400)
            button_add.place(relx=0.5,rely=0.7,anchor = tkinter.CENTER)
            
            
            
            back_button = customtkinter.CTkButton(master=frame_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.05,rely=0.05)
            
            
                
            
            root_new.mainloop()
        
    
    def inventory(self):
                
            def back():
                root_new.destroy()
                self.main_page()

            def update():
                root_new.destroy()
                self.inventoryupdate()
            
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("INVENTORY")
            
            frame_new = customtkinter.CTkScrollableFrame(master=root_new,width=450, height=300,label_text="AVAILABLE INGREDIENTS", corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            conn = None
            str = []
            try:
                    conn = oracledb.connect(
                    user="jeffin",
                    password="jancy123",
                    dsn="localhost/xe")
                        
                    cursor = conn.cursor()
                        
                    cursor.execute(f"select ingredient_id,ingredient_name from user_ingredient natural join ingredient where user_id = '{self.user}'")
                            
                    rows = cursor.fetchall()

                    for row in rows:
                        str.append(row)
                        
                        

            except Exception as err:
                    print('Error while connecting to the db')
                    print(err)
                    exit()
                
            finally:

                    cursor.close()
                    conn.close()
            
            print(str)
            
            if str:
                for x in range(len(str)):
                    text = str[x][1]
                    customtkinter.CTkButton(master=frame_new, text=text, width=400).pack(pady=10)
            else:
                customtkinter.CTkButton(master=frame_new, text="No Ingredients Available", width=400).pack(pady=10)
                
            
            
            back_button = customtkinter.CTkButton(root_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.03,rely=0.03)
            
            update = customtkinter.CTkButton(root_new, text="UPDATE INVENTORY", corner_radius=6, command=update, width=400)
            update.place(relx=0.5,rely=0.93,anchor = tkinter.CENTER)
            
            root_new.mainloop()
    
    def meals(self):
        
            def back():
                root_new.destroy()
                self.main_page()
            def shopping():
                root_new.destroy()
                self.shoppinglist()
            def view():
                root_new.destroy()
                self.searchrecipe()
            #Define the new window
            root_new = customtkinter.CTk()
            root_new.geometry(f"{500}x{500}")
            root_new.title("PLAN MEAL")
            
            #Add your widgets for new_window...
            frame_new = customtkinter.CTkScrollableFrame(master=root_new,width=450, height=300,label_text="SUGGESTED RECIPES", corner_radius=10)
            frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            conn = None
            str = []
            missing = []
            try:
                    conn = oracledb.connect(
                    user="jeffin",
                    password="jancy123",
                    dsn="localhost/xe")
                        
                    cursor = conn.cursor()
                        
                    cursor.execute("""SELECT r.recipe_id, r.recipe_name
                                    FROM recipe r
                                    WHERE NOT EXISTS (
                                        SELECT ri.recipe_id
                                        FROM recipe_ingredient ri
                                        JOIN ingredient i ON ri.ingredient_id = i.ingredient_id
                                        JOIN allergy a ON i.ingredient_name = a.name
                                        JOIN user_allergy ua ON a.al_id = ua.al_id
                                        WHERE ri.recipe_id = r.recipe_id
                                        AND ua.user_id = :1
                                    )""", (self.user,))
                            
                    rows = cursor.fetchall()

                    for row in rows:
                        str.append(row)
                        
                        

            except Exception as err:
                    print('Error while connecting to the db1')
                    print(err)
                    exit()
                
            finally:

                    cursor.close()
                    conn.close()
            
            if str:
                for x in range(len(str)):
                    text = str[x][0]+":"+str[x][1]
                    customtkinter.CTkButton(master=frame_new, text=text, width=400).pack(pady=10)
                for x in range(len(str)):
                    text = str[x][0]
                    try:
                            conn = oracledb.connect(
                            user="jeffin",
                            password="jancy123",
                            dsn="localhost/xe")
                                
                            cursor = conn.cursor()
                                
                            cursor.executemany("""SELECT i.ingredient_name
                                                FROM ingredient i
                                                JOIN recipe_ingredient ri ON i.ingredient_id = ri.ingredient_id
                                                LEFT JOIN user_ingredient ui ON i.ingredient_id = ui.ingredient_id AND ui.user_id = :1
                                                WHERE ri.recipe_id = :2
                                                AND ui.user_id IS NULL""", [(self.user,text)])
                                    
                            rows = cursor.fetchall()

                            for row in rows:
                                missing.append(row)
                                
                            self.missing = list(set(missing))           

                    except Exception as err:
                            print('Error while connecting to the db2')
                            print(err)
                            exit()
                        
                    finally:

                            cursor.close()
                            conn.close()
                    
                    
                    
                        
            else:
                customtkinter.CTkButton(master=frame_new, text="Add More Recipes", width=400).pack(pady=10)
                self.missing = []
                    
            back_button = customtkinter.CTkButton(root_new, text="GO BACK", corner_radius=6, command=back, width=150)
            back_button.place(relx=0.03,rely=0.03)
            
            button_view = customtkinter.CTkButton(root_new, text="VIEW RECIPE", corner_radius=6, command=view, width=200)
            button_view.place(relx=0.25,rely=0.92,anchor = tkinter.CENTER)
            button_shopping = customtkinter.CTkButton(root_new, text="SHOPPING LIST", corner_radius=6, command=shopping, width=200)
            button_shopping.place(relx=0.75,rely=0.92,anchor = tkinter.CENTER)
                
            
            root_new.mainloop()
    
    
    
    
    def main_page(self):
        
        def recipesadd():
            root_new.destroy()
            self.recipesadd()
        def recipesview():
            root_new.destroy()
            self.recipesview()    
        def inventory():
            root_new.destroy()
            self.inventory()
        def meals():
            root_new.destroy()
            self.meals()
        def logout():
            root_new.destroy()
            self.login_window()
        
        print(self.user)  
        #Define the new window
        root_new = customtkinter.CTk()
        root_new.geometry(f"{500}x{500}")
        root_new.title("MEAL TRACKER")
        
        #Add your widgets for new_window...
        frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
        frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        
        button_addrecipes = customtkinter.CTkButton(master=frame_new, text="ADD RECIPE", corner_radius=6, command=recipesadd, width=400)
        button_addrecipes.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        button_viewrecipes = customtkinter.CTkButton(master=frame_new, text="VIEW RECIPES", corner_radius=6, command=recipesview, width=400)
        button_viewrecipes.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        button_inventory = customtkinter.CTkButton(master=frame_new, text="INVENTORY", corner_radius=6, command=inventory, width=400)
        button_inventory.place(relx=0.5,rely=0.5,anchor = tkinter.CENTER)
        button_meal = customtkinter.CTkButton(master=frame_new, text="SUGGEST MEALS", corner_radius=6, command=meals, width=400)
        button_meal.place(relx=0.5,rely=0.6,anchor = tkinter.CENTER)
        
        back_button = customtkinter.CTkButton(root_new, text="LOG OUT", corner_radius=6, command=logout, width=150)
        back_button.place(relx=0.6,rely=0.1)
        
        
        root_new.mainloop()    
    
    def sign_up(self):
        def back():
            root_new.destroy()
            self.login_window()
        def sign_up():
                list =(entry_1.get(),entry_4.get(),entry_2.get(),entry_3.get())
                allergy = [checkbox_1.get(),checkbox_2.get(),checkbox_3.get(),checkbox_4.get(),checkbox_5.get()]
                userid = entry_1.get()
                if '' not in list:
                    conn = None
                    try:
                        conn = oracledb.connect(
                        user="jeffin",
                        password="jancy123",
                        dsn="localhost/xe")
                        
                        
                        
                        list =[(entry_1.get(),entry_4.get(),entry_2.get(),entry_3.get())]
                        
                        cursor = conn.cursor()
                        
                        exists = cursor.var(oracledb.NUMBER)
                        
                        cursor.callproc("check_user_id", (userid, exists))
                        result = exists.getvalue()

                        if result == 1:
                            print("User ID exists in the table.")
                            entry_1.configure(fg_color=("#E34234","#E34234"))
                            label = customtkinter.CTkLabel(master=frame_new,text="User already exists", font= ("Helvetica",13))
                            label.place(relx=0.20, rely=0.12, anchor=tkinter.CENTER)
                            return

                                
                        
                        cursor.executemany("INSERT INTO user_account (user_id, password, fname, lname) VALUES (:1, :2, :3, :4)", list)
                            
                        for i in range (len(allergy)):
                            if allergy[i] == 1:
                                cursor.executemany("INSERT INTO user_allergy VALUES (:1,:2)",[(entry_1.get(),i+1)])
                                
                        
                        conn.commit()        

                    except Exception as err:
                        print('Error while connecting to the db')
                        print(err)
                        exit()
                        
                    finally:
                        cursor.close()
                        conn.close()
                    
                
                    root_new.destroy()
                    self.login_window()
        
        
        #Define the new window
        root_new = customtkinter.CTk()
        root_new.geometry(f"{500}x{500}")
        root_new.title("SIGN UP PAGE")
        
        #Add your widgets for new_window...
        frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
        frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        

        entry_1 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="User ID")
        entry_1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        entry_2 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="First Name")
        entry_2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        
        entry_3 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Last Name")
        entry_3.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        
        entry_4 = customtkinter.CTkEntry(master=frame_new, corner_radius=20, width=400, placeholder_text="Password")
        entry_4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        label = customtkinter.CTkLabel(master=frame_new, text = "Allergies:", font= ("Helvetica",14))
        label.place(relx=0.15, rely=0.6, anchor=tkinter.CENTER)
        
        checkbox_1 = customtkinter.CTkCheckBox(master=frame_new, text="Milk")
        checkbox_1.place(relx=0.25, rely=0.7, anchor=tkinter.CENTER)
        checkbox_2 = customtkinter.CTkCheckBox(master=frame_new, text="Eggs")
        checkbox_2.place(relx=0.4, rely=0.7, anchor=tkinter.CENTER)
        checkbox_3 = customtkinter.CTkCheckBox(master=frame_new, text="Nuts")
        checkbox_3.place(relx=0.55, rely=0.7, anchor=tkinter.CENTER)
        checkbox_4 = customtkinter.CTkCheckBox(master=frame_new, text="Fish")
        checkbox_4.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)
        checkbox_5 = customtkinter.CTkCheckBox(master=frame_new, text="Soy")
        checkbox_5.place(relx=0.85, rely=0.7, anchor=tkinter.CENTER)
        

        button_signup = customtkinter.CTkButton(master=frame_new, text="CREATE USER", corner_radius=6, command=sign_up, width=400)
        button_signup.place(relx=0.5,rely=0.8,anchor = tkinter.CENTER)
        
        back_button = customtkinter.CTkButton(master=frame_new, text="GO BACK", corner_radius=6, command=back, width=150)
        back_button.place(relx=0.6,rely=0.05)
        
        root_new.mainloop()   
        

    
    def login_window(self):
        def login_event():
            conn = None
            if entry_1.get()!='' and entry_2.get()!='':
                try:
                    label = customtkinter.CTkLabel(master=frame, text = "", font= ("Helvetica",13))
                    label.place(relx=0.30, rely=0.32, anchor=tkinter.CENTER)
                    conn = oracledb.connect(
                    user="jeffin",
                    password="jancy123",
                    dsn="localhost/xe")
                    
                    cursor = conn.cursor()
                    
                    
                    
                    exists = cursor.var(oracledb.NUMBER)
                    userid = entry_1.get()
                    cursor.callproc("check_user_id", (userid, exists))
                    result = exists.getvalue()

                    if result == 0:
                        print("User ID does not exist in the table.")
                        entry_1.configure(fg_color=("#E34234","#E34234"))
                        label.configure(text="Wrong Password/User Doesn't Exist!")
                        return
                    
                    cursor.execute("SELECT password FROM user_account WHERE user_id = :user_id", user_id=entry_1.get())

                    row = cursor.fetchone()
                    
                    
                    
                    if row and entry_2.get() == row[0] :
                        self.user = entry_1.get()                                               
                        root_login.destroy() #Destroy the login window after the verification
                        self.main_page() #Make the new_window
                    else: #If password doesn't match
                        entry_1.configure(fg_color=("#E34234","#E34234"))
                        entry_2.configure(fg_color=("#E34234","#E34234"))
                        label.configure(text="Wrong Password/User Doesn't Exist!")
                        return

                    
                            

                except Exception as err:
                    print('Error while connecting to the db')
                    print(err)
                    exit()
                    
                finally:

                    cursor.close()
                    conn.close()
                

        
        
        def sign_up():
            root_login.destroy()
            self.sign_up()
            
        #Define the login page window          
        root_login = customtkinter.CTk() 
        root_login.geometry(f"{500}x{500}")
        root_login.title("LOGIN PAGE")

        #Add some widgets for login page
        frame = customtkinter.CTkFrame(master=root_login,width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
        entry_1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
        entry_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button_login = customtkinter.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=login_event, width=400)
        button_signup = customtkinter.CTkButton(master=frame, text="NEW USER", corner_radius=6, command=sign_up, width=400)
        button_login.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        button_signup.place(relx=0.5,rely=0.7,anchor = tkinter.CENTER)

        font = customtkinter.CTkFont(family="Helvetica",size = 35, weight = "bold",slant= 'roman' )
        Title = customtkinter.CTkLabel(master=frame, text = "MEAL PLANNER", font= font)
        Title.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        
        
        
        root_login.mainloop()
        



app = App()
app.mainloop()