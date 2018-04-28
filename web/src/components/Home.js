import React,{Component} from 'react'
import styled  from 'styled-components'
import socketIOClient from 'socket.io-client';

const HomeWrapper = styled.div `
  
`
export default class Home extends Component{
    constructor(props) {
        super(props);
        this.state = {
            endpoint: "http://10.0.0.189:3001",
            boolean: 'true'


        };
    }

    startToRun = () => {
        const socket = socketIOClient(this.state.endpoint);
        socket.emit('startToRun', 'true');
    }

    setBoolean = (boolean) => {
        const socket = socketIOClient(this.state.endpoint);
        this.setState({ boolean })
        socket.emit('startToRun', boolean);
    }
    render() {
        const socket = socketIOClient(this.state.endpoint);
        socket.on('startToRun', (boolean) => {
            console.log(`${boolean}`);
        });
        return (
            <HomeWrapper>
                <div style={{ textAlign: "center" }}>
                    <button onClick={() => this.startToRun() }>Start!</button>
                    <button onClick={() => this.setBoolean(!this.state.boolean)}>Stop!</button>



                </div>
            </HomeWrapper>
        );
    }
}