#simple quiz game using python


def give_options(w,x,y,z):
	print("a: ",w)
	print("b: ",x)
	print("c: ",y)
	print("d: ",z)
print("Hello! Welcome to the Quiz" "/n" "All questions carries 10 marks each")
ans=input("Are you ready to start the Quiz(yes/no): ")
a="Note: Write answers! Do not write options. "
score=0
total_questions=5
correct_ans=["all of the mentioned","Def","#","print()","Class"]
if ans.lower()=="yes":

#frst question
	print(a)
	print("Question : Which type of Programming does Python support?")
	give_options("object-oriented programming","structured programming","functional programming","all of the mentioned")
	ans=input(">>>")
	if ans.lower()==correct_ans[0].lower():
		score+=10
		print("Correct")
	else:
		print("Incorrect")

#scnd question
	print(a)
	print("Question : Which keyword is used for function in Python language?")
	give_options("Function","Def","Fun","Define")
	ans=input(">>>")
	if ans.lower()==correct_ans[1].lower():
		score+=10
		print("Correct")
	else:
		print("Incorrect")

#third question
	print(a)
	print("Question : Which of the following character is used to give single-line comments in Python?")
	give_options("//","#","!","?")
	ans=input(">>>")
	if ans.lower()==correct_ans[2].lower():
		score+=10
		print("Correct")
	else:
		print("Incorrect")

#fourth question
	print(a)
	print("Question : Which of the following functions is a built-in function in python?")
	give_options("factorial()","print()","seed()","sqrt()")
	ans=input(">>>")
	if ans.lower()==correct_ans[3].lower():
		score+=10
		print("Correct")
	else:
		print("Incorrect")

#fifth question
	print(a)
	print("Question : Which of the following is not a core data type in Python programming?")
	give_options("Tuples","Lists","Class","Dictionary")
	ans=input(">>>")
	if ans.lower()==correct_ans[4].lower() :
		score+=10
		print("Correct")
	else:
		print("Incorrect")


if score< 30:
	print("oops, your score is ",score,"/50 , Better luck next time.")
elif score==30:
	print("wow! you scored ",score,"/50, you are quite smart.")
else:
	print("Congratulations! it's a perfect ",score,"/50 ,you are Intelligent.")
