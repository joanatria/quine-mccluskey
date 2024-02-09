import globalvars

# Arguments:    x - variable in minterms
# Description:  find variables in minterm, example: --01 has C' and D as variables
# Return:       var_list - list of variables 
def find_var(x): 
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+65)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+65))
    return var_list

# Arguments:    x - variable in minterms
# Description:  flattens list (means of appending lists to another)
# Return:       flattened_items - flattened items in a list
def flatten_list(x): 
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items

# Arguments:    a - variable (minterms)
# Description:  finds out which minterms are merged, example: 111- is obtained by merging 14(1110) and 15(1111)
# Return:       temp - placeholder since function is to be used several times
def find_minterms(a): 
    common = a.count('-')
    if common == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(common) for i in range(pow(2,common))]
    temp = []
    for i in range(pow(2,common)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

# Arguments:    a,b - variable (minterms)
# Description:  checks if 2 minterms differ by 1 bit ONLY
# Return:       boolean(true) and mismatch_index - index of non-common bits
def compare(a,b): 
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True,mismatch_index)

# Arguments:    x,y variables(minterms)
# Description:   multiply 2 minterms
# Return:       result - to be used in mul_exp(x,y)
def mul_min(x,y): 
    result = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            result.append(i)
    for i in y:
        if i not in result:
            result.append(i)
    return result

# Arguments:    x,y variables(minterms)
# Description:   multiply 2 expression results
# Return:       result - list of expressions to be used in main function
def mul_exp(x,y): 
    result = []
    for i in x:
        for j in y:
            tmp = mul_min(i,j)
            result.append(tmp) if len(tmp) != 0 else None
    return result

# Arguments:    my_list and dc_list - list of minterms and list of don't cares
# Description:  removes don't care terms from a given list
# Return:       result - refined list
def refine(my_list,dc_list): 
    result = []
    for i in my_list:
        if int(i) not in dc_list:
            result.append(i)
    return result

# Arguments:    x - variable
# Description:  find essential prime implicants from prime implicants chart
# Return:       result - list of minterms
def find_epi(x): 
    result = []
    for i in x:
        if len(x[i]) == 1:
            result.append(x[i][0]) if x[i][0] not in result else None
    return result

# Arguments:    table (table of minterms), terms (minterms)
# Description:   removes minterms which are already covered from table
# Return:       none
def remove_terms(table,terms): 
    for i in terms:
        for j in find_minterms(i):
            try:
                del table[j]
            except KeyError:
                pass

# Arguments:    group - dictionary of results
# Description:   prints minterm's initial table with group number and binary representation
# Return:       vari - string of output with binary representation
def print_initable(groups):
    vari = ''
    vari +="\n Group No. \t Minterms \t Binary of Minterms\n%s"%('='*50)
    for i in sorted(groups.keys()):
        vari += "\n%d:" %i
        for j in groups[i]:
            vari +="\t\t%d\t\t%s"%(int(j,2),j) + "\n"
        vari += '='*50 + "\n"

    return vari

# Arguments:    local_unmarked - set of unmarked per table
# Description:   prints unmarked terms
# Return:       elem - string output
def unmarked(local_unmarked):
    if (len(local_unmarked) == 0):
        elem = "Unmarked elements(Prime Implicants) of this table: None \n"
        
    else:
        elem = ''
        elem += "Unmarked elements(Prime Implicants) of this table: "
        elem += ', '.join(local_unmarked) + "\n"

    return elem

# Arguments:    all_pi - set of prime implicants
# Description:   prints all prime implicants

# Return:       pi - string output
def allpi(all_pi):
    if len(all_pi)==0:
        pi = "All Prime Implicants: None"

    else:
        pi = ''
        pi += "\nAll Prime Implicants: "
        pi += ', '.join(all_pi)

    return pi

# Arguments:    group - dictionary of results
# Description:   prints minterm's next tables with group number and binary representation
# Return:       varn - string of output with binary representation
def print_nextable(groups):
    varn = ''
    varn +="\nGroup No.\tMinterms\t \t Binary of Minterms\n%s"%('='*50)
    for i in sorted(groups.keys()):
        varn += "\n%d:"%i 
        for j in groups[i]:
            varn += "\t\t%-24s\t\t%s"%(','.join(find_minterms(j)),j) + "\n" 
        varn += '='*50 + "\n"
    
    return varn

