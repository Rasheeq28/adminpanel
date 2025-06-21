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
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Sidebar navigation
# st.sidebar.title("Navigation")
# main_section = st.sidebar.radio("Go to", ["Manage Member", "Manage Job"])
#
# # === Manage Member Section ===
# if main_section == "Manage Member":
#     sub_section = st.sidebar.radio("Member Options", ["Add Member", "Update Member", "Delete Member"])
#
#     if sub_section == "Add Member":
#         st.title("Add New Member")
#
#         mode = st.radio("Choose input method:", ("Manual Entry", "Upload CSV"))
#
#         if mode == "Manual Entry":
#             with st.form("member_form"):
#                 name = st.text_input("Name")
#                 designation = st.text_input("Designation")
#                 facebookUrl = st.text_input("Facebook URL")
#                 linkedinUrl = st.text_input("LinkedIn URL")
#                 imageUrl = st.text_input("Image URL")
#
#                 status = st.selectbox("Status", options=["current", "alumni"])
#                 panel = st.selectbox("Panel", options=[
#                     "executive_member",
#                     "sub_executive",
#                     "executive",
#                     "general_member",
#                     "advisory"
#                 ])
#
#                 submitted = st.form_submit_button("Add Member")
#
#             if submitted:
#                 if not name or not panel:
#                     st.error("Name and panel are required.")
#                 else:
#                     data = {
#                         "name": name,
#                         "designation": designation,
#                         "facebookUrl": facebookUrl,
#                         "linkedinUrl": linkedinUrl,
#                         "imageUrl": imageUrl,
#                         "status": status,
#                         "panel": panel,
#                     }
#
#                     try:
#                         supabase.table("Member").insert(data).execute()
#                         st.success("Member added successfully!")
#                     except Exception as e:
#                         st.error(f"Failed to add member: {e}")
#
#         elif mode == "Upload CSV":
#             uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
#             if uploaded_file is not None:
#                 try:
#                     df = pd.read_csv(uploaded_file)
#
#                     required_cols = ["name","designation","facebookUrl","linkedinUrl","imageUrl","status","panel"]
#                     missing_cols = [col for col in required_cols if col not in df.columns]
#                     if missing_cols:
#                         st.error(f"Missing columns in CSV: {missing_cols}")
#                     else:
#                         if st.button("Insert all members from CSV"):
#                             records = df.to_dict(orient="records")
#                             try:
#                                 supabase.table("Member").insert(records).execute()
#                                 st.success(f"Inserted {len(records)} members successfully!")
#                             except Exception as e:
#                                 st.error(f"Failed to insert members: {e}")
#                 except Exception as e:
#                     st.error(f"Error reading CSV file: {e}")
#
#
#     elif sub_section == "Update Member":
#
#         st.title("Update Member")
#
#         # Fetch all members
#
#         try:
#
#             response = supabase.table("Member").select("*").execute()
#
#             members = response.data
#
#         except Exception as e:
#
#             st.error(f"Error fetching members: {e}")
#
#             members = []
#
#         if members:
#
#             member_dict = {f"{m['name']} ({m['id']})": m for m in members}
#
#             selected_label = st.selectbox("Select a member to update", list(member_dict.keys()))
#
#             selected_member = member_dict[selected_label]
#
#             with st.form("update_member_form"):
#
#                 name = st.text_input("Name", value=selected_member["name"])
#
#                 designation = st.text_input("Designation", value=selected_member.get("designation", ""))
#
#                 facebookUrl = st.text_input("Facebook URL", value=selected_member.get("facebookUrl", ""))
#
#                 linkedinUrl = st.text_input("LinkedIn URL", value=selected_member.get("linkedinUrl", ""))
#
#                 imageUrl = st.text_input("Image URL", value=selected_member.get("imageUrl", ""))
#
#                 status = st.selectbox("Status", options=["current", "alumni"],
#                                       index=["current", "alumni"].index(selected_member["status"]))
#
#                 panel = st.selectbox("Panel", options=[
#
#                     "executive_member",
#
#                     "sub_executive",
#
#                     "executive",
#
#                     "general_member",
#
#                     "advisory"
#
#                 ], index=[
#
#                     "executive_member",
#
#                     "sub_executive",
#
#                     "executive",
#
#                     "general_member",
#
#                     "advisory"
#
#                 ].index(selected_member["panel"]))
#
#                 submitted = st.form_submit_button("Update Member")
#
#             if submitted:
#
#                 updated_data = {
#
#                     "name": name,
#
#                     "designation": designation,
#
#                     "facebookUrl": facebookUrl,
#
#                     "linkedinUrl": linkedinUrl,
#
#                     "imageUrl": imageUrl,
#
#                     "status": status,
#
#                     "panel": panel,
#
#                 }
#
#                 try:
#
#                     supabase.table("Member").update(updated_data).eq("id", selected_member["id"]).execute()
#
#                     st.success("Member updated successfully!")
#
#                 except Exception as e:
#
#                     st.error(f"Failed to update member: {e}")
#
#         else:
#
#             st.info("No members found in the database.")
#
#
#
#
#
#
#     elif sub_section == "Delete Member":
#
#         st.title("Delete Member")
#
#         # Fetch all members
#
#         try:
#
#             response = supabase.table("Member").select("id, name, designation, status, panel").execute()
#
#             members = response.data
#
#         except Exception as e:
#
#             st.error(f"Error fetching members: {e}")
#
#             members = []
#
#         if members:
#
#             # Map labels to IDs and full member info
#
#             member_map = {
#
#                 f"{m['name']} - {m.get('designation', '')} ({m['id']})": m
#
#                 for m in members
#
#             }
#
#             selected_labels = st.multiselect(
#
#                 "Search and select member(s) to delete:",
#
#                 options=list(member_map.keys()),
#
#                 help="Type a name to filter and select multiple members"
#
#             )
#
#             selected_members = [member_map[label] for label in selected_labels]
#
#             if selected_members:
#
#                 st.write("### Preview Selected Members:")
#
#                 st.dataframe(pd.DataFrame(selected_members))
#
#                 confirm = st.checkbox("I confirm I want to delete the selected member(s)")
#
#                 if confirm:
#
#                     if st.button("Delete Selected Members"):
#
#                         try:
#
#                             for member in selected_members:
#                                 supabase.table("Member").delete().eq("id", member["id"]).execute()
#
#                             st.success(f"Deleted {len(selected_members)} member(s) successfully!")
#
#                             st.rerun()
#
#                         except Exception as e:
#
#                             st.error(f"Failed to delete members: {e}")
#
#             else:
#
#                 st.warning("Select at least one member to delete.")
#
#         else:
#
#             st.info("No members found in the database.")
#
# # === Manage Job Section ===
# elif main_section == "Manage Job":
#     st.title("Manage Job")
#     st.info("Job management functionality coming soon...")


