from tkinter import Tk,Label,Button,PhotoImage
from tkinter.scrolledtext import ScrolledText
from numpy.linalg import solve
from numpy import matrix

def f():
    pass

def reset():
    listbox.delete('1.0','end')
    ans.config(text='Simultaneous Linear Equation')

def extract(x):
    l=len(x)
    counter=l-1
    right=''
    coefficient={}
    for i in range(counter,-1,-1):
        if x[i]=='=': break
        right+=x[i]
    right=right[::-1]
    #print (right)
    counter=i-1
    while(counter>-1):
        c=x[counter]
        z=''
        while(x[counter] not in '+-') and counter>0:
            z+=x[counter]
            counter-=1
        z+=x[counter]
        z=z[::-1]
        coefficient[z[-1]]=z[:-1]
                   
        

        counter-=1
    for d in coefficient:
        if coefficient[d]=='-':
            coefficient[d]='-1'
        elif coefficient[d]=='+':
            coefficient[d]='1'
        elif '+' in coefficient[d]:
            coefficient[d]=coefficient[d].replace('+','')
        elif coefficient[d]=='':
            coefficient[d]='1'
    #print(coefficient)
    return (coefficient,right)
        


def SolveButton():
    text=(listbox.get('1.0','end')).split('\n')
    #equations=equations.remove('')
##    print(text)
##    print(type(text))
    equations=[]
    for i in text:
        if i!='':
            equations.append(i)

#    print(equations)
    extracted=list(map(extract,equations))
    if len(extracted)!=len(extracted[0][0]):
#        print('Invalid')
        ans.config(text='Invalid System')

##    print(equations)
##    print(extracted)
    else:
            
        L=[]
        R=[]

        for i in extracted:
            d,r=i
            l=[]
            keys=list(d.keys())
            keys.sort()
            for j in keys:
                l.append(float(d[j]))
            L.append(l)
            R.append([float(r)])

        L=matrix(L)
        R=matrix(R)
    #    print(L)
    #    print(R)
        try:
            x=solve(L,R)

            s=''
            for i in range(len(keys)):
                s=s+' '+str(keys[i])+'='+str(x[i,0])+' ; '
            
            ans.config(text=s)    
        
        except:
            ans.config(text='Invalid System')
    

    

root=Tk()
root.title('v 0.1')
root.geometry('400x300')
root.iconbitmap('icon.ico')
root.resizable(0,0)
Label(root,text='Enter the Equations',font=('TimesNewRoman'),fg='blue').place(relx=0.02,rely=0.02)
Label(root,text='Eg: 4x+3y+0z=9',font=('TimesNewRoman',8)).place(relx=0.76,rely=0.02)
listbox=ScrolledText(root,width=46,height=12)
listbox.place(relx=0.02,rely=0.11)

Button(root,text='Reset',fg='blue',command=reset,height=2,width=25,border=0).place(relx=0.02,rely=0.77)
Button(root,text='Solve',fg='blue',command=SolveButton,height=2,width=25,border=0).place(relx=0.5,rely=0.77)


ans=Label(root,text='Simultaneous Linear Equation',font=('TimesNewRoman'),bg='blue',fg='white')
ans.pack(fill='x',side='bottom')


root.mainloop()
