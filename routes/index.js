var express = require('express');
var router = express.Router();

var PythonShell = require('python-shell');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {title:'Hacksiez', });
});

router.post('/', function (req, res, next) {
	
	// Get form body here
	var pyshell = new PythonShell('totes.py', {scriptPath:"./", pythonOptions: ['-u']});
	var sentence = req.body.sentence;

	console.log(sentence);

	// Strip newline characters, etc
	sentence = sentence.replace(/(\r\n|\n|\r|\t)/gm,"");

	pyshell.send(sentence).end(function (err) {
		if (err) throw err;
		console.log('finished');
	});
	

	//var output = '';
	// Message is whatever is printed by the python function
	
	pyshell.on('message', function (message) {		
	  // More error handling
	  /*
		  if (message.length < 2) {
		  	res.render('index', {alert: "Something went wrong..."});
		  }*/
		console.log(message);
		if (message == 'x'){
			res.render('index', {output:"Something went wrong", before:req.body.sentence})
		}
		else{
		  	
		  	res.render('index', {output:message, before:req.body.sentence});
		}
	});



});

module.exports = router;
