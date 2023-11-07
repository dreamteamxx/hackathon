import React from 'react'
import ReactDOM from 'react-dom/client'
import './App.css'
import './index.css'
import {Redirect, Route} from "react-router-dom";
import {Provider} from 'react-redux';
import store from "./store";
import '@ionic/react/css/core.css'
/* Basic CSS for apps built with Ionic */
import '@ionic/react/css/normalize.css';
import '@ionic/react/css/structure.css';
import '@ionic/react/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/react/css/padding.css';
import '@ionic/react/css/float-elements.css';
import '@ionic/react/css/text-alignment.css';
import '@ionic/react/css/text-transformation.css';
import '@ionic/react/css/flex-utils.css';
import '@ionic/react/css/display.css';
import {IonApp, IonRouterOutlet, setupIonicReact} from "@ionic/react";
import {IonReactRouter} from "@ionic/react-router";
import Login from "./pages/Login.tsx";
import Error from "./pages/Error.tsx"
import EmployerLogin from "./components/login/EmployerLogin.tsx";
import Tabs from './pages/Tabs.tsx';

setupIonicReact()

//todo возможно заменить react-responsive-redux на react-respinsive

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Provider store={store}>
            <IonApp>
                <IonReactRouter>
                    <IonRouterOutlet>
                        <Route path={'/'} exact>
                            <Redirect to={'/login'}/>
                        </Route>
                        <Route path={'/login'} exact component={Login}/>
                        <Route path={'/login/:employerType'} component={EmployerLogin}/>
                        <Route path={'/tabs'} render={() => <Tabs/>}/>
                        <Route component={Error}/>
                    </IonRouterOutlet>
                </IonReactRouter>
            </IonApp>
        </Provider>
    </React.StrictMode>
)
