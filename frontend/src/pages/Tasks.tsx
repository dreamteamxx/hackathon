import {
    IonCard,
    IonCardHeader,
    IonCardSubtitle, IonCardTitle,
    IonChip,
    IonContent,
    IonHeader, IonIcon,
    IonRefresher,
    IonRefresherContent, IonRippleEffect,
    IonTitle,
    IonToolbar, RefresherEventDetail
} from "@ionic/react";
import {useEffect, useState} from "react";
import Task from "./Task.tsx";
import {useCookies} from "react-cookie";
import {personCircleOutline} from "ionicons/icons"
import cl from "../css/IonFixes.module.css"
import InvisibleIonButton from "../components/buttons/invisibleIonButton/InvisibleIonButton.tsx";
import Profile from "../components/buttons/profile/Profile.tsx";
//@ts-ignore
export default function Tasks({history}){
    const [items, setItems] = useState<{text: string, id: number}[]>([])
    const [cookies] = useCookies(["role"])

    const generateItems = () => {
        const newItems = []
        for (let i = 0; i < 50; i++){
            newItems.push({text: `Задача ${1 + items.length + i}`, id: i})
        }
        setItems([...items, ...newItems])
    }
    function handleRefresh(event: CustomEvent<RefresherEventDetail>) {
        setTimeout(() => {
            // Any calls to load data go here
            event.detail.complete();
        }, 2000);
    }

    useEffect(() => {
        if (JSON.stringify(cookies["role"]) !== "\"employer\"") history.push("/login")
        generateItems()
    }, []);
    return (
        <>
            <IonHeader mode={"md"}>
                <IonToolbar mode={"md"}>

                    <div style={{
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "space-between"
                    }}>

                        <div style={{
                            display: "flex",
                            justifyContent: "space-between",
                            alignItems: "center"
                        }}>
                            {/*<div style={{paddingLeft: "1em"}}>*/}
                                <IonTitle className={cl.clearLeftTitle}>
                                    <h1>Задачи</h1>
                                </IonTitle>
                            {/*</div>*/}
                            {/*<div style={{paddingRight: "1em"}}>*/}
                            {/*    <InvisibleIonButton size={'large'} id={'profile'}>*/}
                            {/*        <IonRippleEffect/>*/}
                            {/*        <IonIcon slot={'icon-only'} color={'dark'} size={'large'} icon={personCircleOutline}/>*/}
                            {/*    </InvisibleIonButton>*/}
                            {/*</div>*/}
                        </div>
                        <div style={{
                            display: "flex",
                            justifyContent: 'center',
                            gap: "2em",
                            minWidth: '100%',
                        }}>
                            <IonChip color={'primary'}>Выполнено: 0</IonChip>
                            <IonChip color={'danger'}>Осталось: 50</IonChip>
                        </div>
                    </div>
                </IonToolbar>
            </IonHeader>
            <IonContent style={{maxHeight: "95%"}}>
                <Profile/>
                <IonRefresher slot="fixed" onIonRefresh={handleRefresh}>
                    <IonRefresherContent></IonRefresherContent>
                </IonRefresher>
                <div style={{paddingBottom: "4em"}}>
                    {items.map((item, index) => (
                        <div key={"0" + String(index)}>
                            <IonCard key={index} button id={`open-modal-${index}`}>
                                <IonCardHeader>
                                    <div style={{
                                        display: "flex",
                                        justifyContent: 'space-between'
                                    }}>
                                        <div>
                                            <IonCardTitle>{item.text}</IonCardTitle>
                                            <IonCardSubtitle>Выдача карты</IonCardSubtitle>
                                        </div>
                                        <div style={{
                                            display:"flex",
                                            flexDirection: "column",
                                            justifyContent: 'center'
                                        }}>
                                            <p style={{marginTop: 0, marginBottom: 0}}>Время</p>
                                            <p style={{marginTop: 0, marginBottom: 0}}>12:24</p>
                                        </div>
                                    </div>
                                </IonCardHeader>
                            </IonCard>
                            <Task itemIndex={index} taskData={item}/>
                        </div>
                    ))}
                </div>
                {/*<IonInfiniteScroll onIonInfinite={(ev) => {*/}
                {/*    generateItems()*/}
                {/*    setTimeout(() => {*/}
                {/*        ev.target.complete()*/}
                {/*    }, 5000)*/}
                {/*}}>*/}
                {/*    <IonInfiniteScrollContent></IonInfiniteScrollContent>*/}
                {/*</IonInfiniteScroll>*/}
            </IonContent>
        </>
    )
}