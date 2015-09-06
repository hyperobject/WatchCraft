/**
 * This is the frontend for the Pebble-WebSockets interface to Minecraft
 */

var Vector2 = require('vector2');
var Vibe = require('ui/vibe');
var UI = require('ui');
var Accel = require('ui/accel');

Accel.init();
var card = new UI.Card({
  backgroundColor:'vividCerulean',
  title:'Pebblecraft!',
  body:'Connecting...'
});
var socket = new WebSocket("ws://<computer IP address here>:8181");
socket.onopen = function() {
  card.body('Connected.');
  card.backgroundColor('blueMoon');
  
};

card.on('click', 'up', function(e){
    socket.send('pebble:up');
    /*if (inventory==9){
      inventory = 1;
    } else {
      inventory += 1;
    }*/
  });
  
  card.on('click', 'down', function(e){
    socket.send('pebble:down');
    /*if (inventory == 1){
      inventory = 9;
    } else {
      inventory -= 1;
    }*/
    
  });

  card.on('click', 'select', function(e){
    Vibe.vibrate('short');
    socket.send('pebble:select');
  });

  card.on('longClick', 'select', function(e){
    Vibe.vibrate('double');
    socket.send('pebble:longselect')
  });


socket.onmessage = function(e) {
  console.log("got response: " + e.data);
  card.subtitle('Slot ' + e.data);
  card.backgroundColor('blueMoon');
};
socket.onclose = function(e) {
  console.log("Closed.");
  card.body('Disconnected.');
  card.backgroundColor('red');
};

card.show();
