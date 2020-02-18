const express = require('express')
const path = require('path')

const app = express()
const server = require("http").createServer(app)
const io = require("socket.io")(server)

app.use(express.static(path.join(__dirname)))

// handle incoming connections from clients
io.sockets.on('connection', function(socket) {
    // once a client has connected, we expect to get a ping from them saying what room they want to join
    socket.on('room', function(room) {
        socket.join(room);

        socket.room = room
        //socket._rooms.push(room)
        socket.emit("ENTROU")

        // socket.join(room).on('msg', function(msg) {
        //   console.log(msg)
        // })

    });

    socket.on('msg', function(msg) {
      console.log(msg)      
      //io.sockets.in("123").emit('message', msg);//certo
      //io.to('123').emit('message', msg);//ceto

      io.sockets.in(socket.room).emit('message', msg);

      //delete socket.rooms[socket.id];
      //var keys = Object.keys(socket.rooms);
      //var sala = keys[0]
      //io.sockets.in(sala).emit('message', msg);

      // var keys = Object.keys(socket.rooms);
      // for (var i = 0; i < keys.length; i++) {
      //   io.sockets.in(socket.rooms[keys[i]]).emit('message', msg);
      //   io.to(socket.rooms[keys[i]]).emit('message', msg);
      // }
      
      //io.to("12345", "123").emit('message', msg);//errado
      //socket.broadcast.emit("message", msg)
      //socket.in("123").emit('message', msg);
      //io.to(["123", "12345"]).emit('message', msg);//errado
      //socket.to("123").emit('message', msg);
      //socket.to('123', '1234').emit('hello');
      //io.sockets.to(Object.keys(socket.rooms)).emit('message', msg);

    })

});

// now, it's easy to send a message to just the clients in a given room
//room = "abc123";
//io.sockets.in(room).emit('message', 'what is going on, party people?');

// this message will NOT go to the client defined above
//io.sockets.in('foobar').emit('message', 'anyone in this room yet?');

server.listen(3000)