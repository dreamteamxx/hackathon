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
import {useAppSelector} from "../hooks/storeHooks.ts";
import {chevronBack} from "ionicons/icons";
import DangerIonButton from "../components/buttons/DangerIonButton/DangerIonButton.tsx";
import PrimaryIonButton from "../components/buttons/PrimaryIonButton/PrimaryIonButton.tsx";
//@ts-ignore
export default function Task({itemIndex, taskData}){
    const modal = useRef<HTMLIonModalElement>(null);
    const userName = useAppSelector(state => state.userName.userName)
    return(
        <IonModal key={"10" + String(itemIndex)} ref={modal} trigger={`open-modal-${itemIndex}`}>
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
                            <p>Пиво захвати)</p>
                        </div>
                    </IonItem>
                    <IonItem>
                        <div>
                            <p><strong>Продукт</strong></p>
                            <p>🔥Реалистичный фаллоимитатор фаллос-страпон с подогревом</p>
                        </div>
                    </IonItem>
                </IonList>
                <div style={{position: "absolute", bottom: 0, left:0, display: "flex", minWidth: '94%', justifyContent: 'space-between', paddingBottom: '.5em', gap: "1em"}}>
                    <PrimaryIonButton mode={'md'} id={'open-success-toast'} wrapperStyle={{minWidth: "50%"}} style={{minWidth: "100%"}} strong>
                        Выполнено
                    </PrimaryIonButton>
                    <DangerIonButton mode={'md'} id={'open-loose-toast'} wrapperStyle={{minWidth: "50%"}} style={{minWidth: "100%"}} strong>
                        Перенести
                    </DangerIonButton>
                </div>
                <IonToast trigger={'open-success-toast'} message={'Связь с сервером не установлена'} duration={1000}></IonToast>
                <IonToast trigger={'open-loose-toast'} message={'Хуй те а не перенос'} duration={1000}></IonToast>
            </IonContent>
            <IonFooter>
                <IonToolbar>

                </IonToolbar>
            </IonFooter>
        </IonModal>
    )
}