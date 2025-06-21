# # import streamlit as st
# # import pandas as pd
# # from supabase import create_client, Client
# #
# # # Supabase config
# # SUPABASE_URL = st.secrets["supabase"]["url"]
# # SUPABASE_KEY = st.secrets["supabase"]["key"]
# #
# # supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# #
# # # Table names
# # TABLE_NAME = "Member"
# # JOBS_TABLE = "Job"
# #
# # st.title("Supabase Data Viewer")
# #
# # # Fetch data from Member table
# # with st.spinner("Loading Member data..."):
# #     member_response = supabase.table(TABLE_NAME).select("*").execute()
# #     member_data = member_response.data
# #     if member_data:
# #         member_df = pd.DataFrame(member_data)
# #         st.subheader("Member Table")
# #         st.dataframe(member_df)
# #     else:
# #         st.warning("No data found in Member table.")
# #
# # # Fetch data from Job table
# # with st.spinner("Loading Job data..."):
# #     job_response = supabase.table(JOBS_TABLE).select("*").execute()
# #     job_data = job_response.data
# #     if job_data:
# #         job_df = pd.DataFrame(job_data)
# #         st.subheader("Job Table")
# #         st.dataframe(job_df)
# #     else:
# #         st.warning("No data found in Job table.")
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Load secrets
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# TABLE_NAME = "Member"
# JOBS_TABLE = "Job"
#
# st.title("Supabase Data Viewer")
#
# try:
#     member_response = supabase.table(TABLE_NAME).select("*").execute()
#     st.subheader("Member Table")
#     st.dataframe(pd.DataFrame(member_response.data))
# except Exception as e:
#     st.error(f"Error fetching 'Member' table: {e}")
#
# try:
#     job_response = supabase.table(JOBS_TABLE).select("*").execute()
#     st.subheader("Job Table")
#     st.dataframe(pd.DataFrame(job_response.data))
# except Exception as e:
#     st.error(f"Error fetching 'Job' table: {e}")


# import streamlit as st
# from supabase import create_client, Client
#
# # Initialize Supabase client (replace with your URL and anon key)
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("Add New Member")
#
# with st.form("member_form"):
#     name = st.text_input("Name")
#     designation = st.text_input("Designation")
#     facebookUrl = st.text_input("Facebook URL")
#     linkedinUrl = st.text_input("LinkedIn URL")
#     imageUrl = st.text_input("Image URL")
#     status = st.selectbox("Status", options=["current", "alumni"])
#
#     panel = st.selectbox("Panel", options=[
#         "executive_member",
#         "sub_executive",
#         "executive",
#         "general_member",
#         "advisory"
#     ])
#
#     submitted = st.form_submit_button("Add Member")
#
# if submitted:
#     # Simple validation example
#     if not name or not designation:
#         st.error("Name and Designation are required.")
#     else:
#         # Insert the new member into Supabase
#         data = {
#             "name": name,
#             "designation": designation,
#             "facebookUrl": facebookUrl,
#             "linkedinUrl": linkedinUrl,
#             "imageUrl": imageUrl,
#             "status": status,
#             "panel": panel,
#         }
#
#         response = supabase.table("Member").insert(data).execute()
#
#         if response.error:
#             st.error(f"Failed to add member: {response.error.message}")
#         else:
#             st.success("Member added successfully!")
#             st.json(response.data)

#
# import streamlit as st
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("Add New Member")
#
# with st.form("member_form"):
#     name = st.text_input("Name")
#     designation = st.text_input("Designation")
#     facebookUrl = st.text_input("Facebook URL")
#     linkedinUrl = st.text_input("LinkedIn URL")
#     imageUrl = st.text_input("Image URL")
#
#     status = st.selectbox("Status", options=["current", "alumni"])
#     panel = st.selectbox("Panel", options=[
#         "executive_member",
#         "sub_executive",
#         "executive",
#         "general_member",
#         "advisory"
#     ])
#
#     submitted = st.form_submit_button("Add Member")
#
# if submitted:
#     if not name or not designation:
#         st.error("Name and Designation are required.")
#     else:
#         data = {
#             "name": name,
#             "designation": designation,
#             "facebookUrl": facebookUrl,
#             "linkedinUrl": linkedinUrl,
#             "imageUrl": imageUrl,
#             "status": status,
#             "panel": panel,
#         }
#
#         response = supabase.table("Member").insert(data).execute()
#
#         if response.status_code >= 400:
#             st.error(f"Failed to add member: {response.data}")
#         else:
#             st.success("Member added successfully!")
#             st.json(response.data)


