import {
    IonButton,
    IonContent, IonFooter,
    IonHeader, IonItem, IonList,
    IonModal,
    IonTitle, IonToast,
    IonToolbar,
    IonIcon,
    IonButtons
} from "@ionic/react";
import {useRef} from "react";
import {chevronBack, callOutline, chatbubbleEllipsesOutline, locationOutline} from "ionicons/icons";
import PrimaryIonButton from "../components/buttons/PrimaryIonButton/PrimaryIonButton.tsx";
import InvisibleIonButton from "../components/buttons/invisibleIonButton/InvisibleIonButton.tsx";
import {useAppSelector} from "../hooks/storeHooks.ts";
import {App} from "@capacitor/app";
//@ts-ignore
export default function Task({itemIndex, taskData}){
    const modal = useRef<HTMLIonModalElement>(null);
    const userName = useAppSelector(state => state.userName.userName)
    App.addListener('backButton', () => {
        if (!modal.current) return
        modal.current.dismiss()
    })
    return(
        <IonModal
            key={"10" + String(itemIndex)}
            ref={modal}
            trigger={`open-modal-${itemIndex}`}
        >
            <IonHeader mode={'md'}>
                <IonToolbar mode={'md'}>
                    <div style={{
                        display: "flex",
                        minWidth: "100%",
                        alignItems: 'center'
                    }}>
                        <IonButtons>
                            <IonButton style={{}} shape={'round'} color={'tertiary'} onClick={() => modal.current?.dismiss()}>
                                <IonIcon slot={'icon-only'} icon={chevronBack}/>
                            </IonButton>
                        </IonButtons>
                        {/*<Button shape={'circle'} type={'primary'} icon={<LeftOutlined />} onClick={() => modal.current?.dismiss()}/>*/}
                        <IonTitle><h1 style={{paddingRight: "1.5em", marginBottom: 20}}>{taskData?.text}</h1></IonTitle>
                    </div>
                </IonToolbar>
            </IonHeader>
            <IonContent className="ion-padding" style={{position: "relative"}}>
                <IonList>
                    <IonItem>
                        <div style={{
                            display: 'inline-flex',
                            gap: '1em'
                        }}>
                            <p><strong>Задача</strong></p>
                            <p>Выдача карты</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div style={{
                            display: 'inline-flex',
                            gap: '1em'
                        }}>
                            <p><strong>ФИО</strong></p>
                            <p>{userName}</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div style={{
                            display: 'inline-flex',
                            gap: '1em'
                        }}>
                            <p><strong>Адрес доставки</strong></p>
                            <p>В некст версии</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div style={{
                            display: 'inline-flex',
                            gap: '1em'
                        }}>
                            <p><strong>Время</strong></p>
                            <p>12:24 - 13:00</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div style={{
                            display: 'inline-flex',
                            gap: '1em'
                        }}>
                            <p><strong>Коментарий</strong></p>
                            <p>комент</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div>
                            <p><strong>Продукт</strong></p>
                            <p>карта</p>
                        </div>
                    </IonItem>
                </IonList>
                <div style={{position: "absolute", bottom: 0, left:0, display: "flex", minWidth: '98%', justifyContent: 'space-between', paddingBottom: '.5em', gap: "1em"}}>
                    <PrimaryIonButton mode={'md'} id={'open-success-toast'} style={{minWidth: "100%"}} wrapperStyle={{minWidth: "100%"}} strong>
                        Выполнено
                    </PrimaryIonButton>
                </div>
                <IonToast trigger={'open-success-toast'} message={'Связь с сервером не установлена'} duration={1000}></IonToast>
            </IonContent>
            <IonFooter>
                <IonToolbar>
                    <div style={{
                        display: "flex",
                        justifyContent: "space-between",
                        paddingLeft: "1em",
                        paddingRight: "1em"
                    }}>
                        <InvisibleIonButton size={'large'} href={'tel:79774039527'}>
                            <IonIcon size={'large'} style={{color: 'black'}} slot={'icon-only'} icon={callOutline}/>
                        </InvisibleIonButton>
                        <InvisibleIonButton size={'large'} href={'sms:79774039527'}>
                            <IonIcon size={'large'} style={{color: 'black'}} slot={'icon-only'} icon={chatbubbleEllipsesOutline}/>
                        </InvisibleIonButton>
                        <InvisibleIonButton size={'large'} href={'geo:124.028582,-29.201930'}>
                            <IonIcon size={'large'} style={{color: 'black'}} slot={'icon-only'} icon={locationOutline}/>
                        </InvisibleIonButton>
                    </div>
                </IonToolbar>
            </IonFooter>
        </IonModal>
    )
}