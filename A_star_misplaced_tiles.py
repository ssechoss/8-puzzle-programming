result = []
goal=[0,1,2,3,4,5,6,7,8]
input_file = "input.txt"
is_print = True

import time
import queue

a_iterations=0
a_total_time=0
a_total_steps=0
a_total_iterations=0


def a_star_mis_main(): 
    global result
    file = open(input_file,"r")
    lines = file.readlines()

    for line in lines:
        start=[]
        temp = line.replace(',','').split(' ')
        for i in range(9):
             start.append(int(temp[i]))
        #print(start)
        a_star_misplaced_tiles(start)
    a_average_steps=a_total_steps/len(lines)
    a_average_time =a_total_time/len(lines)
    a_average_iterations=a_total_iterations/len(lines)
    #print("average steps",average_steps)
    #print("average time",average_time)
    #print("average iterations",average_iterations)
    result.append(("A*(Misplaced)",a_average_steps,a_average_time,a_average_iterations))
    return 
    
def a_star_misplaced_tiles(start):    
    global a_iterations
    global is_print
    global a_total_time
    global a_total_steps
    global a_total_iterations
    start_time= time.time()
    
    current = list(start)
    frontiers = queue.PriorityQueue()
    path_now = []
    path_now.append(list(start))
    frontiers.put((heuristic(start),0,start,path_now))#(f(n),g(n),current_state)
    exit_states=set()
    exit_states.add(tuple(start))
    
    while frontiers:

        a_iterations+=1
        current_tuple = frontiers.get()
        current=current_tuple[2]
        cost=current_tuple[1]
        path_now=list(current_tuple[3])
        
        
        h = heuristic(current)
        if h==0:
            end_time = time.time()
            a_total_time+=end_time-start_time
            a_total_steps+=cost
            a_total_iterations+=a_iterations
            #print("steps",cost)
            #print("run time:",end_time-start_time)
            #print("iterations #:",a_iterations)
            if is_print:
                result.insert(0,path_now)
                is_print = False
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
    for i in range(9):
        if current[i]!=goal[i]:
            count+=1
    return count   

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
    a_star_mis_main()
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