# import streamlit as st
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("Add New Member")
#
# with st.form("member_form"):
#     name = st.text_input("Name")
#     designation = st.text_input("Designation")
#     facebookUrl = st.text_input("Facebook URL")
#     linkedinUrl = st.text_input("LinkedIn URL")
#     imageUrl = st.text_input("Image URL")
#
#     status = st.selectbox("Status", options=["current", "alumni"])
#     panel = st.selectbox("Panel", options=[
#         "executive_member",
#         "sub_executive",
#         "executive",
#         "general_member",
#         "advisory"
#     ])
#
#     submitted = st.form_submit_button("Add Member")
#
# if submitted:
#     if not name or not designation:
#         st.error("Name and Designation are required.")
#     else:
#         data = {
#             "name": name,
#             "designation": designation,
#             "facebookUrl": facebookUrl,
#             "linkedinUrl": linkedinUrl,
#             "imageUrl": imageUrl,
#             "status": status,
#             "panel": panel,
#         }
#
#         try:
#             response = supabase.table("Member").insert(data).execute()
#             st.success("Member added successfully!")
#             st.json(response.data)
#         except Exception as e:
#             st.error(f"Failed to add member: {e}")

# basic add
# import streamlit as st
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("Add New Member")
#
# with st.form("member_form"):
#     name = st.text_input("Name")
#     designation = st.text_input("Designation")
#     facebookUrl = st.text_input("Facebook URL")
#     linkedinUrl = st.text_input("LinkedIn URL")
#     imageUrl = st.text_input("Image URL")
#
#     status = st.selectbox("Status", options=["current", "alumni"])
#     panel = st.selectbox("Panel", options=[
#         "executive_member",
#         "sub_executive",
#         "executive",
#         "general_member",
#         "advisory"
#     ])
#
#     submitted = st.form_submit_button("Add Member")
#
# if submitted:
#     if not name or not designation:
#         st.error("Name and Designation are required.")
#     else:
#         data = {
#             "name": name,
#             "designation": designation,
#             "facebookUrl": facebookUrl,
#             "linkedinUrl": linkedinUrl,
#             "imageUrl": imageUrl,
#             "status": status,
#             "panel": panel,
#         }
#
#         try:
#             supabase.table("Member").insert(data).execute()
#             st.success("Member added successfully!")
#         except Exception as e:
#             st.error(f"Failed to add member: {e}")


# csv upload
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("Add New Member")
#
# mode = st.radio("Choose input method:", ("Manual Entry", "Upload CSV"))
#
# if mode == "Manual Entry":
#     with st.form("member_form"):
#         name = st.text_input("Name")
#         designation = st.text_input("Designation")
#         facebookUrl = st.text_input("Facebook URL")
#         linkedinUrl = st.text_input("LinkedIn URL")
#         imageUrl = st.text_input("Image URL")
#
#         status = st.selectbox("Status", options=["current", "alumni"])
#         panel = st.selectbox("Panel", options=[
#             "executive_member",
#             "sub_executive",
#             "executive",
#             "general_member",
#             "advisory"
#         ])
#
#         submitted = st.form_submit_button("Add Member")
#
#     if submitted:
#         if not name or not designation:
#             st.error("Name and Designation are required.")
#         else:
#             data = {
#                 "name": name,
#                 "designation": designation,
#                 "facebookUrl": facebookUrl,
#                 "linkedinUrl": linkedinUrl,
#                 "imageUrl": imageUrl,
#                 "status": status,
#                 "panel": panel,
#             }
#
#             try:
#                 supabase.table("Member").insert(data).execute()
#                 st.success("Member added successfully!")
#             except Exception as e:
#                 st.error(f"Failed to add member: {e}")
#
# elif mode == "Upload CSV":
#     uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
#     if uploaded_file is not None:
#         try:
#             df = pd.read_csv(uploaded_file)
#
#             # Optional: Validate required columns exist
#             required_cols = ["name","designation","facebookUrl","linkedinUrl","imageUrl","status","panel"]
#             missing_cols = [col for col in required_cols if col not in df.columns]
#             if missing_cols:
#                 st.error(f"Missing columns in CSV: {missing_cols}")
#             else:
#                 if st.button("Insert all members from CSV"):
#                     records = df.to_dict(orient="records")
#                     try:
#                         supabase.table("Member").insert(records).execute()
#                         st.success(f"Inserted {len(records)} members successfully!")
#                     except Exception as e:
#                         st.error(f"Failed to insert members: {e}")
#         except Exception as e:
#             st.error(f"Error reading CSV file: {e}")


# nav buttons
import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Initialize Supabase client
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sidebar navigation
st.sidebar.title("Navigation")
main_section = st.sidebar.radio("Go to", ["Manage Member", "Manage Job"])

