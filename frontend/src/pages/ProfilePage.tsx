import {IonCard, IonContent, IonIcon} from "@ionic/react";
import {Avatar} from "antd";
import {useAppSelector} from "../hooks/storeHooks.ts";
import {keyOutline} from "ionicons/icons"

export default function ProfilePage () {
    const userName = useAppSelector(state => state.userName.userName)
    return (
        <>
            <IonContent fullscreen className={"ion-padding"}>
                <div style={{
                    display: "flex",
                    justifyContent: "space-evenly",
                    flexDirection: "column",
                    minWidth: "100%",
                    minHeight: "100%"
                }}>
                    <div style={{
                        display: "flex",
                        justifyContent: "center",
                        alignContent: "center",
                        minWidth: "100%"
                    }}>
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            alignContent: "center"
                        }}>
                            <div style={{display: "flex", justifyContent:"center", minWidth: "100%"}}>
                                <Avatar size={100}><span style={{fontSize: 32}}>{userName.substring(0, 2)}</span></Avatar>
                            </div>
                            <p style={{marginBottom: 0, fontSize: 28}}>Иван Иванович</p>
                            <p style={{marginTop: 0, marginBottom: 0, color: "blue"}}>@{userName}</p>
                            <p style={{marginTop: 0, marginBottom: 0}}>Middle</p>
                        </div>
                    </div>
                    <IonCard button>
                        <div style={{
                            display: "flex",
                            gap: "1em",
                            minWidth: "100%",
                            alignItems: "center",
                            paddingInline: "1em",
                            fontSize: 18,
                            paddingTop: ".5em",
                            paddingBottom: ".5em"
                        }}>
                            <div>
                                <IonIcon icon={keyOutline}/>
                            </div>
                            <span>Настройки аккаунта</span>
                        </div>
                    </IonCard>
                </div>
            </IonContent>
        </>
    )
}