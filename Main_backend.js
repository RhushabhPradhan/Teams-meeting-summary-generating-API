const fs = require('fs');
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    if (req.url == '/') {
        res.end('this is the main page')
    } else if (req.url == '/contact') {
        fs.readFile(`${__dirname}/summary.json`, 'utf-8', (err, data) => {
            console.log(data)
            res.end(data)
        })
    } else {
        res.end('this is error page')
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});