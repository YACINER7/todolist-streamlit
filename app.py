import logging
import streamlit as st
from todolist_utils import add_task, remove_task

logging.basicConfig(level=logging.INFO)

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Ma TodoList")

new_task = st.text_input("Ajouter une tâche", placeholder="Ex: Apprendre Streamlit...")
due_date = st.date_input("Échéance")

if st.button("Ajouter", type="primary"):
    if not add_task(st.session_state["tasks"], new_task.strip(), str(due_date)):
        st.error("La tâche est vide ou existe déjà.")
    else:
        st.rerun()

st.subheader("Liste des tâches")

if not st.session_state["tasks"]:
    st.info("Aucune tâche pour le moment. Ajoutez-en une !")
else:
    for i, t in enumerate(st.session_state["tasks"]):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        with col1:
            if t["done"]:
                st.markdown(f"~~✅ {t['task']}~~")
            else:
                st.markdown(f"⏳ **{t['task']}**")
        with col2:
            if not t["done"]:
                if st.button("Fait", key=f"done_{i}"):
                    print("Avant :", st.session_state["tasks"][i])
                    st.session_state["tasks"][i]["done"] = True
                    print("Après :", st.session_state["tasks"][i])
                    st.rerun()
            else:
                if st.button("Restaurer", key=f"undone_{i}"):
                    st.session_state["tasks"][i]["done"] = False
                    st.rerun()
        with col3:
            if st.button("Supprimer", key=f"delete_{i}"):
                remove_task(st.session_state["tasks"], t["task"])
                st.rerun()
