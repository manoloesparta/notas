const expect = require('chai').expect
const app = require('..').default

describe('#app', function(){
	it('Voy a verficar que si sirva una regla',function(){
		const result = app('Hola')
		expect(result).to.equal(0)
	})
})