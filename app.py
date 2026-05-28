# fichier : app.py
import streamlit as st

# Stockage des tâches en mémoire (disparaît si on relance l'app)
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Ma TodoList")

# Ajouter une nouvelle tâche
new_task = st.text_input("Ajouter une tâche", placeholder="Ex: Apprendre Streamlit...")
if st.button("Ajouter", type="primary"):
    cleaned_task = new_task.strip()
    if cleaned_task == "":
        st.error("La tâche ne peut pas être vide ou ne contenir que des espaces.")
    else:
        st.session_state["tasks"].append({"task": cleaned_task, "done": False})
        st.rerun()

# Afficher les tâches
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
                    st.session_state["tasks"][i]["done"] = True
                    st.rerun()
            else:
                if st.button("Restaurer", key=f"undone_{i}"):
                    st.session_state["tasks"][i]["done"] = False
                    st.rerun()
        with col3:
            if st.button("🗑️", key=f"delete_{i}", help="Supprimer cette tâche"):
                st.session_state["tasks"].pop(i)
                st.rerun()

# Lancer l'application avec : streamlit run app.py