# promotion button
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Initialize Supabase client
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Sidebar navigation
# st.sidebar.title("Navigation")
# main_section = st.sidebar.radio("Go to", ["Manage Member", "Manage Job"])
#
# # === Manage Member Section ===
# if main_section == "Manage Member":
#     sub_section = st.sidebar.radio("Member Options", [
#         "Add Member", "Update Member", "Delete Member", "Promote Member"
#     ])
#
#     # --- ADD MEMBER ---
#     if sub_section == "Add Member":
#         st.title("Add New Member")
#         mode = st.radio("Choose input method:", ("Manual Entry", "Upload CSV"))
#
#         if mode == "Manual Entry":
#             with st.form("member_form"):
#                 name = st.text_input("Name")
#                 designation = st.text_input("Designation")
#                 facebookUrl = st.text_input("Facebook URL")
#                 linkedinUrl = st.text_input("LinkedIn URL")
#                 imageUrl = st.text_input("Image URL")
#                 status = st.selectbox("Status", ["current", "alumni"])
#                 panel = st.selectbox("Panel", [
#                     "executive_member", "sub_executive", "executive",
#                     "general_member", "advisory"
#                 ])
#                 submitted = st.form_submit_button("Add Member")
#
#             if submitted:
#                 if not name or not panel:
#                     st.error("Name and panel are required.")
#                 else:
#                     data = {
#                         "name": name,
#                         "designation": designation,
#                         "facebookUrl": facebookUrl,
#                         "linkedinUrl": linkedinUrl,
#                         "imageUrl": imageUrl,
#                         "status": status,
#                         "panel": panel,
#                     }
#                     try:
#                         supabase.table("Member").insert(data).execute()
#                         st.success("Member added successfully!")
#                     except Exception as e:
#                         st.error(f"Failed to add member: {e}")
#
#         elif mode == "Upload CSV":
#             uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
#             if uploaded_file:
#                 try:
#                     df = pd.read_csv(uploaded_file)
#                     required_cols = ["name", "designation", "facebookUrl", "linkedinUrl", "imageUrl", "status", "panel"]
#                     if not all(col in df.columns for col in required_cols):
#                         st.error("Missing required columns.")
#                     elif st.button("Insert all members from CSV"):
#                         supabase.table("Member").insert(df.to_dict("records")).execute()
#                         st.success(f"Inserted {len(df)} members.")
#                 except Exception as e:
#                     st.error(f"Error reading CSV: {e}")
#
#     # --- UPDATE MEMBER ---
#     elif sub_section == "Update Member":
#         st.title("Update Member")
#         try:
#             members = supabase.table("Member").select("*").execute().data
#         except Exception as e:
#             st.error(f"Error fetching members: {e}")
#             members = []
#
#         if members:
#             member_dict = {f"{m['name']} ({m['id']})": m for m in members}
#             selected_label = st.selectbox("Select a member to update", list(member_dict))
#             selected_member = member_dict[selected_label]
#
#             with st.form("update_member_form"):
#                 name = st.text_input("Name", selected_member["name"])
#                 designation = st.text_input("Designation", selected_member.get("designation", ""))
#                 facebookUrl = st.text_input("Facebook URL", selected_member.get("facebookUrl", ""))
#                 linkedinUrl = st.text_input("LinkedIn URL", selected_member.get("linkedinUrl", ""))
#                 imageUrl = st.text_input("Image URL", selected_member.get("imageUrl", ""))
#                 status = st.selectbox("Status", ["current", "alumni"], index=["current", "alumni"].index(selected_member["status"]))
#                 panel = st.selectbox("Panel", [
#                     "executive_member", "sub_executive", "executive", "general_member", "advisory"
#                 ], index=[
#                     "executive_member", "sub_executive", "executive", "general_member", "advisory"
#                 ].index(selected_member["panel"]))
#                 submitted = st.form_submit_button("Update Member")
#
#             if submitted:
#                 updated_data = {
#                     "name": name,
#                     "designation": designation,
#                     "facebookUrl": facebookUrl,
#                     "linkedinUrl": linkedinUrl,
#                     "imageUrl": imageUrl,
#                     "status": status,
#                     "panel": panel,
#                 }
#                 try:
#                     supabase.table("Member").update(updated_data).eq("id", selected_member["id"]).execute()
#                     st.success("Member updated successfully!")
#                 except Exception as e:
#                     st.error(f"Failed to update member: {e}")
#         else:
#             st.info("No members found.")
#
#     # --- DELETE MEMBER ---
#     elif sub_section == "Delete Member":
#         st.title("Delete Member")
#         try:
#             members = supabase.table("Member").select("id, name, designation, status, panel").execute().data
#         except Exception as e:
#             st.error(f"Error fetching members: {e}")
#             members = []
#
#         if members:
#             member_map = {f"{m['name']} - {m.get('designation', '')} ({m['id']})": m for m in members}
#             selected_labels = st.multiselect("Search and select member(s) to delete:", list(member_map))
#             selected_members = [member_map[label] for label in selected_labels]
#
#             if selected_members:
#                 st.write("### Preview Selected Members:")
#                 st.dataframe(pd.DataFrame(selected_members))
#                 confirm = st.checkbox("I confirm I want to delete the selected member(s)")
#
#                 if confirm and st.button("Delete Selected Members"):
#                     try:
#                         for member in selected_members:
#                             supabase.table("Member").delete().eq("id", member["id"]).execute()
#                         st.success(f"Deleted {len(selected_members)} member(s)!")
#                         st.rerun()
#                     except Exception as e:
#                         st.error(f"Failed to delete: {e}")
#             else:
#                 st.warning("Select at least one member to delete.")
#         else:
#             st.info("No members found.")
#
#     # --- PROMOTE MEMBER ---
#     elif sub_section == "Promote Member":
#         st.title("Promote Member")
#         try:
#             members = supabase.table("Member").select("id, name, panel, designation").execute().data
#         except Exception as e:
#             st.error(f"Error fetching members: {e}")
#             members = []
#
#         if members:
#             label_to_member = {
#                 f"{m['name']} - {m['panel']} ({m['id']})": m for m in members
#             }
#             selected_labels = st.multiselect("Select members to promote:", list(label_to_member))
#             selected_members = [label_to_member[label] for label in selected_labels]
#
#             if selected_members:
#                 updated_members = []
#
#                 for member in selected_members:
#                     current_panel = member["panel"]
#                     next_panel = None
#                     needs_designation = False
#
#                     if current_panel == "general_member":
#                         next_panel = "executive_member"
#                     elif current_panel == "executive_member":
#                         next_panel = "sub_executive"
#                         needs_designation = True
#                     elif current_panel == "sub_executive":
#                         next_panel = "executive"
#                         needs_designation = True
#
#                     if next_panel:
#                         st.markdown(f"**{member['name']}**: `{current_panel}` ➝ `{next_panel}`")
#                         designation = ""
#                         if needs_designation:
#                             designation = st.text_input(f"New Designation for {member['name']}:", key=member["id"])
#                             if not designation.strip():
#                                 st.warning(f"Designation required for {member['name']}")
#                                 continue
#                         updated_members.append({
#                             "id": member["id"],
#                             "panel": next_panel,
#                             "designation": designation if needs_designation else None
#                         })
#                     else:
#                         st.info(f"{member['name']} is already at the top or unpromotable.")
#
#                 if updated_members and st.button("Promote Selected"):
#                     try:
#                         for m in updated_members:
#                             update_data = {"panel": m["panel"]}
#                             if m["designation"] is not None:
#                                 update_data["designation"] = m["designation"]
#                             supabase.table("Member").update(update_data).eq("id", m["id"]).execute()
#                         st.success(f"Promoted {len(updated_members)} member(s) successfully!")
#                         st.rerun()
#                     except Exception as e:
#                         st.error(f"Failed to promote: {e}")
#             else:
#                 st.info("No members selected.")
#         else:
#             st.info("No members found.")
#
# # === Manage Job Section ===
# elif main_section == "Manage Job":
#     st.title("Manage Job")
#     st.info("Job management functionality coming soon...")


