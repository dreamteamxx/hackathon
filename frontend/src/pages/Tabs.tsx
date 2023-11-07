import {IonIcon, IonLabel, IonRouterOutlet, IonTabBar, IonTabButton, IonTabs} from "@ionic/react";
import {Redirect, Route} from "react-router-dom";
import Tasks from "./Tasks.tsx";
import MapPage from "./MapPage.tsx";
import EducationPage from "./EducationPage.tsx";
import Task from "./Task.tsx";
import {mapOutline, listOutline, schoolOutline} from "ionicons/icons"

export default function Tabs() {
    return(
        <IonTabs>
            <IonRouterOutlet>
                <Redirect exact path={'/tabs'} to={'/tabs/tasks'}/>
                <Route exact path={"/tabs/tasks"}>
                   <Tasks/>
                </Route>
                <Route exact path={"/tabs/map"}>
                   <MapPage/>
                </Route>
                <Route exact path={"/tabs/education"}>
                   <EducationPage/>
                </Route>
                <Route exact path={'/tabs/tasks/:id'} component={Task}/>
                <Route exact path={"/tabs"}>
                    <Redirect to={'/tabs/tasks'}/>
                </Route>
            </IonRouterOutlet>
            <IonTabBar slot={'bottom'} mode={'md'}>
                <IonTabButton tab={'tasks'} href={'/tabs/tasks'}>
                    <IonIcon icon={listOutline}/>
                    <IonLabel>Задачи</IonLabel>
                </IonTabButton>
                <IonTabButton tab={'map'} href={'/tabs/map'}>
                    <IonIcon icon={mapOutline}/>
                    <IonLabel>Карта</IonLabel>
                </IonTabButton>
                <IonTabButton tab={'education'} href={'/tabs/education'}>
                    <IonIcon icon={schoolOutline}/>
                    <IonLabel>Обучение</IonLabel>
                </IonTabButton>
            </IonTabBar>
        </IonTabs>
    )
}