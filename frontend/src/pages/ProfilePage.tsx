import {IonActionSheet, IonCard, IonContent, IonIcon, useIonRouter} from "@ionic/react";
import {Avatar} from "antd";
import {useAppSelector} from "../hooks/storeHooks.ts";
import {logOutOutline} from "ionicons/icons"
import { useState } from "react";
import { OverlayEventDetail } from "@ionic/react/dist/types/components/react-component-lib/interfaces";
import {CapacitorCookies} from "@capacitor/core"
import {clearStore} from "../store";

//@ts-ignore
export default function ProfilePage () {
    const userName = useAppSelector(state => state.userName.userName)
    const [isActionSheetOpen, setActionSheetOpen] = useState(false)
    const router = useIonRouter()
    const logOut = (action:OverlayEventDetail<any>) => {
        if (action?.data?.action === "logout") {
            CapacitorCookies.clearAllCookies().then(() => {
                clearStore()
                setActionSheetOpen(false)
                router.push("/login", "root", "replace")
            })
        }
        else setActionSheetOpen(false)
    }
    return (
        <>
            <IonContent fullscreen className={"ion-padding"}>
                <div style={{
                    display: "flex",
                    justifyContent: "space-between",
                    flexDirection: "column",
                    minWidth: "100%",
                    minHeight: "100%",
                }}>
                    <div style={{
                        display: "flex",
                        justifyContent: "center",
                        alignContent: "center",
                        minWidth: "100%",
                        paddingTop: '10em'
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
                            <p style={{marginTop: 0, marginBottom: 0, fontSize: 18}}>Грейд: Middle</p>
                        </div>
                    </div>
                    <IonCard button onClick={() => setActionSheetOpen(true)}>
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
                                <IonIcon icon={logOutOutline}/>
                            </div>
                            <span style={{color: 'red'}}>Выйти</span>
                        </div>
                    </IonCard>
                </div>
            </IonContent>
            <IonActionSheet
                isOpen={isActionSheetOpen}
                header={"Вы уверены что хотите выйти ?"}
                buttons={[
                    {
                        text: "Да",
                        role: "destructive",
                        data: {
                            action: "logout"
                        }
                    },
                    {
                        text: "Нет",
                        role: 'cancel',
                        data: {
                            action: "cancel"
                        }
                    }
                ]}
                onDidDismiss={({detail}) => logOut(detail)}
            />
        </>
    )
}