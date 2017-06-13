function* generador(){
	let a = 0, b = 1
	while(true){
		let f = a
		a = b
		b = f + a
		yield f
		let reset = yield f
		if (reset) a = 0, b = 1
	}
}

const gene = generador()
gene.next().value()

//para hacer reset
gene.next(true)