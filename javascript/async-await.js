async function getLuke(){
	try{
		const response = await fetch("http://www.swapi.co/api/people/1/")
		const luke = await response.json()
		const responseHomeworld = await fetch(luke.homeworld)
		luke.homeworld = await responseHomeworld.json()
		console.log(`${luke.name} nacio en ${luke.homeworld.name}`)
	}catch(err){
		console.log(`Request failed: ${err}`)
	}
}