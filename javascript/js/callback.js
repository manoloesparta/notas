function get(URL, callback){
	const xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function () {
		const DONE = 4
		const OK = 200
		if (this.readyState === DONE) {
			if(this.status === OK){
				//Todo OK
				callback(null, JSON.parse(this.responseText))
			}else {
				//Jubo un error
				callback(newError(`Se produjo un error al realizar el request ${this.status}`))
			}
		}
	}

	xhr.open('GET', URL);
	xhr.send(null);
}

/* Funcion para tratar el error */
function handleError(err){
	console.log(`Request failed: ${err}`)
}


/*llamada al metodo */
get('http://www.swapi.co/api/people/1/', functiononResponse(err, luke){
	if(err) return handleError(err)

	/* Para traer el mundo */
	get(luke.homeworld, functiononHomeworldResponse(err, homeworld){
		if(err) return handleError(err)

		luke.homeworld = homeworld
		console.log(`${luke.name} nació en ${luke.homeworld.name}`)
	})

	console.log(`Request succeded`)
	console.log('luke', luke)
})