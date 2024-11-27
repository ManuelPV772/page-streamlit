import streamlit as st
import sqlite3

# Función para obtener los usuarios desde la base de datos
def get_users():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("SELECT id, name, age FROM users")
    data = c.fetchall()
    conn.close()
    return data

# Función para guardar cambios en el nombre o edad de un usuario
def update_user(user_id, new_name, new_age):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
    conn.commit()
    conn.close()

# Función para eliminar un usuario
def delete_user(user_id):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# Crear o conectar a una base de datos SQLite
conn = sqlite3.connect("user_data.db")
c = conn.cursor()

# Crear una tabla si no existe
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()

# Título de la aplicación
st.title("Registro de Usuarios")

# Formulario para ingresar datos
st.subheader("Introduce tu nombre y edad")
name = st.text_input("Nombre:")
age = st.number_input("Edad:", min_value=1, step=1)

if st.button("Guardar"):
    if name and age:
        # Insertar datos en la base de datos
        conn = sqlite3.connect("user_data.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
        st.success(f"Datos guardados: {name}, {age} años")
        # Actualizar la lista de usuarios en tiempo real
        st.session_state.data = get_users()
    else:
        st.error("Por favor, completa todos los campos.")

# Inicializar los datos en session_state si no están presentes
if "data" not in st.session_state:
    st.session_state.data = get_users()

# Mostrar datos guardados
st.subheader("Usuarios Registrados")
data = st.session_state.data  # Usar datos del estado actual

if data:
    for row in data:
        st.markdown("---")  # Línea divisoria para separar registros
        # Mostrar datos en un cuadro estructurado
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
                <strong>ID:</strong> {row[0]}<br>
                <strong>Nombre:</strong> {row[1]}<br>
                <strong>Edad:</strong> {row[2]} años
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Botones para acciones
        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input(f"Nuevo nombre para ID {row[0]}", value=row[1], key=f"name_{row[0]}")
            new_age = st.number_input(f"Nueva edad para ID {row[0]}", min_value=1, step=1, value=row[2], key=f"age_{row[0]}")

            if st.button(f"Guardar cambios en {row[0]}", key=f"save_{row[0]}"):
                # Ejecuta la actualización y actualiza la tabla en un solo clic
                update_user(row[0], new_name, new_age)
                st.success(f"Registro actualizado: {new_name}, {new_age} años")
                st.session_state.data = get_users()  # Refrescar los datos inmediatamente

        with col2:
            if st.button(f"Eliminar {row[0]}", key=f"delete_{row[0]}"):
                # Ejecuta la eliminación y actualiza la tabla en un solo clic
                delete_user(row[0])
                st.warning(f"Registro eliminado: ID {row[0]}")
                st.session_state.data = get_users()  # Refrescar los datos inmediatamente
else:
    st.info("No hay usuarios registrados aún.")
