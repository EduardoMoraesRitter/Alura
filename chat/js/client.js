// set-up a connection between the client and the server
//const socket = io('http://localhost:3000');

var socket = io.connect('http://localhost:3000');

// let's assume that the client page, once rendered, knows what room it wants to join
var room = "abc123";

socket.on('connect', function() {
   // Connected, let's sign-up for to receive messages for this room
   //socket.emit('room', room);
});

socket.on('message', function(recebemsg) {
    var antigo = document.getElementById("text").innerHTML;
    document.getElementById("text").innerHTML = antigo + "<br/>" + recebemsg;
});

socket.on('ENTROU', function(data) {
    console.log('entrou:', data);
 });

function entrarSala(){ 
    var sala = document.getElementById("sala").value;
    socket.emit('room', sala);
    console.log(sala)
}


function msgSala(){ 
    var msg = document.getElementById("msg").value;
    socket.emit('msg', msg);
    console.log(msg)
}