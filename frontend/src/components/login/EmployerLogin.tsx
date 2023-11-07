import {
    IonContent,
    IonPage,
    IonToolbar,
    IonIcon,
    IonInput, IonHeader, IonTitle, IonProgressBar,
} from "@ionic/react";
import {chevronBack} from 'ionicons/icons'
import "./login.module.css"
import {MouseEventHandler, useEffect, useState} from "react";
import {setUserType} from "../../store/slices/userTypeSlice.ts";
import {useAppDispatch} from "../../hooks/storeHooks.ts";
import {setUserName} from "../../store/slices/userNameSlice.ts";
import CircleIonButton from "../buttons/circleIonButton/CircleIonButton.tsx";
import PrimaryIonButton from "../buttons/PrimaryIonButton/PrimaryIonButton.tsx";
// @ts-ignore
export default function EmployerLogin({history, match}) {
    const [loginProperties, setLoginProperties] = useState<{
        name: string | number | null | undefined,
        surname: string | number | null | undefined,
        fatherName: string | number | null | undefined
    }>({
        name: '',
        surname: '',
        fatherName: ''
    })
    const [isNextButtonDisabled, setNextButtonDisabled] = useState(true)
    const [isAllBlocked, setAllBlocked] = useState(false)

    enum EmployerTypeName{
        manager = "Менеджер",
        employer = "Сотрудник"
    }
    const userTypeDispatch = useAppDispatch()
    const userNameDispatch = useAppDispatch()
    const handleNextButton:MouseEventHandler<HTMLIonButtonElement> = (e) => {
        e.preventDefault()
        setAllBlocked(true)

        setTimeout(() => {
            userTypeDispatch(setUserType({
                type: match.params.employerType,
                // @ts-ignore
                humanaizedType: EmployerTypeName[match.params.employerType]
            }))
            userNameDispatch(setUserName(`${loginProperties.surname} ${loginProperties.name} ${loginProperties.fatherName}`))
            setAllBlocked(false)
            history.push('/tabs')
        }, 2000)
    }

    useEffect(() => {
        if (!loginProperties.name || !loginProperties.surname || !loginProperties.fatherName) return
        if (loginProperties.name?.toString().trim().length > 3 && loginProperties.surname?.toString().trim().length > 3 && loginProperties.fatherName.toString().trim().length > 3){
            setNextButtonDisabled(false)
        }
    }, [loginProperties]);
    return (
        <IonPage>
            <IonHeader mode={'md'}>
                <IonToolbar mode={'md'}>
                    <IonTitle>Вход в систему</IonTitle>
                    {isAllBlocked &&<IonProgressBar type="indeterminate"></IonProgressBar>}
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <div style={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    minHeight: '100%'
                }}>
                    <div style={{
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'center',
                        minHeight: '100%',
                        paddingBottom: "20em"
                    }}>
                        {/*@ts-ignore*/}
                        <h2>{EmployerTypeName[match.params.employerType]}</h2>
                        <div style={{
                            display: 'flex',
                            justifyContent: 'center',
                            alignContent: 'center',
                            paddingTop: "1em"
                        }}>
                            <div style={{
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '1em'
                            }}>
                                <IonInput disabled={isAllBlocked} onIonChange={(e) => setLoginProperties({...loginProperties, surname: e.target.value})} mode={'md'} shape={'round'} fill={'outline'} label={'Фамилия'} style={{maxHeight: '60px'}} labelPlacement={'floating'} required/>
                                <IonInput disabled={isAllBlocked} onIonChange={(e) => setLoginProperties({...loginProperties, name: e.target.value})} mode={'md'} shape={'round'} fill={'outline'} label={'Имя'} style={{maxHeight: '60px'}} labelPlacement={'floating'} required/>
                                <IonInput disabled={isAllBlocked} onIonChange={(e) => setLoginProperties({...loginProperties, fatherName: e.target.value})} mode={'md'} shape={'round'} fill={'outline'} label={'Отчество'} style={{maxHeight: '60px'}} labelPlacement={'floating'} required/>

                            </div>
                        </div>
                    </div>
                </div>
                <div style={{
                    display: 'flex',
                    justifyContent: "space-between",
                    position: 'fixed',
                    bottom: 10,
                    minWidth: "99%",
                    paddingRight: '1em',
                    paddingLeft: "1em",
                    alignItems: "center"
                }}>
                    <CircleIonButton disabled={isAllBlocked} size={'small'} routerDirection={'back'} routerLink={'/login'}>
                    <IonIcon slot={'icon-only'} icon={chevronBack}/>
                    </CircleIonButton>
                    <PrimaryIonButton onClick={handleNextButton} strong disabled={isNextButtonDisabled || isAllBlocked} shape={'round'} style={{
                        minWidth: "8em"
                    }}>
                        Далее
                    </PrimaryIonButton>
                </div>
            </IonContent>
        </IonPage>
    )
}