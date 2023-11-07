import {IonContent, IonHeader, IonTitle, IonToolbar} from "@ionic/react";
import ionCl from "../css/IonFixes.module.css"
import MapboxMap from "../components/map/MapboxMap.tsx";

export default function MapPage(){

    return(
        <>
            <IonHeader mode={"md"}>
                <IonToolbar mode={"md"} className={ionCl.fullScreenToolbar}>
                    <IonTitle>
                        <h1>Карта</h1>
                    </IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <MapboxMap/>
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