# job section
import streamlit as st
import pandas as pd
from supabase import create_client, Client
from datetime import datetime

# Initialize Supabase client
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sidebar navigation
st.sidebar.title("Navigation")
main_section = st.sidebar.radio("Go to", ["Manage Member", "Manage Job"])

# === Manage Member Section ===
if main_section == "Manage Member":
    sub_section = st.sidebar.radio("Member Options", [
        "Add Member", "Update Member", "Delete Member", "Promote Member"
    ])

    # --- ADD MEMBER ---
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
                status = st.selectbox("Status", ["current", "alumni"])
                panel = st.selectbox("Panel", [
                    "executive_member", "sub_executive", "executive",
                    "general_member", "advisory"
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
            if uploaded_file:
                try:
                    df = pd.read_csv(uploaded_file)
                    required_cols = ["name", "designation", "facebookUrl", "linkedinUrl", "imageUrl", "status", "panel"]
                    if not all(col in df.columns for col in required_cols):
                        st.error("Missing required columns.")
                    elif st.button("Insert all members from CSV"):
                        supabase.table("Member").insert(df.to_dict("records")).execute()
                        st.success(f"Inserted {len(df)} members.")
                except Exception as e:
                    st.error(f"Error reading CSV: {e}")

    # --- UPDATE MEMBER ---
    elif sub_section == "Update Member":
        st.title("Update Member")
        try:
            members = supabase.table("Member").select("*").execute().data
        except Exception as e:
            st.error(f"Error fetching members: {e}")
            members = []

        if members:
            member_dict = {f"{m['name']} ({m['id']})": m for m in members}
            selected_label = st.selectbox("Select a member to update", list(member_dict))
            selected_member = member_dict[selected_label]

            with st.form("update_member_form"):
                name = st.text_input("Name", selected_member["name"])
                designation = st.text_input("Designation", selected_member.get("designation", ""))
                facebookUrl = st.text_input("Facebook URL", selected_member.get("facebookUrl", ""))
                linkedinUrl = st.text_input("LinkedIn URL", selected_member.get("linkedinUrl", ""))
                imageUrl = st.text_input("Image URL", selected_member.get("imageUrl", ""))
                status = st.selectbox("Status", ["current", "alumni"], index=["current", "alumni"].index(selected_member["status"]))
                panel = st.selectbox("Panel", [
                    "executive_member", "sub_executive", "executive", "general_member", "advisory"
                ], index=[
                    "executive_member", "sub_executive", "executive", "general_member", "advisory"
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
            st.info("No members found.")

    # --- DELETE MEMBER ---
    elif sub_section == "Delete Member":
        st.title("Delete Member")
        try:
            members = supabase.table("Member").select("id, name, designation, status, panel").execute().data
        except Exception as e:
            st.error(f"Error fetching members: {e}")
            members = []

        if members:
            member_map = {f"{m['name']} - {m.get('designation', '')} ({m['id']})": m for m in members}
            selected_labels = st.multiselect("Search and select member(s) to delete:", list(member_map))
            selected_members = [member_map[label] for label in selected_labels]

            if selected_members:
                st.write("### Preview Selected Members:")
                st.dataframe(pd.DataFrame(selected_members))
                confirm = st.checkbox("I confirm I want to delete the selected member(s)")

                if confirm and st.button("Delete Selected Members"):
                    try:
                        for member in selected_members:
                            supabase.table("Member").delete().eq("id", member["id"]).execute()
                        st.success(f"Deleted {len(selected_members)} member(s)!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed to delete: {e}")
            else:
                st.warning("Select at least one member to delete.")
        else:
            st.info("No members found.")

    # --- PROMOTE MEMBER ---
    elif sub_section == "Promote Member":
        st.title("Promote Member")
        try:
            members = supabase.table("Member").select("id, name, panel, designation").execute().data
        except Exception as e:
            st.error(f"Error fetching members: {e}")
            members = []

        if members:
            label_to_member = {
                f"{m['name']} - {m['panel']} ({m['id']})": m for m in members
            }
            selected_labels = st.multiselect("Select members to promote:", list(label_to_member))
            selected_members = [label_to_member[label] for label in selected_labels]

            if selected_members:
                updated_members = []

                for member in selected_members:
                    current_panel = member["panel"]
                    next_panel = None
                    needs_designation = False

                    if current_panel == "general_member":
                        next_panel = "executive_member"
                    elif current_panel == "executive_member":
                        next_panel = "sub_executive"
                        needs_designation = True
                    elif current_panel == "sub_executive":
                        next_panel = "executive"
                        needs_designation = True

                    if next_panel:
                        st.markdown(f"**{member['name']}**: `{current_panel}` ➝ `{next_panel}`")
                        designation = ""
                        if needs_designation:
                            designation = st.text_input(f"New Designation for {member['name']}:", key=member["id"])
                            if not designation.strip():
                                st.warning(f"Designation required for {member['name']}")
                                continue
                        updated_members.append({
                            "id": member["id"],
                            "panel": next_panel,
                            "designation": designation if needs_designation else None
                        })
                    else:
                        st.info(f"{member['name']} is already at the top or unpromotable.")

                if updated_members and st.button("Promote Selected"):
                    try:
                        for m in updated_members:
                            update_data = {"panel": m["panel"]}
                            if m["designation"] is not None:
                                update_data["designation"] = m["designation"]
                            supabase.table("Member").update(update_data).eq("id", m["id"]).execute()
                        st.success(f"Promoted {len(updated_members)} member(s) successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed to promote: {e}")
            else:
                st.info("No members selected.")
        else:
            st.info("No members found.")

# === Manage Job Section ===
# elif main_section == "Manage Job":
#     st.sidebar.subheader("Job Options")
#     job_action = st.sidebar.radio("Select Action", ["Add Job", "Update Job", "Delete Job"])
#
#     # --- ADD JOB ---
#     JOB_TYPES = ["contract", "full_time", "internship", "part_time"]
#     WORK_MODES = ["remote", "onsite", "hybrid"]  # WorkMode enum values
#
#     # --- ADD JOB ---
#     if job_action == "Add Job":
#         st.title("Add New Job")
#         mode = st.radio("Choose input method:", ["Manual Entry", "Upload CSV"])
#
#         JOB_TYPES = ["contract", "full_time", "internship", "part_time"]
#         WORK_MODES = ["remote", "onsite", "hybrid"]
#
#         if mode == "Manual Entry":
#             with st.form("add_job_form"):
#                 company = st.text_input("Company")
#                 position = st.text_input("Position")
#                 location = st.text_input("Location")
#                 type_ = st.selectbox("Type", JOB_TYPES)
#                 salary = st.text_input("Salary")
#                 workMode = st.selectbox("Work Mode", WORK_MODES)
#                 vacancy = st.number_input("Vacancy", step=1, min_value=1)
#
#                 recruiterMail = st.text_input("Recruiter Email")
#                 recruitingUrl = st.text_input("Recruiting URL")
#                 companyImage = st.text_input("Company Image URL")
#
#                 description = st.text_area("Description")
#                 responsibilities = st.text_area("Responsibilities")
#                 requirements = st.text_area("Requirements")
#                 skills = st.text_area("Skills")
#
#                 submitted = st.form_submit_button("Add Job")
#
#             if submitted:
#                 job_data = {
#                     "company": company,
#                     "position": position,
#                     "location": location,
#                     "type": type_,
#                     "salary": salary,
#                     "workMode": workMode,
#                     "vacancy": vacancy,
#                     "recruiterMail": recruiterMail,
#                     "recruitingUrl": recruitingUrl,
#                     "companyImage": companyImage,
#                     "description": description,
#                     "responsibilities": responsibilities,
#                     "requirements": requirements,
#                     "skills": skills,
#                     "Timestamp": datetime.utcnow().isoformat()
#                 }
#                 try:
#                     supabase.table("Job").insert(job_data).execute()
#                     st.success("✅ Job added successfully!")
#                 except Exception as e:
#                     st.error(f"❌ Error inserting job: {e}")
#
#
#     elif job_action == "Delete Job":
#         st.title("Delete Job Postings")
#     try:
#         jobs = supabase.table("Job").select("id, company, position, type, workMode").execute().data
#     except Exception as e:
#         st.error(f"❌ Error fetching job listings: {e}")
#         jobs = []
#
#     if jobs:
#         df_jobs = pd.DataFrame(jobs)
#         df_jobs["search_label"] = df_jobs.apply(
#             lambda row: f"{row['company']} - {row['position']} ({row['id']})", axis=1
#         )
#         job_map = {label: row for label, row in zip(df_jobs["search_label"], jobs)}
#
#         # Searchable dropdown
#         selected_labels = st.multiselect(
#             "🔍 Search and select job(s) to delete:",
#             options=list(job_map.keys())
#         )
#
#         selected_jobs = [job_map[label] for label in selected_labels]
#
#         if selected_jobs:
#             st.markdown("### 🔎 Preview Selected Jobs")
#             st.dataframe(pd.DataFrame(selected_jobs))
#
#             confirm = st.checkbox("✅ I confirm I want to delete the selected job(s)")
#
#             if confirm and st.button("🗑️ Delete Selected Jobs"):
#                 try:
#                     for job in selected_jobs:
#                         supabase.table("Job").delete().eq("id", job["id"]).execute()
#                     st.success(f"✅ Deleted {len(selected_jobs)} job(s) successfully!")
#                     st.rerun()
#                 except Exception as e:
#                     st.error(f"❌ Failed to delete job(s): {e}")
#         else:
#             st.info("⚠️ No job selected yet.")
#     else:
#         st.info("ℹ️ No job postings found.")



# # --- UPDATE JOB ---
    # elif job_action == "Update Job":
    #     st.title("Update Job")
    #
    #     try:
    #         jobs = supabase.table("Job").select("*").execute().data
    #     except Exception as e:
    #         st.error(f"Failed to fetch jobs: {e}")
    #         jobs = []
    #
    #     if jobs:
    #         job_map = {f"{j['position']} at {j['company']} ({j['id']})": j for j in jobs}
    #         selected = st.selectbox("Select Job to Update", list(job_map))
    #         job = job_map[selected]
    #
    #         with st.form("update_job_form"):
    #             company = st.text_input("Company", value=job["company"])
    #             position = st.text_input("Position", value=job["position"])
    #             location = st.text_input("Location", value=job["location"])
    #             type_index = JOB_TYPES.index(job["type"]) if job["type"] in JOB_TYPES else 0
    #             type_ = st.selectbox("Type", JOB_TYPES, index=type_index)
    #             salary = st.text_input("Salary", value=job["salary"])
    #             workMode = st.selectbox("Work Mode", ["remote", "onsite", "hybrid"],
    #                                     index=["remote", "onsite", "hybrid"].index(job["workMode"]))
    #             vacancy = st.number_input("Vacancy", value=job["vacancy"], step=1)
    #
    #             recruiterMail = st.text_input("Recruiter Email", value=job["recruiterMail"])
    #             recruitingUrl = st.text_input("Recruiting URL", value=job["recruitingUrl"])
    #             companyImage = st.text_input("Company Image URL", value=job["companyImage"])
    #
    #             description = st.text_area("Description", value=job["description"])
    #             responsibilities = st.text_area("Responsibilities", value=job["responsibilities"])
    #             requirements = st.text_area("Requirements", value=job["requirements"])
    #             skills = st.text_area("Skills", value=job["skills"])
    #
    #             submitted = st.form_submit_button("Update Job")
    #
    #         if submitted:
    #             job_data = {
    #                 "company": company,
    #                 "position": position,
    #                 "location": location,
    #                 "type": type_,
    #                 "salary": salary,
    #                 "workMode": workMode,
    #                 "vacancy": vacancy,
    #                 "recruiterMail": recruiterMail,
    #                 "recruitingUrl": recruitingUrl,
    #                 "companyImage": companyImage,
    #                 "description": description,
    #                 "responsibilities": responsibilities,
    #                 "requirements": requirements,
    #                 "skills": skills
    #             }
    #             try:
    #                 supabase.table("Job").update(job_data).eq("id", job["id"]).execute()
    #                 st.success("Job updated successfully!")
    #             except Exception as e:
    #                 st.error(f"Error updating job: {e}")
    #
    # # --- DELETE JOB ---
    # elif job_action == "Delete Job":
    #     st.title("Delete Job")
    #     try:
    #         jobs = supabase.table("Job").select("id, company, position").execute().data
    #     except Exception as e:
    #         st.error(f"Failed to fetch jobs: {e}")
    #         jobs = []
    #
    #     if jobs:
    #         job_map = {f"{j['position']} at {j['company']} ({j['id']})": j for j in jobs}
    #         selected_jobs = st.multiselect("Select Job(s) to Delete", list(job_map))
    #
    #         if selected_jobs:
    #             preview_jobs = [job_map[label] for label in selected_jobs]
    #             st.write("### Preview:")
    #             st.dataframe(pd.DataFrame(preview_jobs))
    #             confirm = st.checkbox("I confirm I want to delete the selected job(s)")
    #
    #             if confirm and st.button("Delete Selected Job(s)"):
    #                 try:
    #                     for j in preview_jobs:
    #                         supabase.table("Job").delete().eq("id", j["id"]).execute()
    #                     st.success(f"Deleted {len(preview_jobs)} job(s).")
    #                     st.rerun()
    #                 except Exception as e:
    #                     st.error(f"Failed to delete: {e}")
    #     else:
    #         st.info("No jobs found.")
    elif main_section == "Manage Job":
        st.sidebar.subheader("Job Options")
        job_action = st.sidebar.radio("Select Action", ["Add Job", "Update Job", "Delete Job"])

        JOB_TYPES = ["contract", "full_time", "internship", "part_time"]
        WORK_MODES = ["remote", "onsite", "hybrid"]

        # --- ADD JOB ---
        if job_action == "Add Job":
            st.title("Add New Job")
            mode = st.radio("Choose input method:", ["Manual Entry", "Upload CSV"])

            if mode == "Manual Entry":
                with st.form("add_job_form"):
                    company = st.text_input("Company")
                    position = st.text_input("Position")
                    location = st.text_input("Location")
                    type_ = st.selectbox("Type", JOB_TYPES)
                    salary = st.text_input("Salary")
                    workMode = st.selectbox("Work Mode", WORK_MODES)
                    vacancy = st.number_input("Vacancy", step=1, min_value=1)

                    recruiterMail = st.text_input("Recruiter Email")
                    recruitingUrl = st.text_input("Recruiting URL")
                    companyImage = st.text_input("Company Image URL")

                    description = st.text_area("Description")
                    responsibilities = st.text_area("Responsibilities")
                    requirements = st.text_area("Requirements")
                    skills = st.text_area("Skills")

                    submitted = st.form_submit_button("Add Job")

                if submitted:
                    job_data = {
                        "company": company,
                        "position": position,
                        "location": location,
                        "type": type_,
                        "salary": salary,
                        "workMode": workMode,
                        "vacancy": vacancy,
                        "recruiterMail": recruiterMail,
                        "recruitingUrl": recruitingUrl,
                        "companyImage": companyImage,
                        "description": description,
                        "responsibilities": responsibilities,
                        "requirements": requirements,
                        "skills": skills,
                        "Timestamp": datetime.utcnow().isoformat()
                    }
                    try:
                        supabase.table("Job").insert(job_data).execute()
                        st.success("✅ Job added successfully!")
                    except Exception as e:
                        st.error(f"❌ Error inserting job: {e}")

            elif mode == "Upload CSV":
                uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
                if uploaded_file:
                    try:
                        df = pd.read_csv(uploaded_file)
                        if "Timestamp" not in df.columns:
                            df["Timestamp"] = datetime.utcnow().isoformat()

                        supabase.table("Job").insert(df.to_dict("records")).execute()
                        st.success(f"✅ Inserted {len(df)} jobs from CSV!")
                    except Exception as e:
                        st.error(f"❌ Error processing CSV: {e}")

        # --- UPDATE JOB ---
        elif job_action == "Update Job":
            st.title("Update Existing Job")
            try:
                jobs = supabase.table("Job").select("*").execute().data
            except Exception as e:
                st.error(f"❌ Error fetching job listings: {e}")
                jobs = []

            if jobs:
                job_map = {
                    f"{j['company']} - {j['position']} ({j['id']})": j for j in jobs
                }
                selected_label = st.selectbox("🔍 Select a job to update:", list(job_map))
                selected_job = job_map[selected_label]

                with st.form("update_job_form"):
                    company = st.text_input("Company", selected_job["company"])
                    position = st.text_input("Position", selected_job["position"])
                    location = st.text_input("Location", selected_job["location"])
                    type_ = st.selectbox("Type", JOB_TYPES, index=JOB_TYPES.index(selected_job["type"]))
                    salary = st.text_input("Salary", selected_job["salary"])
                    workMode = st.selectbox("Work Mode", WORK_MODES, index=WORK_MODES.index(selected_job["workMode"]))
                    vacancy = st.number_input("Vacancy", step=1, min_value=1, value=selected_job["vacancy"])

                    recruiterMail = st.text_input("Recruiter Email", selected_job["recruiterMail"])
                    recruitingUrl = st.text_input("Recruiting URL", selected_job["recruitingUrl"])
                    companyImage = st.text_input("Company Image URL", selected_job["companyImage"])

                    description = st.text_area("Description", selected_job["description"])
                    responsibilities = st.text_area("Responsibilities", selected_job["responsibilities"])
                    requirements = st.text_area("Requirements", selected_job["requirements"])
                    skills = st.text_area("Skills", selected_job["skills"])

                    submitted = st.form_submit_button("Update Job")

                if submitted:
                    updated_data = {
                        "company": company,
                        "position": position,
                        "location": location,
                        "type": type_,
                        "salary": salary,
                        "workMode": workMode,
                        "vacancy": vacancy,
                        "recruiterMail": recruiterMail,
                        "recruitingUrl": recruitingUrl,
                        "companyImage": companyImage,
                        "description": description,
                        "responsibilities": responsibilities,
                        "requirements": requirements,
                        "skills": skills
                    }
                    try:
                        supabase.table("Job").update(updated_data).eq("id", selected_job["id"]).execute()
                        st.success("✅ Job updated successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Failed to update job: {e}")
            else:
                st.info("ℹ️ No job postings available to update.")

        # --- DELETE JOB ---
        elif job_action == "Delete Job":
            st.title("Delete Job Postings")
            try:
                jobs = supabase.table("Job").select("id, company, position, type, workMode").execute().data
            except Exception as e:
                st.error(f"❌ Error fetching job listings: {e}")
                jobs = []

            if jobs:
                df_jobs = pd.DataFrame(jobs)
                df_jobs["search_label"] = df_jobs.apply(
                    lambda row: f"{row['company']} - {row['position']} ({row['id']})", axis=1
                )
                job_map = {label: row for label, row in zip(df_jobs["search_label"], jobs)}

                selected_labels = st.multiselect(
                    "🔍 Search and select job(s) to delete:",
                    options=list(job_map.keys())
                )

                selected_jobs = [job_map[label] for label in selected_labels]

                if selected_jobs:
                    st.markdown("### 🔎 Preview Selected Jobs")
                    st.dataframe(pd.DataFrame(selected_jobs))

                    confirm = st.checkbox("✅ I confirm I want to delete the selected job(s)")

                    if confirm and st.button("🗑️ Delete Selected Jobs"):
                        try:
                            for job in selected_jobs:
                                supabase.table("Job").delete().eq("id", job["id"]).execute()
                            st.success(f"✅ Deleted {len(selected_jobs)} job(s) successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Failed to delete job(s): {e}")
                else:
                    st.info("⚠️ No job selected yet.")
            else:
                st.info("ℹ️ No job postings found.")
