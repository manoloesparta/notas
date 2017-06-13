function iterador(){
	let a = 0, b = 1
	return {
		next: function(){
		let f = a
		a = b
		b = f + a
		return {value: f, done: false}
		}
	}
}

const iter = iterador()
iter.next().value