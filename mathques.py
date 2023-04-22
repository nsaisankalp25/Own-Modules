import tkinter
from tkinter import Label, Button, Entry, Grid
import random
from random import randint

rt = tkinter.Tk()
rt.title("Math AI Questions")
rt.geometry("500x500")

def des():
    def desdef():
        rt.destroy()
    exit_b = Button(rt, text ='Exit', font = ('open sans',12), command = desdef)
    exit_b.grid(row = 1, column = 0)
def welcomedef(event):
    def select():
        def easydef():
            easy_b.destroy()
            inter_b.destroy()
            select_l.destroy()
            hard_b.destroy()
            pro_b.destroy()

            def check(event):
                try:
                    global ans
                    ans = ans_e.get()
                    ans = float(ans)
                except ValueError:
                    Label(rt, text = "Must enter a valid number")
                r_ans = rnum1 + rnum2 - rnum3
                if ans == r_ans:
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    con = Label(rt, text = f'Congrats {name}!!!! \n your right, anwer: {ans}',
                    font = ('montserrat', 14), fg = 'green')
                    con.grid(row = 0, column = 0)
                    des()
                    

                else: 
                    wrong = Label(rt, text = f"Oops, Better luck next time {name}", 
                    font = ('open sans', 14), fg = 'blue')
                    wrong.grid(row = 0, column = 0)
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    des()
                

            rnum1 = random.randint(1,10)
            rnum2 = random.randint(1,10)
            rnum3 = random.randint(1,10) 

            ques = Label(rt, text = f'{rnum1}+{rnum2}-{rnum3}', fg = 'red', font = ('consolas', 15))
            ques.grid(row = 0, column = 0)
            ans_l = Label(rt, text = 'Enter answer[in numbers]: ', fg = 'purple', font = ('quicksand',12))
            ans_l.grid(row = 1, column = 0)
            ans_e = Entry(rt, font = ('open sans', 16))
            ans_e.grid(row = 1, column = 1)
            ans_e.bind("<Return>", check)


        def interdef():
            easy_b.destroy()
            inter_b.destroy()
            select_l.destroy()
            hard_b.destroy()
            pro_b.destroy()

            def check(event):
                try:
                    global answer
                    answer = ans_e.get()
                    answer = float(answer)
                except ValueError:
                    Label(rt, text = "Must enter a valid number")
                r_ans = (rnum1*rnum2)+(rnum3*rnum4)
                if answer == r_ans:
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    con = Label(rt, text = f'Congrats {name}!!!! \n your right, anwer: {answer}',
                    font = ('montserrat', 14), fg = 'green')
                    con.grid(row = 0, column = 0)
                    des()

                else: 
                    wrong = Label(rt, text = f"Oops, Better luck next time {name}", 
                    font = ('open sans', 14), fg = 'blue')
                    wrong.grid(row = 0, column = 0)
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    des()
                

            rnum1 = random.randint(1,50)
            rnum2 = random.randint(1,50)
            rnum3 = random.randint(1,50) 
            rnum4 = random.randint(1,50)
            print((rnum1*rnum2)+(rnum3*rnum4))

            ques = Label(rt, text = f'{rnum1}×{rnum2}+{rnum3}×{rnum4}',
            fg = 'red', font = ('consolas', 15))
            ques.grid(row = 0, column = 0)
            ans_l = Label(rt, text = 'Enter answer[in numbers]: ', fg = 'purple', font = ('quicksand',12))
            ans_l.grid(row = 1, column = 0)
            ans_e = Entry(rt, font = ('open sans', 16))
            ans_e.grid(row = 1, column = 1)
            ans_e.bind("<Return>", check)
             
            

        def harddef():
            easy_b.destroy()
            inter_b.destroy()
            select_l.destroy()
            hard_b.destroy()
            pro_b.destroy()

            def check(event):
                try:
                    global answer
                    answer = ans_e.get()
                    answer = float(answer)
                except ValueError:
                    Label(rt, text = "Must enter a valid number")
                r_ans = (rnum1*(rnum2**2)) + (((rnum3*rnum4) - rnum1))
                if answer == r_ans:
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    con = Label(rt, text = f'Congrats {name}!!!! \n your right, anwer: {answer}',
                    font = ('montserrat', 14), fg = 'green')
                    con.grid(row = 0, column = 0)
                    des()

                else: 
                    wrong = Label(rt, text = f"Oops, Better luck next time {name}",
                    font = ('open sans', 14), fg = 'blue')
                    wrong.grid(row = 0, column = 0)
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    des()
                

            rnum1 = random.randint(1,50)
            rnum2 = random.randint(1,50)
            rnum3 = random.randint(1,50) 
            rnum4 = random.randint(1,50)
            print((rnum1*(rnum2**2)) + (((rnum3*rnum4) - rnum1)))

            ques = Label(rt, text = f'{rnum1}×{rnum2}^2 + {rnum3}×{rnum4}-{rnum1}',
            fg = 'red', font = ('consolas', 15))
            
            ques.grid(row = 0, column = 0)
            ans_l = Label(rt, text = 'Enter answer[in numbers]: ', fg = 'purple', font = ('quicksand',12))
            ans_l.grid(row = 1, column = 0)
            ans_e = Entry(rt, font = ('open sans', 16))
            ans_e.grid(row = 1, column = 1)
            ans_e.bind("<Return>", check)
             
            

        def prodef():
            easy_b.destroy()
            inter_b.destroy()
            select_l.destroy()
            hard_b.destroy()
            pro_b.destroy()

            def check(event):
                try:
                    global answer
                    answer = ans_e.get()
                    answer = float(answer)
                except ValueError:
                    Label(rt, text = "Must enter a valid number")
                r_ans = ((rnum1**3) + (r1*(rnum2**2)*rnum2) + ((r2*rnum3)*(rnum4**2)+(rnum1**3)))
                if answer == r_ans:
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    con = Label(rt, text = f'Congrats {name}!!!! \n your right, anwer: {answer}',
                    font = ('montserrat', 14), fg = 'green')
                    con.grid(row = 0, column = 0)
                    des()

                else: 
                    wrong = Label(rt, text = f"Oops, Better luck next time {name}",
                    font = ('open sans', 14), fg = 'blue')
                    wrong.grid(row = 0, column = 0)
                    ques.destroy()
                    ans_e.destroy()
                    ans_l.destroy()
                    
                    des()
                

            rnum1 = random.randint(1,50)
            rnum2 = random.randint(1,50)
            rnum3 = random.randint(1,50) 
            rnum4 = random.randint(1,50)
            r1 = random.randint(2,5)
            r2 = random.randint(2,5)
            print(((rnum1**3) + (r1*(rnum2**2)*rnum2) + ((r2*rnum3)*(rnum4**2)+(rnum1**3))))

            ques = Label(rt,  fg = 'red', font = ('consolas', 15),
            text = f"{rnum1}^3 + {r1}×{rnum2}^2 ×{rnum2} + {r2}×{rnum3}×{rnum4}^2 +{rnum1}^3")
            
            ques.grid(row = 0, column = 0)
            ans_l = Label(rt, text = 'Enter answer[in numbers]: ', fg = 'purple', font = ('quicksand',12))
            ans_l.grid(row = 1, column = 0)
            ans_e = Entry(rt, font = ('open sans', 16))
            ans_e.grid(row = 1, column = 1)
            ans_e.bind("<Return>", check)
             
            


        name_w_l.destroy()
        next_b2.destroy()
        select_l = Label(rt, text = 'Select Level', font = ('magenta', 14))
        select_l.grid(row = 0, column = 0)
        easy_b = Button(rt, text = 'Easy', command = easydef, font = ('calibri', 13), padx = 30)
        easy_b.grid(row = 1, column = 1)
        inter_b = Button(rt, text = 'Intermediate', command = interdef, font = ('calibri', 13), padx = 1)
        inter_b.grid(row = 2, column = 1)
        hard_b = Button(rt, text = 'Hard', command = harddef, font = ('calibri', 13), padx = 29)
        hard_b.grid(row = 3, column = 1)
        pro_b = Button(rt, text = 'Pro', command = prodef, font = ('calibri', 13), padx = 34)
        pro_b.grid(row = 4, column = 1)


    print('in welcome def')
    name = name_e.get()
    name_e.destroy()
    name_l.destroy()
    name_w_l = Label(rt, text = f'Welcome to Math problems\n {name}', fg = 'red', font = ('montserrat', 15))
    name_w_l.grid(row = 0, column = 0)
    next_b2 = Button(rt, text = ':-)  Next -->', command = select, fg = 'blue', font = ('calibri', 14))
    next_b2.grid(row = 0, column = 1)
    

name_l = Label(rt, text = 'Enter your name:', font = ('helvetica', 15))
name_l.grid(row = 0, column = 0)
name_e = Entry(rt, font = ('montserrat', 14))
name_e.grid(row = 0, column = 1)
name_e.bind("<Return>", welcomedef)


rt.mainloop()