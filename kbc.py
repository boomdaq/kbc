p="kon banega crorepati"
q="__________________"
print(p.center(50))
print(q.center(50))
def w():
	print("Wrong answer")
amount=0
q=["1) what is the capital of india:","2) prime minister of india:","3) capital of west bengal:"]
print(q[0])

newdelhi="a"
uttarakhand="b"
narendramodi="a"
mamtabannerjee="b"
kolkata="a"
print("(a)new delhi\n(b)uttarakhand")
c=input()
if (newdelhi==c):
	print("correct answer")
	amount=amount+10
else:
	w()
	amount=amount+0
print(q[1])
print("(a)narendra modi\n(b)mamta bannerjee")
c=input()
if(narendramodi==c):
	print("correct answer")
	amount=amount+10
else:
	w()
print(q[2])
print("(a)kolkata (b)medinipur")
c=input()
if(kolkata==c):
	print("correct answer")
	amount=amount+10
else:
	w()
	amount=amount+0
print("you won ₹",amount)