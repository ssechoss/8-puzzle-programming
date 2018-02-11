result = []
goal=[0,1,2,3,4,5,6,7,8]
input_file = "input.txt"
is_print = True

import time

dfs_iterations=0
dfs_total_time=0
dfs_total_steps=0
dfs_total_iterations=0

def dfs_main(): 
   
    file = open(input_file,"r")
    lines = file.readlines()

    for line in lines:
        start=[]
        temp = line.replace(',','').split(' ')
        for i in range(9):
             start.append(int(temp[i]))
      
        iterative_deepening_dfs(start)
    dfs_average_steps = dfs_total_steps/len(lines)
    dfs_average_time = dfs_total_time/len(lines)
    dfs_average_iterations=dfs_total_iterations/len(lines)
    #print("average steps",dfs_average_steps)
    #print("average time",average_time)
    #print("average iterations",average_iterations)
    result.append(("IDS\t",dfs_average_steps,dfs_average_time,dfs_average_iterations))
    

    
def iterative_deepening_dfs(start):    
    global dfs_total_time
    global dfs_total_steps
    global dfs_total_iterations
    global is_print
    d_start_time=time.time()
   
    for depth in range(50):
        exit_states = set()
        exit_states.add(tuple(start))        
                  
        paths = []
        paths.append(tuple(start))
        if dfs(depth,exit_states,paths,start,0):
            d_end_time = time.time()
            dfs_total_time+=d_end_time-d_start_time
            dfs_total_steps+=depth
            dfs_total_iterations+=dfs_iterations
            #print("depth",depth)
            #print("run time:",end_time-start_time)   
            #print("iteration #:",iterations)
            #print(result)# output step by step
            if is_print:
                result.insert(0,(paths))
                is_print = False
            
            return
        
def dfs(depth, exit_states, paths, current, step):
    global dfs_iterations
    dfs_iterations+=1
    if step ==depth:
        return is_goal(current)
    option=get_move(current)
    for op in option:  
        next_state = swap(list(current),current.index(0),op)
        next_state_tuple = tuple(next_state)
        if next_state_tuple in exit_states:
            continue;
        paths.append(next_state_tuple)
      
        exit_states.add(next_state_tuple)
        if dfs(depth,exit_states,paths,next_state,step+1):
            return True
        paths.remove(next_state_tuple)
        exit_states.remove(next_state_tuple)
    return False

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
    dfs_main()
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
