const express = require('express');
const app = express();
//~ const resources = require('./resources.json');

app.get('/', function(req, res) {
  res.send("Hi, I'm root");
});

app.use('/static', express.static('/home/www/arqui/static/files'));

app.get('/process/:n', function(req, res) {
  const n = req.params.n;

  for (var i = n; i >= 0; i--) {
  	for (var j = n; j >= 0; j--) {
  		a = 2
  	}
  }
  res.send("OK");
});

app.listen(8080, function () {
  console.log('listening on port 8080!')
})
