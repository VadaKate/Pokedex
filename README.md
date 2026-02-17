# Pokedex CLI
## A Python-based Command Line Interface tool that retrieves data from [PokeAPI](https://pokeapi.co/) and displays the following:

* Name: Searches Pokedex API and confirms creature is present in database (and spelt correctly).
* Pokedex ID: Provides the relevant creature's Pokedex ID.
* Height: Shows relevant creature's height in metres.
* Weight: Shows relevant creature's weight in kilograms.
* Type/s: Shows relevant creature's type.
* Move/s: Shows relevant creature's moveset using 5 random moves.
* Error Message: When a non-Pokemon creature's name is entered, it asks for input to be re-entered correctly.

Once all the information is provided, the terminal asks whether the trainer would like to search for another Pokemon.
If answer is positive, the application loops- allowing further searches, else process terminates.

