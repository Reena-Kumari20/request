import requests
import json
course=[]
id_list=[]
def first_API():
    x = requests.get('http://saral.navgurukul.org/api/courses')
    y=(x.text)
    print(x)
    with open("courses.json","w") as f:
        fi=json.loads(y)
        print(type(fi))
        json.dump(fi,f,indent=2)
    list1=(fi["availableCourses"])
    length=len(list1)
    index=0
    while index<length:
        course_available=list1[index]["name"]
        course.append(course_available)
        id_avaible=list1[index]["id"]
        id_list.append(id_avaible)
        print(index,course_available,id_avaible)
        index+=1
first_API()
def second_API():
    global a
    user=int(input("Enter id:- "))
    a=id_list[user]
    global slug_list
    slug_list=[]
    sec_ond=requests.get("http://saral.navgurukul.org/api/courses/"+a+"/exercises")
    b=(sec_ond.text)
    print(sec_ond.text)
    with open("data2.json","w") as file1:
        file2=json.loads(b)
        json.dump(file2,file1,indent=4)
    for i in range(len(file2["data"])):
        print(i+1,file2["data"][i]["name"])
        slug_list.append(file2["data"][i]["slug"])
        if file2["data"][i]["childExercises"]==[]:
            child=file2["data"][i]["childExercises"]
            print("      ", child)
        else:
            for j in file2["data"][i]["childExercises"]:
                print("     ", j["name"])
    i=1
    while i<len(slug_list):
        print(i,slug_list[i])
        i=i+1
second_API()

def again():
    while True:
        user=input("Enter up/slug/exit: ")
        if user=="up":
            first_API()
            second_API()
            again()
        elif user=="slug":
            length=len(slug_list)
            slug_index=int(input("enter the slug index: "))
            slug_api=(" http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=request_using-json")
            slug_api=slug_api.replace("request_using-json",(slug_list[slug_index]))
            slug_api=slug_api.replace("75",(a))
            call=requests.get(slug_api)
            print(call.text)

            user_input=input("Enter up/next/previous/exit:  ")
            if user_input=="up":
                first_API()
                second_API()
            elif user_input=="next":
                if slug_index==length-1:
                    print("no next slug exists")
                else:
                    slug_api=slug_api.replace((slug_list[slug_index]),(slug_list[slug_index+1]))
                    call1=requests.get(slug_api)
                    print(call1.text)
            elif user_input=="previous":
                if slug_index==0:
                    print("no previous")
                else:
                    slug_api=slug_api.replace((slug_list[slug_index]),(slug_list[slug_index-1]))
                    call2=requests.get(slug_api)
                    print(call2.text)
            elif user_input=="exit":
                print("Thank you")
                return "EXIT"
        elif user=="exit":
            break
again()


    



