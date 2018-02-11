result = []
goal=[0,1,2,3,4,5,6,7,8]
input_file = "input.txt"
is_print = True

import time
import queue

nodes = 0
b_total_time=0
b_total_steps=0
b_total_iterations=0

def bfs_main(): 
   
    file = open(input_file,"r")
    lines = file.readlines()

    for line in lines:
        start=[]
        temp = line.replace(',','').split(' ')
        for i in range(9):
             start.append(int(temp[i]))
     
        bfs(start)
    b_average_steps=b_total_steps/len(lines)
    b_average_time = b_total_time/len(lines)
    b_average_iterations=b_total_iterations/len(lines)
    #print("average steps",average_steps)
    #print("average time",average_time)
    #print("average iterations",average_iterations)
    result.append(("BFS\t",b_average_steps,b_average_time,b_average_iterations))
    return 
    
def bfs(start):
    global b_total_time
    global b_total_steps
    global b_total_iterations
    global nodes
    global is_print
    b_start_time= time.time()

    current = list(start)
    path_now = []
    path_now.append(list(start))
    frontiers = queue.Queue()
    
    frontiers.put((start,path_now))
    exit_dir=dict()
    exit_dir.update({tuple(start):0})
    while frontiers:
        nodes +=1 
        current_tuple = frontiers.get()
        current=current_tuple[0]
        path_now = current_tuple[1]
        b_steps=exit_dir.get(tuple(current), )
        
        if tuple(current) in exit_dir:
            del exit_dir[tuple(current)]
        
        if is_goal(current):
            b_end_time = time.time()
            b_total_time+=b_end_time-b_start_time
            b_total_steps+=b_steps
            b_total_iterations+=nodes
            if is_print:
                result.insert(0,path_now)
                is_print = False
            #print("steps",b_steps)
            #print("run time:",end_time-start_time)           
            #print("nodes #:",nodes)
            return 
        
        option=get_move(current)
        for op in option:  
            next_state = swap(list(current),current.index(0),op)
            if tuple(next_state) in exit_dir:
                continue;
            exit_dir.update({tuple(next_state):b_steps+1})
            path_next=list(path_now)
            path_next.append(next_state)
            frontiers.put((next_state,path_next))
    return     

   
def is_goal(state):   
    for i in range(9):
        if state[i]!=goal[i]:
            return False
    return True

def get_move(current): 
    index = current.index(0)
    option=[]
    if int(index/3) < 2:
        option.append(index+3)
    if int(index/3) >0:
        option.append(index-3)
    if int(index%3) > 0:
        option.append(index-1)
    if int(index%3)<2:
        option.append(index+1)
    return option

def swap(matrix,position_a,position_b):
    temp = matrix[position_a]
    matrix[position_a] = matrix[position_b]
    matrix[position_b]=temp
    
    return matrix

def print_result(result):
    bfs_main()
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
