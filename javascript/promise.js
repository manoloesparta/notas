functionget(URL){
	//New Promise recibe una funcion
	returnnewPromise((resolve, reject)=>{
		const xhr = new XMLHttpRequest();

		xhr.onreadystatechange = function () {
			const DONE = 4
			const OK = 200
			if (this.readyState === DONE) {
				if(this.status === OK){
					//Todo OK
					resolve(JSON.parse(this.responseText))
				}else {
					//Hubo un error
					reject(newError(`Se produjo un error al realizar el request ${this.status}`))
				}
			} 
		}

		xhr.open('GET', URL);
		xhr.send(null);
	})
}

/* Funcion para tratar el error */
functionhandleError(err){
	console.log(`Request failed: ${err}`) 
}

let luke

/*llamada al metodo */
get('http://www.swapi.co/api/people/1/')
	//lamada a funcion normal
	.then(function(response){
		luke = response
		//promesa
		return get(luke.homeworld)
	})
	//llamada a funcion con arrow functions
	.then((homeworld)=>{
		luke.homeworld = homeworld
		console.log(`${luke.name} nació en ${luke.homeworld.name}`)
	})
	.catch((err)=> handleError(err))