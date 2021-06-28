from tkinter import *
from tkinter import messagebox
import time

class CandyDispenser:
      def __init__(self, root):
          self.window = root
          self.window.config(bg="#f7f7f7")

          #Some list to store candy
          self.last_label_value_keep = []
          self.candy_value_counter = []

          #Canvas widget and coordinate of it in stack container make
          self.candy_make = 0
          self.final_set_candy = 0
          self.extra_decrease = 0

          #Label,Button,Entry initialization
          self.heading_name = None
          self.sub_heading = None
          self.stack_indicator = None
          self.push_btn = None
          self.pop_btn = None
          self.element_take_entry = None
          self.entry_number = None
          self.element_take_label = None
          self.add_btn = None
          self.top_index = None
          self.index_neg = None
          self.index_0 = None
          self.index_1 = None
          self.index_2 = None
          self.index_3 = None
          self.index_4 = None
          self.index_5 = None

          self.number = IntVar()
          self.value_entry = IntVar()
          self.value_entry.set(" ")

          #Default coordinate set
          self.canvas_width = 700
          self.canvas_height = 700
          self.number_set_x = 40
          self.number_set_y = 105
          self.candy_left = 26
          self.candy_right = 72
          self.candy_up = 100
          self.candy_down = 130
          self.down_achieve = 400
          self.top_y = 400

          #Make canvas
          self.stack_canvas = Canvas(self.window, width=self.canvas_width, height=self.canvas_height,bg="white", relief=RAISED, bd=10)
          self.stack_canvas.pack(fill=BOTH)

          #Function call
          self.make_stack_container()
          self.make_buttons()
          self.heading_and_sub_heading()
          self.set_index()

      def heading_and_sub_heading(self): #Main heading, sub heading and indicator label set
          self.heading_name = Label(self.stack_canvas, text="Candy dispenser", bg="white", fg="blue", font=("times new roman",30,"bold","italic"))
          self.heading_name.place(x=140,y=30)

          self.sub_heading = Label(self.stack_canvas, text="candy index", bg="white", fg="blue",  font=("Helvetica",20,"bold","italic"))
          self.sub_heading.place(x=20,y=300)

          self.stack_indicator = Label(self.stack_canvas, text="Candy Container", bg="white", fg="blue",  font=("Helvetica",20,"bold","italic"))
          self.stack_indicator.place(x=180,y=450)

      def make_buttons(self): #Make Buttons to access and make top with arrow
          self.push_btn = Button(self.window,text="Push()",fg="white",bg="blue",font=("Arial",15,"bold"),
                                 relief=RAISED,bd=7,command=self.push_element)
          self.push_btn.place(x=30,y=535)

          self.pop_btn = Button(self.window, text="Pop()", fg="white", bg="blue", font=("Arial", 15, "bold"),
                                relief=RAISED,bd=7,command=self.pop_candy)
          self.pop_btn.place(x=500, y=535)

          self.top_index = Label(self.window, text="<-- Top Candy", fg="blue", bg="white", font=("Arial", 20, "bold"))
          self.top_index.place(x=310, y=self.top_y)

      def make_stack_container(self): #Making of stack container
          self.stack_canvas.create_line(250,198,250,435,fill="black",width=3)
          #self.stack_canvas.create_line(250,400,300,400,fill="black",width=3)
          self.stack_canvas.create_line(250,404,300,404,fill="black",width=6)
          self.stack_canvas.create_line(250,404,300,414,fill="black",width=3)
          self.stack_canvas.create_line(250,414,300,414,fill="black",width=3)
          self.stack_canvas.create_line(250,414,300,424,fill="black",width=3)
          self.stack_canvas.create_line(250,424,300,424,fill="black",width=3)
          self.stack_canvas.create_line(250,424,300,434,fill="black",width=3)
          self.stack_canvas.create_line(250,434,300,434,fill="black",width=6)
          self.stack_canvas.create_line(300, 198, 300, 435, fill="black", width=3)

      def set_index(self): #Index of the stack set
          #self.index_neg = Label(self.stack_canvas,text="-1",fg="blue",bg="white",font=("Arial",15,"bold"))
          #self.index_neg.place(x= 215, y=403)

          self.index_0 = Label(self.stack_canvas, text="0", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_0.place(x=220, y=370)

          self.index_1 = Label(self.stack_canvas, text="1", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_1.place(x=220, y=332)

          self.index_2 = Label(self.stack_canvas, text="2", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_2.place(x=220, y=299)

          self.index_3 = Label(self.stack_canvas, text="3", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_3.place(x=220, y=266)

          self.index_4 = Label(self.stack_canvas, text="4", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_4.place(x=220, y=232)

          self.index_5 = Label(self.stack_canvas, text="5", fg="blue", bg="white", font=("Arial", 15, "bold"))
          self.index_5.place(x=220, y=199)

      def push_element(self): #Push button action
          if len(self.last_label_value_keep) == 6:
             messagebox.showerror("Overflow","The candy dispenser is full !")
          else:
              # Access Button deactivation
              self.pop_btn.config(state=DISABLED)
              self.push_btn.config(state=DISABLED)

              #Element value give diagram set
              self.element_take_label = Label(self.window,text="Enter the candy label: ",
                                         bg="white",fg="blue",font=("Arial",13,"bold"))
              self.element_take_label.place(x=170,y=536)

              self.element_take_entry = Entry(self.window,font=("Arial",13,"bold"),bg="white",
                                              fg="blue",relief=SUNKEN,bd=5, textvar=self.value_entry)
              self.element_take_entry.place(x=167,y=560)

              self.element_take_entry.focus()

              self.add_btn = Button(self.window, text="push()", font=("Arial", 10, "bold"), bg="blue", fg="white", relief=RAISED, bd=3, padx=3, pady=3, command=lambda: self.make_candy('<Return>'))
              self.add_btn.place(x=400, y=560)
              self.window.bind('<Return>',self.make_candy)

      def make_candy(self,e):#Element containing candy making
          try:
              #Deactivation of input segment
              self.element_take_label.place_forget()
              self.element_take_entry.place_forget()
              self.add_btn.place_forget()

              #Bloack making process
              self.candy_make = self.stack_canvas.create_rectangle(self.candy_left, self.candy_up, self.candy_right, self.candy_down, fill="blue", width=2, outline="blue")
              self.entry_number = Label(self.stack_canvas, textvar=self.number, bg="blue", fg="white", font=("Arial",11,"bold"))
              self.entry_number.place(x=self.number_set_x, y=self.number_set_y)

              # only integer value allow set
              if type(self.value_entry.get()) == int:
                  self.number.set(self.value_entry.get())

              self.push_candy()

          except:
              self.stack_canvas.delete(self.candy_make)
              self.entry_number.destroy()
              self.value_entry.set(" ")
              messagebox.showerror("Wrong happen", "Something wrong here....Correctly do it(Only integer value allowed)")
              self.pop_btn.config(state=NORMAL)
              self.push_btn.config(state=NORMAL)
              pass

      def push_candy(self):#Element entry process in stack container
          try:
              #Element coordinate set in stack container
              self.down_achieve -= 28 + self.extra_decrease
              self.top_y -= 35
              self.top_index.place_forget()
              self.top_index.place(x=310, y=self.top_y)

              #Candy movement controlling horizontal
              while self.number_set_x<265:
                  self.stack_canvas.delete(self.candy_make)
                  self.entry_number.place_forget()
                  self.number_set_x+=2
                  self.candy_left+=2
                  self.candy_right+= 2
                  self.candy_make = self.stack_canvas.create_rectangle(self.candy_left, self.candy_up, self.candy_right, self.candy_down, fill="blue", width=2, outline="blue")
                  self.entry_number.place(x=self.number_set_x, y=self.number_set_y)
                  self.window.update()

              # candy movement controlling vertical
              while self.number_set_y < self.down_achieve:
                  self.stack_canvas.delete(self.candy_make)
                  self.entry_number.place_forget()
                  self.number_set_y += 2
                  self.candy_up+= 2
                  self.candy_down+= 2
                  self.candy_make = self.stack_canvas.create_rectangle(self.candy_left, self.candy_up, self.candy_right, self.candy_down, fill="blue", width=2, outline="blue")
                  self.entry_number.place(x=self.number_set_x, y=self.number_set_y)
                  time.sleep(0.02)
                  self.window.update()

              self.reset_with_position_set()

          except:
              pass

      def reset_with_position_set(self): #Reset the coordinate value
          #Number candy value set another Label to store it
          self.final_set_candy = Label(self.window, text=self.value_entry.get(), bg="blue", fg="white",font=("Arial",11,"bold"))
          self.final_set_candy.place(x=self.number_set_x, y=self.number_set_y)

          #Storing of label,widget for future reference
          self.last_label_value_keep.append(self.final_set_candy)
          self.candy_value_counter.append(self.candy_make)

          #Reset
          self.value_entry.set(" ")
          self.entry_number.place_forget()

          #Access Button activation
          self.push_btn.config(state=NORMAL)
          self.pop_btn.config(state=NORMAL)

          #Set default coordinate
          self.candy_left = 26
          self.candy_up = 100
          self.candy_right = 72
          self.candy_down = 130
          self.number_set_x = 40
          self.number_set_y = 105
          self.extra_decrease =6


      def pop_candy(self): #candy containing candy get out from stack container
          if len(self.last_label_value_keep) ==0: #Stack container empty checking
              messagebox.showerror("Underflow","The Candy dispenser is empty isEmpty()= True")
          else:
              #Delete the pop() reference
              self.last_label_value_keep.pop().destroy()
              self.stack_canvas.delete(self.candy_value_counter.pop())
              self.top_y += 35
              self.top_index.place_forget()
              self.top_index.place(x=310, y=self.top_y)
              self.down_achieve += 28 + self.extra_decrease
              if len(self.last_label_value_keep) == 5:
                  self.push_btn.config(state=NORMAL)
             
                 


if __name__ == '__main__':
    window= Tk()
    window.title("Candy Dispenser")
    window.geometry("700x700")
    window.maxsize(700,700)
    window.minsize(600,600)
    #window.iconbitmap("/home/mbote-joseph/Stack-Visualizer/stack_icon.ico")
    CandyDispenser(window)
    window.mainloop()
