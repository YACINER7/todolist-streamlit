import streamlit as st

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
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .task-card.done {
        border-left-color: #aaa;
        opacity: 0.6;
    }
    .task-text {
        font-size: 16px;
        color: #222;
    }
    .task-text.done {
        text-decoration: line-through;
        color: #888;
    }
    .badge {
        background: #e8f0fe;
        color: #4f8ef7;
        border-radius: 20px;
        padding: 2px 12px;
        font-size: 13px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.markdown("## Ma TodoList")

col1, col2 = st.columns([0.75, 0.25])
with col1:
    new_task = st.text_input("", placeholder="Nouvelle tâche...", label_visibility="collapsed")
with col2:
    if st.button("Ajouter", use_container_width=True):
        if new_task.strip() != "":
            st.session_state["tasks"].append({"task": new_task, "done": False})
            st.rerun()

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
    st.markdown(f"""
    <div class='task-card {done_class}'>
        <span class='task-text {done_class}'>{t['task']}</span>
        <span class='badge'>{'Terminé' if t['done'] else 'À faire'}</span>
    </div>
    """, unsafe_allow_html=True)

    if not t["done"]:
        if st.button("Marquer comme fait", key=f"done_{i}"):
            st.session_state["tasks"][i]["done"] = True
            st.rerun()
