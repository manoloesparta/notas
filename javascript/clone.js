let a = {b:1}
let b = a
function cambiar_valor(){
	const clone = Object.assign({}, persona)
	clone.b++
	return clone
}