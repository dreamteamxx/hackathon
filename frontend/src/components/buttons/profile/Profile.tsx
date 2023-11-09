import {
    IonButton,
    IonButtons,
    IonContent,
    IonHeader, IonIcon,
    IonModal,
    IonTitle,
    IonToolbar
} from "@ionic/react";
import {useRef} from "react";
import {chevronBack} from "ionicons/icons";
import {useAppSelector} from "../../../hooks/storeHooks.ts";

export default function Profile(){
    const userName = useAppSelector(state => state.userName.userName)
    const modal = useRef<HTMLIonModalElement>(null)
    return(
        <IonModal
            ref={modal}
            trigger={'profile'}
            // @ts-ignore
        >
         <IonHeader mode={"md"}>
             <IonToolbar mode={"md"}>
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
                     <IonTitle><h1 style={{paddingRight: "1.5em", marginBottom: 20}}>Аккаунт</h1></IonTitle>
                 </div>
             </IonToolbar>
         </IonHeader>
            <IonContent>
                {userName}
            </IonContent>
        </IonModal>
    )
}