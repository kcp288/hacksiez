var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {title:'Hacksiez', });
});

router.post('/', function (req, res, next) {
	/*
	// Get form body here
	var pyshell = new PythonShell('driver.py', {scriptPath:"./haiku-generator/", pythonOptions: ['-u']});
	var generated = req.body.haiku;

	// Strip newline characters, etc
	generated = generated.replace(/(\r\n|\n|\r|\t)/gm,"");

	pyshell.send(generated).end(function (err) {
		if (err) throw err;
		console.log('finished');
	});

	// Error handling
	if (generated.length < 50){
		res.render('haiku', {layout:'haiku.hbs', title: "Haiku Generator", alert: "Input is not long enough."});
	}
	else {
		var output = '';
		// Message is whatever is printed by the python function
		pyshell.on('message', function (message) {		  
		  // More error handling
		  if (message.length < 1) {
		  	res.render('haiku', {layout:'haiku.hbs', title: "Haiku Generator", alert: "Something went wrong..."});
		  }

		  else { 
		  	output_array = message.split(' * ');
		  	console.log(output_array);
		  	for (i = 0; i < output_array.length; i++) {
		  		output += output_array[i] + "<br>";
		  	}
		  	console.log(output);
		  	res.render('haiku', {layout:'haiku.hbs', title: "Haiku Generator", haiku: output});
		  }
		});
	}
	*/
	res.render('index', {title:'Hacksiez', output:req.body.sentence})

});


module.exports = router;
