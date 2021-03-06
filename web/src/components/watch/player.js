import React, {Component} from 'react';
import styled from 'styled-components';
import Hls from 'hls.js';

const PlayerWrapper = styled.div`
    position:relative;
`;

const PlayerInner = styled.div`

`;

const VideoTitle = styled.h2 `
    font-size: 22px; 
    color: rgba(0, 0, 0 , 0.7);
    line-height: 25px;
    font-weight: 400;
    
`;

const VideoLiveButtonTitle = styled.span `
    display: inline-block;
    border: 1px solid red;
    padding: 2px 10px;
    line-height: 25px;
    font-size: 14px;
    margin-right: 5px;
    font-weight: 400;
`;


export default class Player extends Component {
    constructor(props) {
        super(props);
        this._onTouchInsidePlayer = this._onTouchInsidePlayer.bind(this)
    }
    componentDidMount() {
        if(Hls.isSupported() && this.player) {
            const video = this.player;
            const streamURL =  "http://localhost:3002/live/tabvn/index.m3u8";

            video.addEventListener('contextmenu', (e) => {


                e.preventDefault();
                return false;
            })

            var hls = new Hls();
            hls.loadSource(streamURL);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED,function() {
                video.play();
            });
        }

    }
    _onTouchInsidePlayer(){

        if(this.player.paused){
            this.player.play();
        }else{

            this.player.pause();
        }
    }
    render() {
        const style = {
            width: 640,
            height: 360,
            background: '#000',
        }
        return <PlayerWrapper>
            <PlayerInner>
                <video controls={false} onClick={this._onTouchInsidePlayer} style = {style} ref = {(player => this.player = player)} autoPlay={true}></video>
                <VideoTitle><VideoLiveButtonTitle>Live</VideoLiveButtonTitle>Live Stream Camera From Self-Driving Car</VideoTitle>
            </PlayerInner>
        </PlayerWrapper>
    }
}