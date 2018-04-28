import React, { Component } from 'react';
import styled from 'styled-components';
import  {borderColor, headerHeight, containerWidth} from "./theme";
import {userAvatar} from "../images/avatar.png";

import Navigation from './Navigation';

import Watch from './watch/watch';
import LandingPage from './Landing';
import SignUpPage from './SignUp';
import SignInPage from './SignIn';

import HomePage from './Home';


import {Route, Switch} from 'react-router-dom';
import { firebase } from '../firebase';





const AppWrapper = styled.div `
   
`;

const Container = styled.div `
    max-width: ${containerWidth}px;
    margin: 0 auto;
`
const Header = styled.div `
      
        height: ${headerHeight}px;
        border-bottom: 1px solid ${borderColor};
`

const Main = styled.div `
    padding: 20px 0;
    
`

const Footer = styled.div `
    border-top: 1px solid ${borderColor};
    padding: 10px 0;
`
const Copyright = styled.p`
    font-size: 12px;
    text-align: center;
`
const HeaderTitle = styled.div `
    font-size: 35px;
    font-weight: 800;
    line-height: ${headerHeight}px;
    flex-grow: 1;
    text-align: center;
    color: rgba(0, 0, 0, 0.8);
`
const HeaderUserMenu = styled.div `
    width: 50px;
    display: flex;
    align-items: center;
`
const HeaderWrapper = styled.div `
    display: flex;
    
`
const HeaderUserAvatar = styled.img `
    border-radius: 50%;
    width: 30px;
    height: 30px;
`

const UserTitle = styled.div `
    font-size: 14px;
    font-weight: 600;
    line-height: ${headerHeight}px;
    padding-right: 10px;
    `;

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            authUser: null,
        };
    }
    componentDidMount() {
        firebase.auth.onAuthStateChanged(authUser => {
            authUser
                ? this.setState(() => ({ authUser }))
                : this.setState(() => ({ authUser: null }));
        });
    }

    render() {
        return <AppWrapper>
            <Header>
                <HeaderWrapper>
                    <HeaderTitle>Camera</HeaderTitle>
                    <HeaderUserMenu>

                        <HeaderUserAvatar alt="" src={userAvatar}/>
                    </HeaderUserMenu>
                </HeaderWrapper>
            </Header>
            <Main>
                <Container>
                        <Switch>
                        <div>
                            <Navigation authUser={this.state.authUser} />

                            <hr/>

                            <Route exact path = {'/watch'} component = {Watch}/>
                        <Route exact path = {'/'} component = {LandingPage}/>
                        <Route exact path = {'/home'} component = {HomePage}/>
                            <Route exact path = {'/signin'} component = {SignInPage}/>
                            <Route exact path = {'/signup'} component = {SignUpPage}/>


                        </div>
                        </Switch>

                </Container>
            </Main>
            <Footer>
                <Container>
                    <Copyright>® EC500J1, Lijun Xiao, Peixin Li</Copyright>
                </Container>
            </Footer>
        </AppWrapper>


        }


    }
export default App;



