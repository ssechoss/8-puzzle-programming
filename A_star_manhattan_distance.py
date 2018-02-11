result = []
goal=[0,1,2,3,4,5,6,7,8]
input_file = "input.txt"
is_print = True

import time
import queue

m_iterations=0
total_time=0
total_steps=0
total_iterations=0

def a_star_man_main(): 
    
    file = open(input_file,"r")
    lines = file.readlines()

    for line in lines:
        start=[]
        temp = line.replace(',','').split(' ')
        for i in range(9):
             start.append(int(temp[i]))
        #print(start)
        a_star_m_distance(start)
    average_steps=total_steps/len(lines)
    average_time = total_time/len(lines)
    average_iterations=total_iterations/len(lines)
   
    #print("average steps",average_steps)
    #print("average time",average_time)
    #print("average iterations",average_iterations)
    result.append(("A*(Manhattan)",average_steps,average_time,average_iterations))
    
def a_star_m_distance(start):
    global m_iterations
    global is_print
    global total_time
    global total_steps
    global total_iterations
    start_time= time.time()
   
    current = list(start)
    path_now = []
    path_now.append(list(start))
    frontiers = queue.PriorityQueue()
    frontiers.put((heuristic(start),0,start,path_now))#(f(n),g(n),current_state)
    exit_states=set()
    exit_states.add(tuple(start))
    
    while frontiers:
        m_iterations+=1
        current_tuple = frontiers.get()
        current=current_tuple[2]
        cost=current_tuple[1]
        path_now =current_tuple[3]
        
        
        h = heuristic(current)
       
        if h==0:
            end_time = time.time()
            total_time+=end_time-start_time
            total_steps+=cost
            total_iterations+=m_iterations
            if is_print:
                result.insert(0,path_now)
                is_print = False
            
            #print("run time:",end_time-start_time)
            #print("steps",cost)
            #print("iterations #:",iterations)
            return 
             
        
        option=get_move(current)
        for op in option:  
            next_state = swap(list(current),current.index(0),op)
            if tuple(next_state) in exit_states:
                continue;
            exit_states.add(tuple(next_state))
            path_next=list(path_now)
            path_next.append(next_state)
            frontiers.put((heuristic(next_state)+cost+1,cost+1,next_state,path_next))  
    return 
   
def heuristic(current):
    count = 0
    for i in range(1,9):
        c_index = current.index(i)
        g_index = goal.index(i)
        row = abs(int(c_index/3)-int(g_index/3))
        column = abs(int(c_index%3)-int(g_index%3))
        count = count + row + column
    return count

def get_move(current): 
    index = current.index(0)
    option=[]
    if int(index/3) < 2:
        option.append(index+3)
    if int(index/3) > 0:
        option.append(index-3)
    if int(index%3) > 0:
        option.append(index-1)
    if int(index%3) < 2:
        option.append(index+1)
    return option

def swap(matrix,position_a,position_b):
    temp = matrix[position_a]
    matrix[position_a] = matrix[position_b]
    matrix[position_b]=temp
    
    return matrix

def print_result(result):
    a_star_man_main()
    output=result[0]
    count = 0
    for each in output:
        
        for i in range(3):
            print(each[i * 3 + 0], each[i * 3 + 1], each[i * 3 + 2])
        count += 1
        if count < len(output):
            print('to')
    
    print("\t\t","Average_Steps","\t","Average_Time","\t","Average_Iterations")
    
    summary = []
    for i in range(1,len(result)):
        summary.append(result[i])
  
    for each in summary:
        print(each[0],"\t",round(each[1],2),"\t\t",round(each[2],4),"\t",int(each[3]))

print_result(result)
