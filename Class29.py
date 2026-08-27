#University Management system using Python & Stremlit
import streamlit as st #used for fronted development
#config the forntend page
st.set_page_config(
    page_title="University Management system",
    layout="wide"
)
st.title("University Management Portal")

#creating a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges=[]

#side bar
menu_choice= st.sidebar.radio(
    "SELECT ACTION",
    (
        "Creating College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "Display Colleges List"
    )
)
class college:
    def __init__(self,cname):
        self.cname=cname
        self.students=[]
        self.teachers=[]
    def add_student(self, s):
        self.students.append(s)
    def add_teacher(self, t):
        self.teachers.append(t)
#this function will find the college object from the college list
def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname==cname),None)
class person:
    def __init__(self,branch,name):
        self.branch=branch
        self.name=name
        

class student(person):
    def __init__(self,roll,sname,branch):
        self.rollno=roll#rollno of the student is stored locally
        super().__init__(branch,sname)#sname and branch is stored in the parent class
class teacher(person):
    def __init__(self, subject, tname, branch):
        self.subject = subject
        super().__init__(branch,tname)

#creating new college
if menu_choice=="Creating College":
    cname=st.text_input("Enter New College Name")
    if st.button("CREATE"):
        clg_obj=college(cname)#creating a college class object
        st.session_state.colleges.append(clg_obj)#storing class object in the list
        st.success(f"{cname} created successfully")
#Adding the students in the college
elif menu_choice== "Add Student":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        clgname=st.selectbox("Choose college",[obj.cname for obj in st.session_state.colleges])
        roll=st.text_input("Enter your roll number")
        sname=st.text_input("Enter Student name")
        branch=st.text_input("Enter the branch")
        if st.button("ADD STUDENT"):
            if not(clgname and roll and sname and branch):
                st.error("Please enter all the above information")
            else:
                clg=find_college(clgname)
                stu_obj=student(roll,sname,branch)
                clg.add_student(stu_obj)
                st.success("student added successfully")
#adding new teacher
elif menu_choice== "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        clgname=st.selectbox("Choose college",[obj.cname for obj in st.session_state.colleges])
        subject=st.text_input("Enter your subject")
        tname=st.text_input("Enter Teacher name")
        branch=st.text_input("Enter the branch")
        if st.button("ADD TEACHER"):
            if not(clgname and subject and tname and branch):
                st.error("Please enter all the above information")
            else:
                clg=find_college(clgname)
                tea_obj=student(subject,tname,branch)
                clg.add_teacher(tea_obj)
                st.success("teacher added successfully")

#display Students
elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        clgname = st.selectbox("Choose college", [obj.cname for obj in st.session_state.colleges])
        clg = find_college(clgname)
        st.subheader(f'List of Students in {clgname}')
        if clg.students:
            for i,s in enumerate(clg.students, 1):
                st.write(f'{i} : {s.name}')
        else:
            st.warning("No Student found")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        clgname = st.selectbox("Choose college",[obj.cname for obj in st.session_state.colleges])
        clg = find_college(clgname)
        st.subheader(f'List of Teachers in {clgname}')
        if clg.teachers:
            for i,t in enumerate(clg.teachers, 1):
                st.write(f'{i} : {t.name}')
        else:
            st.warning("No teachers found")

elif menu_choice== "Display Colleges List":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        st.subheader(f'Lists of Colleges')
        for i,c in enumerate(st.session_state.colleges,1):
            st.write(f"{i}:{c.cname}")