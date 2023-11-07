import {IonContent, IonHeader, IonTitle, IonToolbar} from "@ionic/react";
import {Empty} from "antd";

export default function EducationPage(){
    return(
        <>
            <IonHeader mode={'md'}>
                <IonToolbar mode={'md'}>
                    <IonTitle>
                        <h1>Обучение</h1>
                    </IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <div style={{
                    display: 'flex',
                    flexDirection: "column",
                    justifyContent: 'center',
                    minHeight: "100%"
                }}>
                   <Empty/>
                </div>
            </IonContent>
        </>
    )
}