import heapq
from array import array
from bitstring import BitArray,BitStream
import sys


class Huffman:
  count=0;
  def __init__(self):
      self.data = 0;
      self.c = 0;
      self.left=None;
      self.right=None;


#For sorting the objects
  def __lt__(self,other):
      return self.data < other.data


#For assigning code to the numbers
  def printcode(self,s):
    if(self.left==None and self.right==None and self.c!='#@!'):
        global Lis;
        print(self.c,":",s,self.data)
        Lis.append([self.c,s]);        #Code for each unique character will be stored in the list
        return;
    sl=self.left;
    sl.printcode(s+"0")
    sr=self.right;
    sr.printcode(s+"1")


Lis=[];
charArray=[];
charfreq=[];
file=open(r'C:\Users\akash\OneDrive\Desktop\Images\SampleTextFile_1000kb.txt','r');    #Location of the file which needs to be compressed
filecon=file.read();
##print(filecon,type(filecon));
charArray="".join(set(filecon));    #Removing the duplicate characters
##print(charArray,len(charArray));
L=list(charArray)                   #List of individual characters
for i in L:
    charfreq.append(filecon.count(i));
##print(L);
##print(charfreq);
#charArray=['f','e','d','c','b','a']
#charfreq=[45,16,13,12,9,5]
len_filecon=len(filecon);
q=[]
n=len(charArray)
for i in range(n):
   h = Huffman()
   h.c = charArray[i]
   h.data = charfreq[i]
   q.append(h)
#   elif(h.c=="0"):
#      h0=h;
#   elif(h.c=="1"):
#      h1=h;
q.sort()
for item in q:
    print(item.c,item.data,end=" ")
##print();
root=Huffman();
s=min(q);
##print(s.data);
q_len=len(q);
print(q_len);
while(len(q)>1):
  x=Huffman();
  y=Huffman();
  f=Huffman();
#  if(counter==0):
#    x=h0;
#  else:
  x = min(q);
  q.remove(min(q));
#  if(counter==q_len):
#     y=h1;
#  else:
  y=min(q);
  q.remove(min(q));
  print(x.c,x.data,y.c,y.data)
  f.data=x.data+y.data;
##  print(f.data)
  f.c='#@!';                 #The selection of this combination should be very rare
  f.left=x;
  f.right=y;
#  root=f;
  q.append(f);
root=f;
##print(root);
count=0;
root.printcode("");
file=open(r"C:\Users\akash\OneDrive\Desktop\Images\Symtable.txt","w");   #Location of the Symtable file which has characters and code of each character
for i in Lis:
  file.write(i[0]);
  file.write(i[1]);
  file.write(" ");
file.close();
file=open(r"C:\Users\akash\OneDrive\Desktop\Images\compressed.txt","wb");  #Location of the compressed file
#dec=file.read()
temp_string=filecon
check_st="";
for i in Lis:
   if(i[0]=="0"):
    temp_string=temp_string.replace(i[0],"^$^");
    check_st=i[1];
for i in Lis:
    if(i[0]=="1"):
        temp_string = temp_string.replace(i[0], i[1]);
temp_string=temp_string.replace("^$^",check_st);
print(temp_string);
for i in Lis:
 if(i[0]!="0" and i[0]!="1"):
  temp_string=temp_string.replace(i[0],i[1]);
print(temp_string)
temp_string="0b"+temp_string             #Addition of "0b" is required by BitString to convert it
print("length",len(temp_string));
b = BitArray(temp_string);
b.tofile(file);
file.close();
length_tempst=len(temp_string)-2;       #This variable will be passed to the Huffmantextdecom.py file











