import {IonContent} from "@ionic/react";
import MapboxMap from "../components/map/MapboxMap.tsx";

export default function MapPage(){

    return(
        <>
            {/*<IonHeader mode={"md"}>*/}
            {/*    <IonToolbar mode={"md"} className={ionCl.fullScreenToolbar}>*/}
            {/*        <IonTitle>*/}
            {/*            <h1>Карта</h1>*/}
            {/*        </IonTitle>*/}
            {/*    </IonToolbar>*/}
            {/*</IonHeader>*/}
            <IonContent fullscreen={true}>
                <div style={{minHeight: "100%"}}>
                    <MapboxMap/>
                </div>
                {/*<div style={{*/}
                {/*    display: 'flex',*/}
                {/*    flexDirection: "column",*/}
                {/*    justifyContent: 'center',*/}
                {/*    minHeight: "100%"*/}
                {/*}}>*/}
                {/*    Карты нет и токена тоже 😥*/}
                {/*</div>*/}
            </IonContent>
        </>
    )
}