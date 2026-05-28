import streamlit as st

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Ma TodoList")

new_task = st.text_input("Nouvelle tâche")
if st.button("Ajouter"):
    if new_task.strip() != "":
        st.session_state["tasks"].append({"task": new_task, "done": False})

total = len(st.session_state["tasks"])
faites = sum(1 for t in st.session_state["tasks"] if t["done"])
if total > 0:
    st.caption(f"{faites}/{total} tâches terminées")

st.divider()

if total == 0:
    st.write("Aucune tâche pour l'instant.")

for i, t in enumerate(st.session_state["tasks"]):
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        if t["done"]:
            st.markdown(f"~~{t['task']}~~")
        else:
            st.write(t["task"])
    with col2:
        if not t["done"]:
            if st.button("Fait", key=f"done_{i}"):
                st.session_state["tasks"][i]["done"] = True
                st.rerun()
