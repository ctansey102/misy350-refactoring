import streamlit as st
from assignment_manager_oop.assignment_manager import AssignmentManager
from assignment_manager_oop.assignment_store import AssignmentStore

class AssignmentDashboard:
    def __init__(self, manger: 'AssignmentManager',
                 store: "AssignmentStore") -> None:
        self.manager = manger
        self.store = store
        

    def main(self):
        if st.session_state["page"] == "dashboard":
            self.show_manage_assignments()

    def show_manage_assignments(self):
        assignments = self.manager.all()
        for assignment in assignments:
            st.write(f"Title: {assignment['title']}")

        if st.button("Add New Assignment"):
            st.session_state['page']

    def show_add_new_assignment(self):
        pass