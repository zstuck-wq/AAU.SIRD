
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('CourseOffering-1_27_2026.csv')
df = df[df['LearningCourse.CourseCode__c'].str.contains(r'(^[A-Z]{3}[0-9]{3}$)')]



st.title("**AAU Course Catalog**", text_alignment="center")

st.divider()

st.markdown("<h3 style='text-align: center'>Browse all courses, select a term, a school, or a course.</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

terms = sorted(df['AcademicSession.Name'].unique(), reverse=True)

schools = ["School of Arts, Humanities, and Social Sciences",
           "School of International Relations and Diplomacy",
           "School of Business"]
          
codes = df['LearningCourse.CourseCode__c'].unique()
codes = np.sort(codes)

names = df['LearningCourse.Name'].unique()
names = np.sort(names)

term_select = col1.selectbox("Select a Term", terms, index=None, placeholder="Select a Term ...")

school_select = col2.selectbox("Select a School", schools, index=None, placeholder="Select a School ...")

code_select = col1.multiselect("Select a Course by Code", codes, default = None, placeholder="Select Courses ...")

course_select = col2.multiselect("Select a Course by Name", names, default = None, placeholder="Select Courses ...")

if len(code_select) != 0 and len(course_select) != 0:
  filter = df['LearningCourse.CourseCode__c'].isin(code_select) & df['LearningCourse.Name'].isin(course_select)
  df = df[filter].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}", expanded = True):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information") 

elif len(course_select) != 0:
  df = df[df['LearningCourse.Name'].isin(course_select)].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}", expanded = True):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
  
elif len(code_select) != 0:
  df = df[df['LearningCourse.CourseCode__c'].isin(code_select)].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}", expanded = True):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")

elif school_select and term_select is not None:
  df = df[df["AcademicSession.Name"] == term_select].reset_index(drop=True)
  df = df[df['LearningCourse.ParentProvider__c'] == school_select].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}"):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")

elif school_select is not None:
  df = df[df['LearningCourse.ParentProvider__c'] == school_select].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}"):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")

elif term_select is not None:
  df = df[df["AcademicSession.Name"] == term_select].reset_index(drop=True)
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True)

  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}"):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")

else:
  df = df.drop_duplicates(subset=['LearningCourse.CourseCode__c'], keep='first').reset_index(drop=True).sort_values(by=['LearningCourse.CourseCode__c'])
  for row in df.itertuples(index = False):
    with st.expander(f"{row[3]} - {row[6]}"):
      st.write("**Course Description**")
      if not row[4].isnull():
        st.markdown(f"{row[4]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")
      st.divider()
      st.write("**Course Learning Outcomes**")
      if not row[5].isnull():
        st.markdown(f"{row[5]}", unsafe_allow_html=True)
      else:
        st.mardown(f"**{row[3]}** is missing this information")

st.divider()
