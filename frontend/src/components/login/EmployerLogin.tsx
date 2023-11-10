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
import {App} from "@capacitor/app";
import {useCookies} from "react-cookie";
// @ts-ignore
export default function EmployerLogin({history, match}) {
    const [loginProperties, setLoginProperties] = useState<{
        username: string | number | null | undefined,
        password: string | number | null | undefined
    }>({
        username: '',
        password: '',
    })
    const [isNextButtonDisabled, setNextButtonDisabled] = useState(true)
    const [isAllBlocked, setAllBlocked] = useState(false)

    App.addListener('backButton', () => {
        window.history.back()
    })

    enum EmployerTypeName{
        manager = "Менеджер",
        employer = "Сотрудник"
    }
    const userTypeDispatch = useAppDispatch()
    const userNameDispatch = useAppDispatch()
    const [_, setCookie] = useCookies(["role"]);

    const handleNextButton:MouseEventHandler<HTMLIonButtonElement> = (e) => {
        e.preventDefault()
        setAllBlocked(true)

        setTimeout(() => {
            userTypeDispatch(setUserType({
                type: match.params.employerType,
                // @ts-ignore
                humanaizedType: EmployerTypeName[match.params.employerType]
            }))
            let cookieExipred = 1000 * 60 * 60 * 24 * 30
            setCookie("role", match.params.employerType,{maxAge: cookieExipred, path: "/"})
            userNameDispatch(setUserName(`${loginProperties.username}`))
            setAllBlocked(false)
            history.push('/tabs')
        }, 2000)
    }

    useEffect(() => {
        console.log(document.cookie)
        if (!loginProperties.username || !loginProperties.password) return
        if (loginProperties.username?.toString().trim().length > 1 && loginProperties.password?.toString().trim().length > 3){
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
                                <IonInput minlength={2} autofocus clearInput autoCapitalize={'sentences'} autocomplete={'username'} disabled={isAllBlocked} onIonInput={(e) => setLoginProperties({...loginProperties, username: e.target.value})} mode={'md'} shape={'round'} fill={'outline'} label={'Логин'} style={{maxHeight: '60px'}} labelPlacement={'floating'} required/>
                                <IonInput pattern={"password"} type={"password"} minlength={2} clear-on-edit clearInput autocomplete={'current-password'} disabled={isAllBlocked} onIonInput={(e) => setLoginProperties({...loginProperties, password: e.target.value})} mode={'md'} shape={'round'} fill={'outline'} label={'Пароль'} style={{maxHeight: '60px'}} labelPlacement={'floating'} required/>
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