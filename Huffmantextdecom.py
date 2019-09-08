import heapq
from array import array
from Huffmantextcom import length_tempst,len_filecon
from bitstring import BitArray,BitStream


file=open(r'C:\Users\akash\OneDrive\Desktop\Images\Symtable.txt','r');
Sym=file.read().split(" ");
ind=0;
print(Sym)
del Sym[-1];
for i in range(len(Sym)):
    if(Sym[i]==""):
       sp=" "+Sym[i+1];     #Space appended with next element
       print(sp);
       ind=i;
if(Sym[ind]==""):
 Sym.remove(Sym[ind]);
 Sym.remove(Sym[ind]);
 Sym.append(sp);
print(Sym);
file.close();
Symcode=[];
for i in Sym:
    Symcode.append([i[0],i[1:len(i)]]);
print(Symcode)
file=BitStream(filename=r'C:\Users\akash\OneDrive\Desktop\Images\compressed.txt');
print(file.pos)
con=file.read(length_tempst).bin                 #Binary contents in the file
print(con)
start_pos=0;
j=0;
Res_list=[];
while(j<len_filecon):
 for i in Symcode:
    if(i[1]==con[start_pos:(start_pos+len(i[1]))]):
       print(i[0],i[1]);
       start_pos = start_pos + len(i[1]);
       Res_list.append(i[0]);
       break;
 j=j+1;
res="".join(Res_list)
file=open(r'C:\Users\akash\OneDrive\Desktop\Images\decompressed.txt','w');
file.write(res);
file.close();









