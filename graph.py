from tkinter import *
from tkinter import messagebox
import random
import math
Gwidth=640
Ghight=480
hod=0
class vertex:
    def __init__(self,v):
        self.value=v
        self.conected=[]
        self.button=Button(root,text=str(v)+'$') #,command=start_clik
        self.button.bind('<Button-1>',self.vertex_clik)
        self.center_x=0
        self.center_y=0
    def vertex_clik(self,event):
        global hod
        print(event)
        l=len(self.conected)
        hod+=1
        label2['text']='Ходов:' +str(hod)
        self.value-=l
        for i in self.conected:
            main_graph.vertexses[i].value+=1
        main_graph.update()
        if main_graph.check_win():
            messagebox.showinfo('ПОБЕДА','КОМУНИЗМ ПОСТРОЕН ЗА '+str(hod)+' ПЯТИЛЕТОК')
            main_graph.clear_space()
        #radius
def generate_vertex_values(n,genis):
    vals=[]
    if n%2==0:
        m=n-2
        vals.append(genis)
        vals.append(0)
    else:
        m=n-1
        vals.append(genis)
    for i in range(1,m//2+1):
       vals.append(i) 
       vals.append(0-i)
    random.shuffle(vals)
    return(vals)
    
class graph: 
    #vertexses
    #n_vertex
    #n_edges
    def __init__(self,n):
        self.vertexses=[]
        self.n_vertex=n
        self.n_edges=random.randint(n-1,n*(n-1)//2)
        x=generate_vertex_values(self.n_vertex,self.n_edges-self.n_vertex+1)
        for i in range(self.n_vertex):
            y=vertex(x[i])
            self.vertexses.append(y)
        vg=list(range(self.n_vertex))
        v1=random.choice(vg)
        vg.remove(v1)
        for i in range(n-1):
            v2=random.choice(vg)
            vg.remove(v2)
            self.vertexses[v1].conected.append(v2)
            self.vertexses[v2].conected.append(v1)
            v1=v2
        edges_left=self.n_edges-n+1
        all_posible_edg=[]
        for i in range(n-1):
            for j in range(i,n):
                if (j not in self.vertexses[i].conected)and(i!=j)and(i not in self.vertexses[j].conected):
                    all_posible_edg.append([i,j])
        for i in range(edges_left):
            o=random.choice(all_posible_edg)
            v1=o[0]
            v2=o[1]
            all_posible_edg.remove(o)
            self.vertexses[v1].conected.append(v2)
            self.vertexses[v2].conected.append(v1)
    def print_state(self):
        print('vertex ',self.n_vertex,'edge ',self.n_edges)
        for i in range(self.n_vertex):
            print(i,self.vertexses[i].value,self.vertexses[i].conected)
    def draw(self):
        f=(2*math.pi)/self.n_vertex
        r=min(Gwidth,Ghight)/2-40
        xc=Gwidth//2
        yc=Ghight//2
        for i in range(len(self.vertexses)):
            yi=math.floor(r*math.sin(f*i)+yc)
            xi=math.floor(r*math.cos(f*i)+xc)
            self.vertexses[i].button.place(x=xi,y=yi)
            self.vertexses[i].center_x=xi+5
            self.vertexses[i].center_y=yi+5
        for i in range(len(self.vertexses)):
            for j in self.vertexses[i].conected:
                canvas.create_line(self.vertexses[i].center_x,self.vertexses[i].center_y,self.vertexses[j].center_x,self.vertexses[j].center_y,width=3)
    def clear_space(self):
        for i in range(len(self.vertexses)):
            self.vertexses[i].button.place_forget()
        canvas.delete('all')
        self.vertexses.clear()
    def update(self):
        for i in range(len(self.vertexses)):
            self.vertexses[i].button['text']=str(self.vertexses[i].value)+'$'
    def check_win(self):
        flag=True
        for i in range(len(self.vertexses)):
            if self.vertexses[i].value<0:
                flag=False
        return flag

root =Tk()
main_graph=0
def start_clik():
    global main_graph
    global hod
    hod=0
    label2['text']='Ходов:0'
    if main_graph!=0:
        main_graph.clear_space()
    main_graph=graph(int(spin.get()))
    main_graph.draw()
    main_graph.print_state()
     #x=len(main_graph.vertexses)
     #print(main_graph.vertexses[random.randint(0,x-1)].value)

#make_gui()
root.title('Постройте КОМУНИЗМ')
root.geometry(str(Gwidth)+'x'+str(Ghight))
canvas=Canvas(root,width=Gwidth,height=Ghight)
canvas.pack()
label1=Label(root,text='Вершин:')
spin=Spinbox(root,from_=5,to=12,width=5)
label1.place(x=5,y=5)
spin.place(x=70,y=5)
start_button=Button(root,text='Начaть',command=start_clik)
start_button.place(x=120,y=5)
label2=Label(root,text='Ходов:'+str(hod))
label2.place(x=400,y=5)
def main():
    #make_gui()
    random.seed(version=2)
    root.mainloop()
if __name__=='__main__':
    main()