import * as firebase from 'firebase';
const config = {
    apiKey: "AIzaSyAb0YlgKwspcwaZWqVzklndPj9hYtF5F9c",
    authDomain: "selfdrvingcar-9e1b3.firebaseapp.com",
    databaseURL: "https://selfdrvingcar-9e1b3.firebaseio.com",
    projectId: "selfdrvingcar-9e1b3",
    storageBucket: "selfdrvingcar-9e1b3.appspot.com",
    messagingSenderId: "879462042399"
};

if (!firebase.apps.length) {
    firebase.initializeApp(config);
}

const auth = firebase.auth();

export {
    auth,
};