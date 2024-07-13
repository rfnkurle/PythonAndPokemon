

function Display() {
   
    const pokemons = [
        {name: 'Pikachu', power: 'poison', photoUrl: 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'},
        {name: 'Charizard', power: 'fire', photoUrl: 'https://assets.pokemon.com/assets/cms2/img/pokedex/full//006.png'},
        {name: 'Bulbasaur', power: 'poison', photoUrl: 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT7i1N2B9yf9M47k-TsfBgcctSXSm7VbQFccuVrJ0ofT2KDWWrn'},
        {name: 'Charmander', power: 'sass', photoUrl: 'https://assets.pokemon.com/assets/cms2/img/pokedex/full//004.png'},
    ]

    return (
        <>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {pokemons.map((pokemon, index) => (
                    <div className="bg-white rounded-lg shadow-md overflow-hidden" key={index}>
                        <img
                            src={pokemon.photoUrl}
                            alt={`A Pokemon`}
                            className="w-full h-48 object-cover"
                            width="400"
                            height="300"
                        />
                        <div className="p-4">
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">{pokemon.name}</h3>
                            <p className="text-gray-600">Power: {pokemon.power}</p>
                        </div>
                    </div>
                ))}
            </div>
        </>
    )
}

export default Display;
