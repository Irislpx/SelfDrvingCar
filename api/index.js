const http = require('http');
const express = require('express');
const socketIO = require('socket.io');
const { spawn } = require('child_process');
const util = require('util');


const PORT = 3001;
const app = express();
const server = http.createServer(app);
const io = socketIO(server);


io.on('connection', (client) => {
    console.log('User connected');
    // here you can start emitting events to the client
    client.on('subscribeToTimer', (interval) => {
        console.log('client is subscribing to timer with interval ', interval);
        setInterval(() => {
            client.emit('timer', new Date());
        }, interval);
    });

    client.on('startToRun', (boolean) => {
        // once we get a 'change color' event from one of our clients, we will send it to the rest of the clients
        // we make use of the socket.emit method again with the argument given to use from the callback function above
        console.log('Status: ', boolean);
        io.sockets.emit('startToRun', boolean);
        if (boolean === 'true') {
            var process = spawn('python3', ['./drive1.py']);
            process.stdout.on('data',function(chunk){

                var textChunk = chunk.toString('utf8');// buffer to string

                util.log(textChunk);
            });
        }

    })
    client.on('disconnect', () => {
        console.log('user disconnected')
    });
});


server.listen(PORT,() => {
    console.log(`Server is running on: http://localhost:${PORT}`);
})