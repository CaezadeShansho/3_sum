
import math

def binary_search(arr,num1,num2,cont,index):
	n=len(arr)
	if n==0:
		return False
	else:
		mid1=math.floor((n+index)/2)
		while True:
			if arr[mid1]<num2:
				return False

			mid2=mid1
			
			if arr[mid1]+num1+num2==0:
				print("combinacion", num1, num2, arr[mid1])
				return True
			elif arr[mid1]+num1+num2>0:
				n=mid1
				mid1=math.floor(mid1/2)
			elif arr[mid1]+num1+num2<0:
				mid1=math.floor((n+mid1)/2)

			if mid1==mid2:
				return False		

def super_triple(arr):
	size=len(arr)
	cont=0
	for i in range(size):
		for j in range(i+1,size):
			if binary_search(arr,arr[i],arr[j],cont,j)==True:
				cont+=1
	return cont		

arr=[]
k=0
while True:
	k=input("num:")
	if k=="":
		break

	k=int(k)
	arr.append(k)

arr=sorted(arr)
print(arr)
print("total:",super_triple(arr))