import logging
import streamlit as st
from core.todolist_utils import add_task, remove_task, mark_done

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

st.set_page_config(page_title="TodoList", layout="centered")

st.markdown("""
<style>
    .main { max-width: 650px; margin: auto; }

    .task-card {
        background: #f8f9fa;
        border-left: 4px solid #4f8ef7;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }
    .task-card.done {
        border-left-color: #aaa;
        opacity: 0.6;
    }
    .task-text {
        font-size: 16px;
        color: #222;
        font-weight: 500;
    }
    .task-text.done {
        text-decoration: line-through;
        color: #888;
    }
    .task-meta {
        font-size: 12px;
        color: #999;
        margin-top: 2px;
    }
    .badge {
        background: #e8f0fe;
        color: #4f8ef7;
        border-radius: 20px;
        padding: 2px 12px;
        font-size: 13px;
        font-weight: 600;
    }
    .badge.done {
        background: #f0f0f0;
        color: #aaa;
    }
</style>
""", unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.markdown("## Ma TodoList")

col1, col2, col3 = st.columns([0.55, 0.2, 0.25])
with col1:
    new_task = st.text_input("", placeholder="Nouvelle tâche...", label_visibility="collapsed")
with col2:
    due_date = st.date_input("", label_visibility="collapsed")
with col3:
    if st.button("Ajouter", use_container_width=True):
        try:
            add_task(st.session_state["tasks"], new_task, str(due_date))
            logging.info("Tâche ajoutée : %s", new_task)
            st.rerun()
        except ValueError as e:
            logging.warning("Ajout refusé : %s", e)
            st.error(str(e))

total = len(st.session_state["tasks"])
faites = sum(1 for t in st.session_state["tasks"] if t["done"])

if total > 0:
    st.progress(faites / total)
    st.caption(f"{faites} sur {total} tâches terminées")

st.markdown("---")

if total == 0:
    st.markdown("<p style='color:#aaa; text-align:center;'>Aucune tâche pour l'instant</p>", unsafe_allow_html=True)

for i, t in enumerate(st.session_state["tasks"]):
    done_class = "done" if t["done"] else ""
    due = f"<div class='task-meta'>Échéance : {t['due_date']}</div>" if t.get("due_date") else ""
    st.markdown(f"""
    <div class='task-card {done_class}'>
        <div style='display:flex; justify-content:space-between; align-items:center;'>
            <span class='task-text {done_class}'>{t['task']}</span>
            <span class='badge {done_class}'>{'Terminé' if t['done'] else 'À faire'}</span>
        </div>
        {due}
    </div>
    """, unsafe_allow_html=True)

    if not t["done"]:
        col_a, col_b = st.columns([0.5, 0.5])
        with col_a:
            if st.button("Marquer comme fait", key=f"done_{i}"):
                print(f"[DEBUG] avant mark_done : {st.session_state['tasks'][i]}")
                mark_done(st.session_state["tasks"], i)
                logging.info("Tâche marquée comme faite : %s", t["task"])
                print(f"[DEBUG] après mark_done : {st.session_state['tasks'][i]}")
                st.rerun()
        with col_b:
            if st.button("Supprimer", key=f"del_{i}"):
                remove_task(st.session_state["tasks"], t["task"])
                logging.info("Tâche supprimée : %s", t["task"])
                st.rerun()
