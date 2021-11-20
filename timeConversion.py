import re
time = "12:40:22AM"
list=time.split(":")
if("AM" in time):
    if(int(list[0])==12):
        hr=int(list[0])-12
    else:
        hr=list[0]
if("PM" in time):
    if(int(list[0])==12):
        hr=list[0]
    else:
        hr=int(list[0])+12
if(int(hr)>=24):
    hr=hr-24
mini=list[1]
sec=re.split(r'PM|AM',list[-1])
if hr<12:
    hour=f'{hr:02d}'
result=hour+":"+mini+":"+sec[0]
print(result)


