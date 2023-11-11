import {useEffect} from 'react'
import './App.css'
import {IonButton, IonContent, IonPage,} from "@ionic/react";

function App() {
    useEffect(() => {
        console.log(document.cookie.length)
    }, []);
  return (
    <IonPage>
      {/*<IonHeader>*/}
      {/*    <IonToolbar>*/}
      {/*        <IonTitle>Main page</IonTitle>*/}
      {/*    </IonToolbar>*/}
      {/*</IonHeader>*/}
        <IonContent>
                <IonButton routerLink={"/login"}>Login</IonButton>
        </IonContent>
    </IonPage>
  )
}

export default App
