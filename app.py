import streamlit as st
from tools import get_pokemon

st.title("Poke API in Streamlit")

poke_id = st.number_input("Escoge el id del pokemon", min_value = 1, max_value = 1008)

pokemon = get_pokemon(poke_id)

if "error" not in pokemon:
	st.image(pokemon['image'])
	st.header(f"name: {pokemon['name']}")
	st.write(f"Number: {pokemon['number']}")
	st.write(f"HP: {pokemon['hp']}")
	st.write(f"Attack: {pokemon['attack']}")
	st.write(f"Defense: {pokemon['defense']}")
	st.write(f"Special Attack: {pokemon['special_attack']}")
	st.write(f"Speed: {pokemon['speed']}")
else:
	st.header("Something is off 😔")