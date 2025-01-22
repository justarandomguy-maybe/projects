with open ("drawing.flag.svg",'r') as file:
   content = file.readlines()
interest_lines = [line for line in content if "tspan" in line]
flag = "".join([elem.split(">")[1].split("<")[0] for elem in interest_lines]).replace(" ","")
print(flag)