# === Manage Member Section ===
if main_section == "Manage Member":
    sub_section = st.sidebar.radio("Member Options", ["Add Member", "Update Member", "Delete Member"])

    if sub_section == "Add Member":
        st.title("Add New Member")

        mode = st.radio("Choose input method:", ("Manual Entry", "Upload CSV"))

        if mode == "Manual Entry":
            with st.form("member_form"):
                name = st.text_input("Name")
                designation = st.text_input("Designation")
                facebookUrl = st.text_input("Facebook URL")
                linkedinUrl = st.text_input("LinkedIn URL")
                imageUrl = st.text_input("Image URL")

                status = st.selectbox("Status", options=["current", "alumni"])
                panel = st.selectbox("Panel", options=[
                    "executive_member",
                    "sub_executive",
                    "executive",
                    "general_member",
                    "advisory"
                ])

                submitted = st.form_submit_button("Add Member")

            if submitted:
                if not name or not panel:
                    st.error("Name and panel are required.")
                else:
                    data = {
                        "name": name,
                        "designation": designation,
                        "facebookUrl": facebookUrl,
                        "linkedinUrl": linkedinUrl,
                        "imageUrl": imageUrl,
                        "status": status,
                        "panel": panel,
                    }

                    try:
                        supabase.table("Member").insert(data).execute()
                        st.success("Member added successfully!")
                    except Exception as e:
                        st.error(f"Failed to add member: {e}")

        elif mode == "Upload CSV":
            uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
            if uploaded_file is not None:
                try:
                    df = pd.read_csv(uploaded_file)

                    required_cols = ["name","designation","facebookUrl","linkedinUrl","imageUrl","status","panel"]
                    missing_cols = [col for col in required_cols if col not in df.columns]
                    if missing_cols:
                        st.error(f"Missing columns in CSV: {missing_cols}")
                    else:
                        if st.button("Insert all members from CSV"):
                            records = df.to_dict(orient="records")
                            try:
                                supabase.table("Member").insert(records).execute()
                                st.success(f"Inserted {len(records)} members successfully!")
                            except Exception as e:
                                st.error(f"Failed to insert members: {e}")
                except Exception as e:
                    st.error(f"Error reading CSV file: {e}")


    elif sub_section == "Update Member":

        st.title("Update Member")

        # Fetch all members

        try:

            response = supabase.table("Member").select("*").execute()

            members = response.data

        except Exception as e:

            st.error(f"Error fetching members: {e}")

            members = []

        if members:

            member_dict = {f"{m['name']} ({m['id']})": m for m in members}

            selected_label = st.selectbox("Select a member to update", list(member_dict.keys()))

            selected_member = member_dict[selected_label]

            with st.form("update_member_form"):

                name = st.text_input("Name", value=selected_member["name"])

                designation = st.text_input("Designation", value=selected_member.get("designation", ""))

                facebookUrl = st.text_input("Facebook URL", value=selected_member.get("facebookUrl", ""))

                linkedinUrl = st.text_input("LinkedIn URL", value=selected_member.get("linkedinUrl", ""))

                imageUrl = st.text_input("Image URL", value=selected_member.get("imageUrl", ""))

                status = st.selectbox("Status", options=["current", "alumni"],
                                      index=["current", "alumni"].index(selected_member["status"]))

                panel = st.selectbox("Panel", options=[

                    "executive_member",

                    "sub_executive",

                    "executive",

                    "general_member",

                    "advisory"

                ], index=[

                    "executive_member",

                    "sub_executive",

                    "executive",

                    "general_member",

                    "advisory"

                ].index(selected_member["panel"]))

                submitted = st.form_submit_button("Update Member")

            if submitted:

                updated_data = {

                    "name": name,

                    "designation": designation,

                    "facebookUrl": facebookUrl,

                    "linkedinUrl": linkedinUrl,

                    "imageUrl": imageUrl,

                    "status": status,

                    "panel": panel,

                }

                try:

                    supabase.table("Member").update(updated_data).eq("id", selected_member["id"]).execute()

                    st.success("Member updated successfully!")

                except Exception as e:

                    st.error(f"Failed to update member: {e}")

        else:

            st.info("No members found in the database.")




    elif sub_section == "Delete Member":

        st.title("Delete Member")

        # Fetch all members

        try:

            response = supabase.table("Member").select("id, name, designation").execute()

            members = response.data

        except Exception as e:

            st.error(f"Error fetching members: {e}")

            members = []

        if members:

            search_term = st.text_input("Search by name")

            filtered_members = [m for m in members if
                                search_term.lower() in m["name"].lower()] if search_term else members

            if filtered_members:

                st.write("Select members to delete:")

                selected_ids = []

                for member in filtered_members:

                    label = f"{member['name']} - {member.get('designation', '')} ({member['id']})"

                    if st.checkbox(label, key=f"delete_{member['id']}"):
                        selected_ids.append(member["id"])

                if selected_ids:

                    if st.button("Delete Selected"):

                        try:

                            for mid in selected_ids:
                                supabase.table("Member").delete().eq("id", mid).execute()

                            st.success(f"Deleted {len(selected_ids)} member(s) successfully!")

                            st.rerun()


                        except Exception as e:

                            st.error(f"Failed to delete members: {e}")

                else:

                    st.warning("Select at least one member to delete.")

            else:

                st.info("No members matched your search.")

        else:

            st.info("No members found in the database.")


# === Manage Job Section ===
elif main_section == "Manage Job":
    st.title("Manage Job")
    st.info("Job management functionality coming soon...")
