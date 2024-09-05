const WebSocket = require('ws'); //引入WebSocket模块
const server = new WebSocket.Server({ port: 8080 }); //创建一个WebSocket服务器实例，指定服务器监听的端口号为8080

server.on('connection', socket => { //监听客户端连接事件
    socket.on('message', message => { // 监听消息事件。当客户端发送消息时，会触发这个事件，并传入消息内容。
        // Broadcast the message to all clients except the sender
        server.clients.forEach(client => {
            if (client !== socket && client.readyState === WebSocket.OPEN) { //如果不是发送消息的客户端，并且它的连接状态是打开的，就将消息发送给这个客户端
                client.send(message);
            }
        });
    });
});
