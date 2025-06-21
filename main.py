# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Supabase config
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Table names
# TABLE_NAME = "Member"
# JOBS_TABLE = "Job"
#
# st.title("Supabase Data Viewer")
#
# # Fetch data from Member table
# with st.spinner("Loading Member data..."):
#     member_response = supabase.table(TABLE_NAME).select("*").execute()
#     member_data = member_response.data
#     if member_data:
#         member_df = pd.DataFrame(member_data)
#         st.subheader("Member Table")
#         st.dataframe(member_df)
#     else:
#         st.warning("No data found in Member table.")
#
# # Fetch data from Job table
# with st.spinner("Loading Job data..."):
#     job_response = supabase.table(JOBS_TABLE).select("*").execute()
#     job_data = job_response.data
#     if job_data:
#         job_df = pd.DataFrame(job_data)
#         st.subheader("Job Table")
#         st.dataframe(job_df)
#     else:
#         st.warning("No data found in Job table.")
import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Load secrets
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

TABLE_NAME = "Member"
JOBS_TABLE = "Job"

st.title("Supabase Data Viewer")

try:
    member_response = supabase.table(TABLE_NAME).select("*").execute()
    st.subheader("Member Table")
    st.dataframe(pd.DataFrame(member_response.data))
except Exception as e:
    st.error(f"Error fetching 'Member' table: {e}")

try:
    job_response = supabase.table(JOBS_TABLE).select("*").execute()
    st.subheader("Job Table")
    st.dataframe(pd.DataFrame(job_response.data))
except Exception as e:
    st.error(f"Error fetching 'Job' table: {e}")
