const text_box = document.getElementById('text_box')
const disabled_keys = ['ArrowLeft', 'ArrayRight', 'ArrowUp', 'ArrowDown']

text_box.addEventListener('keydown', function(event){
	console.log(event.key)
	if (disabled_keys.includes(event.key)) {
		console.log(`Key not allowed ${event.key}`)
		event.preventDefault();
	}
});

text_box.addEventListener('mousedown', function(event){
	console.log('Mousedown')
	event.preventDefault()
	text_box.focus()
});
