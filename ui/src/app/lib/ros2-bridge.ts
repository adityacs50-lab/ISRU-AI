export class ROS2Bridge {
  private ws: WebSocket;

  constructor(url: string = 'ws://localhost:9001') {
    this.ws = new WebSocket(url);
  }

  publish(topic: string, data: any) {
    this.ws.send(JSON.stringify({ topic, data }));
  }

  subscribe(topic: string, callback: (data: any) => void) {
    this.ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.topic === topic) {
        callback(message.data);
      }
    };
  }
}