# Arguments:    mt, dc - user input, all_pi - set, chart - dictionary
# Description:   prints prime implicants
# Return:       prime - string of prime implicants
def prime_implicant(mt, all_pi, dc, chart):
    sz = len(str(mt[-1])) # The number of digits of the largest minterm
    prime = ''
    prime += '\nPrime Implicants chart:\n\nMinterms | %s\n%s'%(' '.join((' '*(sz-len(str(i))))+str(i) for i in mt),'='*(len(mt)*(sz+1)+16)) + "\n"
    for i in all_pi:
        merged_minterms,y = find_minterms(i),0
        prime += "%s | "%','.join(merged_minterms) + ''
        for j in refine(merged_minterms,dc):
            x = mt.index(int(j))*(sz+1) # This is the position where we should place 'X'
            prime += ' '*abs(x-y)+' '*(sz-1)+'X'
            y = x+sz
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
        prime += '\n'+'='*(len(mt)*(sz+1)+16) + "\n"
    
    return prime

# Arguments:    chart - dictionary of results
# Description:   prints essential prime implcants and final answer
# Return:       epi_var = epi and final answer
def epi(EPI):
    epi_var = ''
    epi_var += "\nEssential Prime Implicants: "+', '.join(str(i) for i in EPI)

    return epi_var

# Arguments:    chart - dictionary of results, EPI - find epi in chart
# Description:   prints final answer
# Return:       final - string final answer
def print_final(chart, EPI):
    final = ''
    if(len(chart) == 0): # If, after deleting EPI-related columns, no minterms are left,
        final_result = [find_var(i) for i in EPI] # Final resultult with only EPIs
    else: 
        P = [[find_var(j) for j in chart[i]] for i in chart]
        while len(P)>1: # Keep multiplying until we get the SOP form of P
            P[1] = mul_exp(P[0],P[1])
            P.pop(0)
        final_result = [min(P[0],key=len)] # selecting the P term with the minimum variables
        final_result.extend(find_var(i) for i in EPI) # Adding the EPIs to final solution
    final += '\n\n\nSolution: F = '+' + '.join(''.join(i) for i in final_result) +"\n"

    return final

# Arguments:    mt (minterms from user input), size (number of variables user input), dc (don't cares from user input)
# Description:   whole implementation of Quine-McCluskey Method
# Return:       none
def maindriver(input_mt, input_size, input_dc):
 try:
    mt = [int(i) for i in input_mt.strip().split()]
    size = int(input_size)
    dc = [int(i) for i in input_dc.strip().split()]
    mt.sort()
    minterms = mt+dc
    minterms.sort()
    groups = {}
    all_pi = set()
    chart = {}
    
    # primary grouping of minterms (counting number of 1s)
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]

    # printing of primary table
    globalvars.varin = print_initable(groups)

    # creating tables and finding prime implicants 
    count =1
    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]: # loop that iterates the elements in the current group
                for k in tmp[l[i+1]]: # Loop that iterates the next group elements
                    result = compare(j,k) # Compare the minterms
                    if result[0]: # If the minterms differ by 1 bit only
                        try:
                            groups[m].append(j[:result[1]]+'-'+j[result[1]+1:]) if j[:result[1]]+'-'+j[result[1]+1:] not in groups[m] else None # Put a '-' in the changing bit and add it to corresultponding group
                        except KeyError:
                            groups[m] = [j[:result[1]]+'-'+j[result[1]+1:]] # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                        should_stop = False
                        marked.add(j) # Mark element j
                        marked.add(k) # Mark element k
            m += 1
        local_unmarked = set(flatten_list(tmp)).difference(marked) # Unmarked elements of each table
        all_pi = all_pi.union(local_unmarked) # Adding Prime Implicants to global list
        if(count==1):
            globalvars.varin+=unmarked(local_unmarked)
        else:
            globalvars.varnx += unmarked(local_unmarked)
        
        if should_stop: # If the minterms cannot be combined further
            globalvars.pi = allpi(all_pi)
            break


        #printing of next tables
       
        globalvars.varnx += print_nextable(groups) 
            
        count+=1

    # Printing of Prime Implicant Table
    globalvars.table = prime_implicant(mt,all_pi,dc, chart)

    # Finding essential prime implicants
    EPI = find_epi(chart) 
    globalvars.epi = epi(EPI)
    remove_terms(chart,EPI) # Remove EPI related columns from chart

    globalvars.ans = print_final(chart, EPI)
 except Exception as e:
    maindriver
    