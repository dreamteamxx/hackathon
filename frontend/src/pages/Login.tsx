import {IonContent, IonImg, IonPage} from "@ionic/react";
import sovkombankLogo from "../assets/sovcombank.png"
import PrimaryIonButton from "../components/buttons/PrimaryIonButton/PrimaryIonButton";
import DangerIonButton from "../components/buttons/DangerIonButton/DangerIonButton.tsx";
// import {StatusBar} from "@capacitor/status-bar"
// @ts-ignore
export default function Login({history}) {
    return (
        <IonPage>
            <IonContent>
                <div
                    style={{
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "center",
                        alignContent: "center",
                        minHeight: "100%",
                        paddingLeft: "2em",
                        paddingRight: "2em",
                        gap: '2em',
                        paddingBottom: "5em"
                }}>
                    <IonImg
                        src={sovkombankLogo}
                        alt={'лого СОВКОМПБАНК'}
                        style={{widths: "7em", height: '7em'}}
                    />
                    <div
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            justifyContent: "space-between",
                            gap: "2em"
                    }}>
                        <PrimaryIonButton routerLink={"/login/employer"} style={{minWidth: "80%"}} strong>Сотрудник</PrimaryIonButton>
                        <DangerIonButton routerLink={"/login/manager"} style={{minWidth: "80%"}} strong>Менеджер</DangerIonButton>
                    </div>
                </div>
            </IonContent>
        </IonPage>
    )
}